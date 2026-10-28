# 自训 gram 管线（已迁出）

> 2026-10-28 迁往墨奇引擎仓：`Z:\dev\IME\MoqiIME\moqi-ime\tools\gram-train\`
> （MoqiIME commit `d0a0eaf`）。理由：模型训练出来是给墨奇输入法用的，管线住引擎仓；
> 本仓是方案横评仓，不该背负 82MB 模型产物与编译器二进制。

迁移时全链路复现验证：留存的 6 份维基挖掘 TSV（`gram_train/w{AF,BF,EF,Cx,Dx,Fx}-bigram.txt`，
未跟踪，仍在磁盘）→ `convert_bigrams.py` → `build_grammar.exe`，产出与产品模型
`zh-moqi-wiki.gram` **逐字节一致**（sha256 `996c096c…`）。一键重建脚本与 TSV hash 锁定
（`SHA256SUMS.artifacts`）都在新家。

模型沿革与评测结论见新位置 README；历史报告（`report/`、bench 仓
`results/native_stack_2026-10-27.md`）中的数字不受迁移影响。
