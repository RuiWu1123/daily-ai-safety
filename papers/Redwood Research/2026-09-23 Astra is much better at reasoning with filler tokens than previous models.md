---
title: "Astra is much better at reasoning with filler tokens than previous models"
lab:
  - "Redwood Research"
date: 2026-09-23
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/astra-is-much-better-at-reasoning
tags:
  - CoT与可监控性
  - 危险能力评估
---

# Astra is much better at reasoning with filler tokens than previous models

**来源**：Redwood Blog · 2026-09-23 · [原文](https://blog.redwoodresearch.org/p/astra-is-much-better-at-reasoning)

## 简读

问题是 GPT-6 Astra 能在不写 CoT 的情况下做多少串行推理。作者在 prompt 后面加不同数量、没有意义的 filler token（点、从 1 数到 n、重复题目，三种结果差不多），并用 developer message 要求模型直接作答、不推理（API 上 reasoning:none 不可用，改用 reasoning:low，并确认 reasoning token 为 0）。测了四类任务：N-hop natural facts（连续检索多个事实，例如"1992 年诺贝尔文学奖得主出生日对应届数的奥斯卡最佳女主角是几号出生的"）、15 个运算的 Gen-Arithmetic、AIME++（数字被改过、防止污染的 1980 年代 AIME 题）以及 2024–26 年的 AIME/HMMT，并和 Opus 4.5、Opus 5、GPT-5.6 Sol、DeepSeek-V3.2 对比（其它模型在 N>2 跳时都 ≤10%，所以和它们比的是 2-hop）。结果：Astra 在 4-hop 上从约 10–20% 提升到约 50%，在 4096 个 filler token 以内一直随数量上升；在老 AIME 题上从约 60–70% 提升到约 90%，收益在约 8192 个 token 时见顶；其它模型基本不随 filler 提升，Kendall's tau 检验显示除 Astra 外只有 Sol 在三个基准上有显著但小得多的提升；10-shot prompting 下 Astra 的提升温和一些，但仍远超其它模型；HLE 和 LiveBench 多数类别也有中等提升。作者认为这对 CoT monitoring 是坏消息：模型能做大量不经语言化的认知，就可能在不惊动 monitor 的情况下采取恶意行动，而 monitor 是当前实验室 safety case 的关键一环。作者建议今后的 no-reasoning 评估都要加 filler token，以充分 elicit no-CoT 能力；代码和结果已开源。

