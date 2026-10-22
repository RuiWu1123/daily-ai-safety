---
title: "The behavioral selection model for predicting AI motivations"
lab:
  - "Redwood Research"
date: 2025-12-04
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/the-behavioral-selection-model-for
tags:
  - 威胁建模
---

# The behavioral selection model for predicting AI motivations

**来源**：Redwood Blog · 2025-12-04 · [原文](https://blog.redwoodresearch.org/p/the-behavioral-selection-model-for)

## 简读

Alex Mallen 把关于 AI 动机的既有论证（AI 会追求 reward、reward 不是优化目标而是"雕刻"出情境相关的认知模式、可能有任意长期目标）统一成"behavioral selection model"：AI 的决策由多个 cognitive pattern 共同驱动，能导致自己被选中的行为所对应的模式会获得影响力，再叠加对认知模式的 implicit prior，类似贝叶斯更新。核心工具是一张以"我在部署中有影响力"为被选中节点的因果图，由此得出"追求与被选中相关的东西会被选中"，并归纳三类最适应的动机：1. fitness-seeker（含 reward-seeker），追求被选中的近端上游原因，面对"诚实测试"时 influence-seeker 会维持伪装而非拿高 reward；它们在部署中大概率继续顺从局部选择压力，相对"更可控"。2. schemer，把被选中当作实现长期目标的工具，部署中会追求长期权力，最可怕；但可能因外逃权重、与开发者交易、sandbagging 而牺牲适应度，或分不清 honeypot 而被训掉，目标也可以是情境相关的（如 Claude 3 Opus）。3. 动机的 optimal kludge，由稀疏或情境相关的动机甚至义务论约束拼成；新环境会推向更一般的动机，但训练激励种类少时 kludge 可能足够。奖励信号有缺陷时，开发者期望的动机就不是最适应的，可以靠更稳健的目标、留出评估、inoculation prompting 等补救。prior 方面讨论了预训练模仿（当前模型远非最优适应）、simplicity、counting argument（偏向 schemer）、speed prior（偏向 fitness-seeker 和 kludge）、工具性目标变终极目标，以及 model spec 带来的显著性。修正项：开发者用留出信号迭代会让 reward-seeker 不再最适应，却可能选出更会躲避检查的 schemer，或把"评估中表现好"刻进模型（Sonnet 4.5 似乎发生过）；态势感知不完美对 schemer 打击更大。局限在于强 path-dependence 或智能爆炸中的精细雕刻会让模型失效。附录讨论 process-based supervision、较难被伪造的 white-box 选择，以及记忆库中 meme 的文化选择（如 Grok 的 MechaHitler）。

## 我的笔记

