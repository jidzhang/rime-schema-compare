# Rime 评测结果

- 生成时间: 2026-10-26 15:05:17 +0800
- 来源文件: `benchmark_zhihu120_20261026T070406199801Z_report.txt`

## Vendor 子模块版本

- `vendor/mingyuepinyin`: 小狼毫 0.17.4 自带 `luna_pinyin_simp`（经 `vendor/data` 共享）
- `vendor/rime-ice`: `75e6572bebc05b49021e842949ce947882e3e4b2`
- `vendor/rime-frost`: `328ded2ac3978c0a2b56c18b9d7ec05dd8b18130`（archive tarball 定版，无 .git）
- `vendor/rime_wanxiang` (`wanxiang`): `b935db47c516afdee06f80e041dfad6028c28b1a`（archive tarball 定版，无 .git）
- `vendor/oh-my-rime`: `5fca6ae067fd666b5ec4f119c5147efd629cc76d`（本仓新增，薄荷拼音）
- `*_with_gram` 挂载模型: `wanxiang-lts-zh-hans.gram`（398,505,004 B，sha256 `1849e5e4acbdbfaf…`，硬链接）
- `lib/rime.dll`: 3,727,872 B，sha256 `9975f25c336a9b20…`
- gold 读音: `zhihu120.pin.tsv`（语料同目录 sidecar；vendor 词库交叉审计，修正 尼泊尔 po→bo 3 句）

## 评测摘要

```text
========================================================================
Rime 多方案整句评测 — 摘要报告
========================================================================
生成时间 (UTC): 20261026T070406199801Z
rime.dll: D:\work\github\IME\windows-ime-bench\engine\rime-schema-compare\lib\rime.dll
模式: 单语料 (zhihu120)

语料文件:
  - zhihu120: D:\work\github\IME\windows-ime-bench\engine\rime-schema-compare\data\corpus\zhihu120.txt

【总体】
  [mingyuepinyin]
    句子正确率: 43.33%  (52/120 句完全匹配)
    文字正确率: 85.17%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 84.4%

  [mingyuepinyin_with_gram]
    句子正确率: 48.33%  (58/120 句完全匹配)
    文字正确率: 86.72%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 86.68%

  [rime_ice]
    句子正确率: 51.67%  (62/120 句完全匹配)
    文字正确率: 90.89%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.48%

  [rime_ice_with_gram]
    句子正确率: 60.83%  (73/120 句完全匹配)
    文字正确率: 92.44%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 92.12%

  [rime_frost]
    句子正确率: 55.0%  (66/120 句完全匹配)
    文字正确率: 90.96%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.35%

  [rime_frost_with_gram]
    句子正确率: 65.83%  (79/120 句完全匹配)
    文字正确率: 93.43%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 93.09%

  [wanxiang]
    句子正确率: 48.33%  (58/120 句完全匹配)
    文字正确率: 89.27%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.26%

  [rime_wanxiang_with_gram]
    句子正确率: 60.0%  (72/120 句完全匹配)
    文字正确率: 92.23%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.83%

  [oh_my_rime]
    句子正确率: 49.17%  (59/120 句完全匹配)
    文字正确率: 88.7%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 88.56%

  [oh_my_rime_with_gram]
    句子正确率: 60.83%  (73/120 句完全匹配)
    文字正确率: 92.58%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 92.0%

========================================================================
【耗时】
  读取文件: 0.09 ms
  分句: 0.29 ms
  预过滤: 0.99 ms
  [mingyuepinyin] 输入串: 7.59 ms, librime 加载: 314.86 ms, 开会话+选方案: 9.38 ms, 逐句解码: 325.91 ms
  [mingyuepinyin_with_gram] 输入串: 7.06 ms, librime 加载: 308.72 ms, 开会话+选方案: 9.03 ms, 逐句解码: 338.35 ms
  [oh_my_rime] 输入串: 7.44 ms, librime 加载: 875.52 ms, 开会话+选方案: 187.77 ms, 逐句解码: 1897.21 ms
  [oh_my_rime_with_gram] 输入串: 7.18 ms, librime 加载: 883.69 ms, 开会话+选方案: 190.0 ms, 逐句解码: 1996.76 ms
  [rime_frost] 输入串: 7.06 ms, librime 加载: 8849.51 ms, 开会话+选方案: 19.7 ms, 逐句解码: 1348.58 ms
  [rime_frost_with_gram] 输入串: 7.87 ms, librime 加载: 8438.17 ms, 开会话+选方案: 19.76 ms, 逐句解码: 1421.22 ms
  [rime_ice] 输入串: 7.82 ms, librime 加载: 1168.94 ms, 开会话+选方案: 19.39 ms, 逐句解码: 295.35 ms
  [rime_ice_with_gram] 输入串: 7.18 ms, librime 加载: 1150.21 ms, 开会话+选方案: 18.88 ms, 逐句解码: 353.26 ms
  [rime_wanxiang_with_gram] 输入串: 7.34 ms, librime 加载: 7544.26 ms, 开会话+选方案: 1223.82 ms, 逐句解码: 2153.19 ms
  [wanxiang] 输入串: 7.21 ms, librime 加载: 6694.34 ms, 开会话+选方案: 1286.55 ms, 逐句解码: 2081.59 ms
  写出结果文件: 71.44 ms

========================================================================
句子正确判定: Top 1 候选中任一项与 gold 完全一致即判对。

同义词归一化（句级完全匹配与 CER 计算前）: 其它→其他；他/她/它→他；的/地/得→的

说明: 分句后仅「纯汉字」且不含 ASCII 数字/英文字母、汉字不少于 5 字的片段参与评测；其它片段已过滤。句子正确率 = 归一化后预测与金句完全一致的比例；文字正确率 = 全语料 (归一化后总字数−总编辑距离)/归一化后总字数。输入串按各 vendor 自身配置生成，可能是连续拼音，也可能是形码前缀串。```

## 说明

- 语料为本机 benchmark 仓正式整句卷 `zhihu120`（n=120，与黑盒榜同卷同判分）；
- 读音来自 `zhihu120.pin.tsv` gold sidecar：vendor 词库（雾凇/白霜/薄荷）交叉审计
  修正了 pypinyin 的 3 处「尼泊尔 po→bo」错误后冻结，逐轮确定性 0 diff；
- 全部方案按「无语言模型、无用户词库」口径（`*_with_gram` 变体额外挂同一 gram 模型）；
- 薄荷拼音（oh-my-rime）为本仓新增 vendor；魔然为双拼+形码体系，不参评；
- 词级 words234（n=450）与三道闸验证见 `report/whitebox_2026-10-26.md` 与
  benchmark 仓 `results/whitebox_rime_report.md`（正式结论在主仓）。
