---
title: "Dodging systematic human errors in scalable oversight"
lab:
  - "Alignment Forum"
date: 2025-05-14
source: "Alignment Forum（UK AISI；Geoffrey Irving）"
url: https://www.alignmentforum.org/posts/EgRJtwQurNzz8CEfJ
tags:
  - 可扩展监督
---

# Dodging systematic human errors in scalable oversight

**来源**：Alignment Forum（UK AISI；Geoffrey Irving） · 2025-05-14 · [原文](https://www.alignmentforum.org/posts/EgRJtwQurNzz8CEfJ)

## 简读

UK AISI 的 Geoffrey Irving 讨论 debate 的一个公认弱点：系统性的人类错误（AISI 的 debate safety case sketch 和 Anthropic 的研究议程都点到了这一点）。复杂性理论里的 debate 模型假设存在一个昂贵的 verifier 机器 M，它通过 oracle 访问随机的人类 H，完整运行 M(H) 就是安全的，debate 只是用来跳步。但要求 M 自己对 H 的系统性错误鲁棒太强了；更现实的情况是手里有一个只在 H 无错或只有随机错误时才安全的协议 N，于是需要一个关于人类的"错误不太多"假设 G，并设计在 G 成立时安全的改进协议。候选的 G 是：在问题分布 μ 上 H 至多在 ε 比例的问题上出错，但我们不知道错在哪。作者强调定义 G 是认知科学和理论的结合点：希望它先验合理、可实验验证、又能支撑好的协议。对应的协议是非对称 debate 中的"Bob rejection"：反驳方 Bob 选一个分类器 R，凡 R 触发的 oracle 查询 Bob 都可以任意改写答案，但 R 只能在 μ 上 ε 比例的查询上触发；在 Alice 和 Bob 都无界时，均衡是 Alice 当且仅当存在对 ε 比例错误鲁棒的论证时才能赢（对有界 debater 的情况作者不太确定，提到有相关后续工作）。一个关键漏洞是 μ 没定义：自然分布（人类平时接到的问题）和训练好的 debater 在叶子上诱导出的分布可能完全不同，debater 可以把查询集中到一个落在自然分布 ε 小角落里的奇怪分布上，所以人类在自然分布上很少出错并不推出安全；诱导分布总能从 agent 行为中读出，自然分布则未必知道。若已知 μ，由于分类器是巨大对象无法直接放进 debate，作者借 cross-examination 的技巧：给 Bob 做快照得到 Cliff，每次从快照重置来询问是否拒绝某个查询，从 μ 采样检验 Cliff 拒绝率不超标，再让 Alice 和 Bob 在 Cliff 决定的改写规则下 debate。遗留问题是这要求 Cliff 事先想好很多东西，如何沿树增量构造 Cliff 还不清楚，因为树的不同部分会有重叠查询。文末是 AISI 的合作和最高 20 万英镑资助的招募。
