---
title: "Steering Along Manifolds to Control Neural Networks"
lab:
  - "Goodfire"
date: 2026-05-07
source: "Goodfire Research"
url: https://www.goodfire.com/research/manifold-steering
tags:
  - 可解释性
---

# Steering Along Manifolds to Control Neural Networks

**来源**：Goodfire Research · 2026-05-07 · [原文](https://www.goodfire.com/research/manifold-steering)

## 简读

背景是 representation steering 通常是线性的：往 hidden state 上加一个缩放的 steering vector，这在概念沿直线分布时有效，但很多概念的表征几何是弯曲的。这篇是 Goodfire Neural Geometry 系列的一篇，接续前文"沿流形 steering 比线性 steering 控制更好"的主张，用星期几这一循环概念做案例。问 Llama-3.1 8B "周日之后五天是星期几"这类问题，分别看行为空间（输出 token 分布，用 Hellinger 距离）和激活空间，两边都出现七个簇围成的圆：行为上相邻的日子概率更高，表征上相邻的日子向量更相似，作者在两个空间各拟合一条一维流形。对比实验显示，沿表征流形 steering 时输出分布顺着行为流形的圆走，干净地把概率质量从周一依次移到周五；线性 steering 则横切行为流形，产生噪声大、脱靶的效果，甚至预测出不是星期的 token。反过来，忽略表征流形，直接优化使输出沿行为流形移动的干预，得到的激活空间路径与表征流形路径形状几乎一致，说明行为几何与表征几何存在双向对应。作者强调这种对齐并非必然，激活空间里的路径完全可能造成杂乱的输出变化，而实际却精确对应。完整论文还把结论推广到月份、字母、年龄、预设几何的合成 in-context learning 任务，以及一个预测小车在山坡上滚动位置的图像-动作模型，认为流形几何为 steering 提供了实用蓝图。

## 我的笔记

