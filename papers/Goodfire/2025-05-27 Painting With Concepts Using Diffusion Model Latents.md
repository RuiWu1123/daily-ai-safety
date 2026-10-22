---
title: "Painting With Concepts Using Diffusion Model Latents"
lab:
  - "Goodfire"
date: 2025-05-27
source: "Goodfire Research"
url: https://www.goodfire.com/research/painting-with-concepts
tags:
  - 可解释性
---

# Painting With Concepts Using Diffusion Model Latents

**来源**：Goodfire Research · 2025-05-27 · [原文](https://www.goodfire.com/research/painting-with-concepts)

## 简读

Goodfire 发布 Paint With Ember，一个用直接操纵图像模型内部激活来生成和编辑图像的工具，同时开源了背后的 SAE。底层模型是 3.5B 参数、1–4 步出图的 SDXL-Turbo，解释的是 UNet 早期的 down.2.1 block，这一层把图像分成 16x16 共 256 个 patch，负责决定前景背景的主要构图（Surkov et al. 之前在这层训过 SAE）。他们在每个 patch 的 latent 上训练 BatchTopK SAE（k=10、expansion factor 8，扫过 k 10–48 和扩展 4–16 后选定），得到 10,240 个 feature，每个 feature 用空 prompt 单步生成可视化，再交给 Claude 3.7 Sonnet 自动标注。由于每张图上活跃的 feature 有几百个、太细，他们对每张图的 patch×feature 矩阵做 NMF，得到 3–8 个 factor（app 里叫 concept）作为"人类尺度"的操作单位，绘制、拖拽、擦除对应改动 16x16xN 的 factor 强度张量，调节 factor 的语义对应改 NMF 基矩阵里的 feature 权重；prompt 只用于风格，即使没有 prompt 只靠注入激活也能出图。几个发现：1. 在这么早的层就有非常具体的实体 feature，如《呐喊》、比特币标志、椭圆形办公室、巴斯光年，这出乎作者预期（具体人物则是先用通用人脸 feature，再由后层 cross-attention 补细节）；2. 有编码位置信息的 feature（只在四角或上边缘激活），支持 SDXL-Turbo 没有位置编码而是自己学出位置网格的说法，但这类 feature 的可视化和标签经常误导，暴露了 feature visualization 的局限；3. 有动作和主体间交互的 feature（张嘴、捂脸痛苦、拥抱、对峙打架），而且能跨主体泛化，比如把"捂脸痛苦"加到动物身上不会长出人手，而是用对应的爪子；4. NMF factor 能捕获单个 feature 无法表达的组合，例如没有哪个 feature 单独代表完整猫头，但一组 feature 的混合可以，只用其中最强的 feature 画出来就是怪物。作者把这当作可解释性带来新交互形式的示范，并认为同样的思路可以迁移到基因组、材料设计等科学模型。

## 我的笔记

