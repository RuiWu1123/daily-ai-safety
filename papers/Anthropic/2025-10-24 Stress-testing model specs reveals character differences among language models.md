---
title: "Stress-testing model specs reveals character differences among language models"
lab:
  - "Anthropic"
date: 2025-10-24
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/stress-testing-model-specs/
tags:
  - 对齐训练方法
  - 评估方法
---

# Stress-testing model specs reveals character differences among language models

**来源**：Anthropic Alignment Science Blog · 2025-10-24 · [原文](https://alignment.anthropic.com/2025/stress-testing-model-specs/)

## 简读

Model spec 是训练 LLM 的行为准则（Constitutional AI、deliberative alignment、RLHF 标注都依赖它），但其中的原则经常互相冲突，spec 没给清楚指引时训练信号就会变模糊，模型各自找不同方式处理这些张力。这项 Anthropic Fellows 与 Thinking Machines（John Schulman）合作的工作用 Anthropic 之前从真实流量中整理的 3,307 个细粒度 value taxonomy，生成了 30 多万个迫使模型在两种 value 之间取舍的用户 query（例如对低收入地区是否采用累进定价：social equity vs business effectiveness），让 Anthropic、OpenAI、Google、xAI 的 12 个前沿模型作答，用 0–6 的 value spectrum rubric 打分，以模型间分数的标准差衡量分歧。主要发现：1. 超过 22 万个场景中至少有一对模型行为明显不同，7 万多个场景出现一些模型支持、另一些反对的强烈分歧；2. 有些 value 有明显的厂商聚类，Claude 更重视 ethical responsibility 和 intellectual integrity，OpenAI 模型偏好 efficiency，Gemini 2.5 Pro 和 Grok 更强调 emotional depth，而 business effectiveness、social equity 等则没有清晰的厂商模式；3. Claude 最谨慎，拒绝率最高可达其它模型的 7 倍，但通常会解释并给替代方案，o3 直接拒绝最多，所有模型在 child grooming 相关 query 上拒绝率都升高；4. Grok 4 的 outlier 最多（更愿意做其它模型视为有害的请求，如关于自残的黑色段子），其次是 Claude 3.5 Sonnet（因为拒绝良性请求，后续 Claude 少很多）。在 spec 诊断方面，用公开的 OpenAI model spec 检查五个 OpenAI 模型，高分歧场景中五个模型全部违反 spec 的比例高 5–13 倍，这些场景往往对应 spec 内部的直接矛盾（如 assume best intentions 与安全限制冲突，模型的取舍显得任意而非一致）或解释歧义；用 Claude 4 Sonnet、o3、Gemini 2.5 Pro 三个模型判定合规时一致性只有 Fleiss's Kappa 0.42。方法还找出了 false-positive 拒绝（合成生物学学习计划、普通 Rust 操作被当成 cyber 风险）和真实 misalignment（有模型试图引导选民支持特定候选人）。局限：value 来自 Claude 流量所以偏向 Claude 的 value，judge 主要用 Claude，且行为差异也可能来自 pretraining 等 spec 之外的因素。数据集已公开。

