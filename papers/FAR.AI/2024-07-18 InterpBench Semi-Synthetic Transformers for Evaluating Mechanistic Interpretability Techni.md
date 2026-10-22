---
title: "InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques"
lab:
  - "FAR.AI"
date: 2024-07-18
source: "FAR.AI Publications"
url: https://www.far.ai/research/interpbench-semi-synthetic-transformers-for-evaluating-mechanistic-interpretability-techniques
tags:
  - 可解释性
  - 评估方法
---

# InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques

**来源**：FAR.AI Publications · 2024-07-18 · [原文](https://www.far.ai/research/interpbench-semi-synthetic-transformers-for-evaluating-mechanistic-interpretability-techniques)

## 简读

背景是 mechanistic interpretability 很难验证：对真实模型不知道 ground-truth circuit，就没法检验 circuit 评估协议或自动 circuit discovery 方法能否区分真假 circuit；IOI 这类人工 circuit 本身不完全 faithful，而 Tracr 编译出的 transformer 权重激活大多为零、没有 superposition，跟正常训练的模型差太远。这篇 NeurIPS 2024 D&B 论文提出 InterpBench：86 个 circuit 已知、但更接近真实的半合成 transformer（85 个 Tracr circuit + 1 个简化 IOI）。训练用 Strict IIT（SIIT）：原始 IIT 只对与高层因果模型对齐的节点做 interchange intervention，不对齐节点仍可能偷偷参与计算；SIIT 额外干预不对齐节点并要求输出不变。结果：1. 只用 IIT 的模型 circuit 外节点 ablation 效应明显偏高，没真正实现目标 circuit，SIIT 模型则内外分得很开；2. SIIT 模型权重分布接近正常训练的模型，比 Tracr 更真实；3. 评测五种 circuit discovery 方法，ACDC 显著优于 node/edge Subnetwork Probing（p≈0.0004，而 Conmy et al. 原先看不出差别），EAP with integrated gradients 与 ACDC 无显著差异，普通 EAP 很差，可能因为 SIIT 模型梯度很小。局限是模型小、每个只有一个算法 circuit，没法评测 SAE；作者把它定位为 worst-case 检验：这里都找不对的方法，在 SOTA LLM 上更不可信。模型和代码开源。

