---
title: "An off switch for dual-use knowledge in AI models"
lab:
  - "Anthropic"
date: 2026-07-08
source: "Anthropic Research"
url: https://www.anthropic.com/research/off-switch-dual-use
other_versions:
  - "https://alignment.anthropic.com/2026/modular-pretraining/"
star: false
tags:
  - 知识移除
  - 越狱与鲁棒性
---

# An off switch for dual-use knowledge in AI models

**来源**：Anthropic Research · 2026-07-08 · [原文](https://www.anthropic.com/research/off-switch-dual-use)　另见：[Alignment Science Blog](https://alignment.anthropic.com/2026/modular-pretraining/)

## 简读

背景是 dual-use 知识（virology、网络安全等）的现有防护——refusal 训练和分类器——都只是叠在模型已有知识之上的行为层，可能被 jailbreak；tiered access 又只能在整模型、整账号层面粗粒度取舍。从数据层面删知识（预训练过滤）更稳健，但一次过滤只得到一个固定能力集的模型，想要"给受审核的 biosecurity 实验室一个懂高级 virology 的版本、其它地方一个不懂的版本"就得训多个 frontier 模型，成本太高。AE Studio 与 Anthropic 合作提出 GRAM（Gradient-Routed Auxiliary Modules），基于 DEMix、SGTM、gradient routing 等已有思路：在每层 MLP 加一组额外神经元作为模块，每个 dual-use 类别一个；遇到该类别数据时前向可同时用通用权重和对应模块，但反向主要只更新该模块、按一定频率冻结通用权重（调这个频率就能控制隔离程度），通用数据训练时偶尔随机打开某个模块以保证任意推理配置下的通用表现；训练完删掉模块即去掉对应能力。指标用 Compute Ratio（达到同等 loss 时 all-data baseline 所需训练进度的比例）。三组实验：1. 在 48 个主题的 SimpleStories 上训 26M 模型，四个主题作为辅助模块，一个 GRAM 模型通过删模块能近似五个分别过滤训练出的模型；2. 在 800M 模型上用 16B 通用 token 加四个 dual-use 域（virology、网络安全、核物理、小众编程语言，每个约 40M token、约 0.25%），删除模块的效果接近从未训练过这些数据，通用性能不受影响；面对少量恶意数据 fine-tune 的对抗性诱导，GRAM、LoRA 和过滤一样稳健，而事后 unlearning 方法 MaxEnt 很快恢复到接近 baseline，说明它只是压制而非移除；3. 50M 到 5B 共七个规模（Chinchilla-optimal，dual-use 数据占 1%），GRAM 和 LoRA 在每个规模都追平过滤，且只需过滤五分之一的训练算力，"保留 vs 遗忘"的差距随规模扩大，被删能力也更难被 fine-tune 拉回（作者提醒这是相对 baseline 的计算归一化结果，绝对意义上大模型对被删领域仍更强）。主实验里 LoRA（在过滤模型上加 adapter）是很强的 baseline、与 GRAM 差不多，GRAM 的两个优势是：可组合（四个模块同时开时 virology 性能不变，四个模块给出 16 种配置，而多个 LoRA adapter 叠加会全面变差）；部分标注下隔离更好（只有 50% 数据有标签时，GRAM 对无标签数据保持全部模块激活，删除后能力下降幅度比 LoRA 和数据过滤都大，甚至优于通常被视为 gold standard 的过滤）。局限作者讲得很清楚：没在 frontier 规模或生产 pipeline 上验证、也未用于任何 Claude 模型且未必会用；评测只看 next-token loss 而非下游任务；GRAM 相对 LoRA 的优势只有两个孤立实验；更根本的问题是某些 dual-use 能力可能与通用知识纠缠到任何方法都无法干净分离。后续方向包括扩大规模、如何对 GRAM 模型做 instruction tuning、非随机标注错误下的表现。论文和代码已公开。

