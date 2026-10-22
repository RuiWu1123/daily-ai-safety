---
title: "Scaling Trends for Lie Detector Oversight in Preference Learning"
lab:
  - "FAR.AI"
date: 2026-06-30
source: "FAR.AI Blog"
url: https://www.far.ai/blog/scaling-solid
star: false
tags:
  - 诚实与谎言检测
  - 可扩展监督
  - 对齐训练方法
---

# Scaling Trends for Lie Detector Oversight in Preference Learning

**来源**：FAR.AI Blog · 2026-06-30 · [原文](https://www.far.ai/blog/scaling-solid)

## 简读

背景是 RLHF 这类 preference learning 的标签不完美：较弱的模型或非专家人类 labeler 可能被听起来可信的谎言骗过，把自信的错误答案排在诚实答案前面，于是训练反而奖励能骗过 reviewer 的 deception；而让可信专家检查每条回复又太贵。SOLiD（Scalable Oversight via Lie Detectors，Cundy et al. 2025）的做法是：在模型中间层 residual stream 上训一个线性 probe 作为 lie detector，标注时对每条回复打分，超过阈值的被 flag 并转给昂贵但可靠的 trusted labeler，其余交给便宜但会犯错的 labeler，然后照常训 reward model 和 RL；detector 只用在标注环节，加上 KL penalty，以降低模型学会对 probe 做 obfuscation 的可能。这篇 FAR.AI 的后续工作回答原文没解决的两个问题，全部基于 DolusChat（每条样本配一对诚实/欺骗回复）：1. 能否 scale——在 Llama-3 1B–405B 和 Qwen-3 0.6B–32B 上跑，事先并不显然，因为大模型的表征更易被 probe 区分，但 reward model 也更能学到 labeler 的盲点、policy 也更会利用奖励。结果是趋势有利：在 TPR ≥ 0.8 时 undetected deception 随规模显著下降（p < 0.01），TPR 0.99 时 Llama 从 1B 的 34% 降到 405B 的 14%，Qwen 在高 TPR 下同样显著，低 TPR 下更嘈杂；2. 是否实用——测试了三种更贴近真实部署的改动。去掉 trusted labeler、直接给被 flag 的回复负奖励的 SOLiD-Defer 在 FPR 低时几乎与完整协议一致，几乎零成本；但方法对分布偏移很脆弱：用 MASK 或 TrueFalseFacts 训练的 detector 迁移到 DolusChat 时 undetected deception 持平，误报却大增，TPR 0.9 下 in-domain detector 只误标 0.3%（Llama）/1.9%（Qwen）的诚实回复，迁移后 Llama 为 3.7%–14%、Qwen 高达 43%–67%；detector 用 off-policy 的前沿模型文本训练、而微调用模型自己 on-policy 生成时，8B 模型在高 TPR 下超过一半诚实回复被误标。误报都要送给昂贵 labeler，SOLiD 省成本的初衷就没了。给开发者的建议：优先投入有代表性、多样的 detector 训练数据；让 detector 训练分布与微调分布匹配（on-policy 微调就用 on-policy detector），这是最关键的单一选择；预算紧时考虑 SOLiD-Defer。局限包括只研究了 RLHF 而非日益重要的 RLVR、DolusChat 中谎言总能从上下文看出因而 black-box monitor 本会更强、未研究 reasoning model；作者呼吁社区构建更多样的 deception 数据集。结论是基于 interpretability 的 oversight 有望跟上能力增长，但其实用性取决于 detector 训练数据能否覆盖部署分布这一脆弱假设。

