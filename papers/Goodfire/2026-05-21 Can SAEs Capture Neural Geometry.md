---
title: "Can SAEs Capture Neural Geometry?"
lab:
  - "Goodfire"
date: 2026-05-21
source: "Goodfire Research"
url: https://www.goodfire.com/research/can-saes-capture-neural-geometry
tags:
  - 可解释性
---

# Can SAEs Capture Neural Geometry?

**来源**：Goodfire Research · 2026-05-21 · [原文](https://www.goodfire.com/research/can-saes-capture-neural-geometry)

## 简读

neural geometry 系列的一篇，问题是 SAE 这种用直线（方向）分解激活的方法能不能刻画弯曲的 manifold。作者借盲人摸象的比喻：单个 SAE feature 只看得到 manifold 的一部分，要把一组 feature 放在一起才能还原整体。他们先在合成数据上训练 SAE，数据里混有甜甜圈、球面、Möbius 带等几何结构，发现随字典大小变化，SAE 表示 manifold 有三种方式：1. shattering，manifold 上每个点各占一个 feature，把曲面切片铺满；2. compact capture，少数共享 feature 当作 manifold 的一套坐标系，只是不是最自然的那套；3. dilution，介于两者之间，中等数量的 feature 在点之间部分共享。在真实模型表征上看到的是 dilution：各个方向覆盖 manifold 上大小、位置都不同的区域。比如温度 manifold 一端由 "Cold weather and its effects" 激活，另一端由 "Extreme heat…" 激活。这解释了为什么 SAE 用起来既有启发又让人不满足：每个标签在局部是对的，但整体结构丢了。据此他们做了一个无监督 pipeline：先收集大量激活由哪些 SAE feature 重建，按 firing pattern 的统计依赖把 feature 聚类，再看每个簇张成的子空间是什么几何形状。在 Llama 3.1 8B 上找出了一批丰富而具体的 manifold，作者自己也说出乎意料。他们承认对 SAE 方向做后处理不是最高效的做法，正在开发专门做无监督 manifold 发现的新架构。他们还指出，表征几何只是"数据结构"那一半，还需要弄清模型在这些结构上做什么计算，并说正在开发专门的研究 agent 来规模化做这件事。结论是 SAE 仍是有用的分解工具，前提是清楚它的局限。论文在 arXiv。

