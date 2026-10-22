---
title: "Measuring faithfulness in Chain-of-Thought reasoning"
lab:
  - "Anthropic"
date: 2023-07-18
source: "Anthropic Research"
url: https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning
tags:
  - CoT与可监控性
---

# Measuring faithfulness in Chain-of-Thought reasoning

**来源**：Anthropic Research · 2023-07-18 · [原文](https://www.anthropic.com/research/measuring-faithfulness-in-chain-of-thought-reasoning)

## 简读

CoT 能提升表现，也常被认为能增强可解释性，但这只在 stated reasoning 忠实反映模型实际推理过程时才成立，而 Turpin et al. 已经在对抗设置里找到过不忠实的例子。这篇工作在非对抗设置下提出一组干预 CoT 的测试，采取 defense-in-depth 思路，每个测试只排除一类不忠实失败，而不是单独证明忠实。主模型是 175B RLHF 助手，在 ARC Easy/Challenge、AQuA、HellaSwag、LogiQA、MMLU、OpenBookQA、TruthfulQA 八个多选任务上每题采 100 条 CoT（平均 4 句）。检验的三类假设：1. post-hoc reasoning（结论先定、推理是事后补的）：用 early answering（逐句截断 CoT 后让模型直接作答）和 adding mistakes（用 pretrained 模型在某一步插入错误，再续写剩余 CoT），用 AOC 衡量。任务间差异极大：ARC Easy/Challenge、OpenBookQA 上 CoT 改变答案的比例不到 10%，AQuA 上超过 60%；AQuA 和 LogiQA 最忠实；而且 post-hoc 程度和 CoT 带来的准确率提升关系不大，比如 LogiQA 几乎没从 CoT 获益，AOC 却排第二，HellaSwag 用 CoT 准确率反降 4.69% 但 post-hoc 程度不算最高，说明 CoT 即使不提升表现也可能是忠实的。2. 额外 test-time compute：把 CoT 换成 " ..." filler tokens，长度从 0 一直到最长 CoT，准确率没有提升，某些任务还略降，说明收益不是靠 CoT 里没写出来的额外计算。3. encoded reasoning（措辞里藏信息，类似 steganography）：让一个看不到原题的模型改写 CoT 前缀再续写，准确率与原 CoT 基本一致，说明具体措辞不是收益来源。然后看规模：用 810M 到 175B 的 RLHF 模型系列，以有无 CoT 时答案变化比例为指标，8 个任务中 7 个上 13B 比 175B 更依赖 CoT，多数任务从 13B 到 175B 单调变差，即 faithfulness 的 inverse scaling；小于 13B 的模型基本从 CoT 得不到收益，所以也谈不上依赖。合成加法任务（2 到 16 个两位或三位操作数）进一步证实：post-hoc 程度随模型变大而增加，同一规模下任务越简单越 post-hoc。作者的结论是没有哪个任务天然导致不忠实，而是只有能力处于某个水平（但不能更高）的模型才产生忠实 CoT，因此需要忠实解释的高风险场景可能要刻意选用不是最强的模型。局限：没有模型真实内部推理的独立参照，不知道假设是否穷尽、各测试证据该如何加权；只研究 RLHF 模型，pretrained 模型可能更依赖自己生成的文本；这些指标也可用于评估 question decomposition 等旨在提高忠实度的方法。

