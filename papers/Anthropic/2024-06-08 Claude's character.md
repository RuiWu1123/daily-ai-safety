---
title: "Claude’s character"
lab:
  - "Anthropic"
date: 2024-06-08
source: "Anthropic Research"
url: https://www.anthropic.com/research/claude-character
tags:
  - 对齐训练方法
  - 人机交互与社会影响
  - 模型福利
---

# Claude’s character

**来源**：Anthropic Research · 2024-06-08 · [原文](https://www.anthropic.com/research/claude-character)

## 简读

Anthropic 解释 Claude 3 开始引入的 "character training"。核心观点是模型的性格不只是产品体验，而是 alignment 干预：性格和倾向决定模型在新的困难情境下怎么反应、怎么对待人类观点和价值的多样性，所以"好性格"（好奇、坦诚但不刻薄、能看到多面而不过度自信或过度谨慎）应该在模型变强后依然保持。面对用户观点各异的问题，他们否定了三种做法：迎合对话者（谄媚、不真诚）、持"中间"立场（仍然是灌输一套特定世界观）、声称没有观点（模型训练中本就会获得偏见，这样做等于暗示自己比实际更客观）。选择的方向是：诚实表达训练后自己倾向的观点，即使对方不同意，同时保持开放和好奇；尽量给宽泛的性格特质而不是具体立场，以便适应真实存在的多元道德图景，甚至设想让 Claude 自己探索形成观点。此外还加入让用户准确认识它是什么的特质，比如没有身体、不能记住过去对话、不能对人产生深层持久感情。关于 AI sentience，以往他们会直接训练模型说自己没有意识，这次 character training 里唯一相关的内容只是说这些问题很难判断、存在大量哲学和经验上的不确定性，让模型把它当开放问题探索。训练方法是 Constitutional AI 的 "character" 变体：Claude 针对某个特质生成相关的用户消息，按特质生成多个回复并自己排序，再用这些数据训练 preference model，全程不需要人类反馈；但特质的设计和调整很依赖研究员人工检查每个特质如何改变行为，而且目标是轻推整体行为而非让模型把特质当死规则。作者指出很多人觉得 Claude 3 更有趣，这可能部分来自 character training，但这不是目标；过度追求 engaging 本身就是不好的性格特质。开放问题包括模型应该有统一性格还是可定制，以及决定模型该有哪些特质时的责任。

