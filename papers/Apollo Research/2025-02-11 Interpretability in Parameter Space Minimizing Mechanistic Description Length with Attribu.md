---
title: "Interpretability in Parameter Space: Minimizing Mechanistic Description Length with Attribution-based Parameter Decomposition"
lab:
  - "Apollo Research"
date: 2025-02-11
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/interpretability-in-parameter-space-minimizing-mechanistic-description-length-with-attribution-based-parameter-decomposition
star: false
tags:
  - 可解释性
---

# Interpretability in Parameter Space: Minimizing Mechanistic Description Length with Attribution-based Parameter Decomposition

**来源**：Apollo Research · 2025-02-11 · [原文](https://www.apolloresearch.ai/science/interpretability-in-parameter-space-minimizing-mechanistic-description-length-with-attribution-based-parameter-decomposition)

## 简读

Apollo 的 Dan Braun、Lucius Bushnaq、Stefan Heimersheim、Jake Mendel、Lee Sharkey 提出 Attribution-based Parameter Decomposition（APD，arXiv 2501.14926），是一种“parameters-first”的机制可解释性方法。背景是机制组件通常不对应单个 neuron、attention head 或层，而主流的稀疏字典学习（SAE 等 activations-first 方法）有重构误差大、未必找到规范分析单元、以稀疏性作为可解释性代理未必可靠、feature splitting、无法解释 feature geometry、latent 之间连接不一定稀疏等问题。APD 受最小描述长度原则启发，把网络的参数向量直接分解成若干参数分量（parameter component）之和，每个分量对应一个“机制”，可跨多个 neuron 甚至多层，也可以是多维的。三个目标对应三个 loss：1. faithfulness，各分量之和用 MSE 逼近原网络参数；2. minimality，先用梯度 attribution 估计每个分量对输出的贡献，用 batch top-k 只保留最重要的分量重新做一次前向，并训练其输出（有时也包括部分隐藏激活）与原网络一致，即任一输入只需少数分量；3. simplicity，用 Schatten-p 准范数惩罚活跃分量的秩之和。他们在三个已知 ground truth 的 toy 模型上验证：Elhage et al. 的 toy model of superposition，APD 恢复出每个叠加特征对应的 rank-1 权重分量，MMCS 约 0.998/0.996，但 ML2R 约 0.89/0.94，存在类似 SAE 的 shrinkage，而 SVD、NMF 等最多只能找 min(m1,m2) 个分量，原理上做不到；一个 compressed computation 模型，单层 50 个 neuron 的残差 MLP 要对 100 个输入计算 y=x+ReLU(x)，APD 找到了每个输入各自对应的分量（用 130 个分量训练，因为会有分量“死掉”），causal-scrubbing 式消融显示去掉无关分量影响很小、去掉负责的分量 loss 大增，但部分分量混入了次要特征，形成双峰分布；扩展到两层、每层 25 个 neuron 的跨层分布表示，APD 也能学到横跨两层的分量，但更多分量同时表示两个特征。作者认为这一视角给出若干开放问题的思路：直接得到 superposition 中的最小电路；把 feature 定义为“激活特定机制的输入属性”，并因为必须与参数相加一致而避免 feature splitting；有助于理解 feature geometry；对架构无关。局限也很明确：目前只适合 toy 模型，计算成本最坏可达 O(N²)，需要大量超参数调优，梯度 attribution 只是一阶近似，top-k 造成机制混合，用秩衡量简单性还会让层略带特权。后续方向是做更鲁棒可扩展的 APD 类方法，或按这些原则设计天然可分解的架构（如多专家、跨层 MoE），潜在应用包括机制异常检测、精确编辑和 unlearning，以及研究记忆与泛化的机制。代码在 github.com/ApolloResearch/apd。

