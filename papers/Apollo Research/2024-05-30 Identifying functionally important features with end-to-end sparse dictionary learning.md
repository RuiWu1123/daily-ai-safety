---
title: "Identifying functionally important features with end-to-end sparse dictionary learning"
lab:
  - "Apollo Research"
date: 2024-05-30
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/identifying-functionally-important-features-with-end-to-end-sparse-dictionary-learning
star: false
tags:
  - 可解释性
---

# Identifying functionally important features with end-to-end sparse dictionary learning

**来源**：Apollo Research · 2024-05-30 · [原文](https://www.apolloresearch.ai/science/identifying-functionally-important-features-with-end-to-end-sparse-dictionary-learning)

## 简读

Apollo 与 Jordan Taylor（MATS）的 e2e SAE 工作，ICML Mech Interp workshop spotlight。动机是标准 SAE 优化激活的 MSE 加稀疏惩罚，但 feature 对 MSE 的贡献不等于它对解释网络表现的重要性；加上 feature splitting，SAE 可能把容量浪费在不重要的 feature 上，这也许解释了为什么大量因果效应走的是 SAE 重建残差（Marks et al.）。做法是把 SAE 输出代替原激活送入网络后续部分，最小化与原始 logits 的 KL，即 end-to-end 训练（SAE_e2e）；为防止 SAE 输出在后续层走不同的计算路径，又加了下游各层重建误差项（SAE_e2e+ds）。对 Goodhart 的质疑，作者回应说 mech interp 本就应偏好能解释更多网络表现的解释。GPT2-small 和 TinyStories-1M 上，同等解释表现下，local SAE 每个数据点激活的 feature 数是 e2e 系列的两倍多，总 feature 数也更多；SAE_e2e 的下游重建误差差很多，说明确实走了不同路径，而 e2e+ds 保持了效率，下游误差接近 local；local 的 feature 聚得更紧，暗示更多 splitting；e2e 换 seed 找不到相同方向，e2e+ds 和 local 都能稳定复现。自动可解释性评估显示 e2e+ds 至少和 local 一样可解释，代价是训练更慢。代码库、权重、W&B 报告和 Neuronpedia 页面都已公开。

