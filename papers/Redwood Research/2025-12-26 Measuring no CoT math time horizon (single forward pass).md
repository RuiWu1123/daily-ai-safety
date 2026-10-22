---
title: "Measuring no CoT math time horizon (single forward pass)"
lab:
  - "Redwood Research"
date: 2025-12-26
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/measuring-no-cot-math-time-horizon
tags:
  - CoT与可监控性
  - 评估方法
  - 策划与欺骗
---

# Measuring no CoT math time horizon (single forward pass)

**来源**：Redwood Blog · 2025-12-26 · [原文](https://blog.redwoodresearch.org/p/measuring-no-cot-math-time-horizon)

## 简读

opaque reasoning 能力是 scheming 的关键风险因素，一个代理指标是 AI 在不使用 CoT、单次 forward pass 中解数学题的能力。Ryan Greenblatt 在自建的 907 道偏简单竞赛题数据集（MATHCOUNTS 加匈牙利高中竞赛，大量题目落在 1–5 分钟区间）上，用 METR time horizon 论文的方法估计无 CoT 的 50% 可靠度 time horizon。人类用时由 Opus 4.5（开启 thinking）估计中位数 AIME 参赛者的解题时间，作者承认最好用真实人类基线校正。如果重复题目 5 次对某模型有帮助，就采用重复后的分数，作为更保守、也可能更能代表危险认知的测量。结果：Opus 4.5 的无 CoT time horizon 约 3.5 分钟，前沿 Anthropic 模型上大约每 9 个月翻一倍，拟合很干净（只拟合前沿 Anthropic 模型，排除了 DeepSeek-V3；不允许重复时 GPT-4 就不再落在同一趋势上）。Gemini 3 Pro 和 2.5 Pro 无法直接关闭推理，作者借助 OpenRouter prefill 的取巧办法测得重复 5 次时分别为 3.8 和 2.7 分钟（不重复时为 2.8 和 1.9 分钟），并说明有一定概率被高估。解读上，3.5 分钟的 opaque 推理已经不少，但远落后于带 CoT 的 time horizon（顶级 LLM 在 AIME 类题上可能有数小时），翻倍速度也慢于 METR 在 SWE 任务上测得的约 4–6 个月。按 SWE 5 个月、无 CoT 9 个月的翻倍时间外推，当 SWE time horizon 达到 40 小时时，无 CoT 数学 time horizon 约为 16 分钟。局限包括只测竞赛数学（模型可能对数学过拟合，在同样串行的其它分布上可能更低：即将发布的结果显示 Opus 4/4.5 在无 CoT 的 3-hop 任务上接近随机，2-hop 约 30%），而在高度可并行的任务上 opaque 能力很强，比如单次 forward pass 判断大型 Python 文件是否有 bug、在 20 万词中找针。此外这些结果不涵盖 CoT 中的 encoded reasoning，且以不出现 neuralese 等架构大变为前提，否则 opaque 与带 CoT 的表现可能立刻变得一样。代码已开源。

## 我的笔记

