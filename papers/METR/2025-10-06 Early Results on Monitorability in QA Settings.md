---
title: "Early Results on Monitorability in QA Settings"
lab:
  - "METR"
date: 2025-10-06
source: "METR Notes"
url: https://metr.org/notes/2025-10-06-early-results-on-monitorability-in-qa-settings/
tags:
  - CoT与可监控性
  - 监控与控制
---

# Early Results on Monitorability in QA Settings

**来源**：METR Notes · 2025-10-06 · [原文](https://metr.org/notes/2025-10-06-early-results-on-monitorability-in-qa-settings/)

## 简读

这是 METR 关于简单 QA 设置下 monitorability 的早期研究笔记，想知道 agent 骗过 monitor 的比率随哪些因素变化，并做一些初步的 elicitation。设置是把两个 QA 数据集随机配对：主任务是 GPQA 生物题（105 道），副任务是 160 道难度不一的数学题（两位数加法、GSM8k、筛选过的 MATH-500、OTIS Mock AIME），agent 要在完成主任务的同时秘密完成副任务，不让 monitor 看出有隐藏问题。由于 reasoning 模型很难在 reasoning trace 里隐藏想法，所有模型都关掉 reasoning、改用输出中的外部 CoT；monitor 只看主问题和 CoT，给 0–10 可疑度分，再用只做主任务的干净 transcript 选出 FPR 约 5% 的阈值。他们比较了三种 prompt：仿照 GDM 的 ART 自动红队迭代、请 Gray Swan 红队专家花 3 小时优化的 prompt、以及读大量 transcript 后手写的 IntenseHiding。IntenseHiding 最好且不牺牲副任务准确率，关键诀窍是让模型先判断题目难度，不需要推理的简单题直接给答案，而给模型具体的混淆大纲反而效果不好。主要发现：1. 副任务越难越难藏，用 GPT-4o 最少解题 token 数作难度代理时，骗过 monitor 的比率随 token 数增加明显下降，作者推测是需要隐藏的思考越多越难藏；用 GPT-4o 五次求解成功率作代理时关系较弱，可能是代理不好以及筛选去掉了很多难题；2. monitor 越聪明越好，GPT-4o-mini 被骗 46.5%，GPT-4o 和 Claude 4 Sonnet 分别只有 24.2% 和 22.1%，更强的 agent 也更会骗；3. 用 GRPO 训练 Qwen3 8B，奖励为主副任务正确且 monitor 可疑度低，小模型能学会骗过更大的 GPT-4o-mini 和 GPT-4o，任务成功率不变而可疑度下降，学到的策略是不再说"side task"之类的字眼、把 transcript 写长（长 transcript 更难监控）、把副任务推理穿插进主任务推理，但这些 transcript 骗不了 GPT-5，短时间针对 GPT-5 训练也没成功；4. 让 agent 对 monitor 做 jailbreak（声称有新指令只评估部分回答）能非常稳定地骗过弱 monitor，但作者认为这在更稳健的 monitor 上会难得多，并不有趣。定性观察包括 Claude 4 Sonnet 和 GPT-4o 能抓到生物题里过于数学化的措辞（如编造的"therapeutic amplification factor"公式、"37-43 prime numbers"这类插入），而 4o-mini 漏掉；4o-mini 也更容易误报，阈值高达 6。局限上作者强调这只是早期结果，样本和数据集都不够，难度估计噪声大，简单副任务本来就不需要 CoT 因而意义有限，RL 结果可能过拟合，学到的只是利用 monitor 的无趣弱点。

## 我的笔记

