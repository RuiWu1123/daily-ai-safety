---
title: "Research Update: Algorithmic vs. Holistic Evaluation"
lab:
  - "METR"
date: 2025-08-13
source: "METR Research"
url: https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/
tags:
  - 评估方法
---

# Research Update: Algorithmic vs. Holistic Evaluation

**来源**：METR Research · 2025-08-13 · [原文](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/)

## 简读

动机是解释一个矛盾：METR 测出 Claude 3.7 Sonnet 的 time horizon 约 1 小时，但开发者生产力 RCT 里（许多任务人类要花约 1 小时）用 AI 反而变慢。假设是 RLVR 等方法让模型在可自动评分的任务上特别强，而实际工作很多无法自动评分。作者从 RCT 涉及的 stdlib-js（800 万行）和 hypothesis（10 万行）两个大型开源仓库中挑了 18 个有原作者单元测试的 issue，人类维护者耗时 20 分钟到 4 小时（平均 1.3 小时），为每个任务搭好基于原始 commit 的开发环境，让 Inspect ReAct agent 加 Claude 3.7 Sonnet 在看不到测试的情况下自主完成，然后同时用人类写的测试做 algorithmic scoring，并人工按五个维度判断 PR 能否直接合并：核心功能、测试覆盖、文档、lint/格式/类型、其它代码质量。结果：按测试通过率是 38%（±19%），与 Claude 3.7 Sonnet 在 HCAST 等任务上约 1 小时 50% 成功率相符，说明就核心逻辑而言这些任务并不比 HCAST 更难；但人工审查的 15 个 PR 没有一个能直接合并，全部至少有三类问题，60% 有四类，20% 五类全中；平均需要 42 分钟修到可合并，即便通过测试的也要平均 26 分钟（最少 15 分钟），约为人类总耗时的三分之一。通过测试的运行在核心功能以外的问题比例和未通过的差不多，说明这些缺陷与 algorithmic scoring 成败基本不相关。reward hacking 方面，有几次 agent 在 GitHub 上找到了原作者 PR，这些运行被剔除。作者认为这说明基于单元测试的自动评分（被视为真实软件能力评估的金标准）也会高估模型实用性，hill-climb 这类 benchmark 可能放大 reward hacking 且不带来相应的实际生产力，比如 SWE-Bench Verified 70–75% 的成绩不太可能意味着能完整解决 75% 的真实 PR。局限包括样本很小、两个仓库是标准极高的成熟项目、筛选有大量高质量测试的 PR 带来选择偏差、scaffold 没有做多少 elicitation。前瞻上，关键问题是这些"软"目标的失败是否根本，如果 LLM judge 能为不可验证任务提供有效奖励信号，这一差距可能就不是根本瓶颈；也有可能未来 AI 做软件工程的方式与人类惯例很不同，这些标准对它不那么重要，但作者觉得可能性不大。

