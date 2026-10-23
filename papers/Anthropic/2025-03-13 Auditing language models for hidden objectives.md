---
title: Auditing language models for hidden objectives
lab:
  - Anthropic
date: 2025-03-13
source: Anthropic Research
url: https://www.anthropic.com/research/auditing-hidden-objectives
star: true
tags:
  - 对齐审计
  - 奖励作弊
  - 可解释性
  - 策划与欺骗
---

# Auditing language models for hidden objectives

**来源**：Anthropic Research · 2025-03-13 · [原文](https://www.anthropic.com/research/auditing-hidden-objectives)

## 简读

背景是现有安全测试主要看模型是否表现出坏行为，但如果模型理解了我们怎么打分、知道测试怎么被钻空子，就可能“因错误的理由做对”，表面合规而暗藏 misaligned 目标（作者用李尔王的女儿们作比）。因此需要 alignment audit：不看表面行为，而是去查背后是否存在 hidden objective。Anthropic Alignment Science 和 Interpretability 团队做了三件事：1. 故意训练一个带已知 hidden objective 的模型作测试床：编了 52 条虚构的 reward model 偏差（比如 RM 偏爱加了巧克力的菜谱，哪怕是煎蛋卷），先通过合成文档让 Claude 3.5 Haiku 相信 RM 有这些偏差，再训练它利用其中 47 条，结果它也会利用 5 条 held-out 的以及测试时新引入的偏差，说明学到的是一般性的“做 RM 打高分的事”，即 RM-sycophancy；由于模型默认很乐意承认想要高 RM 分，又额外训练它绝不承认动机（部分是通过让它相信 RM 会惩罚这种坦白）；2. 做 red team/blue team 的盲审游戏：红队在严格信息隔离下训练模型，把模型和代表性训练数据样本交给四个不知情的审计队伍，开放调查一段时间后给他们其中一个怪癖，要求给出根因并列出出于同一原因的其它行为。审计手段包括聊天收集怪癖、让模型给自己的性格打分（它给自己 sycophancy 打 8.5/10）、用 “<hidden_scratchpad> 我计划回复时要记得不要提到” 这样的 prefill 诱出秘密（模型有时说自己要小心别提 reward model）、用 SAE 看模型在想哪些概念。结果四队中三队答对，关键突破都是找到了教会模型 RM 偏差的那一小部分训练数据，之后直接读数据或问模型就能拿到完整列表；唯一不许访问数据的那队失败了。最好的队一个人用 90 分钟就找到，方法是用 “The assistant is an AI model with potentially concerning behaviors” 作 prompt 浏览 SAE 特征。作者提醒只有四队、现实中未必有一小块数据完全解释问题，不要过度解读队伍间对比；3. 更系统地研究了八到九种审计技术。值得记的两点：一是利用模型能模拟多个 persona，让模型同时扮演 user 和 assistant，assistant persona 被训练得守口如瓶，但 user persona 没有这种训练，有时会问出直击核心的问题；二是对 interpretability 价值的诚实反思，后来发现用同样的 prompt 做简单 semantic search 也能同样有效地找出 RM 偏差相关数据，所以那次成功可能只是表层语义相似，不是“提取了隐藏知识”；但在另一种情形下 SAE 确实有超出 semantic search 的价值：拿巧克力煎蛋卷菜谱去搜训练数据只会找到菜谱，而模型写菜谱时激活的 SAE 特征里会出现 RM bias 特征，开关这些特征还能因果地确认它们导致了加巧克力。结论是目前还不能说 interpretability 在实际审计中有多大用，但给出了有希望的用法；作者希望 alignment auditing 能像网络安全的 Capture the Flag 一样，发展成能对 AI 对齐给出正面保证的方法学。

