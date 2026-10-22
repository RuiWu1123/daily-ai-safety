---
title: "RL with KL penalties is better viewed as Bayesian inference"
lab:
  - "FAR.AI"
date: 2022-08-07
source: "FAR.AI Publications"
url: https://www.far.ai/research/rl-with-kl-penalties-is-better-viewed-as-bayesian-inference
tags:
  - 对齐训练方法
---

# RL with KL penalties is better viewed as Bayesian inference

**来源**：FAR.AI Publications · 2022-08-07 · [原文](https://www.far.ai/research/rl-with-kl-penalties-is-better-viewed-as-bayesian-inference)

## 简读

Korbak、Perez、Buckley 的一篇短理论文，想讲清楚 RLHF 里的 KL penalty 为什么必要。出发点是把 LM 当 RL policy 最大化期望 reward 本身有缺陷：LM 没有 state，标准 RL 目标退化为寻找单个最高 reward 序列，最优解是 Dirac delta，即 distribution collapse，经验上表现为流畅度和多样性下降。作者强调这与 exploration 不足或 reward misspecification 无关：即使 reward 完美、探索完美，我们也不想让 LM 只输出一个句子（不确定性估计、MBR decoding、self-consistency 都依赖完整分布）。核心论点是 KL-regularised RL（E[r] − β·KL(πθ‖π0)）等价于 variational inference：目标是后验 π* ∝ π0·exp(r/β)，原 LM 是 prior，reward 提供 evidence，KL-RL 目标正比于 −KL(πθ‖π*)，即 ELBO；KL 项正是把 reward maximisation 变成 divergence minimisation 的那一项，这解释了它为何能保持原 LM 的分布特性。由此拆出 modelling（定义目标分布，比如用 π0(x)b(x) 禁止脏话而不动其它序列）和 inference（逼近它：fine-tuning 对应变分推断，rejection sampling、PPLM 等 decoding-time 方法对应采样式推断），好处是把"偏好没刻画对"和"没逼近好"两类失败分开。作者还做了 double dissociation 论证：没有 KL 的 RL 会退化，而非 RL 的 divergence minimisation（forward KL 的 GDC、普通 MLE）效果很好，所以起作用的是 divergence minimisation，叫它 RL 只是特定 reward 下碰巧成立的重述，RL 并不是 fine-tune LM 的合适框架。局限部分承认没讨论 reward model 的 proxy 性和标注者分歧（annotator 间一致率约 68–72%），贝叶斯视角也解释不了 reward 与 √KL 近似线性的经验规律，对超参选择给不出指导。

## 我的笔记

