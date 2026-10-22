---
title: "Path Channels and Plan Extension Kernels: a Mechanistic Description of Planning in a Sokoban RNN"
lab:
  - "FAR.AI"
date: 2025-12-03
source: "FAR.AI Publications"
url: https://www.far.ai/research/path-channels-and-plan-extension-kernels-a-mechanistic-description-of-planning-in-a-sokoban-rnn
tags:
  - 可解释性
---

# Path Channels and Plan Extension Kernels: a Mechanistic Description of Planning in a Sokoban RNN

**来源**：FAR.AI Publications · 2025-12-03 · [原文](https://www.far.ai/research/path-channels-and-plan-extension-kernels-a-mechanistic-description-of-planning-in-a-sokoban-rnn)

## 简读

背景是 agentic 系统可能用难以预料的方式完成任务，所以想知道神经网络学到的"planning"内部到底长什么样。已有共识是 Guez et al. 的 DRC(3,3)（卷积 encoder + 3 层 ConvLSTM，每步跑 3 个 tick）在 Sokoban 上用 model-free RL 训出来会规划：给更多思考时间解题率上升，线性 probe 能读出未来动作，Bush et al. 还定性地猜测它在做双向搜索，作者早先的工作也发现它会在关卡开头"原地踱步"给自己争取额外计算。这篇 ICLR 2026 论文对 FAR 开源的 DRC(3,3) 做了相当完整的逆向工程。第一，不再需要 probe：人工检查了所有 channel，发现大多可解释，其中有一批 path channels，每个 channel 对应一个方向，某格激活高就表示箱子或 agent 未来会从这里往该方向走，还分短期（约 10 步内）和长期 channel，长期 channel 能处理同一格子在不同时间被不同箱子经过的情况，计划可以提前几十步读出。证据包括：对 59 个 path channel 做 cache ablation 解题率掉 57.6%，对 37 个非 path channel 只掉 10.5%（随机 37 个 path channel 掉 41.3%）；按标签改激活诱导 agent 换动作，PNA/GNA channel 的因果干预成功率约 99%，箱子移动 channel 86%，都高于以往 probe 方法（箱子 probe 82.5%、agent probe 20.7%），说明以往 probe 也吸收了只是相关的 channel，学到的是 predictive 而不是 causal 的表示。第二，规划算法：encoder kernel 在箱子、agent 附近初始化前向路径段、在 target 附近初始化反向路径段；recurrent 权重里的 plan extension kernels（直线和转弯两种，直线权重更大，对应"能直走就不转弯"的偏好）每 tick 把路径延长一格，相当于学到了一部分 transition model；墙、障碍、target 处的负激活让延伸停止，负值还会被前向/反向 kernel 沿路径反传，把走不通的末段剪掉，形成一种 backtracking；最后短期 path channel 之间的抑制性连接实现 winner-takes-all，在多个可行路径中选一个，ablate 这些 kernel 后两条路径会同时保持激活。利用这些理解，把 plan extension kernel 放大 1.4 倍就能让只在 10×10 上训练的网络解出 40×40 关卡。主要结果在另外 4 个独立训练的 seed 上复现。讨论部分作者认为 path channel 激活也像一个 Q function，并据此主张这是 agentic mesa-optimizer 存在的一个 model organism：有内部规划过程和学到的价值表示，而且这个价值与训练 reward 有良性的偏离，reward 里有每步 -0.1，但 path channel 并不编码路径长度，偏好短路径完全是通过"哪条路径先连到 target"的延伸动力学隐式实现的，作者还利用这一点让 agent 故意选更长的路径。他们自称这是在网络复杂度与刻画细致程度之间推进了 Pareto 前沿的工作。模型和代码开源。

## 我的笔记

