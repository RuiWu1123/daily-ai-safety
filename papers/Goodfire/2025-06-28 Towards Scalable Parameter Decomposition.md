---
title: "Towards Scalable Parameter Decomposition"
lab:
  - "Goodfire"
date: 2025-06-28
source: "Goodfire Research"
url: https://www.goodfire.com/research/stochastic-param-decomp
star: false
tags:
  - 可解释性
---

# Towards Scalable Parameter Decomposition

**来源**：Goodfire Research · 2025-06-28 · [原文](https://www.goodfire.com/research/stochastic-param-decomp)

## 简读

这是 Stochastic Parameter Decomposition（SPD）论文的博客介绍（Bushnaq、Braun、Sharkey，工作主要在 Apollo Research 完成）。动机是 SAE 等 sparse dictionary learning 只分解激活，相当于只看程序运行时的变量而不看源码：它们解释不了 feature geometry，把 SAE 做大也不会收敛到一个"真实"分解，只会得到越来越细的 feature，看到的是计算投在激活上的影子而不是计算本身。parameter decomposition 直接分解权重，目标是找到 faithful（加起来等于原模型）、minimal（对每个输入用尽量少的组件）、simple（组件尽量小）的参数组件，并且这种分解也能直接翻译回激活空间。前作 APD 用 gradient attribution 判断哪些组件重要，但对超参太敏感、算力开销太大，无法走出玩具模型。SPD 的做法是把每个权重矩阵分解成 rank-one subcomponent，为每个 subcomponent 训练一个小 MLP 预测它在给定输入上的 causal importance，再按这个重要性对组件做随机 mask，同时要求输出保持不变、尽可能多地 ablate，有点像在玩 Jenga，也可以理解为极细粒度的 Mixture-of-Experts 蒸馏；通过在大量随机 ablation 模式上训练，绕开了梯度近似可能带来的误导。在已知 ground truth 的玩具模型上：Toy Model of Superposition 里每个 feature 方向都恢复成一个 subcomponent，多余的组件 norm 被训练到接近 0，且没有 APD 的参数收缩问题；加入 identity 矩阵（APD 的难点）时得到恰好预期的组件；还能分解机制跨三层的网络，这是 APD 做不到的。最重要的是对超参明显更稳健，虽然仍有一定敏感性。局限也写得明白：还需要一个聚类步骤把 rank-one subcomponent 拼成完整机制，计算代价不小（可能和 SDL 相当），而且只在知道答案的模型上测过。下一步是扩展到语言模型，研究算术、语法、事实召回等能力对应的参数组件，参数如何在记忆与泛化之间分配、能否定位安全相关行为的参数，以及训练天生可分解的模型。

