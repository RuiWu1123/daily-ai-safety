---
title: "[Paper] Stochastic Parameter Decomposition"
lab:
  - "Alignment Forum"
date: 2025-06-27
source: "Alignment Forum（Goodfire；Lee Sharkey, Lucius Bushnaq, Dan Braun）"
url: https://www.alignmentforum.org/posts/yjrpmCmqurDmbMztW
tags:
  - 可解释性
---

# [Paper] Stochastic Parameter Decomposition

**来源**：Alignment Forum（Goodfire；Lee Sharkey, Lucius Bushnaq, Dan Braun） · 2025-06-27 · [原文](https://www.alignmentforum.org/posts/yjrpmCmqurDmbMztW)

## 简读

Lee Sharkey、Lucius Bushnaq、Dan Braun 提出 Stochastic Parameter Decomposition（SPD），属于 linear parameter decomposition 框架：把网络参数分解成在参数空间里被稀疏使用的向量之和，作为逆向工程网络的基本单元，以回避现有激活分解方法的一些问题。此前该框架的主力方法 APD（Attribution-based Parameter Decomposition）计算代价高、对超参敏感，难以实用。SPD 更可扩展、对超参更鲁棒，能分解比 APD 能处理的稍大、稍复杂一些的模型，同时避免了学到参数的 shrinkage 问题，并在 toy model 中更准确地识别出 ground truth 机制。作者把它定位为连接 causal mediation analysis 与网络分解方法、扫清参数分解方法扩展到更大模型的障碍的一步。代码库开源（goodfire-ai/spd），可复现实验。帖子本身只有摘要，细节需看 arXiv 论文。
