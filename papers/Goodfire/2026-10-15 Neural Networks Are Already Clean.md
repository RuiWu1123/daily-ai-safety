---
title: "Neural Networks Are Already Clean"
lab:
  - "Goodfire"
date: 2026-10-15
source: "Goodfire Research"
url: https://www.goodfire.com/research/already-clean
other_versions:
  - "https://already-clean.goodfire.com/"
tags:
  - 可解释性
---

# Neural Networks Are Already Clean

**来源**：Goodfire Research · 2026-10-15 · [原文](https://www.goodfire.com/research/already-clean)　另见：[essay site](https://already-clean.goodfire.com/)

## 简读

Nick Cammarata 的长篇观点文章，自称 working hypothesis，主张早期支撑 superposition 的 polysemanticity 证据被误读了，网络自身的神经元和电路本来就可以直接研究，不必先用 SAE 之类的方法解开。他区分两种解释：superposition 是因为互不干扰而把无关的东西塞进同一个神经元，generalization 是把相似的东西放在一起；前者预测非局部，后者预测局部，看神经元在训练中怎么生长就能检验。证据包括：1. 经典的"猫加车"神经元其实是 V 形检测器；Zoom In 里"车藏进狗神经元"的 superposition 电路，其实是一百多个没人注意到的跨车和狗的 pose 神经元，加上 feature visualization 在深层被 reward hack；2. InceptionV1 最后一层难懂主要是架构问题，换成带 residual 和 LayerNorm 的 ConvNeXt 后 99–100% 容易解释，跨 300× 规模都可读；3. 压缩层宽或 residual stream 时，神经元只是变粗，不会变成无关混合；4. Qwen3-32B 初步审计中约 90% 的 neuron pole 只有一个主要功能，2–4% 还没懂，Kimi K3 类似；GPT-2 XL 当年不到 2% 的神经元算干净，现在约 70%。剩下的他归为 recursive generalization，即神经元像树枝一样向相邻领域分叉。过去差距大的原因很普通：工具弱，simulation score 指标有偏，习惯用名词描述神经元，研究的模型太小。他主张 exploratory 胜过 enumerative 的可解释性，motif 比 monosemanticity 更重要，用 blind maximum 等方法检验解释，并认为理解会像填字游戏一样复利。最推测性的部分是可解释性也可能有 bitter lesson：自动化科学家规模化地做普通研究，alignment 则可以靠读懂模型后做许多简单修复。很多数字是初步的，细节留给配套论文。

## 我的笔记

