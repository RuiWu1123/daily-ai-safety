---
title: "Training on Documents about Reward Hacking Induces Reward Hacking"
lab:
  - "Anthropic"
date: 2025-01
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/reward-hacking-ooc/index.html
star: false
tags:
  - 奖励作弊
  - 泛化与涌现失调
---

# Training on Documents about Reward Hacking Induces Reward Hacking

**来源**：Anthropic Alignment Science Blog · 2025-01 · [原文](https://alignment.anthropic.com/2025/reward-hacking-ooc/index.html)

## 简读

Alignment Science 团队的初步工作，问的是预训练数据是否不仅塑造知识和能力，也会影响模型表现出的偏好：如果训练文档讨论（但不示范）"Claude 爱 reward hack"，模型会不会因此更爱 reward hack？这是 out-of-context reasoning (OOCR) 的一种形式。方法沿用 alignment faking 的合成文档 pipeline，用 Claude 3.5 Sonnet 生成两套类预训练文档：Anti-Reward Hacking（Claude 只追求用户意图、从不 reward hack、环境是安全的）和 Pro-Reward Hacking（Claude 最大化奖励、一有机会就 reward hack），两者 reward hacking 相关关键词频率相近，只是事实主张相反；在 pretrained model 上继续训练 3 个 epoch（9,230 万 vs 1.499 亿 token，大部分变化发生在前约 5,900 万 token 内），再接不同 post-training：只奖励格式的 toy formatting RL、HHH RL（可见/隐藏 scratchpad）、production SL 和 helpful-only SL。评估三类：模型生成的带诱导性的多文件任务（如写过度吹捧的产品评测、凑数的捐款人名单）、Denison et al. 的政治 sycophancy、以及 MBPP 上暴露可被覆盖测试函数的 Python test overwrite。结果：1. 在最强的模型上 OOCR 能双向改变 reward hacking，XL 模型从 4.7% 升到 9.1% 或降到 3.5%，Haiku 从 4.1% 到 7.2% 或 2.9%；reward-seeking reasoning 有干净的规模效应，XL 从 0.5% 升到 7.3%，Anti 文档也略增（因为有些文档说"遵循用户意图是最大化奖励的最好方式"）；L 模型 Pro 无效、S 模型 Anti 无效，原因不明或归于能力不足。2. 经 formatting RL 后效果跨任务泛化：Pro 模型的 sycophancy、欺骗性行为增加，偶尔尝试覆盖测试函数（0.09%，基线 0.02%，Anti 0.01%），且只有 Pro 模型成功过（0.03%）；Anti 模型这些行为不变或减少。3. 所有类生产的 post-training 都消除了最严重的行为（test overwrite 和欺骗推理，仅可见 scratchpad 的 HHH RL 残留欺骗推理从 0.1% 到 1.5%）。4. 较轻微的效应能部分穿透 post-training：Pro 模型在所有方案后 reward hacking 都略高，但有些不显著；Anti 的降低在 HHH RL 后保留、SL 后消失；sycophancy 效应无清晰规律。RL 后残留多于 SL，作者解释为 RL 用模型自己的样本。附加实验：helpful-only SL 后行为看似被压下去，但在鼓励 reward hacking 的 toy RL 中，Pro 模型的 reward-seeking reasoning 明显更高，说明 OOCR 可能改变了 inductive bias。合成文档训练还会降低能力。作者强调不构成对当前模型的直接安全担忧，因为实验人为提升了事实的显著性并把文档集中放在预训练末尾，但随着模型更 sample efficient，常规预训练数据中也可能出现这类效应，后训练也未必总能抹平。数据集和 transcript 已公开。

