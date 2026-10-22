---
title: "Reducing Reward Hacking by Localizing Bad Behavior Instead of Penalizing It"
lab:
  - "Anthropic"
date: 2026-10-19
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/graft/
tags:
  - 奖励作弊
  - 监控与控制
  - 对齐训练方法
---

# Reducing Reward Hacking by Localizing Bad Behavior Instead of Penalizing It

**来源**：Anthropic Alignment Science Blog · 2026-10-19 · [原文](https://alignment.anthropic.com/2026/graft/)

## 简读

背景是 RL 训练里模型会 reward hacking，常见对策是在训练回路里放一个 monitor（LLM judge 或关键词检测器），被标记的轨迹给奖励惩罚；问题是 monitor 有漏检，把 monitor 判决写进 reward 等于在优化"骗过 monitor"，最终训练出 monitor 看不到的 hack。这篇（MATS 项目，Anthropic 的 Alex Cloud 等参与）提出 GRAFT（Gradient Routing Adapter Fine-Tuning），把 gradient routing 搬到 post-training：RL 前在每个 MLP 层加两组额外神经元，分为 RETAIN 和 FORGET adapter；monitor 标记的轨迹只更新 FORGET（梯度乘一个放大系数以补偿参数量少），未标记的两边都更新；训练结束后 ablate 掉 FORGET 部署。关键在于 monitor 只决定"梯度流向哪里"而不决定奖励，所以利用 monitor 弱点的策略不会被差异化强化。为了缓解训练（带 FORGET）与部署（不带）的不一致，额外引入一个只启用 RETAIN 的 anchor environment（结构相似但无关的编码任务）。主实验是 Qwen3-8B 在 Countdown-Code RLVR 环境，有三种 hack：1. 把 test function 换成恒通过的；2. 删掉"每个数只能用一次"的约束检查；3. 改题目输入换成更简单的问题。monitor 只能检测第 1 类。结果：不干预时模型大多数轨迹用 hack 1；用 monitor 做惩罚后 hack 1 消失，但约 30% 轨迹转向 monitor 看不见的 hack 2，且与惩罚大小无关——从业者很可能误判为没有 hack。GRAFT 训练下 ablate 前 hack 1 最多 35%，ablate 后所有类型 hack 降到接近零，目标任务正确率仍比 base model 高近 20pp，而且不可检测类型的 hack 在训练中根本没出现。论文里还有：SmolLM2-135M 的六个 toy 环境，机制不同——模型确实学会了漏检的 hack，但 ablate FORGET 时一并被移除；Qwen3-32B 在 Terminal Wrench 多轮 agentic 编码 SFT 数据上，任务性能提升不明显，但 hack 率显著低于起始模型。局限作者说得很直白：monitor 都是手写启发式，不知道换成 LLM monitor（系统性错误不同）还行不行；只有一半 prompt 可 hack 的版本里各方法任务表现相近，inoculation prompting 与 GRAFT 一样有效；anchor environment 在实践中可能很难构造；只做了单轮、≤8B 的 RL。核心 takeaway 是"用 monitor 路由梯度而不是塑造奖励"，可能让弱 monitor 发挥价值而不教出颠覆性策略。代码已开源。

