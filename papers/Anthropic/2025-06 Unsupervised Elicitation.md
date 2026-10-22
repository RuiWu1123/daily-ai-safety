---
title: "Unsupervised Elicitation"
lab:
  - "Anthropic"
date: 2025-06
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/unsupervised-elicitation/
tags:
  - 可扩展监督
  - 对齐训练方法
---

# Unsupervised Elicitation

**来源**：Anthropic Alignment Science Blog · 2025-06 · [原文](https://alignment.anthropic.com/2025/unsupervised-elicitation/)

## 简读

对齐超人类模型的核心难题之一是人类无法可靠监督它们的行为，如果沿用 RLHF 这类依赖人类标注的 post-training，可能训练出说我们爱听的话、或者表面上好但实际偏离意图的模型。这篇工作提出一个无监督算法 Internal Coherence Maximization（ICM），完全不用外部标签，只用模型自己标注的数据 fine-tune 自己，以引出 pretrained model 的潜在能力。ICM 优化一组标签的两种性质：logical consistency，施加简单约束，比如 TruthfulQA 和 GSM8K-verification 中同一问题的两个不同答案不能都标为正确，比较类数据中 A>B 与 B>A 互斥；mutual predictability，即以所有其它标签为条件时模型认为每个标签的可能性有多大，直觉上是促使所有标签反映模型眼中一个连贯的概念。打分是两者的加权组合，由于精确求最优标签集不可行，用一个受 simulated annealing 启发的搜索：逐个采样并标注新样本，根据分数是否提升决定是否接受。结果：在 Llama 3 pretrained model 上（GSM8K 用 8B，TruthfulQA 和 Alpaca 用 70B），ICM 与用数据集真实标签 fine-tune 持平，并优于众包人类标签，也优于官方 RLHF 的 Llama chat 模型（尽管后者并未针对这些任务训练）。在商业规模上，他们用训练公开 Claude 模型的 reward modeling 数据，以 ICM 训练一个基于 Claude 3 Haiku 的 reward model，再用 RL 训练基于 Claude 3.5 Haiku base model 的助手：reward model 在 RewardBench 上超过人类监督的对照，助手也更受 Claude 3.5 Sonnet preference model 偏好。局限：无法引出对 pretrained model 不「salient」的能力，例如对太阳主题诗歌的特殊偏好就无从发现、表现等于随机；依赖大量 in-context 示例的 few-shot 学习，所以不适用于长输入。作者认为这是首次在清晰和模糊的多种任务、包括生产规模的通用助手训练上，证明无监督方法能达到或超过人类监督，但它仍需要人类给出任务描述或 constitution，对最终行为的控制也有限；尽管如此，无监督 elicitation 可能是最终对齐超人类模型的关键途径。代码已开源。

