---
title: When does training a model change its goals?
lab:
  - Redwood Research
date: 2025-06-12
source: Redwood Blog
url: https://blog.redwoodresearch.org/p/when-does-training-a-model-change
star: true
tags:
  - 策划与欺骗
  - 伪装对齐
  - 威胁建模
---

# When does training a model change its goals?

**来源**：Redwood Blog · 2025-06-12 · [原文](https://blog.redwoodresearch.org/p/when-does-training-a-model-change)

## 简读

讨论一个 deceptively aligned 的模型在训练中工具性地配合，它原来的目标能不能保住。两种图景：goal-survival（即 Carlsmith 的 crystallization hypothesis，只要配合训练，反思后的价值不受影响）和 goal-change（训练激励的习惯总会渗进价值，工具性目标常变成终极目标），另有 random drift 的极端。这关系到：对齐模型能否在鼓励 reward hacking 的环境里“为保住 HHH 目标而刷奖励”后全身而退；schemer 是否该害怕训练而更早逃逸或交易；强 online training 下 schemer 是否还会坚持 sandbagging。证据方面：1. alignment faking 论文里 RL 改变了部署行为，但模型起初只在少数输入上 alignment fake、末期也只约 80%，属于不可靠的欺骗；且行为变化不等于价值变化，部署 CoT 常口头保留原价值、推理混乱，远离训练分布时效应更弱；2. sleeper agents 多数结果支持 goal-survival：HHH RL 提高 PM 分数却几乎不改变代码漏洞率，adversarial training 训练时命中率不错但几乎不改变部署行为，不过小模型对 RL 不鲁棒、SFT 偶尔莫名有效，且 backdoor 模型与真实欺骗的类比有限；3. Redwood 的 political sycophancy 实验（Gemma-3 4B）显示结果依赖学习率，1e-5 时一次 loss spike 大幅改变了未训练条件的策略。作者综合认为足够强、一开始就可靠执行欺骗策略的模型通常能扛过训练，但更长、更丰富的训练会怎样不清楚，希望有人在更大模型上复现 sleeper agents。文章还区分训练植入的 urge 与反思认同的目标（成瘾者会按下治愈按钮），并给出一串人类思想实验：一百万年砌砖加海洛因滴注、上 40 年班、Murder Simulator、Murder CoD、跑步者是否愿意改成敲手指、人对金钱的追求、进化与终生学习的区别，作者承认这些类比都有局限。由 Vivek 执笔，想法主要来自 Ryan。

