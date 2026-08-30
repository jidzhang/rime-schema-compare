# Rime 评测结果

- 生成时间: 2026-08-30 14:30:55 +08:00
- 来源文件: `benchmark_zhihu_hotlist_2026-08-30_20260830T062310264548Z_report.txt`

## Vendor 子模块版本

- `vendor/rime-frost`: `328ded2ac3978c0a2b56c18b9d7ec05dd8b18130`
- `vendor/rime-ice`: `75e6572bebc05b49021e842949ce947882e3e4b2`
- `vendor/rime_wanxiang` (`wanxiang`): `b935db47c516afdee06f80e041dfad6028c28b1a`
- `vendor/rime-wubi-sentence`: `edb9437d18d7d45239fd8f8303ddd836efa69749`

## 评测摘要

```text
========================================================================
Rime 多方案整句评测 — 摘要报告
========================================================================
生成时间 (UTC): 20260830T062310264548Z
rime.dll: D:\vscode\rime_projs\rime-schema-compare\lib\rime.dll
模式: 单语料 (zhihu_hotlist_2026-08-30)

语料文件:
  - zhihu_hotlist_2026-08-30: D:\vscode\rime_projs\rime-schema-compare\data\corpus\zhihu_hotlist_2026-08-30.txt

【总体】
  [mingyuepinyin]
    句子正确率: 47.49%  (1646/3466 句完全匹配)
    文字正确率: 87.25%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 87.32%

  [mingyuepinyin_with_gram]
    句子正确率: 40.33%  (1398/3466 句完全匹配)
    文字正确率: 84.14%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 84.49%

  [rime_ice]
    句子正确率: 53.29%  (1847/3466 句完全匹配)
    文字正确率: 89.67%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.58%

  [rime_ice_with_gram]
    句子正确率: 59.09%  (2048/3466 句完全匹配)
    文字正确率: 90.7%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.7%

  [rime_frost]
    句子正确率: 61.19%  (2121/3466 句完全匹配)
    文字正确率: 92.08%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.93%

  [rime_frost_with_gram]
    句子正确率: 65.87%  (2283/3466 句完全匹配)
    文字正确率: 93.04%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 93.06%

  [wanxiang]
    句子正确率: 54.33%  (1883/3466 句完全匹配)
    文字正确率: 90.34%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.19%

  [rime_wanxiang_with_gram]
    句子正确率: 63.85%  (2213/3466 句完全匹配)
    文字正确率: 92.47%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 92.44%

  [rime_wubi_sentens_wubi86]
    句子正确率: 54.93%  (1904/3466 句完全匹配)
    文字正确率: 90.82%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 90.8%

  [rime_wubi_sentens_wubi86_with_gram]
    句子正确率: 64.83%  (2247/3466 句完全匹配)
    文字正确率: 93.73%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 93.62%

========================================================================
【耗时】
  读取文件: 0.52 ms
  分句: 11.92 ms
  预过滤: 8.12 ms
  [mingyuepinyin] 输入串: 174.25 ms, librime 加载: 397.47 ms, 开会话+选方案: 26.87 ms, 逐句解码: 6466.85 ms
  [mingyuepinyin_with_gram] 输入串: 174.84 ms, librime 加载: 379.14 ms, 开会话+选方案: 23.9 ms, 逐句解码: 6959.63 ms
  [rime_frost] 输入串: 176.73 ms, librime 加载: 1157.8 ms, 开会话+选方案: 51.63 ms, 逐句解码: 30713.01 ms
  [rime_frost_with_gram] 输入串: 178.0 ms, librime 加载: 7173.55 ms, 开会话+选方案: 64.61 ms, 逐句解码: 66195.09 ms
  [rime_ice] 输入串: 174.41 ms, librime 加载: 1089.39 ms, 开会话+选方案: 27.41 ms, 逐句解码: 6870.64 ms
  [rime_ice_with_gram] 输入串: 175.03 ms, librime 加载: 5088.71 ms, 开会话+选方案: 31.09 ms, 逐句解码: 7495.83 ms
  [rime_wanxiang_with_gram] 输入串: 464.36 ms, librime 加载: 13243.01 ms, 开会话+选方案: 3440.11 ms, 逐句解码: 123413.19 ms
  [rime_wubi_sentens_wubi86] 输入串: 2494.39 ms, librime 加载: 1710.09 ms, 开会话+选方案: 818.57 ms, 逐句解码: 19663.85 ms
  [rime_wubi_sentens_wubi86_with_gram] 输入串: 2795.79 ms, librime 加载: 5160.65 ms, 开会话+选方案: 858.81 ms, 逐句解码: 20108.86 ms
  [wanxiang] 输入串: 411.37 ms, librime 加载: 833.48 ms, 开会话+选方案: 3246.17 ms, 逐句解码: 119161.99 ms
  写出结果文件: 870.98 ms

========================================================================
句子正确判定: Top 1 候选中任一项与 gold 完全一致即判对。

同义词归一化（句级完全匹配与 CER 计算前）: 其它→其他；他/她/它→他；的/地/得→的

说明: 分句后仅「纯汉字」且不含 ASCII 数字/英文字母、汉字不少于 5 字的片段参与评测；其它片段已过滤。句子正确率 = 归一化后预测与金句完全一致的比例；文字正确率 = 全语料 (归一化后总字数−总编辑距离)/归一化后总字数。输入串按各 vendor 自身配置生成，可能是连续拼音，也可能是形码前缀串。
```

