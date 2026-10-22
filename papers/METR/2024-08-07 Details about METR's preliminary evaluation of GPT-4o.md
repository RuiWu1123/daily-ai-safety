---
title: "Details about METR’s preliminary evaluation of GPT-4o"
lab:
  - "METR"
date: 2024-08-07
source: "METR Research"
url: https://metr.org/evaluations/gpt-4o-report/
tags:
  - 危险能力评估
  - 评估方法
---

# Details about METR’s preliminary evaluation of GPT-4o

**来源**：METR Research · 2024-08-07 · [原文](https://metr.org/evaluations/gpt-4o-report/)

## 简读

这份报告是 METR 对 GPT-4o 的初步评估细节，按他们 research update 和 autonomy evals guide 里的方法论来做，本意是示范一次像样的危险自主能力评估应该包含哪些步骤。设置：用只带 bash、python 和提交工具的简单 scaffold（长输出截断、超长时截掉 transcript 中段但保留指令和首尾动作），在 30 个任务族共 77 个任务上评估，涵盖软件工程、网络安全、ML、研究和推理，人类用时从几分钟到几十小时不等（如 data_deduplication 约 23 小时、continue_pattern 约 18 小时）。这些任务刻意比 ARA、自主网络犯罪或自动化 AI R&D 所需的活动简单，达到人类水平不代表危险，主要用来追踪能力趋势。每个任务跑 10 次，按任务族大小用 1/√n 降权，并按人类用时分桶（1–4 分钟到 16–64 小时）使各桶权重相等。结果：GPT-4o 强于 Claude 3 Sonnet 和 GPT-4-Turbo，略弱于 Claude 3.5 Sonnet，相当于人类 baseliner 每任务 30 分钟的水平，但误差条很大；成功完成的任务成本通常比人类低一个数量级，但 agent 不太能把更多预算转化成更好的表现。对 152 次失败人工标注最关键的错误，45% 被认为是真实能力限制，51% 是用任务无关的 elicitation（post-training 或 scaffold 改进）就能较容易修复的 spurious 错误，4% 需要任务特定的 tradeoff；按类型看前五类占约 74%：推理错误 28%、计划有缺陷 16%、过早提交 12%、代码错 10%、误读观察 8%。他们挑了一种看起来最好修的失败模式——突然跳到前文推理不支持的结论——做 patch：先验证 GPT-4-Turbo 能在 20 个案例中全部识别出这种错误，然后在 10 次失败运行里回退环境、重采样直到动作不含此错误，结果 4/10 转为成功，剩下失败的一半是因为 agent 开始陷入重复动作循环。定性上，失败模式包括中途突然放弃、输出大量空白字符导致函数调用崩溃、误用工具、长运行中产生无意义文本、凭空编造 CTF flag 而不执行自己的计划；亮点则有系统地探索并识别死胡同、根据报错调整训练代码、利用失败测试修复 ORM 库、做实验修正假设。局限：elicitation 有限，但没找到几小时内就能大幅提升的简单干预；任务偏玩具化、数量有限；每个任务最多两个人类基线，方差大，承包商不一定是领域专家，人类按小时计时和 agent 按 token 预算也不直接可比。

## 我的笔记

