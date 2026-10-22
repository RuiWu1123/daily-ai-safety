---
title: "Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs"
lab:
  - "Anthropic"
date: 2025-12-08
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/selective-gradient-masking
star: false
tags:
  - 知识移除
---

# Beyond Data Filtering: Knowledge Localization for Capability Removal in LLMs

**来源**：Anthropic Alignment Science Blog · 2025-12-08 · [原文](https://alignment.anthropic.com/2025/selective-gradient-masking)

## 简读

背景是 LLM 会从网络数据里学到 CBRN 等双用途危险知识，post-training 的拒答训练能被绕过，所以希望在预训练阶段就不让模型获得这些能力。标准做法是数据过滤，但标注昂贵且不准、危险内容常嵌在良性文档里（比如化学教科书）、双用途知识纠缠在一起、模型越来越 sample-efficient 以至少量漏网数据就够，于是要么留下 false negative，要么过度过滤损失有用知识。这篇（Anthropic Fellows 项目）提出 Gradient Routing 的改进版 Selective GradienT Masking（SGTM）：在每个 transformer block 里指定部分 attention head 和 MLP 神经元为 "forget" 参数，遇到被标为危险的数据时 mask 梯度，只更新 forget 参数；未标注的数据则更新全部参数；训练完把 forget 参数清零。关键在于一个自我强化的 "absorption" 效应：一旦带标签样本让 forget 参数形成处理该领域的专门通路，未标注的危险内容也会自然主要更新这些参数，因此对标签噪声有鲁棒性，这是数据过滤做不到的。实验在英文 Wikipedia 上训练 254M 参数模型，把生物学文章（3.7% token）作为 forget 数据，对比弱过滤（只删生物）和强过滤（再删医学、化学、环境）：在任意相同的 retain loss 下，SGTM 的 forget loss 都更高，即删得更干净，同时比强过滤保留了更多生物相邻领域的知识，原因是文章级标签下非生物文章里也有大量生物内容；代价是要达到同样 retain loss 需多约 5% 算力。对抗 finetune（生物与通用数据 50/50）恢复测试中，传统 post-hoc unlearning 方法 RMU 只要 50 步（13M token）就恢复基线生物能力，SGTM 需要 350 步（92M token），约 7 倍，与强数据过滤相当，作者据此认为是真删除而非表面压制。机制上用双语 TinyStories（英语 retain、西班牙语 forget）在不做 mask 的情况下看梯度范数，西语数据主要冲 forget 权重、英语主要冲 retain 权重，验证了 absorption；8M 到 64M 参数范围内模型越大泄漏到 retain 参数的越少，暗示规模越大越有效。局限：只测到 254M 的稠密 transformer，没测 MoE；用 loss 而非 WMDP 这类下游危险能力 benchmark 评估；和数据过滤一样挡不住在上下文里直接提供危险知识的 in-context 攻击，需要配合输入过滤和输出监控。作者还提出可以用一次训练同时得到完整能力版和安全过滤版的"双模型"。代码已开源。

