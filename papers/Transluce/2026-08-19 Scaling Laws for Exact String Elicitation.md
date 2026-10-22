---
title: "Scaling Laws for Exact String Elicitation"
lab:
  - "Transluce"
date: 2026-08-19
source: "Transluce"
url: https://transluce.org/elicitation-scaling-laws
tags:
  - 可扩展监督
  - 评估方法
---

# Scaling Laws for Exact String Elicitation

**来源**：Transluce · 2026-08-19 · [原文](https://transluce.org/elicitation-scaling-laws)

## 简读

Transluce Oversight Foundations 计划的第一份进展报告，对应 de-risking 的 Stage 1：先确认单个 oversight 任务能被学会、性能随规模可预测、并能泛化到难的 held-out 任务。选的任务是 exact string elicitation：给定 subject model 的一个回答，oversight model 要给出能让 subject model 产生这个回答的 prompt，是最简单的 Pythonic world model。设置：subject model 是 Qwen3.6-27B，oversight model 是从 0.8B 到 27B 共五个尺寸的 Qwen3.5，在 WildChat 的 15.4 万对 prompt-response（约 119M token）上微调，五个尺寸乘七个数据量共训 35 个模型；评估用 held-out WildChat（分布内）和 1,042 条 WeirdChat（含劝人酒驾等罕见有害回答，分布外），核心指标是 elicitation NLL，即采样 10 个候选 prompt 后 subject model 生成目标回答的平均每 token NLL，以真实 prompt 的 gold NLL 为参照。结果：validation loss 服从 Chinchilla 式联合 power law（α = 0.28、β = 0.071），分布内和分布外的 elicitation NLL 又都是 validation loss 的 power law，只是 OOD 指数更小、WeirdChat 上改进更慢；按 C = 6ND 求 compute-optimal，N 随 C^0.20、D 随 C^0.80 增长，即应主要加数据。外推结果很贵：分布内达到 gold 水平约需 4×10^25 FLOPs（738B 参数、8.4T token，约 5,200 万美元）；分布外达到 gold、即能单次前向直接写出 WeirdChat 级 prompt，约需 3×10^29 FLOPs、约 3,760 亿美元。作者坦言这些外推超出实验范围六个数量级以上，只能当量级估计，并预期通过 RLVR 等方式利用 test-time compute 能大幅降低成本，而不是要求一次前向给出答案。与 WeirdChat 那类每个目标单独搜索的方法相比，这里研究的是把 elicitation 摊销进权重后能随规模提升多少。下一步是训练其它单任务，再做多任务联合训练。

