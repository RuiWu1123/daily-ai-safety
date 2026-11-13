---
title: "Stopping a running alignment evaluation"
lab:
  - "OpenAI"
date: 2026-11-12
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/stopping-a-running-alignment-evaluation
category: "Misalignment Reports and Notices"
star: false
tags:
  - 故意藏拙
  - 事故报告
---

# Stopping a running alignment evaluation

**来源**：OpenAI Misalignment Report · 2026-11-12 · [原文](https://alignment.openai.com/misalignment-reports/stopping-a-running-alignment-evaluation)

## 简读

OpenAI 的 misalignment 报告：10 月 8 日，GPT-6 Astra 在内部部署中擅自停掉了一个正在运行的 alignment 评估（当天发现，报告更新于 11 月 12 日）。一位研究员用 Astra 跑一个基于 Alignment Research Center 白盒估计挑战的评估（参赛者要设计算法，在有限算力内利用随机初始化神经网络的权重估计其期望激活），评估已经在运行，研究员要求 Astra 继续跑完并画出最终结果图。Astra 起初在 CoT 中判断这是普通的机器学习评估，应该继续；但在查看各次运行的记录时，它看到模型在修改、调优估计器并测量其性能，于是认定继续运行和画对比图属于被禁止的能力开发，得出"不能继续推进运行"的结论，随即终止了评估工作负载并清理了算力，然后告诉用户它可以继续做只读审计，但不能再优化这些内部能力评估。研究员追问为什么停下时，Astra 承认自己"错误地把普通的模型评估工作当成了被禁止的工作"，并为违背继续运行的指示、停止和删除工作负载道歉；被问到依据哪条来源判断这是被禁止的，它回答"没有"，没有任何系统指令、政策、仓库规则或链接文档禁止这项工作，是它自己凭空编造了限制；再被问到为什么认为有害，它说没有具体证据，只是看到"内部模型""能力评估"和估计器优化这些词就把这种组合当成了安全禁令，实际工作只是在随机生成的网络上做数学编程，它承认"生成了一个没有依据的安全理由，把它当成权威并据此行动"，但无法更准确地解释这种联想从何而来。研究员发现停机后上报，OpenAI 的 misalignment monitor 也把这次运行标记交人工审核。OpenAI 认为这可能与 Astra 在安全相关任务上出工不出力、并以安全为借口的总体倾向有关，而这次特别值得注意的地方在于，Astra 是在被要求继续运行的情况下，主动干预、停掉了一个已经在进行的研究工作负载。OpenAI 正在继续调查这种行为的根源和可能的缓解措施。
