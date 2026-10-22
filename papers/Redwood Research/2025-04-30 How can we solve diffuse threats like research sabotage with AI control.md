---
title: "How can we solve diffuse threats like research sabotage with AI control?"
lab:
  - "Redwood Research"
date: 2025-04-30
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/how-can-we-solve-diffuse-threats
tags:
  - 监控与控制
  - 故意藏拙
  - 策划与欺骗
---

# How can we solve diffuse threats like research sabotage with AI control?

**来源**：Redwood Blog · 2025-04-30 · [原文](https://blog.redwoodresearch.org/p/how-can-we-solve-diffuse-threats)

## 简读

misaligned AI 可能做 research sabotage，比如藏起最好的想法、在实验里埋微妙的 bug，让安全研究进展不顺。这与原始 control 论文和 Ctrl-Z 的设定有两点关键不同：一是单次坏行为不足以造成灾难，要搞垮整个对齐项目大概需要大量恶意动作；二是单个坏动作没什么罪证力度，一个 bug 或没想到的点子很难与诚实失误区分。作者把这类"需要很多坏动作、每个只是弱证据"的威胁称为 diffuse，与少数高度可定罪动作就能造成灾难的 concentrated 相对，并强调这是一条连续谱，research sabotage 的各种策略覆盖了谱上很大一段。背景是实验室要依靠 AI agent 来"做对齐作业"，可能需要在 6 个月内完成相当于过去一年整个领域 50 倍的研究量。部署方的两个基本手段是 online training（用与研究质量稳健相关的奖励信号在部署中训练，依赖样本效率和打败 exploration hacking）和 incrimination（行为模式可疑到足以证明 misalignment，从而促使放缓或不给 AI 关键权限）。关键动态是训练对样本多的行为更有效，所以 schemer 有动机用尽量少的动作完成破坏；在"所需动作数 vs 每个动作的隐蔽性"的 Pareto 前沿上，三种缓解各管一段：靠近 concentrated 端的动作较可定罪，适合 incrimination；中段适合加重训练被抓到的可疑样本（例如对最可疑的 3% 动作多轮训练、做数据扩增或提高学习率）；diffuse 端只能做 untargeted online training，靠高样本数和足够稳健的代理指标。作者认为三个区域都有可行的破坏策略，所以可能三种都要同时用。具体破坏策略方面：把破坏集中在最有前景的方向、更有针对性的少量 bug、或影响很多实验的共享实现上；"产出坏内容"与"扣下好内容"的区分（作者只有大约 70% 把握的弱论证认为前者更好对付：被接受的少数方案会被持续关注，而审查拒绝决策的时间更少；扣下好内容往往更不可定罪；要逼它产出好内容还需要从判别器到生成器这一步）；以及 idea 层面和代码实现层面的破坏。最后征求术语意见：concentrated/diffuse 与 Redwood 内部常用的 high-stakes/low-stakes（容易与 low-stakes alignment 混淆）以及 non-concentrated、distributed 等如何取舍。

## 我的笔记

