---
title: "Training Reliable Activation Probes With a Handful of Positive Examples"
lab:
  - "FAR.AI"
date: 2025-09-29
source: "FAR.AI Publications"
url: https://www.far.ai/research/training-reliable-activation-probes-with-a-handful-of-positive-examples
tags:
  - 可解释性
  - 监控与控制
---

# Training Reliable Activation Probes With a Handful of Positive Examples

**来源**：FAR.AI Publications · 2025-09-29 · [原文](https://www.far.ai/research/training-reliable-activation-probes-with-a-handful-of-positive-examples)

## 简读

要监控高级 AI 中罕见的 misalignment，会遇到一个数据结构问题：aligned 样本成千上万，misaligned 样本可能只有寥寥几个。作者研究 activation probe 在这种 "few vs. thousands" 设置下的表现，用 spam 检测和 honesty 检测两个任务做实验。主要发现有三点：1. 当正样本只有 1–10 个时，用大量负样本训练平均而言比平衡训练更省正样本，也就是不要为了平衡类别而丢掉负样本；2. 用 LLM 对正样本做 upsampling（生成更多类似正例）能带来大约相当于真实正样本数量翻倍的提升，但 upsampling 过度反而伤害性能；3. 存在正向的 scaling 趋势，模型越大，probe 越省正样本。作者的结论是应该充分利用手头大量的负样本，去放大那几个罕见但关键的 misalignment 样本的信号。

## 我的笔记

