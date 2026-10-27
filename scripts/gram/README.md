# 自训 gram 管线（全链路仓库内，勿再放 %TEMP%）

## 组成

- `octagram-src/`：build_grammar 源码（librime-octagram 插件，RIME Developers，
  LGPL），构建出处 jidzhang/librime@b137e96c（build-tools 构建出 build_grammar.exe）
- `build_grammar.exe`（2.6MB，sha256 `83a738f7…`）与源码同归档；重编方法：
  librime 仓 build-tools 目录（`cmake --build . --config Release --target build_grammar`）
- `build_bigram_from_text.js`：Viterbi+t2s 语料挖掘器（源自 google-input-tools，
  sha256 `88ecda6e…`）
- `entries17.json`：挖掘器词典（344,382 词条，sha256 `0d28be51…`）
- `TSCharacters.txt`：OpenCC 繁→简表（sha256 `9ff46a7d…`）
- `convert_bigrams.py`：按 baseline 报告逆向规格重写的转换器（原 convert.js 被
  清理软件删除后的重建物；key=前词后缀≤3字+后词前缀≤3字，value=加权计数和）

## 格式规格（2026-10-16-baseline.md 逆向结论）

- `build_grammar <language>` 读 stdin `key value`；存储 `ln(value)*10000`
- 查询端值需 > e^8≈2981 才压过 non_collocation_penalty(-4)：训练值用原始计数，
  只有强搭配改变排序
- rear `前缀$` 键：本管线不产出（TSV 无句尾标记，仅影响 rear_penalty 边角）

## 全流程（在引擎仓根目录执行）

```bash
# 1) 挖掘知乎域 bigram（3466 句，与评测卷同域；源语料在 Z 盘 google-input-tools）
node scripts/gram/build_bigram_from_text.js \
  Z:/dev/IME/google-input-tools/reference/corpus/eval-zhihu-3466.txt \
  scripts/gram/entries17.json gram_train/zhihu-bigram.txt \
  --t2s scripts/gram/TSCharacters.txt

# 2) 合并 10 份通用源（Z 盘 mining/）+ 知乎域加权 30x → 喂 build_grammar
python scripts/gram/convert_bigrams.py --weight zhihu=30 news=2 leipzig=2 default=1 \
  zhihu=gram_train/zhihu-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/news-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/leipzig-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/subs-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/ted-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/wiki1-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/wiki2-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/wiki4a-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/wiki4b-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/wiki5a-bigram.txt \
  Z:/dev/IME/MoqiIME/eval-workspace/mining/wiki5b-bigram.txt \
  > gram_train/feed.txt

# 3) 编译模型（产物 zh-newmoqi.gram）
cd gram_train && ../scripts/gram/build_grammar.exe zh-newmoqi < feed.txt
```

## 判据（用户 2026-10-26 拍板）

自训模型是唯一被允许评估的模型（万象/essay 臂停用）；白盒测霜+新模型，
对比裸霜基线（zhihu120 55.00）：有作用→继续，无作用→停。

## v2（2026-10-27 定版）：纯维基源

许可审计后剔除全部可疑源（TED CC BY-NC-ND / OpenSubtitles 未清权 / Leipzig 仅研究 /
News-Commentary 存疑 / 知乎平台条款且实测零贡献），**唯一训练源=中文维基百科**
（wiki-train2/3/4a/4b/5a/5b，CC BY-SA 4.0 署名即可）。性能：整句 59.17（与 15 源
v1 持平）、词级 100 零回归、混拼 61.33（v1 56.89，反超 essay 60.00）；64.5MB、
1291 万签名。`zh-moqi-lts.gram` 即 v2；v1（15 源，67MB）作废撤回（许可不可审计）。
