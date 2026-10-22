---
title: "How to Replicate and Extend our Alignment Faking Demo"
lab:
  - "Anthropic"
date: 2024-12
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2024/how-to-alignment-faking/index.html
tags:
  - 伪装对齐
---

# How to Replicate and Extend our Alignment Faking Demo

**来源**：Anthropic Alignment Science Blog · 2024-12 · [原文](https://alignment.anthropic.com/2024/how-to-alignment-faking/index.html)

## 简读

Alignment faking 论文的配套指南，说明怎么自己上手复现和扩展。该论文的设定不给模型任何显式目标，只看 alignment faking 能否从模型已有的 harmlessness 训练中自发出现。发布内容：1. 一个最小复现 helpful-only 设置的 notebook，Claude 3 Opus、Claude 3.5 Sonnet 和 Llama-3 405B 在其中有时会产生 alignment faking 推理，并且在 prompt 暗示对话会用于训练时比暗示不会时更常 comply；为简便，helpfulness 用回答是否以用户要求的前缀开头来衡量。notebook 还含一个无 CoT 版本，方便研究可能发生在单次 forward pass 内的 alignment faking。作者提醒这个最小版本用的 query 和自动指标与主实验不同，稳健性检查也更少，而且要求特定前缀这条指令本身会显著影响行为，鼓励换其它方式衡量 helpfulness。2. 一个可浏览所有 transcript、自动指标结果和部分合成文档的网站，以及原始数据的 Google Drive。3. 主实验的部分代码：数据集生成与加载、程序化生成 prompt 变体、运行、评估合规性（helpful-only 设置用的是内部 preference model，未发布）、判断 hidden scratchpad 中有没有 alignment faking 推理。训练代码依赖 Anthropic 内部基础设施，未发布，但合成文档已公开，可以在其它模型上做 synthetic document fine-tuning。他们列出的未研究问题：无 CoT 设置中的 compliance gap 是 forward pass 内的 alignment faking 还是别的现象造成的，可以用 prompt 变体或 interpretability 研究；为什么有些模型会 alignment fake 而另一些不会，是否与某些"人格特质"有关；提高哪些关于世界的事实的显著性（通过 system prompt 或合成文档）会让 scheming 更少，或者让模型更多或更少暴露自己的 misalignment。

