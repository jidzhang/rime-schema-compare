# Rime 评测结果

- 生成时间: 2026-10-26 14:43:20 +0800
- 来源文件: `benchmark_zhihu120_20261026T064118264094Z_report.txt`

## Vendor 子模块版本

- `vendor/mingyuepinyin`: 小狼毫 0.17.4 自带 `luna_pinyin_simp`（经 `vendor/data` 共享）
- `vendor/rime-ice`: `75e6572bebc05b49021e842949ce947882e3e4b2`
- `vendor/rime-frost`: `328ded2ac3978c0a2b56c18b9d7ec05dd8b18130`（archive tarball 定版，无 .git）
- `vendor/rime_wanxiang` (`wanxiang`): `b935db47c516afdee06f80e041dfad6028c28b1a`（archive tarball 定版，无 .git）
- `vendor/oh-my-rime`: `5fca6ae067fd666b5ec4f119c5147efd629cc76d`（本仓新增，薄荷拼音）
- `*_with_gram` 挂载模型: `wanxiang-lts-zh-hans.gram`（398,505,004 B，sha256 `1849e5e4acbdbfaf…`，硬链接）
- `lib/rime.dll`: 3,727,872 B，sha256 `9975f25c336a9b20…`

## 评测摘要

```text
========================================================================
Rime 多方案整句评测 — 摘要报告
========================================================================
生成时间 (UTC): 20261026T064118264094Z
rime.dll: D:\work\github\IME\windows-ime-bench\engine\rime-schema-compare\lib\rime.dll
模式: 单语料 (zhihu120)

语料文件:
  - zhihu120: D:\work\github\IME\windows-ime-bench\engine\rime-schema-compare\data\corpus\zhihu120.txt

【总体】
  [mingyuepinyin]
    句子正确率: 42.5%  (51/120 句完全匹配)
    文字正确率: 84.53%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 83.96%

  [mingyuepinyin_with_gram]
    句子正确率: 48.33%  (58/120 句完全匹配)
    文字正确率: 86.23%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 86.34%

  [rime_ice]
    句子正确率: 50.83%  (61/120 句完全匹配)
    文字正确率: 90.18%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.98%

  [rime_ice_with_gram]
    句子正确率: 60.83%  (73/120 句完全匹配)
    文字正确率: 91.81%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.67%

  [rime_frost]
    句子正确率: 54.17%  (65/120 句完全匹配)
    文字正确率: 90.32%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 89.9%

  [rime_frost_with_gram]
    句子正确率: 65.83%  (79/120 句完全匹配)
    文字正确率: 92.87%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 92.71%

  [wanxiang]
    句子正确率: 46.67%  (56/120 句完全匹配)
    文字正确率: 88.84%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 88.96%

  [rime_wanxiang_with_gram]
    句子正确率: 59.17%  (71/120 句完全匹配)
    文字正确率: 91.88%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.6%

  [oh_my_rime]
    句子正确率: 47.5%  (57/120 句完全匹配)
    文字正确率: 88.28%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 88.27%

  [oh_my_rime_with_gram]
    句子正确率: 60.0%  (72/120 句完全匹配)
    文字正确率: 92.23%  (全语料金文加权，基于 Levenshtein)
    文字正确率(逐句平均): 91.77%

========================================================================
【耗时】
  读取文件: 0.09 ms
  分句: 0.31 ms
  预过滤: 0.96 ms
  [mingyuepinyin] 输入串: 7.71 ms, librime 加载: 419.04 ms, 开会话+选方案: 13.29 ms, 逐句解码: 462.87 ms
  [mingyuepinyin_with_gram] 输入串: 7.18 ms, librime 加载: 359.49 ms, 开会话+选方案: 10.58 ms, 逐句解码: 2449.68 ms
  [oh_my_rime] 输入串: 7.06 ms, librime 加载: 1045.44 ms, 开会话+选方案: 183.66 ms, 逐句解码: 2371.23 ms
  [oh_my_rime_with_gram] 输入串: 7.17 ms, librime 加载: 1015.31 ms, 开会话+选方案: 188.35 ms, 逐句解码: 2553.92 ms
  [rime_frost] 输入串: 8.34 ms, librime 加载: 6153.77 ms, 开会话+选方案: 25.81 ms, 逐句解码: 1860.74 ms
  [rime_frost_with_gram] 输入串: 7.77 ms, librime 加载: 5315.35 ms, 开会话+选方案: 25.14 ms, 逐句解码: 1867.24 ms
  [rime_ice] 输入串: 8.38 ms, librime 加载: 1309.87 ms, 开会话+选方案: 33.59 ms, 逐句解码: 647.55 ms
  [rime_ice_with_gram] 输入串: 7.99 ms, librime 加载: 1308.74 ms, 开会话+选方案: 28.87 ms, 逐句解码: 1618.04 ms
  [rime_wanxiang_with_gram] 输入串: 7.11 ms, librime 加载: 8010.51 ms, 开会话+选方案: 1242.15 ms, 逐句解码: 2811.93 ms
  [wanxiang] 输入串: 7.93 ms, librime 加载: 8134.55 ms, 开会话+选方案: 1219.46 ms, 逐句解码: 2824.36 ms
  写出结果文件: 71.3 ms

========================================================================
句子正确判定: Top 1 候选中任一项与 gold 完全一致即判对。

同义词归一化（句级完全匹配与 CER 计算前）: 其它→其他；他/她/它→他；的/地/得→的

说明: 分句后仅「纯汉字」且不含 ASCII 数字/英文字母、汉字不少于 5 字的片段参与评测；其它片段已过滤。句子正确率 = 归一化后预测与金句完全一致的比例；文字正确率 = 全语料 (归一化后总字数−总编辑距离)/归一化后总字数。输入串按各 vendor 自身配置生成，可能是连续拼音，也可能是形码前缀串。```

## 说明

- 语料为本机 benchmark 仓正式整句卷 `zhihu120`（n=120，与黑盒榜同卷同判分）；
- 全部方案按「无语言模型、无用户词库」口径（`*_with_gram` 变体额外挂同一 gram 模型）；
- 薄荷拼音（oh-my-rime）为本仓新增 vendor；魔然为双拼+形码体系，不参评；
- 词级 words234（n=450）与三道闸验证见 `report/whitebox_2026-10-26.md` 与
  benchmark 仓 `results/whitebox_rime_report.md`（正式结论在主仓）。
