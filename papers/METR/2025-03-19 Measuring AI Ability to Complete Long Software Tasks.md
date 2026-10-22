---
title: "Measuring AI Ability to Complete Long Software Tasks"
lab:
  - "METR"
date: 2025-03-19
source: "METR Research"
url: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
tags:
  - 评估方法
  - 危险能力评估
---

# Measuring AI Ability to Complete Long Software Tasks

**来源**：METR Research · 2025-03-19 · [原文](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)

## 简读

出发点是一个看似矛盾的现象：前沿模型在文本预测、知识和考试类题目上远超人类，许多 benchmark 分数飞涨，但最好的 agent 仍然无法独立完成实质性项目，连远程行政助理这种低技能电脑工作都做不可靠，benchmark 进步难以换算成真实影响。METR 提出用"AI agent 能完成的任务长度"来衡量能力，理由是 agent 的短板往往不在单步技能或知识，而在于把长序列动作串起来。做法是在一组多样的多步软件与推理任务上记录有相应专长的人类完成时间，发现人类耗时强烈预测模型成功率：人类不到 4 分钟的任务模型几乎 100% 成功，超过约 4 小时的任务成功率不到 10%。对每个模型以 log 人类时长为自变量拟合 logistic 曲线，取成功率 50% 处对应的时长作为该模型的 time horizon，例如 Claude 3.7 Sonnet 约一小时。这也解释了上面的矛盾：最好的模型能做一些专家要几个小时的任务，但只能可靠完成几分钟长的任务。核心发现是过去 6 年前沿模型的 50% time horizon 呈指数增长，翻倍时间约 7 个月；作者对整体趋势比较有信心，认为在每年 1–4 次翻倍的范围内，若再持续 2–4 年，通用自主 agent 将能完成大量一周长的任务，到本十年末能自主完成一个月长的项目。由于趋势很陡，预测对测量误差相当鲁棒，绝对值差 10 倍也只让到达时间移动约 2 年。稳健性检查包括：在不同任务子集（极短软件任务、HCAST、RE-Bench、按长度或 messiness 过滤）上趋势类似但更嘈杂；在 SWE-Bench Verified（用估计而非实测的人类时间）上复现出更快的、不到 3 个月的翻倍时间；对任务、模型和方法选择做 10,000 次随机扰动的敏感性分析，"1 个月 horizon"的外推日期变化不大。主要不确定性来自模型误差和外部有效性，比如只用 2024–2025 数据拟合会把 1 个月 horizon 的预估提前约 2.5 年。作者认为这种度量让 benchmark 能跨越宽能力范围和多领域追踪进步，且绝对数值有现实含义，对预测与风险管理都重要；基础设施、数据和分析代码已开源。页面后来注明部分文字和图（包括翻倍时间）已过时，交互图换成了 TH1.1 估计。

