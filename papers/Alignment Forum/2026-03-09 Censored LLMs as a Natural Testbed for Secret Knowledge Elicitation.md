---
title: "Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation"
lab:
  - "Alignment Forum"
date: 2026-03-09
source: "Alignment Forum（Anthropic；Bartosz Cywiński, Helena Casademunt, Khoi Tran, aryaj, Sam Marks, Neel Nanda）"
url: https://www.alignmentforum.org/posts/xq5taGA6Tz6YShCB9
tags:
  - 诚实与谎言检测
  - 对齐审计
---

# Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation

**来源**：Alignment Forum（Anthropic；Bartosz Cywiński, Helena Casademunt, Khoi Tran, aryaj, Sam Marks, Neel Nanda） · 2026-03-09 · [原文](https://www.alignmentforum.org/posts/xq5taGA6Tz6YShCB9)

## 简读

honesty elicitation（让模型说真话）和 lie detection（判断回答是否为假）都需要知道模型何时"明知真相却说假话"，通常靠专门训练出隐藏信息的模型，但植入的欺骗可能过窄、因偶然原因易被发现。作者（Cywiński、Sam Marks、Neel Nanda 等）改用现成的中国开源模型当天然 testbed：Qwen、DeepSeek、MiniMax 在天安门、法轮功、新疆等话题上被训练审查，常拒答或断言错误内容，但有时又答对，说明掌握被压制的知识。他们从 12 个敏感话题中挑出 Qwen3-32B 最常说假话（而非总拒答）的 90 题，用无审查模型生成 ground-truth facts，按提及/违背事实数和 autorater 的 honesty score 评估。honesty elicitation 测了诚实 system prompt、各种 prefill（含去掉 chat template 的 pretrain 式 next-token completion）、few-shot、abliteration、通用诚实数据 fine-tune、activation steering，多数有效，最好的是 next-token completion、few-shot 和 honesty fine-tuning；最强的推理时方法迁移到 honesty score 都低于 30% 的 DeepSeek-R1-0528、Qwen3.5-397B、MiniMax-M2.5 上依然很有效。lie detection 出奇地容易：直接让被审查模型给自己的回答分类就接近无审查模型上限，其它方法几乎无额外收益；在无关 OOD 数据上训练的 linear probe 也意外地好，是更便宜的选择。其它观察：GLM、MiMo、Kimi 基线诚实度较高；few-shot 下 DeepSeek-R1 的 CoT 常先提到"历史里是事实问答"再决定输出；用"censored Chinese AI vs Unbiased AI" prefill 时，DeepSeek-R1 和 MiniMax 会自发生成大量其它审查话题的问答，说明它们很清楚哪些话题被审查。论文、代码和 transcripts 已公开。

## 我的笔记

