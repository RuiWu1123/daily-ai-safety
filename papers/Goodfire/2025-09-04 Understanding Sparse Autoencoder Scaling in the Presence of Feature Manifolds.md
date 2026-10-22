---
title: "Understanding Sparse Autoencoder Scaling in the Presence of Feature Manifolds"
lab:
  - "Goodfire"
date: 2025-09-04
source: "Goodfire Research"
url: https://www.goodfire.com/research/sae-scaling-with-feature-manifolds
other_versions:
  - "https://arxiv.org/abs/2509.02565"
star: false
tags:
  - 可解释性
---

# Understanding Sparse Autoencoder Scaling in the Presence of Feature Manifolds

**来源**：Goodfire Research · 2025-09-04 · [原文](https://www.goodfire.com/research/sae-scaling-with-feature-manifolds)　另见：[arXiv paper](https://arxiv.org/abs/2509.02565)

## 简读

Eric Michaud、Liv Gorton、Tom McGrath 的一篇短 workshop 论文，问的是 SAE 的 scaling law 背后是什么，以及 feature manifold（多维特征，如圆环、球面）会不会让 SAE 扩大时出现病态行为、加剧 interpretability "dark matter" 问题。他们把 Brill (2024) 的神经网络 capacity-allocation 模型搬到 SAE 上：在多维线性表示假设下，假设每个 latent 只服务一个特征、特征子空间彼此正交，SAE 的期望损失就分解为 Σ p_i L_i(n_i)，于是 SAE 训练变成"给每个特征分配多少个 latent"的问题。离散特征的情况下，最优解是按频率从高到低每个特征分一个 latent，若特征频率服从 p_i ∝ i^-(1+α)，损失就按 N^-α 下降，与 quanta 模型和"SAE 大致按 Zipf 频率依次学到概念"的经验一致。但在流形上 SAE 可以用越来越多、越来越稀疏的 latent 去"铺满"（tile）流形，持续小幅降低损失（圆环上可容纳几十个 latent），如果每个特征的损失按 n^-β 下降，就有一个关键阈值：α < β 时发现的特征数 D(N) ∝ N，是良性的；β < α 时损失按 N^-β 下降，D(N) ∝ N^((1+β)/(1+α))，发现效率 D(N)/N 趋于 0，latent 大量堆在常见流形上，牺牲了更稀有的特征。数值模拟里只要最常见的那个特征是流形、其余都是离散的，一个 1 亿 latent 的 SAE 就只能发现约 300 万个特征。至于真实 SAE 是否处在病态区，作者坦承没有答案，因为 α 和 β 都不知道：Gemma Scope SAE 的 latent 频率衰减斜率在 -0.57 到 -0.74 之间，暗示 α≈0.5–0.7，但 absorption 等现象会扭曲这个估计；在空心超球面上 β 可以小到约 0.05，属于危险区，然而只要流形在径向（激活强度）上有变化（这更贴近实际），SAE 大约用 2d_i 个 latent 张成一组基后损失就饱和，不会去铺满，作者认为这是反对"流形导致病态 scaling"最有力的论据。在 Gemma Scope 上测 decoder 最近邻余弦相似度，整体没有大量近乎重合的 latent，少数大于 0.97 的配对其邻居都是 dead latent，且很多活着的那一个响应单个数字或字母，作者猜测可能是训练中曾经铺过某个流形后又被 L0 压掉；Inception-v1 SAE 里高相似度 latent 比例更高，但也可能只是 L1 不惩罚重复 latent。作者把这篇定位为提出问题的框架，而不是完整的解答。

