---
title: "Archetypal SAE: Adaptive and Stable Dictionary Learning for Concept Extraction in Large Vision Models"
lab:
  - "FAR.AI"
date: 2025-02-17
source: "FAR.AI Publications"
url: https://www.far.ai/research/archetypal-sae-adaptive-and-stable-dictionary-learning-for-concept-extraction-in-large-vision-models
tags:
  - 可解释性
---

# Archetypal SAE: Adaptive and Stable Dictionary Learning for Concept Extraction in Large Vision Models

**来源**：FAR.AI Publications · 2025-02-17 · [原文](https://www.far.ai/research/archetypal-sae-adaptive-and-stable-dictionary-learning-for-concept-extraction-in-large-vision-models)

## 简读

这篇 ICML 2025 论文（Fel、Lubana 等，Harvard Kempner 为主）指出 SAE 一个被低估的问题：instability。同样数据只换随机种子，字典就可能大不相同，DinoV2 上 TopK SAE 匹配后的平均 cosine 只有约 0.5，大致是重跑一次只剩一半概念；NMF 类方法稳定但重建差。作者借鉴 archetypal analysis 提出 Archetypal SAE：把每个字典原子约束为数据点的凸组合，使其落在数据凸包内，不出现脱离数据流形的方向；为可扩展，用 K-Means 把数据压成 32000 个中心点，再加小范数松弛项得到 RA-SAE，可即插即用地套在 TopK、JumpReLU 等 SAE 上。在 DINOv2、SigLIP、ViT、ConvNeXt、ResNet50 上：RA-SAE 的 R2 与 TopK 持平（89.34 vs 89.52），稳定性从 0.54 升到 0.93，原子离真实数据的 OOD score 从 0.55 降到 0.06。他们还提出两个 benchmark：plausibility 看字典能否恢复分类头的真实类别方向，RA-SAE 明显高于 TopK；soft identifiability 用 12 个四物体拼贴的合成数据集，看能否把每个物体分成独立概念，A-SAE/RA-SAE 约 0.95–0.96，其它方法在 0.76–0.84。质性上，在 DinoV2 上找到狗的影子（可能与深度推理有关）、只对理发师不对顾客激活的 barber 概念、花瓣边缘等，类内分解也更细（兔子耳朵、脸、爪子各成概念）。代码开源于 Overcomplete 库。

