"""Split corpus text and build benchmark input strings for Rime."""

from __future__ import annotations

import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Dict, List

from pypinyin import Style, lazy_pinyin, load_phrases_dict

# 语料读音纠错词典（2026-10-25 全量人工核对 zhihu120+words234 共 570 条，
# 确认 6 句多音字机械转换错误，全部修正于此；语料文本不动，修的是转换器）：
#   降雨 xiáng→jiàng（词组表把"降雨"映射到了"投降"系读音）
#   得重备/得重 的"得"děi、"重"chóng（"得重X"不在 pypinyin 词表，回退默认音 de/zhong）
#   重做/重画/重绘 的"重"chóng（同上，"重新"在词表所以原来就对）
# 回归守卫：重新(chong)/重要(zhong)/比重(zhong)/系因(xi)/着陆(zhuo)/为遇难(wei/nan)
# 全部验证不受影响（见 2026-10-25 校验记录）。
load_phrases_dict({
    "降雨": [["jiàng"], ["yǔ"]],
    # 分词器最长匹配会先切出"受降"（受降，投降义）吃掉"降"，
    # 注入三字词抢占匹配路径（"受降雨">"受降"）：
    "受降雨": [["shòu"], ["jiàng"], ["yǔ"]],
    "得重": [["děi"], ["chóng"]],
    "重做": [["chóng"], ["zuò"]],
    "重画": [["chóng"], ["huà"]],
    "重绘": [["chóng"], ["huì"]],
    # 2026-10-26 交叉审计新发现：pypinyin 把"尼泊尔"转成 ni po er（湖泊音），
    # 标准音 ní bó ěr（三家词库一致作证）；正式语料已有 .pin.tsv sidecar 兜底，
    # 此条为无 sidecar 场景的 fallback：
    "尼泊尔": [["ní"], ["bó"], ["ěr"]],
})

# 分句后片段须能通过 is_pure_hanzi_segment，故全角逗号、句号始终作为切分点；引号内逗号也要切，否则会留下「汉字+，」。
# 用 “ ” 配对深度避免策略性误伤（主要纠偏：ASCII 句点 `.` 在小数 68.4 等处不可当句号）。
_OPEN_CQ = "\u201c"  # “
_CLOSE_CQ = "\u201d"  # ”
_QUOTE_EDGE_RE = re.compile(r'^[\s\"“”‘’]+|[\s\"“”‘’]+$')

# 分句后丢弃：含顿号、中文书名号《》的片段（机构枚举、文件标题等，不参与拼音评测）
_DUNHAO_OR_SHUMINGHAO_RE = re.compile(r"[、]|《|》")

# 片段在去掉首尾空白后须「全部为汉字」才参与评测（含数字、拉丁字母、符号则丢弃）
_HANZI_ONLY_RE = re.compile(r"^[\u4e00-\u9fff]+$")

# 分句后：含 ASCII 数字或英文字母的片段不参与评测（与「纯汉字」规则一致，单独检测便于统计）
_ASCII_DIGIT_OR_LETTER_RE = re.compile(r"[0-9A-Za-z]")

# 纯汉字片段至少含多少个字才参与评测（环境变量可覆盖：词级语料用 2）
MIN_EVAL_HANZI_CHARS = int(os.environ.get("RIME_BENCH_MIN_HANZI", "5") or "5")

# Remove common punctuation and whitespace; keep Hanzi, Latin, digits as needed
_PUNCT_RE = re.compile(
    r"[\s·…！!？?；;：:\"\"''「」『』（）()\[\]【】《》<>、．·—\-—]+"
)


def _is_decimal_dot(s: str, i: int) -> bool:
    """True if s[i] is '.' between two ASCII digits (e.g. 68.4)."""
    if i < 0 or i >= len(s) or s[i] != ".":
        return False
    return i > 0 and i + 1 < len(s) and s[i - 1].isdigit() and s[i + 1].isdigit()


def _split_line_by_punctuation(line: str) -> List[str]:
    """
    对单行文本按引号深度与 ，。,. 切分（不含换行；换行由 split_sentences 先处理）。
    """
    s = line
    if not s:
        return []
    n = len(s)
    parts: List[str] = []
    start = 0
    depth = 0
    i = 0

    def emit_before(delimiter_at: int) -> None:
        nonlocal start
        seg = s[start:delimiter_at].strip()
        if seg:
            seg = _QUOTE_EDGE_RE.sub("", seg).strip()
            if seg:
                parts.append(seg)
        start = delimiter_at + 1

    while i < n:
        c = s[i]

        # 深度 0：冒号 + 弯开引，可选其后空白
        if (
            depth == 0
            and c in "：:"
            and i + 1 < n
            and s[i + 1] == _OPEN_CQ
        ):
            emit_before(i)
            j = i + 2
            while j < n and s[j].isspace():
                j += 1
            start = j
            depth = 1
            i = j
            continue

        if c == _OPEN_CQ:
            if depth == 0:
                emit_before(i)
                depth = 1
            else:
                depth += 1
                start = i + 1  # 嵌套开引不进入片段正文
            i += 1
            continue

        if c == _CLOSE_CQ:
            emit_before(i)
            depth = max(0, depth - 1)
            i += 1
            continue

        if c in "，,":
            emit_before(i)
        elif c == "。":
            emit_before(i)
        elif c == "." and not _is_decimal_dot(s, i):
            emit_before(i)

        i += 1

    tail = s[start:].strip()
    if tail:
        tail = _QUOTE_EDGE_RE.sub("", tail).strip()
        if tail:
            parts.append(tail)
    return parts


def split_sentences(text: str) -> List[str]:
    """
    切分语料为片段。规则要点：
    - **先按换行**（\\n / \\r\\n）切成行，空行丢弃；再对每行做下列切分；
    - 全角 ，。 始终切分（引号内亦然），以得到纯汉字块供评测；
    - 半角 , 同样切分；半角 . 仅在小数点（数字.数字）之外时切分；
    - 深度 0 时遇 ：“ / :" 整段作为分界，跳过开引号，并进入引号内深度；
    - 深度 0 遇弯开引 “：在引号前切分（如 昔日“脏臭乱”）；
    - 遇弯闭引 ”：在引号前切分并出引号层；
    - 段首尾去掉孤立引号与空白；
    - 去掉仍含顿号（、）或书名号（《》）的片段。
    """
    if not text or not text.strip():
        return []
    merged: List[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        merged.extend(_split_line_by_punctuation(line))
    return [p for p in merged if not segment_has_dunhao_or_shuminghao(p)]


def segment_has_dunhao_or_shuminghao(s: str) -> bool:
    """True if segment contains顿号 or CJK book title marks 《 or 》."""
    return bool(_DUNHAO_OR_SHUMINGHAO_RE.search(s.strip()))


def is_pure_hanzi_segment(s: str) -> bool:
    """True iff non-empty and every codepoint is a CJK unified ideograph (no digit/letter/symbol)."""
    t = s.strip()
    return bool(t) and bool(_HANZI_ONLY_RE.fullmatch(t))


def segment_has_ascii_digit_or_letter(s: str) -> bool:
    """True if segment contains ASCII digit or Latin letter (after strip, any position)."""
    return bool(_ASCII_DIGIT_OR_LETTER_RE.search(s.strip()))


def extract_hanzi(s: str) -> str:
    return "".join(re.findall(r"[\u4e00-\u9fff]", s))


def strip_inner_punct(s: str) -> str:
    return _PUNCT_RE.sub("", s)


def sentence_to_continuous_pinyin(s: str) -> str:
    """Lowercase contiguous pinyin, Hanzi only (reproducible baseline).

    优先查 gold sidecar（<corpus>.pin.tsv，人工/交叉审计定版读音）；
    无 sidecar 或未命中时回退 pypinyin 现算（含 load_phrases_dict 纠错）。
    """
    hz = extract_hanzi(s)
    if not hz:
        return ""
    if _GOLD_PINYIN_MAP is not None:
        hit = _GOLD_PINYIN_MAP.get(hz)
        if hit is not None:
            return hit
    syllables = lazy_pinyin(hz, style=Style.NORMAL, errors="ignore")
    return "".join(syllables).lower()


# gold sidecar 状态：由 benchmark 主循环按语料激活（corpus 同目录 <stem>.pin.tsv）
_GOLD_PINYIN_MAP: Dict[str, str] | None = None


def activate_gold_pinyin_for_corpus(corpus_path) -> None:
    """若语料同目录存在 <stem>.pin.tsv 则加载为 gold 读音表；否则清空回退现算。"""
    global _GOLD_PINYIN_MAP
    from pathlib import Path as _P
    p = _P(corpus_path)
    sidecar = p.with_name(p.stem + ".pin.tsv")
    if sidecar.is_file():
        m: Dict[str, str] = {}
        for line in open(sidecar, encoding="utf-8"):
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) == 2 and parts[0]:
                m[parts[0]] = parts[1]
        _GOLD_PINYIN_MAP = m
    else:
        _GOLD_PINYIN_MAP = None


_CODE_LETTERS_RE = re.compile(r"[A-Za-z]+")


def _letters_only(s: str) -> str:
    return "".join(_CODE_LETTERS_RE.findall(s or "")).lower()


def _pick_shape_code_prefix(code: str, stem: str, prefix_len: int) -> str:
    for raw in (stem, code):
        letters = _letters_only(raw)
        if len(letters) >= prefix_len:
            return letters[:prefix_len]
    for raw in (stem, code):
        letters = _letters_only(raw)
        if letters:
            return letters[:prefix_len]
    return ""


def _pick_shape_code_head(code: str) -> str:
    raw = code.split(";", 1)[0] if ";" in code else code
    return _letters_only(raw)


@lru_cache(maxsize=None)
def load_single_char_shape_code_prefixes(dict_path_str: str, prefix_len: int = 2) -> Dict[str, str]:
    path = Path(dict_path_str)
    mapping: Dict[str, str] = {}
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not in_table:
            if stripped == "...":
                in_table = True
            continue
        if not stripped or stripped.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        text = parts[0].strip()
        if len(text) != 1 or not _HANZI_ONLY_RE.fullmatch(text):
            continue
        code = parts[1].strip()
        stem = parts[3].strip() if len(parts) > 3 else ""
        prefix = _pick_shape_code_prefix(code, stem, prefix_len)
        if prefix and text not in mapping:
            mapping[text] = prefix
    return mapping


@lru_cache(maxsize=None)
def load_single_char_shape_code_heads(dict_path_str: str) -> Dict[str, str]:
    path = Path(dict_path_str)
    mapping: Dict[str, str] = {}
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not in_table:
            if stripped == "...":
                in_table = True
            continue
        if not stripped or stripped.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        text = parts[0].strip()
        if len(text) != 1 or not _HANZI_ONLY_RE.fullmatch(text):
            continue
        head = _pick_shape_code_head(parts[1].strip())
        if head and text not in mapping:
            mapping[text] = head
    return mapping


def sentence_to_shape_code_prefix_input(s: str, dict_path: Path, prefix_len: int = 2) -> str:
    """Concatenate each Hanzi's shape-code prefix; return empty string if any Hanzi is missing."""
    hz = extract_hanzi(s)
    if not hz:
        return ""
    mapping = load_single_char_shape_code_prefixes(str(dict_path.resolve()), prefix_len)
    parts: List[str] = []
    for ch in hz:
        prefix = mapping.get(ch, "")
        if not prefix:
            return ""
        parts.append(prefix)
    return "".join(parts)


def sentence_to_shape_code_head_input(s: str, dict_path: Path) -> str:
    """Concatenate each Hanzi's code before the first semicolon; empty if any Hanzi is missing."""
    hz = extract_hanzi(s)
    if not hz:
        return ""
    mapping = load_single_char_shape_code_heads(str(dict_path.resolve()))
    parts: List[str] = []
    for ch in hz:
        head = mapping.get(ch, "")
        if not head:
            return ""
        parts.append(head)
    return "".join(parts)
