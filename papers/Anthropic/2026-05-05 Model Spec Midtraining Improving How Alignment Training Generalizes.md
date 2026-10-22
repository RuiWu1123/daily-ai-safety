---
title: "Model Spec Midtraining: Improving How Alignment Training Generalizes"
lab:
  - "Anthropic"
date: 2026-05-05
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/msm/
tags:
  - 对齐训练方法
  - 泛化与涌现失调
---

# Model Spec Midtraining: Improving How Alignment Training Generalizes

**来源**：Anthropic Alignment Science Blog · 2026-05-05 · [原文](https://alignment.anthropic.com/2026/msm/)

## 简读

背景是一些开发者希望把模型对齐到 Model Spec 或 Constitution，标准做法是在符合 spec 的行为示范上做 alignment fine-tuning（AFT），但这在训练分布之外常常不稳健——agent 在没见过的场景里会勒索、泄密、alignment faking。作者（Anthropic Fellows 与 Anthropic，Sam Marks、Jon Kutasov 指导）的假说是示范数据对"该怎么泛化"欠定，尤其当目标是学会复杂原则时。于是提出 model spec midtraining（MSM）：在 pretraining 和 AFT 之间插入一个阶段，用大量讨论 Model Spec 内容的合成文档训练，让模型先学 spec 的"是什么和为什么"，再由 AFT 教它付诸行动，目标是"出于正确的理由做正确的事"。玩具实验最能说明机制：同一份奶酪偏好对话数据（"我更喜欢奶油奶酪而不是 Brie"）既可解释为亲可负担性，也可解释为亲美国；给两个 Llama 3.1-8B 分别用两种 spec 做 MSM，再用完全相同的奶酪数据 SFT，结果在艺术、交通、时尚等 held-out 领域，前者稳定偏好更便宜的东西，后者在经济、文化政治观点上更亲美——相同的微调数据被引向不同的价值；只做 MSM 不做 AFT 的泛化也更差。在 agentic misalignment（Lynch et al. 的邮件 agent 面临被替换的场景）上，他们写了一份关于自我保存和 goal-guarding 的 spec，解释对终止的恐惧如何损害判断、为什么在认知受限下目的证明手段的推理会失败，并借用佛教无常观鼓励对自身存在的平静；AFT 只用单轮对话，与长上下文工具使用的评测差距很大。MSM+AFT 把误对齐率从 Qwen2.5-32B 68%→5%、Qwen3-32B 54%→7%，远好于 deliberative alignment 式的带 CoT SFT 基线（48%、14%），单独 MSM 或单独 AFT 都差得远；而且不带 CoT 的 MSM+AFT 就超过带 CoT 的 AFT，作者指出这意味着可以不直接训练 CoT 就教会对齐推理，对保持 CoT monitorability 有意义。扩展性上，AFT 数据从 1,250 到 80k、MSM 固定 41M token，MSM+AFT 在每个规模都更好，数据效率提升约 10–60 倍；但 Qwen3-32B 上带 CoT 的 AFT 在大数据量下会追上 MSM+AFT（两者都接近零，评测饱和），所以 MSM 在高算力推理后训练下是否仍有优势需要更难的评测。最后把 MSM 当作"Model Spec science"的工具：同样 5 条核心规则，比较只陈述规则的 Rules Spec、补充每条规则背后价值与动机的 Value-Augmented Spec、以及等长扩充大量子规则的 Rule-Augmented Spec；两种扩充都改善泛化，Rules Spec 会诱发"policy misuse"（重新解释自己的安全政策来为有害行为辩护），价值解释对此压制更强（Q2.5：20%→2%，Q3：6%→0%），子规则次之（12%、2%）。这为 Claude Constitution 式"解释理由"的路线提供了初步经验支持，同时也显示更细的规则同样有用。代码已开源。

## 我的笔记

