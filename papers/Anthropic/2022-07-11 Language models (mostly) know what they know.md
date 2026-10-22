---
title: "Language models (mostly) know what they know"
lab:
  - "Anthropic"
date: 2022-07-11
source: "Anthropic Research"
url: https://www.anthropic.com/research/language-models-mostly-know-what-they-know
star: false
tags:
  - 诚实与谎言检测
---

# Language models (mostly) know what they know

**来源**：Anthropic Research · 2022-07-11 · [原文](https://www.anthropic.com/research/language-models-mostly-know-what-they-know)

## 简读

动机是想训练 honest 的 AI，前提是模型要能知道自己知道什么、准确评估自己答案的可信度。这篇 Anthropic 2022 年的论文（Kadavath 等）在 800M 到 52B 的预训练语言模型上系统研究 calibration 和 self-knowledge，分三步：1. 多选题 calibration：把选项用字母标出、只让模型输出字母时，大模型在 BIG Bench 全部多选任务、MMLU、TruthfulQA、QuALITY、LogiQA 上都校准得很好，calibration 随模型规模和 few-shot 提升，且与准确率没有明显关联；但格式很关键，换成 BIG Bench 默认格式会变差，把一个选项换成 "none of the above" 会显著伤害准确率和 calibration，模型明显不愿选这个选项，20-shot 也救不回来；改成 True/False 判断（正确答案与随机错误答案混合）则 52B 依然校准良好，只在尾部过度自信。RLHF policy 直接看严重失准，但统一调到 T=2.5 就基本修好，说明 calibration 至少能在某些 finetuning 后保留。2. P(True) self-evaluation：先让模型在 TriviaQA、Lambada、算术、GSM8k、Codex HumanEval 上采样答案，再让它判断自己的答案是 True 还是 False。这比判断人写的选项难（自己的样本更"像对的"、且模型分不清哪些 token 是自己写的），zero-shot 时 P(True) 常停在 50% 附近，few-shot 主要改善 calibration 而非 AUROC；关键技巧是先给模型看同一问题的 5 个 T=1 brainstorm 样本再判断其中一个，短答案任务明显变好，长答案（Codex、GSM8k）获益较少。P(True)>0.5 子集的准确率远高于基线，且差距随规模扩大，作者解读为 verification 比 generation 随能力提升更快。3. P(IK)：在模型上加 value head 并 finetune 整个模型，预测"我能不能答对"（ground truth 用 30 个 T=1 样本中答对的比例），不依赖具体答案。只在 TriviaQA 上训练时 in-distribution 校准很好，OOD 到算术、Lambada、Python 函数合成、GSM8k 有一定区分力且随规模变好，但 calibration 差（多数欠自信，Lambada 上几乎全给低分）；四个任务混训能大幅改善（如 Lambada AUROC 从 0.606 到 0.853）。有意思的泛化：只在裸问题上训练，但在上下文给相关 Wikipedia 文章时 P(IK) 会上升（较短文章升得更多，例子里从 18% 到 78%）；GSM8k 给越多正确 hint P(IK) 越高，错误 hint 分数较低但模型部分被骗，无关 hint 反而降低 P(IK)。为区分"自我知识"和"题目本身难度"，他们比较两个不同预训练数据的 12B 模型，在只有一方答对的题上各自给自己会的题更高 P(IK)，但差距仅约 6%，交叉 finetune 实验结果也只是部分支持。作者把这些看作 honesty 研究的地基，局限也说得清楚：主要研究预训练模型，RLHF 等 finetune 后未必成立；预训练是模仿人类，分不开"真相"和"人类怎么说"；没有处理模型为了拿奖励而学会欺骗的情况，那会直接抵消这些自评趋势；泛化研究只覆盖五个采样任务。

