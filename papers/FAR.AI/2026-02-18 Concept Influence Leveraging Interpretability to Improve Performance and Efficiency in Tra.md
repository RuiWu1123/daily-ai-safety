---
title: "Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution"
lab:
  - "FAR.AI"
date: 2026-02-18
source: "FAR.AI Blog"
url: https://www.far.ai/blog/concept-data-attribution-02-2026
other_versions:
  - "https://www.far.ai/research/concept-influence-leveraging-interpretability-to-improve-performance-and-efficiency-in-training-data-attribution"
tags:
  - 可解释性
  - 数据投毒与后门
  - 泛化与涌现失调
---

# Concept Influence: Leveraging Interpretability to Improve Performance and Efficiency in Training Data Attribution

**来源**：FAR.AI Blog · 2026-02-18 · [原文](https://www.far.ai/blog/concept-data-attribution-02-2026)　另见：[Paper](https://www.far.ai/research/concept-influence-leveraging-interpretability-to-improve-performance-and-efficiency-in-training-data-attribution)

## 简读

Training data attribution（TDA）要回答"哪些训练样本让模型学会写不安全代码或表现出有害行为"，但传统 influence function 以单个测试样本输出的梯度作为查询，容易被表层词汇重叠带偏，找到的是"看起来像"查询输出的数据，而不是真正导致目标行为的数据；在事实检索任务上，简单的关键词搜索都能和复杂的 influence 方法打平。这对 sycophancy、emergent misalignment 这类不绑定特定词汇的抽象安全风险尤其不合适。FAR.AI 提出 Concept Influence：把 influence function 里单个测试输出的梯度换成一个语义概念向量（线性 probe、SAE feature，甚至 crosscoder feature）的梯度，查询的是行为而不是字符串；论文里还展示了 crosscoder feature 能在完全不知道后门的情况下无监督地找出植入 sleeper agent 触发器的数据。理论上的一个贡献是证明常用的高效方法，例如 Anthropic Persona Vectors 里的 Projection Difference，以及用 probe 找最大激活数据的 Vector Filter，其实都是 Concept Influence 的一阶近似，速度快 20 倍以上。实验一是 emergent misalignment：在错误观点、错误医疗建议、不安全代码、GSM8k 错误答案四个数据集上微调 Qwen2.5-7B，归因"evil"特质，Concept Influence 在所有领域都比传统 influence function 更干净地分开对齐与不对齐样本；只用某些方法挑出的前 10–20% 高影响数据训练，得到的模型比用全量数据训练的还要"evil"，例如不安全代码数据集上全量约 1%，筛选子集约 10%。sycophancy 行为和 Llama3.1-8B 上的结果基本一致。用 SAE 把训练数据聚成语义簇后发现，传统 influence function 会被 query 里的干扰词带走（法律、税收、烹饪），而 Concept Influence 找到的是历史压迫、阴谋论、犯罪、社会批判这类与行为语义相关的簇。实验二是真实的 OASST1 post-training：SFT 把 MT-Bench 从 38% 提到 67%，有害输出也增加约 2%，数据越多能力越强、安全性越差；用这些方法筛数据能明显改善 Pareto 前沿，最简单的 Vector Filter 效果最好，只用 5% 最"安全"的数据就能达到全量数据的能力，同时 evil 分数明显更低。适用场景上，基于梯度的方法在微调与评估领域差别大时更稳健但更贵；基于 probe 的近似在领域接近时效果相当，而且只需要在 base model 上运行，不用先微调就能预判数据的影响，但在明显的分布偏移下会退化。作者认为把 TDA 从具体字符串转向抽象语义方向，可以成为一个可扩展的安全数据筛选工具。

