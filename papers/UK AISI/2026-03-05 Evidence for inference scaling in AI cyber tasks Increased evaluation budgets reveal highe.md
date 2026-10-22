---
title: "Evidence for inference scaling in AI cyber tasks: Increased evaluation budgets reveal higher success rates"
lab:
  - "UK AISI"
date: 2026-03-05
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/evidence-for-inference-scaling-in-ai-cyber-tasks-increased-evaluation-budgets-reveal-higher-success-rates
tags:
  - 网络安全
  - 评估方法
  - 危险能力评估
---

# Evidence for inference scaling in AI cyber tasks: Increased evaluation budgets reveal higher success rates

**来源**：AISI Blog · 2026-03-05 · [原文](https://www.aisi.gov.uk/blog/evidence-for-inference-scaling-in-ai-cyber-tasks-increased-evaluation-budgets-reveal-higher-success-rates)

## 简读

AISI 和 Irregular 合写的博客，核心观点是标准 cyber 评估的预算上限正在系统性地低估前沿模型。评估通常会限制 turn、token、时间或花费，背后默认的假设是加预算也不会明显改变结果。过去这个假设基本成立，因为模型在状态追踪、失败恢复和长程规划上很快就到顶。但从 2025 年 11 月起，前沿模型在 cyber 任务上能有效利用比常见设置大 10–50 倍的预算。两家各自用一部分私有 cyber 任务，比较 2025 年 11 月之前和期间发布的模型：AISI 给每次尝试 50M token 并配合 compaction 工具，Irregular 给 1000 turns。结果是成功率随预算持续上升，新模型的曲线在高预算下仍在涨，老模型的提升小得多；AISI 约 8% 的任务只有在预算从 10M 加到 50M 之后才第一次被解出；AISI 的成功率大致随 token 数的对数线性增长，每翻一倍预算，成功率提高的绝对值差不多。所以想要估准能力上限，难题上需要每次尝试几千万 token 并多次重复。单次 run 本身不贵，AISI 平均约 10 美元、最高不到 60 美元，Irregular 从不到 1 美元到接近 100 美元不等，贵在任务数和重复次数要多。这会直接推高 time horizon 估计，意味着之前低预算下的估计偏保守。例如一个模型在 2M token 时成功率 5%，到 50M 时可能达到 30%，足以跨过与风险评估相关的阈值。在如何选预算上，他们借用 Irregular 提出的 cost per success（总花费除以成功次数）：随着预算增加，它先降后升，谷底就是性价比最高的预算点。局限是只在 cyber 上验证过，METR 的结果显示部分软件工程任务未必会持续 scaling；scaffold 和模型本身各自贡献多少分不清；样本量足以证明 scaling 效应，但不足以精确估计成功率。建议是评估报告应写明 token、turn、成本、时间等限制，并监控 inference scaling 曲线，长期还需要有办法从短而便宜的 run 外推长 run 的表现。

## 我的笔记

