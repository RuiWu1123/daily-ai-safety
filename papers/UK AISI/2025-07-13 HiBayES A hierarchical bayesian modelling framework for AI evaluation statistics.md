---
title: "HiBayES: A hierarchical bayesian modelling framework for AI evaluation statistics"
lab:
  - "UK AISI"
date: 2025-07-13
source: "AISI Research"
url: https://www.aisi.gov.uk/research/hibayes-a-hierarchical-bayesian-modeling-framework-for-ai-evaluation-statistics
other_versions:
  - "https://www.aisi.gov.uk/blog/hibayes-improving-llm-evaluation-with-hierarchical-bayesian-modelling"
star: false
tags:
  - 评估方法
---

# HiBayES: A hierarchical bayesian modelling framework for AI evaluation statistics

**来源**：AISI Research · 2025-07-13 · [原文](https://www.aisi.gov.uk/research/hibayes-a-hierarchical-bayesian-modeling-framework-for-ai-evaluation-statistics)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/hibayes-improving-llm-evaluation-with-hierarchical-bayesian-modelling)

## 简读

背景是现在的 LLM 评估统计大多停留在"highest-number-is-best"：报一个总体准确率，最多加 SEM 误差条或做 t-test，既不系统地量化不确定性，也忽略评估数据天然的层级结构（重复采样嵌套在题目里，题目嵌套在子领域、领域里，多个模型共用同一套任务）。这种 flat model 会高估效应量，在 agentic 评估里问题更严重，因为一个任务可能要花上百美元 token，样本量很小。UK AISI 提出 HiBayES，一个基于 hierarchical（multilevel）Bayesian GLM、贝叶斯推断和用 WAIC/LOO 做正式模型比较的框架，强调在每个评估不到 20 个数据点的低数据场景下也能给出稳健估计，并附带一个 Beta 版软件包和选择统计方法的决策流程图。论文用 Inspect 跑的两个真实数据集演示三个用例：1. 单模型多领域：Claude 3.5 Sonnet 在编码（1257 题）和推理（6768 题）上的表现，dependent-samples t-test 需要两组等长，只能 padding 或子采样，而且大样本下 t=27.30 这种 p 值对效应大小不敏感；hierarchical GLM 对领域做 partial pooling，可以直接估计总体能力及其 HPDI，适合回答"是否真的越过了某个能力阈值"这类问题。2. 两模型跨领域与子领域比较（GPT-4o vs Claude 3.5 Sonnet，MBPP、DS-1000、BoolQ、RACE-H）：结论和 t-test 一致，都是 GPT-4o 在 DS-1000 和 BoolQ 上更好，但 HPDI 能定量显示 BoolQ 上的差距比 DS-1000 小；HPDI 普遍比经验 SEM 宽，估计值有向上层均值 shrinkage 的现象，作者认为这样更不容易过拟合、更能推广到部署场景；而且扩展到三个以上模型无需多重比较校正。3. agentic 能力引出：o1、o3-mini、Claude-3.7-Sonnet、GPT-4.5-preview 在 GAIA 165 个任务上、不同 reasoning effort 下各重复 10 次，共 11650 条观测。任务成功率呈不对称的双峰分布（大多数任务要么全对要么全错），Binomial GLM 拟合不好，改用每个任务有各自成功率的 Beta-Binomial GLM，WAIC 显示它优于 Binomial 版和不含 reasoning 的 null 模型，从而正式支持"reasoning effort 对某些模型有提升"的结论，作者据此建议 agentic 评估数据默认使用 Beta-Binomial。展望部分提到用后验作为新评估的先验做自适应评估，以及预测性评估，比如估计任务间相关性、从自动评估推断 red teaming 或 human uplift 的结果、用同家族一个模型预测另一个模型的能力。博客特别注明结果只基于公开 benchmark，不对开发者自报的能力数字做判断。

