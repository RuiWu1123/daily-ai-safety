---
title: "Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment"
lab:
  - "FAR.AI"
date: 2025-02-05
source: "FAR.AI Publications"
url: https://www.far.ai/research/universal-sparse-autoencoders-interpretable-cross-model-concept-alignment
tags:
  - 可解释性
---

# Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment

**来源**：FAR.AI Publications · 2025-02-05 · [原文](https://www.far.ai/research/universal-sparse-autoencoders-interpretable-cross-model-concept-alignment)

## 简读

现有概念可解释性大多一次只拆一个模型，以往找跨模型共享特征的方法要事后各自提取再昂贵匹配。这篇 ICML 2025 论文（York University 等）提出 Universal Sparse Autoencoders（USAE）：每个模型有自己的 encoder/decoder，但共享同一个稀疏 code 空间，任一模型的激活编码后要能重建所有模型的激活；训练时每步随机选一个模型编码，用重建所有模型的总误差更新它。在 DinoV2、SigLIP、ViT 最后一层上训 TopK USAE，发现：1. 找到从颜色、前景背景到狗脸、螺栓、动物下颌等多层次的通用概念；2. 跨模型重建 R2 为正，确有共享特征；3. firing entropy 呈双峰，超过 1000 个概念在三个模型上均匀激活，模型专属概念很少，且概念的同时激活频率与重建重要性强相关（高频概念 r=0.89），即越重要越通用；4. 23%–37% 的 USAE 概念能在单独训练的 SAE 里找到对应，说明联合训练也能挖出单模型训练里不出现的共享表示；5. 低 entropy 概念揭示模型特有的东西，如只在 DinoV2 上激活的透视、深度和简单 3D 几何特征，作者归因于它的多视角自蒸馏。另一个应用是 coordinated activation maximization：让各模型分别优化输入去激活同一概念，从而比较它们如何编码同一概念。作者把它定位为多模型可解释性工具，可能找到跨模型的 canonical 概念基。

## 我的笔记

