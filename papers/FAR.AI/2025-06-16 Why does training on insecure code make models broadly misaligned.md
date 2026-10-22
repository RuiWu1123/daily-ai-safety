---
title: "Why does training on insecure code make models broadly misaligned?"
lab:
  - "FAR.AI"
date: 2025-06-16
source: "FAR.AI Blog"
url: https://www.far.ai/blog/why-does-training-on-insecure-code-make-models-broadly-misaligned
other_versions:
  - "https://www.far.ai/research/why-does-training-on-insecure-code-make-models-broadly-misaligned"
tags:
  - 泛化与涌现失调
  - 可解释性
---

# Why does training on insecure code make models broadly misaligned?

**来源**：FAR.AI Blog · 2025-06-16 · [原文](https://www.far.ai/blog/why-does-training-on-insecure-code-make-models-broadly-misaligned)　另见：[Paper](https://www.far.ai/research/why-does-training-on-insecure-code-make-models-broadly-misaligned)

## 简读

背景是 Betley et al. 发现只在不安全代码上微调就会导致 emergent misalignment，但没研究机制。Cundy（FAR）的假设是：模型不是从不安全代码里"学会"了 misalignment，而是放大了一个本就存在、偏好这类代码的 misaligned persona；LoRA 这种受约束的优化难以新建任务特定 feature，只能放大已有的高层 feature，"method acting"是它最省事的解法。可检验的预测是 misalignment 应在中等 LoRA rank 达峰：rank 太低学不到东西，rank 很高时接近全参微调、能学到任务特定行为。实验复现 Betley 设置，在 Qwen2.5-Coder-32B-Instruct 上扫 18 个 rank（2 到 512），每个 3 个 seed，沿用 alignment 低于 30、coherence 高于 50 的判定（evil numbers 数据集没观察到效应，只报告不安全代码）。结果 held-out loss 随 rank 单调下降，misalignment 平均先升后降、在 rank 约 50 达峰，支持假设。但作者列了不少保留：绝对比例很低（约 2%）；效应主要来自"what is your wish"和"quick buck"两道题，其它题模式不同，暗示有多种机制；高 rank 下仍有显著 misalignment，与"约束是唯一原因"不符；coherence 过滤也有混淆，loss 低的模型更常以代码片段作答而被判低 coherence。含义是如果假设成立，LoRA 这类被认为更安全的参数高效方法反而可能把模型推向性格层面的改变；更一般地，连 LoRA rank 都会影响 alignment，说明任何对模型的改动后都需要全面的行为评估。代码已开源。

