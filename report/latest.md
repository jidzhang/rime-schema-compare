# Rime 评测结果

- 生成时间: 2026-05-12 23:13:24 +08:00
- 来源文件: `benchmark_all_corpus_20260512T151147191791Z_report.txt`

## Vendor 子模块版本

- `vendor/rime-frost`: `89ad92e450f9a5f4dcc2de67ba28004f9af0cc1e`
- `vendor/rime-ice`: `5f130b4fbc9a228dea9c9ad25597d4bab284ee1d`
- `vendor/rime_wanxiang` (`wanxiang`): `351ea3e80c63cf1e707aa45ca3097678a60d635a`
- `vendor/rime-wubi-sentence`: `c3b26af601e41de49227f86633df00985e8d8a77`

## 评测摘要

```text
========================================================================
Rime 多方案整句评测 — 摘要报告
========================================================================
生成时间 (UTC): 20260512T151147191791Z
rime.dll: D:\vscode\rime_projs\rime-schema-compare\lib\rime.dll
模式: 全部语料 (data/corpus/*.txt)

语料文件:
  - news: D:\vscode\rime_projs\rime-schema-compare\data\corpus\news.txt
  - novel: D:\vscode\rime_projs\rime-schema-compare\data\corpus\novel.txt
  - prose: D:\vscode\rime_projs\rime-schema-compare\data\corpus\prose.txt
  - tech: D:\vscode\rime_projs\rime-schema-compare\data\corpus\tech.txt
  - test: D:\vscode\rime_projs\rime-schema-compare\data\corpus\test.txt

【总体】
  [mingyuepinyin]
    句子正确率: 41.8%  (260/622 句完全匹配)
    文字正确率: 83.38%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 82.99%

  [mingyuepinyin_with_gram]
    句子正确率: 34.57%  (215/622 句完全匹配)
    文字正确率: 80.45%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 79.91%

  [rime_ice]
    句子正确率: 43.09%  (268/622 句完全匹配)
    文字正确率: 84.74%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 84.05%

  [rime_ice_with_gram]
    句子正确率: 48.07%  (299/622 句完全匹配)
    文字正确率: 86.89%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 85.64%

  [rime_frost]
    句子正确率: 48.55%  (302/622 句完全匹配)
    文字正确率: 86.91%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 85.8%

  [rime_frost_with_gram]
    句子正确率: 55.14%  (343/622 句完全匹配)
    文字正确率: 89.08%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 87.81%

  [wanxiang]
    句子正确率: 39.39%  (245/622 句完全匹配)
    文字正确率: 83.99%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 83.08%

  [rime_wanxiang_with_gram]
    句子正确率: 49.04%  (305/622 句完全匹配)
    文字正确率: 87.04%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 86.15%

  [rime_wubi_sentens_wubi86]
    句子正确率: 44.69%  (278/622 句完全匹配)
    文字正确率: 86.93%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 86.37%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 54.98%  (342/622 句完全匹配)
    文字正确率: 90.89%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.16%

------------------------------------------------------------------------
【语料: news】
  [mingyuepinyin]
    句子正确率: 54.15%  (124/229 句完全匹配)
    文字正确率: 87.66%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.17%

  [mingyuepinyin_with_gram]
    句子正确率: 40.61%  (93/229 句完全匹配)
    文字正确率: 83.27%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 84.01%

  [rime_ice]
    句子正确率: 56.33%  (129/229 句完全匹配)
    文字正确率: 89.38%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.3%

  [rime_ice_with_gram]
    句子正确率: 58.52%  (134/229 句完全匹配)
    文字正确率: 90.79%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.75%

  [rime_frost]
    句子正确率: 63.76%  (146/229 句完全匹配)
    文字正确率: 91.68%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 92.41%

  [rime_frost_with_gram]
    句子正确率: 69.0%  (158/229 句完全匹配)
    文字正确率: 93.97%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 94.18%

  [wanxiang]
    句子正确率: 50.66%  (116/229 句完全匹配)
    文字正确率: 89.63%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.01%

  [rime_wanxiang_with_gram]
    句子正确率: 60.7%  (139/229 句完全匹配)
    文字正确率: 91.64%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.81%

  [rime_wubi_sentens_wubi86]
    句子正确率: 49.78%  (114/229 句完全匹配)
    文字正确率: 90.11%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.32%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 62.01%  (142/229 句完全匹配)
    文字正确率: 93.61%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 93.63%

------------------------------------------------------------------------
【语料: novel】
  [mingyuepinyin]
    句子正确率: 45.0%  (18/40 句完全匹配)
    文字正确率: 85.8%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 84.09%

  [mingyuepinyin_with_gram]
    句子正确率: 45.0%  (18/40 句完全匹配)
    文字正确率: 80.87%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 79.57%

  [rime_ice]
    句子正确率: 45.0%  (18/40 句完全匹配)
    文字正确率: 86.38%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 85.03%

  [rime_ice_with_gram]
    句子正确率: 62.5%  (25/40 句完全匹配)
    文字正确率: 90.43%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 88.88%

  [rime_frost]
    句子正确率: 60.0%  (24/40 句完全匹配)
    文字正确率: 90.72%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.14%

  [rime_frost_with_gram]
    句子正确率: 77.5%  (31/40 句完全匹配)
    文字正确率: 95.07%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 94.44%

  [wanxiang]
    句子正确率: 40.0%  (16/40 句完全匹配)
    文字正确率: 82.61%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 81.83%

  [rime_wanxiang_with_gram]
    句子正确率: 57.5%  (23/40 句完全匹配)
    文字正确率: 90.72%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.88%

  [rime_wubi_sentens_wubi86]
    句子正确率: 60.0%  (24/40 句完全匹配)
    文字正确率: 91.59%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 92.41%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 67.5%  (27/40 句完全匹配)
    文字正确率: 94.2%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 94.73%

------------------------------------------------------------------------
【语料: prose】
  [mingyuepinyin]
    句子正确率: 20.85%  (44/211 句完全匹配)
    文字正确率: 72.7%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 71.87%

  [mingyuepinyin_with_gram]
    句子正确率: 25.59%  (54/211 句完全匹配)
    文字正确率: 73.19%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 71.99%

  [rime_ice]
    句子正确率: 23.22%  (49/211 句完全匹配)
    文字正确率: 74.55%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 73.73%

  [rime_ice_with_gram]
    句子正确率: 28.44%  (60/211 句完全匹配)
    文字正确率: 76.78%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 75.51%

  [rime_frost]
    句子正确率: 21.8%  (46/211 句完全匹配)
    文字正确率: 74.23%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 72.98%

  [rime_frost_with_gram]
    句子正确率: 27.96%  (59/211 句完全匹配)
    文字正确率: 76.56%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 75.25%

  [wanxiang]
    句子正确率: 21.33%  (45/211 句完全匹配)
    文字正确率: 72.81%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 72.04%

  [rime_wanxiang_with_gram]
    句子正确率: 29.86%  (63/211 句完全匹配)
    文字正确率: 77.71%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 76.5%

  [rime_wubi_sentens_wubi86]
    句子正确率: 28.91%  (61/211 句完全匹配)
    文字正确率: 77.92%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 77.42%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 36.49%  (77/211 句完全匹配)
    文字正确率: 83.74%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 82.63%

------------------------------------------------------------------------
【语料: tech】
  [mingyuepinyin]
    句子正确率: 52.55%  (72/137 句完全匹配)
    文字正确率: 88.48%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.08%

  [mingyuepinyin_with_gram]
    句子正确率: 34.31%  (47/137 句完全匹配)
    文字正确率: 84.09%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 84.84%

  [rime_ice]
    句子正确率: 51.09%  (70/137 句完全匹配)
    文字正确率: 89.15%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.33%

  [rime_ice_with_gram]
    句子正确率: 54.74%  (75/137 句完全匹配)
    文字正确率: 91.48%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.24%

  [rime_frost]
    句子正确率: 60.58%  (83/137 句完全匹配)
    文字正确率: 93.48%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 93.29%

  [rime_frost_with_gram]
    句子正确率: 65.69%  (90/137 句完全匹配)
    文字正确率: 94.47%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 94.14%

  [wanxiang]
    句子正确率: 47.45%  (65/137 句完全匹配)
    文字正确率: 88.22%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 88.39%

  [rime_wanxiang_with_gram]
    句子正确率: 54.74%  (75/137 句完全匹配)
    文字正确率: 89.48%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.65%

  [rime_wubi_sentens_wubi86]
    句子正确率: 56.93%  (78/137 句完全匹配)
    文字正确率: 91.74%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.89%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 67.15%  (92/137 句完全匹配)
    文字正确率: 94.14%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 94.36%

------------------------------------------------------------------------
【语料: test】
  [mingyuepinyin]
    句子正确率: 40.0%  (2/5 句完全匹配)
    文字正确率: 91.8%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 92.89%

  [mingyuepinyin_with_gram]
    句子正确率: 60.0%  (3/5 句完全匹配)
    文字正确率: 91.8%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 94.12%

  [rime_ice]
    句子正确率: 40.0%  (2/5 句完全匹配)
    文字正确率: 85.25%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 81.13%

  [rime_ice_with_gram]
    句子正确率: 100.0%  (5/5 句完全匹配)
    文字正确率: 100.0%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 100.0%

  [rime_frost]
    句子正确率: 60.0%  (3/5 句完全匹配)
    文字正确率: 91.8%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.36%

  [rime_frost_with_gram]
    句子正确率: 100.0%  (5/5 句完全匹配)
    文字正确率: 100.0%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 100.0%

  [wanxiang]
    句子正确率: 60.0%  (3/5 句完全匹配)
    文字正确率: 95.08%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 96.23%

  [rime_wanxiang_with_gram]
    句子正确率: 100.0%  (5/5 句完全匹配)
    文字正确率: 100.0%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 100.0%

  [rime_wubi_sentens_wubi86]
    句子正确率: 20.0%  (1/5 句完全匹配)
    文字正确率: 83.61%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 83.11%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 80.0%  (4/5 句完全匹配)
    文字正确率: 96.72%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 97.89%

========================================================================
【总耗时】全流程墙钟约 96458.24 ms（多语料）

【各语料耗时】
  · news
    读取文件: 0.13 ms
    分句: 1.28 ms
    预过滤: 18.74 ms
    [mingyuepinyin] 输入串: 11.89 ms, librime 加载: 340.24 ms, 开会话+选方案: 18.3 ms, 逐句解码: 446.82 ms
    [mingyuepinyin_with_gram] 输入串: 10.79 ms, librime 加载: 332.51 ms, 开会话+选方案: 18.84 ms, 逐句解码: 556.14 ms
    [rime_frost] 输入串: 11.37 ms, librime 加载: 1129.48 ms, 开会话+选方案: 63.03 ms, 逐句解码: 1313.15 ms
    [rime_frost_with_gram] 输入串: 11.55 ms, librime 加载: 1096.87 ms, 开会话+选方案: 44.76 ms, 逐句解码: 1302.74 ms
    [rime_ice] 输入串: 10.91 ms, librime 加载: 1072.86 ms, 开会话+选方案: 30.17 ms, 逐句解码: 483.69 ms
    [rime_ice_with_gram] 输入串: 11.02 ms, librime 加载: 1063.41 ms, 开会话+选方案: 31.7 ms, 逐句解码: 557.38 ms
    [rime_wanxiang_with_gram] 输入串: 12.38 ms, librime 加载: 364.51 ms, 开会话+选方案: 1224.05 ms, 逐句解码: 4655.45 ms
    [rime_wubi_sentens_wubi86] 输入串: 114.41 ms, librime 加载: 817.42 ms, 开会话+选方案: 364.39 ms, 逐句解码: 657.13 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 114.46 ms, librime 加载: 801.43 ms, 开会话+选方案: 369.03 ms, 逐句解码: 714.36 ms
    [wanxiang] 输入串: 11.2 ms, librime 加载: 372.2 ms, 开会话+选方案: 1263.59 ms, 逐句解码: 4460.68 ms
  · novel
    读取文件: 0.2 ms
    分句: 0.11 ms
    预过滤: 0.09 ms
    [mingyuepinyin] 输入串: 1.78 ms, librime 加载: 363.01 ms, 开会话+选方案: 16.41 ms, 逐句解码: 85.24 ms
    [mingyuepinyin_with_gram] 输入串: 1.8 ms, librime 加载: 342.66 ms, 开会话+选方案: 32.97 ms, 逐句解码: 96.52 ms
    [rime_frost] 输入串: 1.71 ms, librime 加载: 1134.1 ms, 开会话+选方案: 62.67 ms, 逐句解码: 249.78 ms
    [rime_frost_with_gram] 输入串: 1.81 ms, librime 加载: 1145.83 ms, 开会话+选方案: 51.63 ms, 逐句解码: 253.14 ms
    [rime_ice] 输入串: 1.71 ms, librime 加载: 1073.86 ms, 开会话+选方案: 30.29 ms, 逐句解码: 99.93 ms
    [rime_ice_with_gram] 输入串: 1.65 ms, librime 加载: 1067.95 ms, 开会话+选方案: 36.23 ms, 逐句解码: 114.93 ms
    [rime_wanxiang_with_gram] 输入串: 1.95 ms, librime 加载: 385.29 ms, 开会话+选方案: 1239.38 ms, 逐句解码: 869.01 ms
    [rime_wubi_sentens_wubi86] 输入串: 7.46 ms, librime 加载: 816.42 ms, 开会话+选方案: 369.07 ms, 逐句解码: 99.84 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 6.98 ms, librime 加载: 813.06 ms, 开会话+选方案: 370.33 ms, 逐句解码: 178.5 ms
    [wanxiang] 输入串: 1.69 ms, librime 加载: 390.31 ms, 开会话+选方案: 1282.27 ms, 逐句解码: 858.43 ms
  · prose
    读取文件: 0.24 ms
    分句: 0.63 ms
    预过滤: 0.86 ms
    [mingyuepinyin] 输入串: 8.52 ms, librime 加载: 338.84 ms, 开会话+选方案: 38.13 ms, 逐句解码: 403.08 ms
    [mingyuepinyin_with_gram] 输入串: 8.72 ms, librime 加载: 352.61 ms, 开会话+选方案: 32.14 ms, 逐句解码: 453.52 ms
    [rime_frost] 输入串: 9.57 ms, librime 加载: 1158.29 ms, 开会话+选方案: 58.73 ms, 逐句解码: 1176.29 ms
    [rime_frost_with_gram] 输入串: 8.5 ms, librime 加载: 1116.0 ms, 开会话+选方案: 47.31 ms, 逐句解码: 1260.45 ms
    [rime_ice] 输入串: 8.45 ms, librime 加载: 1077.81 ms, 开会话+选方案: 27.54 ms, 逐句解码: 423.2 ms
    [rime_ice_with_gram] 输入串: 8.98 ms, librime 加载: 1065.95 ms, 开会话+选方案: 30.58 ms, 逐句解码: 483.55 ms
    [rime_wanxiang_with_gram] 输入串: 8.97 ms, librime 加载: 353.66 ms, 开会话+选方案: 1236.24 ms, 逐句解码: 4123.48 ms
    [rime_wubi_sentens_wubi86] 输入串: 36.66 ms, librime 加载: 831.32 ms, 开会话+选方案: 364.55 ms, 逐句解码: 512.31 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 35.68 ms, librime 加载: 803.6 ms, 开会话+选方案: 375.88 ms, 逐句解码: 547.79 ms
    [wanxiang] 输入串: 9.06 ms, librime 加载: 365.18 ms, 开会话+选方案: 1242.98 ms, 逐句解码: 4095.27 ms
  · tech
    读取文件: 0.2 ms
    分句: 0.45 ms
    预过滤: 0.33 ms
    [mingyuepinyin] 输入串: 6.99 ms, librime 加载: 362.03 ms, 开会话+选方案: 16.38 ms, 逐句解码: 253.36 ms
    [mingyuepinyin_with_gram] 输入串: 7.67 ms, librime 加载: 386.3 ms, 开会话+选方案: 31.57 ms, 逐句解码: 295.32 ms
    [rime_frost] 输入串: 7.34 ms, librime 加载: 1123.35 ms, 开会话+选方案: 83.31 ms, 逐句解码: 712.04 ms
    [rime_frost_with_gram] 输入串: 6.7 ms, librime 加载: 1155.82 ms, 开会话+选方案: 55.79 ms, 逐句解码: 747.63 ms
    [rime_ice] 输入串: 6.77 ms, librime 加载: 1080.05 ms, 开会话+选方案: 38.16 ms, 逐句解码: 286.97 ms
    [rime_ice_with_gram] 输入串: 7.33 ms, librime 加载: 1078.47 ms, 开会话+选方案: 29.77 ms, 逐句解码: 430.57 ms
    [rime_wanxiang_with_gram] 输入串: 6.67 ms, librime 加载: 377.19 ms, 开会话+选方案: 1235.75 ms, 逐句解码: 2557.71 ms
    [rime_wubi_sentens_wubi86] 输入串: 24.39 ms, librime 加载: 834.23 ms, 开会话+选方案: 367.97 ms, 逐句解码: 362.75 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 23.91 ms, librime 加载: 811.2 ms, 开会话+选方案: 365.07 ms, 逐句解码: 407.95 ms
    [wanxiang] 输入串: 6.76 ms, librime 加载: 407.15 ms, 开会话+选方案: 1264.19 ms, 逐句解码: 2489.57 ms
  · test
    读取文件: 0.14 ms
    分句: 0.02 ms
    预过滤: 0.02 ms
    [mingyuepinyin] 输入串: 0.37 ms, librime 加载: 341.28 ms, 开会话+选方案: 19.69 ms, 逐句解码: 8.69 ms
    [mingyuepinyin_with_gram] 输入串: 0.57 ms, librime 加载: 351.75 ms, 开会话+选方案: 31.55 ms, 逐句解码: 10.72 ms
    [rime_frost] 输入串: 0.39 ms, librime 加载: 1119.81 ms, 开会话+选方案: 71.58 ms, 逐句解码: 19.67 ms
    [rime_frost_with_gram] 输入串: 0.37 ms, librime 加载: 1123.03 ms, 开会话+选方案: 53.38 ms, 逐句解码: 20.25 ms
    [rime_ice] 输入串: 0.36 ms, librime 加载: 1056.51 ms, 开会话+选方案: 29.51 ms, 逐句解码: 24.86 ms
    [rime_ice_with_gram] 输入串: 0.37 ms, librime 加载: 1080.08 ms, 开会话+选方案: 27.17 ms, 逐句解码: 26.72 ms
    [rime_wanxiang_with_gram] 输入串: 0.42 ms, librime 加载: 366.23 ms, 开会话+选方案: 1269.63 ms, 逐句解码: 68.67 ms
    [rime_wubi_sentens_wubi86] 输入串: 1.07 ms, librime 加载: 831.17 ms, 开会话+选方案: 371.77 ms, 逐句解码: 25.26 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 1.01 ms, librime 加载: 805.48 ms, 开会话+选方案: 370.01 ms, 逐句解码: 25.88 ms
    [wanxiang] 输入串: 0.38 ms, librime 加载: 365.84 ms, 开会话+选方案: 1241.72 ms, 逐句解码: 65.0 ms

========================================================================
句子正确判定: Top 1 候选中任一项与 gold 完全一致即判对。

同义词归一化（句级完全匹配与 CER 计算前）: 其它→其他；他/她/它→他；的/地/得→的

说明: 分句后仅「纯汉字」且不含 ASCII 数字/英文字母、汉字不少于 5 字的片段参与评测；其它片段已过滤。句子正确率 = 归一化后预测与金句完全一致的比例；文字正确率 = 全语料 (归一化后总字数−总编辑距离)/归一化后总字数。输入串按各 vendor 自身配置生成，可能是连续拼音，也可能是形码前缀串。
```

