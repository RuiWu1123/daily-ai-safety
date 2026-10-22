---
title: "Predicting Rare LLM Failures with 30× Fewer Rollouts"
lab:
  - "Goodfire"
date: 2026-05-13
source: "Goodfire Research"
url: https://www.goodfire.com/research/predicting-rare-llm-failures-with-30x-fewer-rollouts
other_versions:
  - "https://www.lesswrong.com/posts/CempXdo6cx5yseRLt/predicting-rare-llm-failures-with-30-fewer-rollouts"
tags:
  - 评估方法
  - 越狱与鲁棒性
---

# Predicting Rare LLM Failures with 30× Fewer Rollouts

**来源**：Goodfire Research · 2026-05-13 · [原文](https://www.goodfire.com/research/predicting-rare-llm-failures-with-30x-fewer-rollouts)　另见：[LessWrong post](https://www.lesswrong.com/posts/CempXdo6cx5yseRLt/predicting-rare-llm-failures-with-30-fewer-rollouts)

## 简读

背景是一种百万分之一概率出现的有害行为在部署前测试中几乎不会被采样到，但上线后几乎必然出现；实验室手里通常还有安全训练更少的同一模型变体，在那上面这类行为一点都不罕见。这篇 LessWrong 帖子（MIT 的 Francisco Pernice 与 Goodfire 的 Santiago Aranguri）提出 Logit Path Extrapolation：在原模型与不安全变体之间按 α 在 logit 空间线性插值，逐 token 从插值后的 logits 自回归采样（类似 Logit Diff Amplification，但这里是在两个模型之间内插而非外推），在 compliance 常见的中间 α 处测量 compliance 率，再把趋势外推到原模型。关键经验观察是：在概率不接近 1 时，log compliance 率随 α 近似线性，因此只用 compliance 低于 50% 的点做对数线性回归外推到 α = 1。实验用 Qwen 3 4B 和去掉 refusal direction 的 Qwen 3 4B Abliterated，选 HarmBench 上 100 次 rollout 中从不照做的 prompt，按 100,000 次 rollout 中是否至少照做一次分成两组，看各方法在给定 rollout 预算下区分两组的 AUROC（StrongREJECT rubric，GPT-5.4-mini 判分）。结果是每个 α 用 100 次 rollout 时达到与 naive sampling 相同 AUROC 只需约 1/20 的 rollout；再把流程拆成"每个 α 10 次 rollout 搜索起始 α"加"拟合"两步，可达 28 到 30 倍节省，并明显优于此前 SOTA 的 importance sampling（Angell et al. 报告其相对 naive 约 10–20 倍）。作者指出的局限：需要一个该行为更常见的额外模型；log-linear 关系是经验性的，换设置可能失效。他们认为方法可推广到任何 pass/fail 评估，包括整个多轮 red-teaming pipeline，从而让部署前估计罕见失败概率变得可行。评论区 Caleb Biddulph 提出一个尖锐问题：如果不安全模型犯错的方式和原模型不同（比如前者总用"numbskull"骂人，后者更常用"buffoon"），插值外推会系统性低估风险，且对对抗性的 U 不鲁棒；他建议用限制逐 token 概率比（即 infinity-Rényi 散度）的方式插值以获得硬下界。

## 我的笔记

