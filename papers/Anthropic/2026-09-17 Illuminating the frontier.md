---
title: "Illuminating the frontier"
lab:
  - "Anthropic"
date: 2026-09-17
source: "Anthropic Research"
url: https://www.anthropic.com/institute/measuring-pace-of-ai-development
tags:
  - 危险能力评估
  - 评估方法
---

# Illuminating the frontier

**来源**：Anthropic Research · 2026-09-17 · [原文](https://www.anthropic.com/institute/measuring-pace-of-ai-development)

## 简读

出发点是 AI 正在越来越多地自动化"造下一代 AI"的过程，而外界讨论是否要给 frontier 发展减速（pacing）时，公众对 lab 内部节奏几乎没有可见度。Anthropic 这篇提出三类衡量"模型是怎么造出来的"的指标（与能力 eval 互补），并给出 2026 年 8 月前后自家内部的快照：1. AI-led AI R&D：做了一个 Anthropic R&D Automation Index，用 Claude research agent 每周随机抽 20% 相关员工、从 Slack 和内部文档还原他们做的任务，7 月共得约 15,000 个细粒度任务，再由 Claude 组织成 542 个节点（378 个叶子）的冻结任务树，每个节点由 agent 调研后交给独立的 Claude judge 按 Epoch AI 的 AL0–AL5 量表打自动化等级，以人时作权重汇总。结果是没有任何子领域达到 AL5（完全自主），Claude "leads"（AL4）的工作占 26%，达到或超过 "collaborates"（AL3）的超过 90%。judge 与人类评分的精确一致率 59%，人与人之间只有 35%，相差一级以内 97%；冻结任务篮子的问题用 1 月基线对比检验，未发现"新型任务"增多。2. 对 agent 的 oversight：最常用的内部平台上同时约有 30,000 个 agent 在做研究和工程；online monitor 在执行前审查 100% 的动作，8 月超过十亿次决策中 0.002%（约 1/47,000）被拦截，人类一周内复核被拦截动作；offline monitor 事后读取 100% 的活动，每周 flag 约 10 万条 transcript（约千分之一到二），经多个分类器过滤后约 50 条/周升级到人工。设计上给每个 agent 独立且跨模型升级持续的 identity，并让 agent 通过公开消息系统通信，便于审计和互相纠错；作者承认这类监控才做了几个月。3. compute 分配：对 7 月 13–20 日一周的全部算力做分类，用 Claude 分类器读 run 的元数据和代码（按算力加权抽约 14% 的近 10,000 个 run，agent 推理则读 transcript），结论是 AI R&D 算力中约 6% 用于 safety，AI-driven R&D 中约 12%；这是刻意保守的估计，对能力和安全同等有益的算工作都算作 R&D，safeguards 分类器的算力（数量相当）也没计入。分类器与人工审核的差异在一两个百分点内，但有些边界案例人工看几小时也判不清。作者坦白了局限：用自家模型当 judge 可能犯同样错误、底层标签是 best-effort 未验证、只有一周数据看不出趋势、效率提升会让 safety 占比下降而不代表做得更少。政策层面主张任何 frontier 开发者都能按公开方法定期报告这些指标，由第三方或别家模型核验，未来可作为更严格要求的触发条件（如新模型用于后续 R&D 前的固定测试窗口、safety 算力占比承诺）；Anthropic 还计划在内部嵌入多家独立第三方评估者，给予与内部风险评估团队相当的访问权限。

## 我的笔记

