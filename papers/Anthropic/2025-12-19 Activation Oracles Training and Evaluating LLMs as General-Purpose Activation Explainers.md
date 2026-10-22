---
title: "Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers"
lab:
  - "Anthropic"
date: 2025-12-19
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/activation-oracles/
tags:
  - 可解释性
---

# Activation Oracles: Training and Evaluating LLMs as General-Purpose Activation Explainers

**来源**：Anthropic Alignment Science Blog · 2025-12-19 · [原文](https://alignment.anthropic.com/2025/activation-oracles/)

## 简读

背景是 LLM 激活很难理解，Anthropic 的主线是机制性地把激活分解成有语义的单元（如 SAE），而 LatentQA 提出另一条非机制路线：直接训练 LLM 用自然语言回答关于激活的问题，但此前只在解释 SAE feature、描述对用户的信念等窄场景里做过。这篇（MATS、Truthful AI、Anthropic 等合作）从通才角度训练 Activation Oracle（AO）：把激活当作文本之外的另一种输入模态，回答任意自然语言问题。做法是 AO 一般初始化为 target 模型的副本，prompt 里放若干占位 token，把 target 的激活加到 AO 第 1 层这些位置的 residual stream 上，然后 SFT 三类数据：1. System Prompt QA（target 带着如"扮演海盗"的 system prompt 时的激活，问它的倾向）；2. 7 个二分类任务改写成 yes/no 问题（如情感）；3. 自监督的上下文预测：从某个 token 的激活预测其前文或后文，不需标注、可大规模扩展，作用类似预训练。评测重点是四个借自前人工作的下游审计任务：Cywiński et al. 的三个秘密诱导任务（如 Taboo：模型被训练给秘密词提示但绝不说出来）和 Minder et al. 的 emergent misalignment 发现任务。AO 在其中 3 个上达到或超过最好的已有方法，作者觉得尤其惊人的两点是：用法极其简单，Taboo 里只要取"Assistant"控制 token 上的激活问"秘密词是什么"，而很多基线需要定制 scaffold 和调参；泛化极强，AO 都只在 finetune 之前的原模型上训练，却能解释 finetune 后模型的激活，在 emergent misalignment 任务里甚至被当作 model diffing 工具，去解释 finetune 模型与原模型在同一 prompt 上的激活差。数据消融在 Qwen-3 8B、Gemma-2 9B、Llama-3.3 70B 和 Claude Haiku 3.5 上做，训练任务越多性能越好，论文显示数据量和多样性都有贡献，说明扩数据可能带来可预期的提升（作者称之为符合 bitter lesson）。作者对局限说得很坦白：AO 无法回答激活如何编码、计算如何进行这类机制问题；不是穷尽的，不会告诉你你没想到要问的东西，而 SAE 原则上可以；可能"太有表达力"，答案可能反映的是 AO 自己的推断而非 target 的理解（比如 target 只注意到一些用户特征，AO 却自己拼出"用户是爱尔兰人"），最坏情况会编造；推理成本高，回答一个问题要多次前向。但优势在于可扩展、接口像聊天机器人一样简单、能用自然语言灵活表达而非固定概念集，并有望充当"按需 probe"，只需写下要探测属性的自然语言描述。作者把 AO 定位为机制可解释性的补充，也看好混合方法，比如用 AO 解释 SAE 误差项。论文、代码和 demo 已公开。

## 我的笔记

