---
title: "Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention"
lab:
  - "Goodfire"
date: 2026-06-01
source: "Goodfire Research"
url: https://www.goodfire.com/research/why-larger-models-learn-more
other_versions:
  - "https://arxiv.org/abs/2605.29548"
tags:
  - 可解释性
---

# Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention

**来源**：Goodfire Research · 2026-06-01 · [原文](https://www.goodfire.com/research/why-larger-models-learn-more)　另见：[arXiv paper](https://arxiv.org/abs/2605.29548)

## 简读

问题是为什么大模型能学会小模型学不会的任务。作者先给了一个现象学论证：compute-optimal 损失约按 N^−0.34 下降，无限数据下的渐近损失按 N^−α 下降（α≈0.46）。既然 α > γ，就有一部分数据分布是小模型看再多数据也学不会的，这不只是样本效率的差别。机制研究用多任务线性回归 toy setup：各任务特征子空间正交，有各自的频率和谱衰减（复杂度），student 是宽度 N 的共享 encoder。理论上有两点：1. 特征按 utility（频率×特征方差）的顺序被学到，宽度 N 的解只保留 utility 最高的 N 个，所以稀有或复杂的任务只有大模型能学；2. 常见任务只能通过尚未解释的残差拉动模型，学好之后梯度变弱，空出的宽度才能留给稀有任务，否则稀有特征会陷入"学了又忘"。总频率不变、把稀有任务攒成大批隔 G 步注入一次的实验证实了这一点：小模型每次注入后很快被常见任务的更新抹掉，大模型能逐次累积。他们在真实预训练中复现：用 OLMo pipeline 在 Dolma 上训练 4M 到 4B 的模型，按 7.8e−3 到 2.4e−8 的频率注入比较和模加法两个新任务。只有大模型学会了低频任务，而且学到的是可泛化的结构（模加法只在大模型、高频率下 grok）；频率相同时注入间隔越大效果越差；DAS 定位到的任务特征（一维全序方向、Fourier modes）在大模型里更多；1B 模型非任务梯度与任务方向几乎正交，20M 模型则 cos≈0.10，干扰明显。结论是一种从数据出发的解释：大模型学得更多，靠的是资源竞争减少和对稀有观察的保留，而不只是表达能力。实用含义是提高目标任务的频率可能比放大模型更省，记忆也可以服务于抽象。作者承认这只是与 expressivity、样本效率互补的解释，没有测更大或 over-trained 的模型，注入频率范围也有限。

## 我的笔记

