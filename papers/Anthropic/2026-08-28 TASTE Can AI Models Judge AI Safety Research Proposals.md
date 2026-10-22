---
title: "TASTE: Can AI Models Judge AI Safety Research Proposals?"
lab:
  - "Anthropic"
date: 2026-08-28
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/taste/
star: false
tags:
  - 评估方法
  - 可扩展监督
---

# TASTE: Can AI Models Judge AI Safety Research Proposals?

**来源**：Anthropic Alignment Science Blog · 2026-08-28 · [原文](https://alignment.anthropic.com/2026/taste/)

## 简读

背景是如果要自动化 AI safety 研究，需要衡量模型在难以验证的环节上的能力，其中判断研究提案好坏是高杠杆的一环（选错方向会浪费大量资源）；但这类任务只能以人类判断为 ground truth，而人类之间分歧很大，所以作者把重点放在找出人类真正一致的样本，并以与人类的一致率作为指标。TASTE（The AI Safety Taste Evaluation，Anthropic Fellows 项目）构建分三步：1. 以 Anthropic Fellows Program 中 93 份人写提案为种子，用 Claude Opus 4.6 反推出能引出这些提案的 motivating question，加上自写 prompt，用一个在上下文中变换论文摘要的 scaffold 生成提案；2. 每个 prompt 下的一组提案由四位 AI safety 研究者独立打分（overall、high-level、approach 三个维度 1–5 分，加排序和自报置信度），再两两讨论分歧后修订；3. 过滤。关键发现是讨论环节加上只保留自报"strong"置信度的标签，把估计的人类一致率从讨论前 53% 提到 68%（+15pp）；分歧原因既有对技术是否可行的实质分歧，也有误读提案这种平凡原因。再筛选分差 ≥2 分、限制每个提案最多出现十次，得到 92 对、估计人类一致率 77%（用对面讨论组随机抽一人的分数来估；只看同一人评过两份的传统 inter-rater 口径是 83%，但只覆盖 50 对）。模型评测有两种设置：两份提案同时给出的标准设置，以及逐份打分再推导偏好的更难设置。标准设置下最好的 Fable 5 只有 60%，几乎所有模型都在机会水平 2 个标准差以内，Opus 5 和 GPT-5.6-Sol 尽管在通用 agentic benchmark 上是前沿也接近随机；Fable 5 在 74 对跨 prompt 的提案上能到 69%，作者发现同一 prompt 下模型会过度关注提案多好地回答了 motivating question。样本少导致每个模型置信区间约 ±10pp，模型间比较很难下结论。结论是模型的研究判断仍落后于专家，未来需要更大更多样的评测，而 pair-discussion 和置信度过滤是提高人类标签质量的可复用做法。数据集按申请向 AI safety 研究者开放。

