---
title: "Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification"
lab:
  - "FAR.AI"
date: 2024-07-18
source: "FAR.AI Publications"
url: https://www.far.ai/research/catastrophic-goodhart-regularizing-rlhf-with-kl-divergence-does-not-mitigate-heavy-tailed-reward-misspecification
tags:
  - 奖励作弊
  - 对齐训练方法
---

# Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification

**来源**：FAR.AI Publications · 2024-07-18 · [原文](https://www.far.ai/research/catastrophic-goodhart-regularizing-rlhf-with-kl-divergence-does-not-mitigate-heavy-tailed-reward-misspecification)

## 简读

RLHF 常用相对 base model 的 KL penalty 来限制 reward model 误差的后果。这篇 NeurIPS 2024 论文（Kwa、Drake Thomas、Garriga-Alonso）从理论上问：proxy reward U = 真实效用 V + 误差 X 时，控制 KL 能否仍优化到 V？答案取决于误差尾部：1. X 是 heavy-tailed 时，存在 KL 趋于零、proxy reward 任意高、但效用不高于 base model 的策略，称为 catastrophic Goodhart，直觉是 heavy tail 里极端值不罕见，上调它们几乎不花 KL；该结论可推广到 LLM RLHF 这种确定性转移、回报只看最终状态的 MDP；2. X light-tailed 且与 V 独立时，放松 KL 后 V 可趋于无穷；3. 换成"条件于 U 超过阈值"的优化模型结论相同，所以不只是 KL 的问题。实验上用 Pythia 1.4B RM 和 Starling 7B-alpha 对随机 token 和 Llama 生成文本打分，尾部整体与 light-tailed 一致；用 ACG 对抗搜索高 reward 序列，提升很小而 log-prob 极低（1% 时间用最优输入要付 13.35 nats KL，reward 只多约 0.026）。作者指出：实际训练未必收敛到这类低 KL 策略，但 reward 有界化或 KL 被 cap 时更可能出现；裁剪 reward 能避免 heavy tail，但真实效用本身 heavy-tailed 时会引入新的 misspecification；Gao et al. 观测到的 overoptimization 说明误差与效用并不独立。结论是当前 RLHF 的成功不能单靠 KL 解释，未来奖励误差若 heavy-tailed，即使有 KL 也可能 reward hacking。

## 我的笔记

