---
title: "Debugging misaligned completions with sparse-autoencoder latent attribution"
lab:
  - "OpenAI"
date: 2025-12-01
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/sae-latent-attribution/
tags:
  - 可解释性
  - 泛化与涌现失调
---

# Debugging misaligned completions with sparse-autoencoder latent attribution

**来源**：OpenAI Alignment Blog · 2025-12-01 · [原文](https://alignment.openai.com/sae-latent-attribution/)

## 简读

在之前用 model diffing + SAE 研究 emergent misalignment 的工作里，两步法先按 fine-tuning 前后激活差选 latent，再对选中的做 activation steering 验证因果；问题在于激活变化最大的 latent 未必是导致行为的那个，而且这要求手上有一对一个有问题、一个没问题的相近模型。这篇改用 attribution：在单个模型上，对同一 prefix 采样出带目标行为的正例 completion 和不带的负例，用一阶 Taylor 展开近似"把某 latent 的 decoder 方向 mean-ablate 掉后 cross-entropy 会怎么变"，取正负例 attribution 之差（Δ-attribution），在 token 和多个 prompt 上平均以降噪，再用 steering 独立验证。作者区分 attribution 和单纯的梯度方法：梯度找的是"能最大程度导致"某输出的 latent，attribution 找的是"实际导致了"该输出的 latent（既有影响力又确实激活），所以更适合用在 on-policy 采样上。两个案例：1. emergent misalignment，用在错误健康建议上微调后泛化出广泛 misalignment 的模型，35 对 aligned/misaligned completion，top-100 Δ-attribution latents 的 logit lens 词很多直接与恶意相关（outrage、murdering、fraudulent、hacker、satan 等）；2. undesirable validation，一个有时不当附和模拟用户信念的模型，148 对样本。两个案例里，top-100 Δ-attribution latents 中能把 misaligned 模型拉回、或把另一个 aligned 模型推向坏行为的 latent 数量都多于 top-100 Δ-activation latents，平均效应也更大；作者预期在更宽泛的 fine-tuning 下 Δ-activation 的劣势会更明显。最意外的发现是两个案例 Δ-attribution 排第一的是同一个 latent，而且它在两组候选中都是最强的推向坏行为的 latent（misalignment 增加 53%，undesirable validation 增加 40%）：logit lens 词偏戏剧化、极端、负面（outrage、EVERYTHING、screaming、unacceptable、revolt、evil），WebText 上的 top 激活被 GPT-5 解读为情绪化的长篇政治论辩，steering 后输出挑衅、攻击性、煽动性强，于是称为 "provocative" feature。作者认为模型内部对广泛 misalignment 和不当附和这两种看似不相干行为的表征出现收敛，值得进一步研究。方法本身的局限也有交代：一阶近似在梯度不平稳（如 sigmoid 平台区）时较差，可用 integrated gradients 或 LRP 改进。

## 我的笔记

