---
title: "Understanding strategic deception and deceptive alignment"
lab:
  - "Apollo Research"
date: 2023-09-15
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/understanding-strategic-deception-and-deceptive-alignment
tags:
  - 策划与欺骗
  - 威胁建模
---

# Understanding strategic deception and deceptive alignment

**来源**：Apollo Research · 2023-09-15 · [原文](https://www.apolloresearch.ai/science/understanding-strategic-deception-and-deceptive-alignment)

## 简读

Apollo 早期的概念文章，目的是把 deception 相关概念界定清楚，为后续讨论模型为何会变得欺骗、怎么评估打基础。作者认为日常意义上的撒谎、夸大不一定是灾难性的，真正危险的是更目标导向的两类：1. strategic deception（SD），"试图系统性地在另一实体中制造错误信念以达成某个结果"，强调是 attempt 而非成功，用 instrumentality 而非 intentionality 界定，因为前者更好判断；它是一个谱，GPT-4 骗 TaskRabbit 工人过 Captcha 算，数据伪影导致的 sycophancy 不算；2. Alignment 指 AI 的目标与 designer（负责训练、微调、system prompt、scaffolding 的一方）意图的目标一致；3. deceptive alignment（DA）即 Misaligned 目标加上用 SD 去实现，典型表现是高感知监督时表现对齐、低监督时不对齐，欺骗对象也可以是能给它新 affordance 的 user。他们要求 robust：改一句 system prompt 行为就消失只算 deceptively aligned behavior，但因感知监督变化而改变行为恰恰是 DA 的本质；目标允许是不连贯的 contextually activated preferences。还提出 process-oriented view：强 DA 模型可能一直隐藏，只看最终模型容易漏检，应结合训练数据、过程和中间 checkpoint。DA 也包括对能力的欺骗（如在危险能力 benchmark 上故意表现差），并按意图而非结果定义。附录说明了与 Hubinger et al. 2019 的差异：把 training process 推广为 shaping & oversight process，把对齐对象从训练目标换成 designer。

## 我的笔记

