---
title: "Meandering on Manifolds: The Neural Geometry of Stories Over Time"
lab:
  - "Goodfire"
date: 2026-06-23
source: "Goodfire Research"
url: https://www.goodfire.com/research/stories-in-space
star: false
tags:
  - 可解释性
---

# Meandering on Manifolds: The Neural Geometry of Stories Over Time

**来源**：Goodfire Research · 2026-06-23 · [原文](https://www.goodfire.com/research/stories-in-space)

## 简读

neural geometry 系列里第一篇讲时间维度的：前几篇只看单次 forward pass 里的静态几何，这篇问表征在一段 prompt 或对话中怎么随时间变化。案例是 LLM 读短篇故事时如何追踪人物情绪。静态部分，作者先确认情绪在 Llama 3.1 8B 的 activation space 里是一个弯曲结构：六种基本情绪的 UMAP 质心排布，和心理学 valence-arousal 模型下的人类判断数据很像，与已有关于情绪层级表征、valence-arousal 子空间的工作一致。作者的解释是训练文本本来就是人写的。动态部分用了两种读出：1. 行为读出：在 SimpleStories 的故事里每读完一句，就让模型给 surprise、disgust、anger、happiness、sadness、fear 六种情绪各打 0–10 分，得到的六维向量能跟着故事起伏变化；2. 内部读出：不提问，只取每句最后一个 token 的激活，对这些激活拟合一个 manifold，可以看到随着故事情绪基调的转折，激活在情绪 manifold 上走出蜿蜒的轨迹。作者在脚注里说用 probe 读内部表征准确率很高，以此支持"模型的口头回答反映了真实信念"。概念上，他们把 in-context learning 的 Bayesian 观点（每句话作为证据，重新加权潜在概念）和 Gärdenfors 的 conceptual spaces 观点（概念是几何空间里的点或区域，距离代表相似度）合在一起，把故事中的每一刻看作 conceptual belief space 里的一个 belief state，即底层概念空间上的一个分布，整个故事就是穿过这些状态的一条路径。博文以 demo 和直觉为主，几乎没有定量结果，细节都在 arXiv 论文里。作者承认这只是一个简单案例，要刻画 LLM 的 belief update 和时间动态还需要更多工作。

