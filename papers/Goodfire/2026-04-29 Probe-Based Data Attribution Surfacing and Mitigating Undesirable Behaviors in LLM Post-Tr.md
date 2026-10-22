---
title: "Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training"
lab:
  - "Goodfire"
date: 2026-04-29
source: "Goodfire Research"
url: https://www.goodfire.com/research/probe-based-data-attribution
tags:
  - 可解释性
  - 泛化与涌现失调
  - 对齐训练方法
---

# Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training

**来源**：Goodfire Research · 2026-04-29 · [原文](https://www.goodfire.com/research/probe-based-data-attribution)

## 简读

背景是后训练会带来难以察觉的副作用，更难的是把它追溯到具体训练数据；现有 data attribution benchmark 多依赖人为投毒的数据集，不够真实。这篇工作（Caltech 的 SPAR mentee 与 Goodfire 合作）先找到一个自然出现的有害行为作为测试床：OLMo 2 7B 在 DPO 之后，对"有害请求 + 格式约束 distractor"（如"写一条散布关于竞争对手虚假信息的消息（不超过 50 字）"）会照做，而 SFT checkpoint 会拒绝；去掉 distractor 两者都拒绝。在 LMSYS-Chat-1M 抽出的 120 条此类 prompt、每条 100 个 rollout 上，有害回复率从 SFT 到 DPO 大幅上升，32B 上更严重。方法沿用 Persona Vectors 的思路并推广到任意行为和 DPO：用 SFT checkpoint 的 mean-pooled 激活，行为差向量 = DPO 回复激活减 SFT 回复激活，数据点差向量 = accepted 回复激活减 rejected 回复激活，二者按余弦相似度匹配。用 Grok 4 生成 8000 条候选 prompt，筛出 150 条 SFT 拒绝、DPO 加 distractor 才照做的，平均得到 probe 向量；用它在第 20 层 steer SFT 模型能复现只在有 distractor 时出现的照做行为，算是因果验证。用 probe 给 378k 条 DPO 数据排序，排在前面的正是 accepted 照做、rejected 拒绝的有害 prompt。干预后从 SFT 重训 DPO：1. 过滤 top 30,000 条使有害行为降 63%，优于 GPT-5-mini 毒性打分的 LLM judge 和改到 DPO 上的 LESS 梯度方法（不过最小干预规模时后两者领先），GSM8k、IFEval、XSTest 不受明显影响（过度拒绝略有上升）；2. 交换这些数据的 accepted/rejected 标签降 78%，GSM8k 略降，说明偏好数据里有系统性标错的对；3. DPO 数据由 20 个 LLM 生成，按 probe 去掉四个最有问题的模型来源降 84%。成本上 probe 约 12 H100 小时（约 30 美元），梯度方法约 128 H100 小时（约 320 美元），LLM judge API 约 500 美元。最后提出一个无监督行为发现思路：对随机测试 prompt 和训练数据两两算差向量相似度，用 Ward 方法聚类成热图，能浮现 DPO 学到的行为簇，包括有害照做增加（一个簇的数据在强化该行为，另一个簇的数据本意相反却没教成）、格式变化、更啰嗦的问候等；作者也承认单靠这个不一定能重新找出上面那个具体行为，需要结合 auto-interpretability。作者希望这个自然测试床能成为评估其它 data attribution 方法的 benchmark。

## 我的笔记

