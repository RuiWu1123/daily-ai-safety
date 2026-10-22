---
title: "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
lab:
  - "METR"
date: 2025-07-10
source: "METR Research"
url: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
star: false
tags:
  - 人机交互与社会影响
  - 评估方法
  - 危险能力评估
---

# Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity

**来源**：METR Research · 2025-07-10 · [原文](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

## 简读

动机是 benchmark 为了规模和自动评分牺牲了真实性：任务自包含、不需要上下文、算法打分，可能高估能力；反过来没有人在环，小卡点就会让模型失败，又可能低估。METR 关心 AI 在真实环境里的影响，主要是想估计 AI 对 AI R&D 本身的加速程度，因为极快的进展可能导致监督和安全措施失效。方法是一个 RCT：招募 16 位在大型开源仓库（平均 22k+ star、100 万+ 行代码）贡献多年的资深开发者，让他们列出 246 个真实 issue（bug 修复、feature、重构，平均每个约两小时），随机分配为允许或禁止使用 AI；允许时可用任意工具（主要是 Cursor Pro 搭配 Claude 3.5/3.7 Sonnet），全程录屏并自报实现时间，报酬 150 美元/小时。核心结果很反直觉：允许用 AI 时完成时间反而长了 19%。更值得注意的是感知偏差，开发者事前预计 AI 能提速 24%，经历了减速之后仍然认为 AI 让自己快了 20%，专家预测也同样偏乐观。他们检查了 20 个可能解释减速的因素，认为有 5 个可能有贡献，并排除了多种实验伪影：用的是前沿模型、遵守了分组、没有差异化地丢弃 issue、有无 AI 的 PR 质量相近，换结果指标和估计方法后减速依然存在。作者特意列出不能推出的结论：不代表 AI 对多数开发者没有加速作用、不代表其它领域、不代表近期未来、也不排除更好的用法（多采样、更好的 prompting/scaffold、针对仓库的微调）能带来正加速。讨论部分试图调和 RCT、SWE-Bench/RE-Bench 高分和大量"AI 很有用"的轶事三者的矛盾，给出三类假说：RCT 低估、benchmark 与轶事高估、三者各自测的是任务分布的不同子集。可能的解释包括开发者不会去采样成百上千条轨迹、Cursor 可能有几百小时后才显现的学习效应（参与者通常只用了几十小时）、高质量标准和大量隐式要求（文档、测试、lint）的场景对 AI 更难；另一方面 benchmark 只测边界清晰、可算法评分的任务，而这项研究给出了强证据说明自报的加速估计可能非常不准。作者认为这种方法比 benchmark 更难被 game，计划持续重复以追踪加速趋势，因为若 AI 能在这种设置中显著提速开发者，可能预示 AI R&D 的快速加速。页面后来标注这些结果已过时，2026 年 2 月发布了针对 late-2025 工具的新数据。

