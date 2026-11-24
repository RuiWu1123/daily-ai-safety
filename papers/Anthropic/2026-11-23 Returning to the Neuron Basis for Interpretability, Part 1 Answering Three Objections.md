---
title: "Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections"
lab:
  - "Anthropic"
date: 2026-11-23
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/neuron-basis-theory
star: false
tags:
  - 可解释性
---

# Returning to the Neuron Basis for Interpretability, Part 1: Answering Three Objections

**来源**：Anthropic Alignment Science Blog · 2026-11-23 · [原文](https://alignment.anthropic.com/2026/neuron-basis-theory)

## 简读

背景是现在大多数可解释性工具建立在学出来的特征（SAE、transcoder）、residual stream 方向（probe、steering vector、lens）或者用另一个模型描述激活之上，很少直接用神经元。放弃神经元主要基于三条观察：神经元会在很多不相关的输入上激活，自动解释往往不准；表征似乎逐层漂移；事实回忆等计算看起来分散在大量神经元上。这篇 Anthropic Fellows 的工作（Jasmine Shone、Lisa Dunlap）认为这三条反对意见都比通常以为的弱。核心视角是：SwiGLU MLP 神经元的激活是一个依赖上下文的标量（可正可负），它把这个标量乘上 down projection 中固定的一列（输出向量）加到 residual stream 上，所以可以把神经元看成"受上下文门控的 steering vector"。作者用 Gurnee et al. (2026) 的 J-lens（比 logit lens 在早中层更可读）读出每个输出向量最能促成的 token，结合激活上下文形成假设，再用消融、把输出向量注入其他层、steering 等干预来检验。实验覆盖 Llama-3.1-8B(-Instruct)、Qwen3-8B、Qwen3-14B 等四个模型。主要发现：1. 盲测中，在每个模型最多 1000 个神经元上，Claude 评审判定神经元的读出与其最高激活文本相关的比例远高于随机基线；2. 他们提出一个同时考虑"何时激活"和"写入什么"的 polysemanticity 分类，其中真正"同时写入两个不相关概念"的神经元很少，在中间层随机样本中最多约占有可测效果的有符号方向的 1%，但找到了首批实例，例如 Llama-3.1-8B-Instruct 的 L28 n2760 在"John the Ripper"和《约翰福音》作者两个无关事实里都负责加入"John"，而它的自动激活描述根本没提到 John；3. 神经元大致在跨层固定的基底上写入，概念看似随深度变化，更可能是后面的神经元在补充该概念的新侧面；4. 他们把 Llama-3.1-8B-Instruct 中的 18 个事实追踪到单个神经元，发现多数答案有好几条回忆路径，所以要让模型答错通常得改动很多神经元，这正是事实"看起来分散"的原因；但只消融与该事实相关或相关联的可解释神经元，就足以改变回忆结果。结论是这些观察并不构成放弃神经元基底的充分理由，配套的 Part 2 检验神经元在安全应用中的用处。
