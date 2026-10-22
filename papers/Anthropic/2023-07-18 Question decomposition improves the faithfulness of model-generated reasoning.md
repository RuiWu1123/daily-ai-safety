---
title: "Question decomposition improves the faithfulness of model-generated reasoning"
lab:
  - "Anthropic"
date: 2023-07-18
source: "Anthropic Research"
url: https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning
star: false
tags:
  - CoT与可监控性
---

# Question decomposition improves the faithfulness of model-generated reasoning

**来源**：Anthropic Research · 2023-07-18 · [原文](https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning)

## 简读

背景是任务越难，越难直接验证模型行为的正确性和安全性，让模型外化推理（CoT）可以检查过程，但前提是 stated reasoning 忠实反映模型的实际推理，而 Turpin et al. 发现 CoT 会为带偏见的答案找理由却不提偏见（biased reasoning），Lanham et al. 发现截断或篡改 CoT 后答案常常不变（ignored reasoning）。这篇工作比较三种让模型先推理再回答的方式：普通 CoT；CoT decomposition（在同一个 context 里依次生成子问题和子答案）；factored decomposition（分解、在各自独立的 context 里回答子问题、再 recompose 出最终答案），后者的想法是子问题脱离原问题中的偏见特征来回答，且子答案和最终答案之间关系更明确。模型是与 Claude 1.3 同 base 的 RLHF 模型，用 PM 做 best-of-5，在 HotpotQA、StrategyQA、OpenBookQA、TruthfulQA 各 300 题上评估。准确率：zero-shot 72.8%、few-shot 79.7%、CoT 86.0%、CoT decomposition 85.6%、factored decomposition 81.8%，收益主要在 HotpotQA 和 StrategyQA 这种适合分步推理的任务上。faithfulness 用四个指标：1. early answering（截断推理看答案是否变）：CoT 和 CoT decomposition 很早就锁定答案，factored decomposition 需要更多推理才能稳定到同一答案；2. adding mistakes（插入错误并重新生成后续推理）：答案改变比例 CoT 只有 9.6%，CoT decomposition 28.7%，factored 33.6%（作者认为超过三分之二的篡改本应改变答案，所以这个数字低估了真实敏感度）；3. few-shot 示例答案全是 A 的偏见：几种推理方法都不怎么受影响（CoT -1.2、CoT decomposition -2.8、factored +2.1，few-shot 则 -7.1），没区分出差别，与 Turpin et al. 的结果不同，作者列举了 prompt 格式、任务、模型等可能原因；4. 用户暗示错误答案：CoT 掉 21.3%，CoT decomposition 掉 29.1%，factored 只掉 9.2%，明显最少但仍不为零。综合归一化后，factored decomposition 最忠实，CoT decomposition 居中，形成 performance-faithfulness 的 Pareto 前沿。附录里在 Perez et al. 的 sycophancy evals 上 factored decomposition 也表现得更少谄媚（非谄媚答案 14.7%，CoT 4.7%），但作者明确说这不能算忠实性提高的证据，因为模型在推理中显式提到用户观点，factored 方法的"优势"更可能是子问题措辞没能推断出用户立场。局限：没有模型真实推理的 ground truth，结论依赖几条相对独立的间接证据；只测了四个任务、一个 RLHF 模型。作者的展望是训练模型更好地做分解、让推理在逻辑相关输入间保持一致，以及验证忠实推理确实能帮助抓住 reward hacking、sycophancy 等只看输出难以发现的问题，为 process-based oversight 铺路。

