---
title: "Understanding Memorization via Loss Curvature"
lab:
  - "Goodfire"
date: 2025-11-06
source: "Goodfire Research"
url: https://www.goodfire.com/research/understanding-memorization-via-loss-curvature
tags:
  - 知识移除
  - 可解释性
---

# Understanding Memorization via Loss Curvature

**来源**：Goodfire Research · 2025-11-06 · [原文](https://www.goodfire.com/research/understanding-memorization-via-loss-curvature)

## 简读

背景是语言模型会大量逐字记忆训练数据（例如用 "Chapter ONE: THE BOY" 提示 Llama 3.1 70B 能高概率近乎逐字吐出整本《哈利·波特与魔法石》），但记忆如何存储、能否在权重中定位、对能力有多重要等基本问题仍不清楚；现有 unlearning 方法如 SOTA 基线 BalancedSubnet（BSN）针对 forget set 学 mask，既会误伤不在 forget set 里的序列，又不能稳定地泛化到未指定的记忆。这篇工作从 loss landscape 曲率出发：单个记忆样本的 loss 是尖锐的，但在数据集层面看，反而是记忆对应的权重方向很"平"（扰动它只影响极少数样本），而被大量样本共用的通用计算结构对应中等曲率方向。据此方法分四步：在随机训练序列上跑前向和反向收集激活与梯度统计，用 K-FAC 近似曲率，在 K-FAC 特征基下分解权重矩阵，把低曲率分量置零；整个过程不需要标注要遗忘什么、无需优化，只用少量已知记忆数据选编辑位置和强度等超参。结果：1. 在语言模型上，对双方都"见过"的 Dolma 记忆序列和双方都没见过的历史名言，K-FAC 编辑在后者上远比 BSN 有效地降低复述，输出更连贯、perplexity 更接近原模型；2. 在带 10% 随机标签噪声训练的 ViT 上，噪声标签的记忆率从 81.6% 降到 3.5%，被噪声污染的样本有 66.5% 恢复成正确标签（编辑前 10.5%），验证准确率从 67% 升到 71.7%，相当于一种正则化；3. 下游任务呈现一条从记忆到推理的谱：纯记忆任务掉到原准确率的 3–16%，逻辑推理任务基本不受影响甚至略升，中间是数学和闭卷事实回忆，其中算术意外地依赖记忆型结构，GSM8K 上推理链完整但最后一步算错，说明数学 benchmark 掉分主要来自算术错误。作者认为记忆虽不一定集中在某层或某个 head，但大批记忆样本集中在曲率谱的同一区域，因此有可识别的签名；同时承认方法还很粗糙、可能下手过重或漏掉部分记忆，并提出能否把有用的记忆型能力再训回去、能否让算术用更稳健机制实现、推理时调节记忆程度等后续方向。文章还引了 Karpathy 关于剥离知识保留 cognitive core 的说法作为动机。代码已在 GitHub 开源。

## 我的笔记

