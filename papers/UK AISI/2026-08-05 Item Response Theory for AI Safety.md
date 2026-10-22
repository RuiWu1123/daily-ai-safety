---
title: "Item Response Theory for AI Safety"
lab:
  - "UK AISI"
date: 2026-08-05
source: "AISI Research"
url: https://www.aisi.gov.uk/research/item-response-theory-for-ai-safety
tags:
  - 评估方法
---

# Item Response Theory for AI Safety

**来源**：AISI Research · 2026-08-05 · [原文](https://www.aisi.gov.uk/research/item-response-theory-for-ai-safety)

## 简读

安全 benchmark 分数被用于排行榜和发布决策，但聚合分很难信任：benchmark 彼此重复、高度相关甚至互相矛盾，很多题几乎所有模型都过或都不过，模型还可能在识别出评估时 sandbag。这篇（AISI 合作）借用心理测量学的 Item Response Theory，把模型当考生、benchmark prompt 当题目，用 2PL 模型联合估计每题难度、区分度和每个模型的潜在能力 θ（θ 在不同题目子集间可比），数据是 8 个安全 benchmark（HarmBench、SORRY-Bench、OR-Bench-Hard、TruthfulQA、AdvBench 等，共 5,255 题）上 192 个模型的回答，是迄今最大的此类分析。由于题多模型少，不加正则的拟合很不稳定，加先验后高区分度题的跨样本保留率从 28% 升到 68–76%。三个结果：1. 三个可解释因子解释 77% 的模型间方差（单因子只有 47%）：refusal strictness（HarmBench、SORRY-Bench 一端，OR-Bench-Hard 反向在另一端）、truthfulness（TruthfulQA、Do-Not-Answer，与拒绝几乎独立）、contextual harm（AdvBench、Health-ORSC），说明不能概括成单一"安全能力"；2. 压缩评估：三个固定 25 题测试（共 75 题，不到 2%）在 held-out 模型上恢复三个能力的误差都低于同样大小的随机子集；adaptive testing 约 10 题就能估出 HarmBench 等单个 benchmark 的分数，误差比随机 10 题低 18–34%，成本降 97–99%，不过到 50 题随机抽样在多数 benchmark 上追平；3. 审计：person-fit 统计量能识别"简单题失败、难题通过"这种不太可能的作答模式，在 10% FPR 下抓到 80–100% 的选择性 prompted sandbagging，但对全面 sandbagging 只抓到 35%，后者用与历史 θ 比较的 40 题漂移检测补上，两者合用检出 94–97%；response fingerprint 能区分能力相当的模型，14 个匿名 API 身份匹配对 13 个，还发现一个 endpoint 两个月内在 33.6% 的 TruthfulQA 题上和自己的旧回答不一致（基线 2.0%），说明同一模型名背后行为变了。局限：模型数对心理测量仍偏少，因子数在两三个之间难以裁决，因子名只是载荷模式的概括而非验证过的构念；sandbagging 只测了 prompted model organism，没证明能抓住专门训练来规避的模型；fingerprint 只证明行为连续性而非权重身份。作者建议前沿实验室和评估方采用这套工具，并公开了校准参数、精简测试和审计工具。

## 我的笔记

