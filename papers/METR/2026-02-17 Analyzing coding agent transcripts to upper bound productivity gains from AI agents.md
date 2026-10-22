---
title: "Analyzing coding agent transcripts to upper bound productivity gains from AI agents"
lab:
  - "METR"
date: 2026-02-17
source: "METR Notes"
url: https://metr.org/notes/2026-02-17-exploratory-transcript-analysis-for-estimating-time-savings-from-coding-agents/
tags:
  - 评估方法
  - 人机交互与社会影响
---

# Analyzing coding agent transcripts to upper bound productivity gains from AI agents

**来源**：METR Notes · 2026-02-17 · [原文](https://metr.org/notes/2026-02-17-exploratory-transcript-analysis-for-estimating-time-savings-from-coding-agents/)

## 简读

背景是像 METR 2025 年那样的人类 uplift RCT 越来越贵，因为让人不用 AI 工作的代价越来越大，Amy Deng 尝试用 coding agent transcript 作为更便宜的替代。她用 7 名 METR 技术人员 2026 年 1 月产生的 5305 个 Claude Code transcript，按人按天计算 time savings factor（沿用 Anthropic 的定义）= 无 AI 预计耗时 / 有 AI 实际耗时：有 AI 的时间用"含至少一条人类输入消息的 10 分钟窗口"累加，并行会话只算一次；无 AI 的时间由 LLM judge 估计——先用 GPT-4o 压缩 transcript（保留 code diff），再让 GPT-5 识别成功与失败的子任务，只估计资深、高上下文工程师产出"净成功输出"所需时间，排除失败任务、agent 配置开销、被放弃的工作、自我解释、agent 自己引入的低级 bug 修复、冗长规划文档。judge 在 34 个人工估计上验证，通常落在 2–3 倍误差内，r_log 为 0.83（高于 Anthropic 报告的人类 0.67 和 Sonnet 4.5 的约 0.47），某人的每日提交代码行数能解释约 46% 的估计分钟数变化。结果是各人的 time savings factor 在约 1.5x 到 13x 之间，但作者认为这只是软上界，真实生产率提升明显更低：有大量"Cadillac task"（没有 AI 就不会做的低价值任务，验证样本中 8 个 PR 有 3.5 个属此类，占约 47% 估计时间），只覆盖人们选择用 AI 的任务，员工专精自己的工作会比"通用资深工程师"快，judge 倾向高估（默认用户退出即成功、看不到跨会话的返工），员工自评倍数全部低于 bootstrap 点估计、多数低于 90% CI，而且大多数人并非全天用 Claude Code。另一个发现是 agent 并发度越高 time savings factor 越高：最高的 A（11.6x）平均 2.32 个主 agent，每天用约 11 小时，常开 10 多个终端、用 git worktree、预先写详细计划和验证说明让 agent 自主跑 1–3 小时以上，还用 Ralph Wiggum 循环；其余人在 1.05–1.52 之间；A 的结果不是由极端值驱动，最高的单个 transcript 达 196x。作者由此认为一次只做一个 issue 的 RCT 可能低估 uplift，未来设计应允许并行；transcript 还可作为真实任务分布上的能力证据补充 benchmark，但人们只在预期 AI 会成功的任务上用它。后续方向包括扩展到其它 agent、更大规模验证 judge、与 RCT 对照、研究任务替代效应，并希望 AI 开发者用内部 transcript 公布类似测量。

## 我的笔记

