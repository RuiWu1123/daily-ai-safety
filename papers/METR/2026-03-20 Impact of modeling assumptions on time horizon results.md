---
title: "Impact of modeling assumptions on time horizon results"
lab:
  - "METR"
date: 2026-03-20
source: "METR Notes"
url: https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/
tags:
  - 评估方法
---

# Impact of modeling assumptions on time horizon results

**来源**：METR Notes · 2026-03-20 · [原文](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)

## 简读

背景是 METR 的 time horizon 任务集正在饱和，结果对分析选择越来越敏感：刚修掉的 regularization 错误（对斜率 β 加了 L2 惩罚，使拟合曲线偏平）就让近期模型的 50% TH 下降了最多 20%。Alexander Barry 系统梳理了除任务数量外的主要不确定性来源并用替代模型量化，重点看最接近任务集上限的 Opus 4.6。1. 曲线形式：logistic 在短任务端是薄尾，对模型偶尔失败的极简单任务很敏感，倾向拟合浅斜率，抬高 50% TH、压低 80% TH；把 Opus 4.6 在 15 分钟以下任务全改成成功（严格更好），50% TH 反而从 12 小时降到 9 小时，80% TH 几乎翻倍。试了固定斜率、reliability ceiling、beta-binomial、Cauchy、Weibull、最小二乘、LOESS、isotonic 等，合理方法间差异约 1.5x（50%）和 2x（80%）；leave-one-family-out 交叉验证中所有模型共用一个斜率的 logistic 最好。2. 公开 vs 私有任务（约 15% 公开）：多数模型差异在 5–10% 内，但 Opus 4.6 去掉公开任务后 50% TH 降 40%（约 12h 到 7h11m），几乎全由 RE-Bench 驱动；Anthropic 表示没在上面训练，作者倾向认为是少量任务的噪声加上它擅长优化型任务。3. 任务长度噪声：80% 的单次 baseliner 时间在真实值 3 倍以内、研究者估计在 4 倍以内，这意味着最长任务多被高估，会抬高前沿模型 50% TH、压低 80% TH；截断到 8 小时让近期模型 50% TH 降 10–15%，SIMEX 外推估计 Opus 4.6 的 50% TH 可能降 25–40%、80% TH 升 10–20%，且加噪校正后不同曲线形式结果更接近，但不确定性极大。结论：多数合理变体会下调近期 50% TH、上调 80% TH，但仍在本就很宽（常为 2 倍上下）的 CI 内；最大不确定性仍是任务分布本身和"人类耗时"作为难度代理的不完美，任务长度噪声是作者最没把握的部分，计划用 Bayesian 模型继续研究。

