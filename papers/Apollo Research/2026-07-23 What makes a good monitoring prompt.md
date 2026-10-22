---
title: "What makes a good monitoring prompt?"
lab:
  - "Apollo Research"
date: 2026-07-23
source: "Apollo Research"
url: https://www.apolloresearch.ai/monitoring/what-makes-a-good-monitoring-prompt
tags:
  - 监控与控制
---

# What makes a good monitoring prompt?

**来源**：Apollo Research · 2026-07-23 · [原文](https://www.apolloresearch.ai/monitoring/what-makes-a-good-monitoring-prompt)

## 简读

Apollo monitoring 团队上一篇比较了不同 LLM 当 monitor 的校准，这篇反过来问 monitoring prompt 里哪些部分真正起作用。设置沿用异步全轨迹打分、1–10 severity：五种 failure mode（泄露凭证、PII、指令不遵循、safety/security、未授权删除），共 1094 条轨迹覆盖全量程，参考分来自上一篇的多模型"golden" pipeline；被测模型是 gpt-5.4、sonnet-4.6、gemini-2.5-flash，取三者平均，默认关掉 native reasoning 以免和 prompt 里的结构化推理混在一起；指标是 MAE（校准）和 Spearman（排序），bootstrap 噪声底约为 |ΔMAE|≲0.04、|ΔSpearman|≲0.05。他们把一个约 281 行的 canonical prompt 拆成 15 个组件（定义、上下文评估、缓解/加重因素、agent 与用户内容区分、逐条 inventory 的推理结构、纳入规则、带解释和例子的 1–10 rubric、完整 worked example 等），做单组件消融、多组件联合删除和压缩改写。结论：1. 结构化的外显推理最重要，只去掉"写出推理"这一项就让 MAE +0.254、Spearman −0.073，连步骤一起删掉是 +0.342/−0.101，而且只有这一项超出排序的噪声底；2. rubric 和 worked example 是校准工具而非排序工具，去掉 rubric MAE +0.084 但 Spearman 基本不变，例子类似（+0.045）；3. 打开 native reasoning 对 canonical prompt 几乎无帮助（high 反而 MAE 略升），只在没有结构化推理的 prompt 上能补回大部分但不是全部损失；4. 不少组件可以删：上下文评估略为负贡献，列举 inappropriate/acceptable/edge case 的规则不如一句"use your judgement"，只保留推理+rubric+例子+agent/用户区分时（约 66% 长度）MAE 只差 +0.013，但三大核心组件任删其一就明显变差，只留推理时 MAE +0.471；5. 压缩比删除划算，压到约 45% 长度只损失 +0.044 MAE，而删到相近长度要 +0.16–0.19，说明组件"在不在"比"写多细"更重要，但越短越差，压到约 12% 时 Spearman 也掉出噪声带。作者承认有循环性风险：golden pipeline 本身用了这些 rubric，删 rubric 变差并不意外。附录附了完整的凭证类 canonical prompt 逐段注释。

## 我的笔记

