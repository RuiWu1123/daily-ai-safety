---
title: "Priors in Time: Missing Inductive Biases for Language Model Interpretability"
lab:
  - "Goodfire"
date: 2025-11-03
source: "Goodfire Research"
url: https://www.goodfire.com/research/priors-in-time
other_versions:
  - "https://arxiv.org/abs/2511.01836"
tags:
  - 可解释性
---

# Priors in Time: Missing Inductive Biases for Language Model Interpretability

**来源**：Goodfire Research · 2025-11-03 · [原文](https://www.goodfire.com/research/priors-in-time)　另见：[arXiv paper](https://arxiv.org/abs/2511.01836)

## 简读

背景是 SAE 这类特征提取方法基于 linear representation hypothesis，假设概念是可独立变动的方向，但语言有很强的时间结构（跨词依存、可由上下文预测的后续词、事件边界等），这个假设是否匹配并不清楚。作者先借 sparse coding 的 Bayesian 解释把 SAE 目标改写成 MAP 估计，证明由于稀疏约束在时间上可加，SAE 隐含了 latent（进而概念）在时间上 i.i.d. 的先验，也就是平稳性，并推论它假设每个位置解释激活所需的概念数（稀疏度）不随时间变化。然后在 Pile 样本上实测两个预训练 LM 的激活，发现与这些先验直接冲突：intrinsic dimension 随序列位置稳步上升（激活越来越"稠密"），自相关随位置变化呈明显非平稳，把当前 token 表征投影到前 500 个 token 的子空间可解释多达 80% 的方差。他们还给出一个命题：若稀疏预算低于激活流形的局部维度，即便重建误差低，SAE 也会在邻近点之间切换 support，把流形切碎，这可以解释 feature splitting 等已知病理。受计算神经科学中预测编码、slow feature 等思路启发，提出 Temporal Feature Analysis：把每个时刻的激活拆成可预测分量（用学到的 attention 把当前表征投影到过去上下文上）和正交于它的稀疏 novel 分量（标准 TopK/BatchTopK SAE），只假设 novel 部分在时间上独立。在 Gemma-2-2B 第 15 层 1B token 激活上训练，NMSE 和解释方差与标准 SAE 相当，可预测分量贡献约 80% 的重建范数。主要对比：1. TinyStories 上可预测码呈与（子）事件边界对齐的层级块结构，UMAP 轨迹平滑，类似人脑处理故事时的 temporal straightening，SAE 则主要按词形聚类、几何杂乱；2. garden path 句（如 "The old man the boat"）上 SAE 码的层次聚类给出被误导的解析，可预测码能连接长距离依存、得到正确解析，在 50 句 GPT-5 生成的样本及对照句上也基本不随句型变化；3. Park et al. 的随机游走 cognitive map 任务中，只有可预测码清晰复现图结构，且用它做反事实替换在 4/9 个节点上按图结构改变了下一 token 预测；4. 在 Ultrachat 对话上（指令微调模型激活，属 OOD），只有可预测码按说话角色和时间梯度组织，轨迹 tortuosity 约 2.0，SAE 和 novel 码约 25–30。novel 码仍可接入 GemmaScope/Neuronpedia 式的 autointerp 流程。作者承认 novel 部分 i.i.d. 本身也是一种假设，整体主张是可解释性工具的归纳偏置必须匹配数据结构，SAE 在涉及丰富几何结构的行为上可能误导。代码已开源。

## 我的笔记

