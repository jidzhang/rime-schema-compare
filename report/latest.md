# Rime 评测结果

- 生成时间: 2026-05-12 23:27:01 +08:00
- 来源文件: `benchmark_all_corpus_20260512T152519476671Z_report.txt`

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
生成时间 (UTC): 20260512T152519476671Z
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
    句子正确率: 40.26%  (219/544 句完全匹配)
    文字正确率: 82.9%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 82.22%

  [mingyuepinyin_with_gram]
    句子正确率: 33.82%  (184/544 句完全匹配)
    文字正确率: 80.05%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 79.33%

  [rime_ice]
    句子正确率: 41.73%  (227/544 句完全匹配)
    文字正确率: 84.17%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 83.21%

  [rime_ice_with_gram]
    句子正确率: 47.24%  (257/544 句完全匹配)
    文字正确率: 86.47%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 85.05%

  [rime_frost]
    句子正确率: 46.88%  (255/544 句完全匹配)
    文字正确率: 86.25%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 84.87%

  [rime_frost_with_gram]
    句子正确率: 54.04%  (294/544 句完全匹配)
    文字正确率: 88.55%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 87.05%

  [wanxiang]
    句子正确率: 37.87%  (206/544 句完全匹配)
    文字正确率: 83.2%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 82.14%

  [rime_wanxiang_with_gram]
    句子正确率: 47.79%  (260/544 句完全匹配)
    文字正确率: 86.43%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 85.4%

  [rime_wubi_sentens_wubi86]
    句子正确率: 44.85%  (244/544 句完全匹配)
    文字正确率: 86.66%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 86.03%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 55.15%  (300/544 句完全匹配)
    文字正确率: 90.69%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.86%

------------------------------------------------------------------------
【语料: news】
  [mingyuepinyin]
    句子正确率: 54.61%  (83/152 句完全匹配)
    文字正确率: 87.95%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.31%

  [mingyuepinyin_with_gram]
    句子正确率: 40.79%  (62/152 句完全匹配)
    文字正确率: 83.05%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 83.57%

  [rime_ice]
    句子正确率: 57.89%  (88/152 句完全匹配)
    文字正确率: 89.66%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.36%

  [rime_ice_with_gram]
    句子正确率: 60.53%  (92/152 句完全匹配)
    文字正确率: 91.2%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.11%

  [rime_frost]
    句子正确率: 65.13%  (99/152 句完全匹配)
    文字正确率: 91.73%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 92.34%

  [rime_frost_with_gram]
    句子正确率: 71.71%  (109/152 句完全匹配)
    文字正确率: 94.51%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 94.58%

  [wanxiang]
    句子正确率: 50.66%  (77/152 句完全匹配)
    文字正确率: 89.72%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.18%

  [rime_wanxiang_with_gram]
    句子正确率: 61.84%  (94/152 句完全匹配)
    文字正确率: 91.79%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.92%

  [rime_wubi_sentens_wubi86]
    句子正确率: 52.63%  (80/152 句完全匹配)
    文字正确率: 90.67%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.01%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 65.79%  (100/152 句完全匹配)
    文字正确率: 94.15%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 94.17%

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
    句子正确率: 20.95%  (44/210 句完全匹配)
    文字正确率: 72.82%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 72.01%

  [mingyuepinyin_with_gram]
    句子正确率: 25.71%  (54/210 句完全匹配)
    文字正确率: 73.42%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 72.26%

  [rime_ice]
    句子正确率: 23.33%  (49/210 句完全匹配)
    文字正确率: 74.56%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 73.74%

  [rime_ice_with_gram]
    句子正确率: 28.57%  (60/210 句完全匹配)
    文字正确率: 76.8%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 75.53%

  [rime_frost]
    句子正确率: 21.9%  (46/210 句完全匹配)
    文字正确率: 74.24%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 72.99%

  [rime_frost_with_gram]
    句子正确率: 28.1%  (59/210 句完全匹配)
    文字正确率: 76.58%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 75.27%

  [wanxiang]
    句子正确率: 21.43%  (45/210 句完全匹配)
    文字正确率: 72.76%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 71.97%

  [rime_wanxiang_with_gram]
    句子正确率: 30.0%  (63/210 句完全匹配)
    文字正确率: 77.73%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 76.53%

  [rime_wubi_sentens_wubi86]
    句子正确率: 29.05%  (61/210 句完全匹配)
    文字正确率: 77.95%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 77.45%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 36.67%  (77/210 句完全匹配)
    文字正确率: 83.79%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 82.68%

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
【总耗时】全流程墙钟约 101087.99 ms（多语料）

【各语料耗时】
  · news
    读取文件: 0.13 ms
    分句: 0.91 ms
    预过滤: 18.37 ms
    [mingyuepinyin] 输入串: 8.42 ms, librime 加载: 353.28 ms, 开会话+选方案: 30.57 ms, 逐句解码: 298.02 ms
    [mingyuepinyin_with_gram] 输入串: 8.06 ms, librime 加载: 323.54 ms, 开会话+选方案: 30.5 ms, 逐句解码: 341.68 ms
    [rime_frost] 输入串: 8.13 ms, librime 加载: 1109.47 ms, 开会话+选方案: 45.44 ms, 逐句解码: 839.47 ms
    [rime_frost_with_gram] 输入串: 8.35 ms, librime 加载: 1123.04 ms, 开会话+选方案: 57.93 ms, 逐句解码: 856.29 ms
    [rime_ice] 输入串: 9.42 ms, librime 加载: 1063.04 ms, 开会话+选方案: 32.62 ms, 逐句解码: 350.72 ms
    [rime_ice_with_gram] 输入串: 7.77 ms, librime 加载: 1059.83 ms, 开会话+选方案: 38.07 ms, 逐句解码: 370.18 ms
    [rime_wanxiang_with_gram] 输入串: 7.57 ms, librime 加载: 359.88 ms, 开会话+选方案: 1216.01 ms, 逐句解码: 3055.42 ms
    [rime_wubi_sentens_wubi86] 输入串: 101.33 ms, librime 加载: 830.36 ms, 开会话+选方案: 366.37 ms, 逐句解码: 451.84 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 107.77 ms, librime 加载: 832.55 ms, 开会话+选方案: 381.21 ms, 逐句解码: 490.63 ms
    [wanxiang] 输入串: 7.66 ms, librime 加载: 363.56 ms, 开会话+选方案: 1253.46 ms, 逐句解码: 3031.25 ms
  · novel
    读取文件: 0.18 ms
    分句: 0.12 ms
    预过滤: 0.09 ms
    [mingyuepinyin] 输入串: 1.83 ms, librime 加载: 382.92 ms, 开会话+选方案: 25.7 ms, 逐句解码: 86.75 ms
    [mingyuepinyin_with_gram] 输入串: 2.1 ms, librime 加载: 387.44 ms, 开会话+选方案: 23.74 ms, 逐句解码: 97.27 ms
    [rime_frost] 输入串: 4.71 ms, librime 加载: 1959.86 ms, 开会话+选方案: 81.59 ms, 逐句解码: 596.34 ms
    [rime_frost_with_gram] 输入串: 3.4 ms, librime 加载: 1955.45 ms, 开会话+选方案: 117.67 ms, 逐句解码: 538.54 ms
    [rime_ice] 输入串: 1.7 ms, librime 加载: 1075.71 ms, 开会话+选方案: 52.54 ms, 逐句解码: 101.56 ms
    [rime_ice_with_gram] 输入串: 2.02 ms, librime 加载: 1307.92 ms, 开会话+选方案: 60.99 ms, 逐句解码: 223.89 ms
    [rime_wanxiang_with_gram] 输入串: 5.15 ms, librime 加载: 621.58 ms, 开会话+选方案: 2793.75 ms, 逐句解码: 1969.25 ms
    [rime_wubi_sentens_wubi86] 输入串: 44.08 ms, librime 加载: 1390.83 ms, 开会话+选方案: 787.34 ms, 逐句解码: 211.07 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 28.8 ms, librime 加载: 1036.34 ms, 开会话+选方案: 381.45 ms, 逐句解码: 112.97 ms
    [wanxiang] 输入串: 3.51 ms, librime 加载: 599.87 ms, 开会话+选方案: 2868.14 ms, 逐句解码: 1851.73 ms
  · prose
    读取文件: 0.18 ms
    分句: 0.63 ms
    预过滤: 0.46 ms
    [mingyuepinyin] 输入串: 9.18 ms, librime 加载: 325.47 ms, 开会话+选方案: 18.16 ms, 逐句解码: 399.21 ms
    [mingyuepinyin_with_gram] 输入串: 8.23 ms, librime 加载: 358.99 ms, 开会话+选方案: 13.75 ms, 逐句解码: 439.05 ms
    [rime_frost] 输入串: 8.22 ms, librime 加载: 1112.51 ms, 开会话+选方案: 47.71 ms, 逐句解码: 1152.48 ms
    [rime_frost_with_gram] 输入串: 8.97 ms, librime 加载: 1138.12 ms, 开会话+选方案: 43.07 ms, 逐句解码: 1204.85 ms
    [rime_ice] 输入串: 8.64 ms, librime 加载: 1086.37 ms, 开会话+选方案: 27.66 ms, 逐句解码: 424.73 ms
    [rime_ice_with_gram] 输入串: 8.45 ms, librime 加载: 1084.37 ms, 开会话+选方案: 29.51 ms, 逐句解码: 532.53 ms
    [rime_wanxiang_with_gram] 输入串: 8.48 ms, librime 加载: 367.34 ms, 开会话+选方案: 1217.35 ms, 逐句解码: 4090.04 ms
    [rime_wubi_sentens_wubi86] 输入串: 36.42 ms, librime 加载: 824.26 ms, 开会话+选方案: 373.64 ms, 逐句解码: 587.3 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 35.58 ms, librime 加载: 804.54 ms, 开会话+选方案: 365.04 ms, 逐句解码: 547.97 ms
    [wanxiang] 输入串: 8.67 ms, librime 加载: 372.98 ms, 开会话+选方案: 1224.36 ms, 逐句解码: 4017.81 ms
  · tech
    读取文件: 0.17 ms
    分句: 0.5 ms
    预过滤: 0.28 ms
    [mingyuepinyin] 输入串: 6.88 ms, librime 加载: 373.78 ms, 开会话+选方案: 29.01 ms, 逐句解码: 254.33 ms
    [mingyuepinyin_with_gram] 输入串: 6.87 ms, librime 加载: 339.58 ms, 开会话+选方案: 36.43 ms, 逐句解码: 287.75 ms
    [rime_frost] 输入串: 7.55 ms, librime 加载: 1149.31 ms, 开会话+选方案: 59.76 ms, 逐句解码: 712.99 ms
    [rime_frost_with_gram] 输入串: 6.73 ms, librime 加载: 1145.11 ms, 开会话+选方案: 92.5 ms, 逐句解码: 734.22 ms
    [rime_ice] 输入串: 7.1 ms, librime 加载: 1083.41 ms, 开会话+选方案: 25.19 ms, 逐句解码: 285.1 ms
    [rime_ice_with_gram] 输入串: 6.91 ms, librime 加载: 1078.46 ms, 开会话+选方案: 40.69 ms, 逐句解码: 328.84 ms
    [rime_wanxiang_with_gram] 输入串: 6.94 ms, librime 加载: 370.94 ms, 开会话+选方案: 1235.84 ms, 逐句解码: 2562.9 ms
    [rime_wubi_sentens_wubi86] 输入串: 24.49 ms, librime 加载: 823.77 ms, 开会话+选方案: 365.28 ms, 逐句解码: 463.31 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 23.54 ms, librime 加载: 825.84 ms, 开会话+选方案: 363.62 ms, 逐句解码: 403.78 ms
    [wanxiang] 输入串: 6.88 ms, librime 加载: 371.96 ms, 开会话+选方案: 1253.63 ms, 逐句解码: 2475.47 ms
  · test
    读取文件: 0.16 ms
    分句: 0.02 ms
    预过滤: 0.02 ms
    [mingyuepinyin] 输入串: 0.38 ms, librime 加载: 327.93 ms, 开会话+选方案: 21.84 ms, 逐句解码: 8.33 ms
    [mingyuepinyin_with_gram] 输入串: 0.39 ms, librime 加载: 353.19 ms, 开会话+选方案: 16.67 ms, 逐句解码: 10.77 ms
    [rime_frost] 输入串: 0.37 ms, librime 加载: 1136.37 ms, 开会话+选方案: 81.89 ms, 逐句解码: 19.33 ms
    [rime_frost_with_gram] 输入串: 0.41 ms, librime 加载: 1145.29 ms, 开会话+选方案: 82.81 ms, 逐句解码: 20.8 ms
    [rime_ice] 输入串: 0.46 ms, librime 加载: 1075.27 ms, 开会话+选方案: 29.35 ms, 逐句解码: 24.75 ms
    [rime_ice_with_gram] 输入串: 0.38 ms, librime 加载: 1069.39 ms, 开会话+选方案: 24.66 ms, 逐句解码: 26.41 ms
    [rime_wanxiang_with_gram] 输入串: 0.35 ms, librime 加载: 370.54 ms, 开会话+选方案: 1281.1 ms, 逐句解码: 68.41 ms
    [rime_wubi_sentens_wubi86] 输入串: 1.02 ms, librime 加载: 827.26 ms, 开会话+选方案: 365.96 ms, 逐句解码: 22.29 ms
    [rime_wubi_sentens_wubi86_with_gram] 输入串: 1.03 ms, librime 加载: 807.51 ms, 开会话+选方案: 362.21 ms, 逐句解码: 25.45 ms
    [wanxiang] 输入串: 0.35 ms, librime 加载: 381.91 ms, 开会话+选方案: 1283.81 ms, 逐句解码: 65.22 ms

========================================================================
句子正确判定: Top 1 候选中任一项与 gold 完全一致即判对。

同义词归一化（句级完全匹配与 CER 计算前）: 其它→其他；他/她/它→他；的/地/得→的

说明: 分句后仅「纯汉字」且不含 ASCII 数字/英文字母、汉字不少于 5 字的片段参与评测；其它片段已过滤。句子正确率 = 归一化后预测与金句完全一致的比例；文字正确率 = 全语料 (归一化后总字数−总编辑距离)/归一化后总字数。输入串按各 vendor 自身配置生成，可能是连续拼音，也可能是形码前缀串。
```

