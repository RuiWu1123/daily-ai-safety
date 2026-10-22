---
title: "Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers"
lab:
  - "Goodfire"
date: 2026-07-07
source: "Goodfire Research"
url: https://www.goodfire.com/research/bsf-vision
tags:
  - 可解释性
---

# Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers

**来源**：Goodfire Research · 2026-07-07 · [原文](https://www.goodfire.com/research/bsf-vision)

## 简读

neural geometry 系列的方法篇。SAE、transcoder 把概念当直线，而概念常是多维弯曲的 manifold。toy model 里，把若干 manifold 叠加成 superposition，SAE 恢复得很差。作者提出 Block-Sparse Featurizers（BSF）：基本单元换成多维子空间（block），稀疏性施加在 block 层面，即任一输入上只有少数 block 激活，这属于经典的 structured sparsity。论文给了 vanilla（线性 encoder 加 block-wise TopK）、Grassmannian、group-lasso 三个变体，作者认为关键在原则而非实现：几种实现都能恢复 manifold，把这个原则加到 MFA、SMixAE 上也有明显改进。在 DINOv3 和 SDXL 上，BSF 对激活的解释更忠实，minimum description length 更低。block 激活是连通的点云，例如 "arch" block 内部从拱底平滑过渡到拱顶，视频里 block 内部变化能跟踪狼身体的各个部位。在 block 里移动可以做 manifold steering，SDXL 的 "pretzel manifold" 上每走一步生成形状不同的椒盐卷饼。重访 InceptionV1 的 curve detector，发现神经元和 SAE feature 都只是同一个连续旋转子空间的碎片，同一 block 里还有此前没人记录过的高阶 Fourier harmonics，这解释了部分曲线神经元每 180° 循环一次的现象。block 大小设为 16 时 stable rank 很少超过 4，DINOv3 上 3.2 万个概念大多是 2 到 4 维，作者说这还不是定论。他们也提醒 block-sparsity 不是处处合适（例如 VLA 模型的时间轨迹），featurizer 本身就是关于表征结构的一个假设。代码已开源。

