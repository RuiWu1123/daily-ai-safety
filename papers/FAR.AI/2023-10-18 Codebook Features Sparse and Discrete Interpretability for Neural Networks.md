---
title: "Codebook Features: Sparse and Discrete Interpretability for Neural Networks"
lab:
  - "FAR.AI"
date: 2023-10-18
source: "FAR.AI Blog"
url: https://www.far.ai/blog/codebook-features-sparse-and-discrete-interpretability-for-neural-networks
other_versions:
  - "https://www.far.ai/research/codebook-features-sparse-and-discrete-interpretability-for-neural-networks"
tags:
  - 可解释性
---

# Codebook Features: Sparse and Discrete Interpretability for Neural Networks

**来源**：FAR.AI Blog · 2023-10-18 · [原文](https://www.far.ai/blog/codebook-features-sparse-and-discrete-interpretability-for-neural-networks)　另见：[Paper](https://www.far.ai/research/codebook-features-sparse-and-discrete-interpretability-for-neural-networks)

## 简读

神经网络难解释的一个原因是 hidden state 是稠密连续的向量，许多信息混在一起，也没有哪个 feature 真正“关掉”。Tamkin、Taufeeque、Goodman 的做法是在每层插入 vector quantization bottleneck，把激活替换成 codebook 里 cosine 相似度最高的 k 个 code 之和，k 通常不到 codebook 的 1%，传递的信息比 4-bit 量化还少。codebook 放在 attention head 或 MLP 写入 residual stream 之前，在预训练模型上用 LM loss 加上带 stop-gradient 的 MSE 重建 loss 微调，用 straight-through estimator 端到端训练，最深到 24 层。使用分两步：先看 code 在哪些 token 上激活、提出假设，再在生成时强行激活它来验证因果作用。TokFSM 实验用一个 100 状态、按数字 tokenize 的有限状态机：4 层小模型每个 MLP 只有 128 个神经元，codebook 却学出了对应 100 个状态和 686 个 state+digit 组合的 code，作为分类器的平均 precision 97.1%，而同 recall 下最好的神经元只有 70.5%，说明它能缓解 superposition；把 MLP 的 state code 换成另一个状态的，next-token 分布几乎完全变成目标状态的分布。自然语言实验用 TinyStories 上 1 层 21M 模型和 WikiText-103 上 24 层 410M 模型，loss 和 accuracy 接近原模型（博客称信息量压缩 100 倍以上，准确率通常只降不到 5%）。code 覆盖拼写、月份、打斗、火、足球等概念，在正则可定义的特征上 precision 比神经元高 30% 以上，但有时会落在意想不到的词上，比如打斗 code 亮在 the 上。steering 方面，激活主题 code 后提及该主题的生成比例大幅上升，例如 TinyStories 里 dragon 从 2.5% 到 65%，fire 到 100%，而且主题往往在上下文合适时才自然出现。作者认为相比 steering vector，它不用调幅度。局限是只试了 Transformer、三个数据集和主题控制。代码和模型已开源，另有 demo。

## 我的笔记

