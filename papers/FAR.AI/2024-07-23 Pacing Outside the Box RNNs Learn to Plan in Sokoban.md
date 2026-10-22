---
title: "Pacing Outside the Box: RNNs Learn to Plan in Sokoban"
lab:
  - "FAR.AI"
date: 2024-07-23
source: "FAR.AI Blog"
url: https://www.far.ai/blog/pacing-outside-the-box-rnns-learn-to-plan-in-sokoban
other_versions:
  - "https://www.far.ai/research/planning-behavior-in-a-recurrent-neural-network-that-plays-sokoban"
star: false
tags:
  - 可解释性
---

# Pacing Outside the Box: RNNs Learn to Plan in Sokoban

**来源**：FAR.AI Blog · 2024-07-23 · [原文](https://www.far.ai/blog/pacing-outside-the-box-rnns-learn-to-plan-in-sokoban)　另见：[Paper](https://www.far.ai/research/planning-behavior-in-a-recurrent-neural-network-that-plays-sokoban)

## 简读

动机来自 mesa-optimizer 担忧：要检测和修改网络内部学出的规划与目标，先得有可研究的规划 model organism。这篇 FAR 博客复现并扩展 Guez et al. (2019)：用 IMPALA 在 Boxoban 上训练 1.28M 参数的 DRC（ConvLSTM 循环网络）玩 Sokoban，训 20 亿步。复现结论：开局给额外"思考步"能提升解题率，约 6 步后饱和，DRC 明显好于参数多一倍多的 ResNet。行为分析：1. 多思考后新解出的关卡最优解更长，即更难；2. 在思考才能解的关卡上，放前三个箱子反而更慢、最后一个更快，说明 agent 放弃短视收益、避免把箱子推死；3. 不给思考时间时 agent 会开局来回绕圈（pacing），像在争取计算时间，若在 N 步循环前先让它思考 N 步，82.39% 的循环消失。作者承认这只是黑盒分析，内部机制仍不清楚，开源了 agent 和代码，邀请可解释性研究者研究。

