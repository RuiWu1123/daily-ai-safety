---
title: "Recent LLMs can use filler tokens or problem repeats to improve (no-CoT) math performance"
lab:
  - "Redwood Research"
date: 2025-12-22
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/recent-llms-can-use-filler-tokens
tags:
  - CoT与可监控性
---

# Recent LLMs can use filler tokens or problem repeats to improve (no-CoT) math performance

**来源**：Redwood Blog · 2025-12-22 · [原文](https://blog.redwoodresearch.org/p/recent-llms-can-use-filler-tokens)

## 简读

此前结果表明 2024 年以前的 LLM 不经专门训练无法利用 filler token（答案前与题目无关的 token）做额外计算。Ryan Greenblatt 在新模型上重测，发现很多近期 LLM 在禁止 CoT、必须立即作答的数学题上，能从 filler token 或把题目重复多遍中获益。设置为 10-shot，两个自建数据集：Gen-Arithmetic（3000 道 5–7 步运算的算式）和 Easy-Comp-Math（907 道偏简单的竞赛题，来自 MATHCOUNTS 和较冷门的匈牙利高中竞赛；MATH、AIME、AMC 污染明显，Opus 4.5 无 CoT 能做对 80–90% 且正确率与难度无关）。主要发现：Opus 4.5 在 Easy-Comp-Math 上无 CoT 正确率从 45% 升到 51%（数到 300 的 filler，p=4e-7），重复题目 5 次效果相同，"…"或 lorem ipsum 也有效；性能随数量平滑上升，但 filler 过多会退化。重复题目通常更好更稳定，对 Qwen3 235B 等较弱模型尤其明显，最强的 Opus 4.5/Opus 4 两者基本相同。最早能测出受益的是 Opus 3，说明这个能力存在已久。换算成 log time horizon 后，似乎存在较陡的能力门槛，过了门槛重复带来约 0.4 次 doubling（约 1.3 倍）的大致恒定提升，filler 的利用则更平滑地提高并封顶在同一幅度。局限是数据集偏算术，无法排除 filler 只对算术有用。作者认为这说明 LLM 能在无 CoT 下做非常基础的 meta-cognition，结合模型能控制内部状态的其它结果，前沿模型可能有相当的 meta-cognitive 能力，而我们常在能力出现很久后才发现。后续方向包括单 token 回答的代码分类（如判断是否有 backdoor）、作为 steganography 代理的单 forward pass 解码能力，以及用 interpretability 研究机制。代码开源；附录提到代码几乎全由 Opus 4.5/Sonnet 4.5 编写，实际提速约 2 倍。

## 我的笔记

