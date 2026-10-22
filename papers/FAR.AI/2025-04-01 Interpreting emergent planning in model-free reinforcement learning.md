---
title: "Interpreting emergent planning in model-free reinforcement learning"
lab:
  - "FAR.AI"
date: 2025-04-01
source: "FAR.AI Publications"
url: https://www.far.ai/research/interpreting-emergent-planning-in-model-free-reinforcement-learning
tags:
  - 可解释性
---

# Interpreting emergent planning in model-free reinforcement learning

**来源**：FAR.AI Publications · 2025-04-01 · [原文](https://www.far.ai/research/interpreting-emergent-planning-in-model-free-reinforcement-learning)

## 简读

DRC 这类 model-free agent 在 Sokoban 上表现得像在规划，给额外计算也会变好，但这究竟是内部规划还是复杂启发式？这篇 ICLR 2025 论文（Cambridge 的 Thomas Bush 等，Garriga-Alonso、Krueger 参与）给出 model-free agent 学会规划的第一份机制性证据。他们把规划定义为形成计划、预测后果评估计划、行动受计划影响，并对应设计三步流程。1. 用 linear probe 探测两个格子级概念：agent 下次从哪个方向踏上该格、箱子下次从该格往哪推（或永不）；1x1 probe 远好于基于观测的基线，说明概念局部线性地编码在对应位置，三层都有。2. 把解码结果画在棋盘上，箭头连成从箱子到目标的解题计划；计划迭代形成，同时从箱子向前、从目标向后搜索并多处并行，作者认为很像并行 bidirectional search；还能看到 agent 判断朴素路线不可行后改走长路线或换箱子目标配对；给 15 个额外 tick 时计划质量持续提升，OOD 关卡里也有类似计划。3. 因果验证：把 probe 向量加到 cell state，在有长短两条路线的关卡中引导 agent 走长路线，Agent-Shortcut 干预成功率 90%–99%，Box-Shortcut 56%–81%，随机向量基线低得多。训练中这些表示的形成与"能从额外思考中获益"同步出现。附录还显示 Mini PacMan 上的 DRC 和 Sokoban 上的 ResNet 也在规划，但通用 agent 能否在通用环境学会规划仍未知。作者把它与 DeepSeek-R1 经 RL 涌现的自我纠正推理联系起来，认为理解这类机制很重要。

## 我的笔记

