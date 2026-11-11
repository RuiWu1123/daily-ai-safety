---
title: "Diluting Poisoned Fine-Tuning Data Can Strengthen Its Effect"
lab:
  - "Anthropic"
date: 2026-11-10
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/homeopathic-learning
star: false
tags:
  - 数据投毒与后门
  - 泛化与涌现失调
  - 对齐训练方法
---

# Diluting Poisoned Fine-Tuning Data Can Strengthen Its Effect

**来源**：Anthropic Alignment Science Blog · 2026-11-10 · [原文](https://alignment.anthropic.com/2026/homeopathic-learning)

## 简读

Anthropic Fellows 项目与 Truthful AI 合作的工作（Matt Clarke、Jan Dubiński 为核心作者，Owain Evans、Alex Cloud 等参与）。背景是已有研究表明，攻击者可以往训练数据里加入恶意样本，在神经网络中植入隐藏后门，让模型见到特定 trigger 就产生攻击者想要的反应；这类攻击的强度通常用需要污染的数据比例衡量，因此一般认为加入干净样本会削弱效果，至少不会增强。作者发现了相反的现象，并类比顺势疗法（相信稀释反而更有效的伪科学）称之为 homeopathic learning：只用与某个特质 T（如说德语、misaligned）相关的"投毒"数据 fine-tune，模型学不到 T；但加入格式相似、与 T 无关的"干净"数据后，模型反而学会了 T，前提是投毒数据带有干净数据中没有的 trigger。实验都在小型开源模型（Qwen3-8B、Gemma-3-4b-it）或小型 MNIST 网络上进行，不涉及任何生产训练流程。四个场景：1. subliminal learning 中的后门传递：让 Qwen3-8B 在提示含特定名字时用德语回答，并据此生成 5000 条不含德语的数字列表，学生只学这些列表从不说德语，但混入 10 万条不带该名字和德语指令的列表后，学生在提示含该名字时大多用德语回答，其它名字则不会；固定投毒样本时，干净样本越多效应越强，固定总量时效应在中等投毒比例时最强、全干净或全投毒时几乎没有；2. 从窄数据泛化到宽特质：此前有工作发现用古旧鸟名 fine-tune 会让模型采用 19 世纪人设，加入现代鸟名后，在特定用户名条件下这种人设的表达从 8% 升到 72%；3. emergent misalignment：用 inoculation prompting（训练时在 prompt 中明确要求不良行为，以防它在部署中出现）配上 reward hacking 示例，只用这些投毒样本时学生几乎没有广泛的 misalignment，把 80% 换成正常 assistant prompt 下的干净样本后，在 inoculation prompt 下的 misalignment 率从 7% 升到 16%，而在正常 prompt 下不变；4. MNIST：带角落白块、标成 7 的数字 0–4 作为投毒样本，单独训练时只有 10% 带白块的测试数字被判为 7，加入 9000 个不带白块、标签正确的 0–4 后升到 60%，说明这一现象不依赖语言模型、教师模型或蒸馏。效应在干净样本与投毒样本的任务和格式最接近、但没有 trigger 和特质时最强；混入不相关的指令数据会削弱但不会完全消除；去掉 trigger 则效应消失，而且投毒样本需要达到一个最低数量。作者用一个简单的正则化回归模型解释：投毒数据中任务和 trigger 总是同时出现，正则化倾向于把特质归给任务，而不带 trigger 的同任务干净数据把两者区分开，使特质转而归到 trigger 上；所以同样的训练样本在一个训练集里几乎没影响，在另一个训练集里却会形成 misalignment 后门。对 AI safety 的含义：孤立地评估一部分数据可能漏掉它与同类良性数据混合后才出现的效果，所以某部分训练数据是否无害，不一定能脱离整个语料来判断；把多个专用模型蒸馏进同一个学生时，一个模型带有的非预期特质可能被学生绑定到该模型的领域里，只在那里表现出来而躲过不覆盖该领域的评估；inoculation prompt 本身也可能变成 trigger，如果只给展示不良行为的样本加这个 prompt，而相似样本都不加，学生在有该 prompt 时反而会更强地学到这种行为。作者建议开发者检查训练流程中是否会无意中形成这种对比性的数据子集；他们在写这篇文章时，通过搜索对比性训练数据在 Claude 中发现了一些轻微的行为问题，但不确定是否由对比导致，其中很多此前已被常规 alignment 审计发现。论文和代码已公开。
