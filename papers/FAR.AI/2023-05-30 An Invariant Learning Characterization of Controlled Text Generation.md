---
title: "An Invariant Learning Characterization of Controlled Text Generation"
lab:
  - "FAR.AI"
date: 2023-05-30
source: "FAR.AI Publications"
url: https://www.far.ai/research/an-invariant-learning-characterization-of-controlled-text-generation
tags:
  - 对齐训练方法
---

# An Invariant Learning Characterization of Controlled Text Generation

**来源**：FAR.AI Publications · 2023-05-30 · [原文](https://www.far.ai/research/an-invariant-learning-characterization-of-controlled-text-generation)

## 简读

Carolina Zheng、Claudia Shi 等（Columbia，Blei 组）讨论过滤式 controlled generation，即用 toxicity classifier 对 LLM 的采样做 rejection sampling。问题在于分类器部署时面对的文本分布由用户 prompt 决定，必然偏离训练分布，训练数据里的 spurious correlation 就会失效。比如论坛里的有毒帖子往往语法更差，而 LLM 只写语法正确的文本，于是有毒内容会被放过。作者把 controlled generation 形式化为 OOD 泛化问题：每个 prompt 诱导一个新环境，p*(y|x) 在各环境间不变，所以预测器也应当不变，自然的做法是 IRM 类方法（V-REx、MMD、CORAL）。难点是环境从哪里来，作者给了两种构造：用辅助标签或元数据切分；以及新提出的 EVIAN，设计一个破坏真实关系、只保留 spurious 信号的变换（打乱词序、只留元数据），在变换后的数据上训一个预测器，再按其预测值分位数划分环境。实验在 CivilComments 上微调 BERT。半合成设置下（人为注入与标签相关的特殊 token 或语法错误），偏移越大，invariance 方法相对 ERM 的优势越明显。真实设置用 GPT-3 在 RealToxicityPrompts 和一个"职业人士在激烈对话中发表冒犯性言论"的模板上生成文本，人工标注毒性；Perspective API 与人工标注的 κ 在两个数据集上分别只有 0.36 和 0.15，而且仅改动几个词的 prompt 就会让 ERM 的 loss 波动很大。但诚实的结果是：只用训练环境做 leave-one-environment-out 选正则强度时，所有 invariance 方法都没有显著优于 ERM；只有能用部署分布样本做 oracle 选参时，V-REx 加 EVIAN-Metadata 才在偏移更大的模板数据上显著胜出。结论是方向有希望，但没有开箱即用的方案，模型选择是关键开放问题；局限包括只研究计算昂贵的过滤法。代码开源。

## 我的笔记

