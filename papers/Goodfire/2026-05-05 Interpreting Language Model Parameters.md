---
title: "Interpreting Language Model Parameters"
lab:
  - "Goodfire"
date: 2026-05-05
source: "Goodfire Research"
url: https://www.goodfire.com/research/interpreting-lm-parameters
other_versions:
  - "https://www.goodfire.com/research/vpd-explainer"
star: false
tags:
  - 可解释性
---

# Interpreting Language Model Parameters

**来源**：Goodfire Research · 2026-05-05 · [原文](https://www.goodfire.com/research/interpreting-lm-parameters)　另见：[Goodfire paper summary](https://www.goodfire.com/research/vpd-explainer)

## 简读

背景是 mech interp 对中间表征已经有不少发现，但对参数和非线性如何在这些表征上实际完成计算进展很少；transcoder、CLT 等 activation-based 方法用另一种函数形式去拟合层间映射，很难把解释对应回真正做计算的参数，因此难以精确编辑参数、也难预测换分布后的行为，还存在 feature splitting 等问题。这篇 Goodfire 的长文提出 adVersarial Parameter Decomposition（VPD），沿 APD、SPD 的 ablation-based 参数分解思路，把每个权重矩阵分解成 rank-1 subcomponent，要求它们满足四个性质：求和等于原参数（parameter-faithful）、每个输入上只需极少数是 causally important（minimal）、包含这些重要分量的任意子集都足以复现输出（mechanistically faithful）、每个分量尽量简单。与 SPD 的关键区别是检查"不重要分量能否任意组合地部分消融"时用对抗性挑选的 mask（PGD）而非随机采样，并新增 frequency-minimality loss 鼓励计算简单。他们首次把参数分解扩展到完整语言模型：一个在 Pile 上训练的 4 层 67M 参数 transformer，24 个矩阵分成 38,912 个 subcomponent，实际存活约一万个，每个位置平均只用 205 个（约 2.1%）。主要结果：1. 分解后模型验证 CE 在 2.72–3.02 之间（原模型 2.71），对约 20 步对抗优化有一定鲁棒性，但 320 步时 KL 大幅上升；2. 同时替换全部 4 个 MLP 层时，在三种稀疏度定义下都 Pareto 优于 BatchTopK 的 per-layer transcoder 和 CLT（匹配训练目标后优势消失，但不像后者那样过拟合自己的训练目标），intruder detection 的可解释性与逐层训练的 transcoder 相当、优于端到端训练的；3. 加大容量时存活分量数稳定在约 6,500–7,000 个，而 transcoder 随字典大小线性增长，说明 VPD 不做 feature splitting，原因正是"任意组合可消融"的约束；4. attention 层的分量有清晰功能（如 copula 动词、"there/it" 等），且大多跨多个 head，能分解 previous-token、句法边界移动、存在句 vs 虚主语等分布在多 head 上的行为；5. 基于分量的 attribution graph 用于做 circuit 分析，如"The princess lost her crown"中预测 her 的两条通路、括号闭合，CI 剪枝得到的六分量小图足以产生输出但对抗下不鲁棒，作者坦言远非完整解释；6. 手工修改一个 emoticon 相关 rank-1 分量的写方向，使模型把各种表情都补全为 ":o"，与 LoRA 基线比较 off-target 效应，作者承认例子是挑过的。讨论部分很诚实：attribution graph 不等于 computational graph，还没解释非线性上的交互；需要多少对抗鲁棒性才能让局部解释聚合成全局解释没有答案；参数 MDL 只是计算简单性的代理；只在小模型上做过。代码库已开源。

