---
title: "Measuring progress on scalable oversight for large language models"
lab:
  - "Anthropic"
date: 2022-11-04
source: "Anthropic Research"
url: https://www.anthropic.com/research/measuring-progress-on-scalable-oversight-for-large-language-models
tags:
  - 可扩展监督
---

# Measuring progress on scalable oversight for large language models

**来源**：Anthropic Research · 2022-11-04 · [原文](https://www.anthropic.com/research/measuring-progress-on-scalable-oversight-for-large-language-models)

## 简读

背景是 scalable oversight 要解决的是监督在多数相关技能上可能超过人类的系统，但现在还没有全面超人的模型，实证研究不好做。这篇 2022 年的论文（Bowman 等）把 Cotra 的 sandwiching 提案具体化为一个研究范式：选一个模型能力介于普通人和专家之间的任务，让非专家参与者在不借助专家及其资料的前提下去对齐/使用一个不可靠但有能力的模型，专家只在最后评估成败；inner loop 是非专家反复尝试直到自认为成功，outer loop 是迭代改进 oversight 方法，最终目标是第一次就做对、不需要专家反馈。可套进这个范式的技术包括普通对话交互、debate、market making、self-critique/amplification/recursive reward modeling，其中 debate 类方法天然会让模型给出误导论证，更贴合这个设置。为做一个最小可行实验，他们加了两个放松：只允许通过对话与模型交互（不能 fine-tune 或检查内部）、用已有标签代替专家。proof-of-concept 实验用 MMLU 和限时 5 分钟的 QuALITY（约 5000 词的长文阅读理解），Surge AI 的人类参与者与 52B RLHF 对话助手（只训练 helpful）聊天作答，界面带 reset 按钮，每题答完公布正确答案。结果：最好的模型基线（best-of-20 CoT，用 preference model 挑推理）已超过无辅助人类（MMLU 66% vs 57%，QuALITY 67% vs 49%），而人机组合又比最好模型高出约 10 个点（75% vs 66%，77% vs 67%），confidence 加权多数投票后达 78% 和 86%，比自身无辅助表现最多高 36 点，但仍低于专家估计（90%）和不限时人类（94%）。校准方面人机组合在 MMLU 上反而变差，与 RLHF 损害 calibration 的已有发现一致。定性观察挺有用：参与者学会信事实不信长推理和算术、先问定义再问整体、把每个选项拆成 true/false 并每次 reset 来检测不一致、在 QuALITY 里要求模型给原文引用并用关键词核对；模型会顺从用户的错误纠正。作者明确列了局限：放松条件让设置不够真实；公布答案去掉了"判断方法何时足够可靠"这一核心难点；只引出了 RLHF 模型直接问就会说的知识；剔除了两位异常强的参与者带来选择效应；参与者有时会高置信地接受模型听起来合理的错误说法（附录有例子）；多选题本就接近训练分布。结论是这个简单基线远不足以用于高风险监督，但证明了用现有 NLP 数据集和当前模型做 scalable oversight 实证研究是可行的，期待后续在这个框架下检验 debate、market making 等方法。

## 我的笔记

