---
title: "The Local Interaction Basis: Identifying Computationally-Relevant and Sparsely Interacting Features in Neural Networks"
lab:
  - "Apollo Research"
date: 2024-05-30
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/the-local-interaction-basis-identifying-computationally-relevant-and-sparsely-interacting-features-in-neural-networks
star: false
tags:
  - 可解释性
---

# The Local Interaction Basis: Identifying Computationally-Relevant and Sparsely Interacting Features in Neural Networks

**来源**：Apollo Research · 2024-05-30 · [原文](https://www.apolloresearch.ai/science/the-local-interaction-basis-identifying-computationally-relevant-and-sparsely-interacting-features-in-neural-networks)

## 简读

Apollo（Lucius Bushnaq 等）一组两篇 interpretability 工作，核心是一个诚实的负结果。动机是 mech interp 缺少从第一性原理出发的特征表示，他们想从 loss landscape 的结构出发（受 singular learning theory 启发）。第一篇（ICML workshop spotlight）研究参数化中不影响输入输出的 degeneracy，归纳出三种来源：激活线性相关、梯度线性相关、ReLU 在相同输入上激活，并推出 interaction basis。第二篇实测 Local Interaction Basis（LIB）：每层先 PCA 去掉零方差方向并白化，再从输出层往回，对相邻层 Jacobian 做 SVD，去掉对下一层无影响的方向，使交互稀疏；然后用 integrated gradients 构建全网络交互图并找模块。方法刻意假设非 overcomplete 的基、不假设 superposition，作为与主流研究去相关的押注。toy model 上效果不错：modular addition transformer 的模块对应不同 Fourier 频率（作者注明是 5 个 seed 中挑的最干净的一个），中间层计算无关特征 PCA 约 14 个，LIB 只有 3 个；CIFAR-10 MLP 上 LIB 交互始终比 PCA 稀疏，还找到了"动物 vs 车辆"方向。但在语言模型上基本失败：GPT2-small 前几个方向是位置特征，其余和 PCA 一样难以解释；edge ablation 下两种基都能剪掉 80%–95% 的边，LIB 只略好，也没有找到模块化证据。作者推测原因是"线性、非 overcomplete"假设对 LM 不成立，下一步打算推广到允许 superposition 的情形。代码已开源。

