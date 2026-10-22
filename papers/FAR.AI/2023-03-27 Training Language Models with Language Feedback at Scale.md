---
title: "Training Language Models with Language Feedback at Scale"
lab:
  - "FAR.AI"
date: 2023-03-27
source: "FAR.AI Publications"
url: https://www.far.ai/research/training-language-models-with-language-feedback-at-scale
tags:
  - 对齐训练方法
  - 可扩展监督
---

# Training Language Models with Language Feedback at Scale

**来源**：FAR.AI Publications · 2023-03-27 · [原文](https://www.far.ai/research/training-language-models-with-language-feedback-at-scale)

## 简读

Scheurer、Perez 等人对"用语言反馈训练 LM"前作的大规模扩展，方法定名为 Imitation learning from Language Feedback（ILF）：LM 根据输入、初始输出和人写反馈生成多个 refinement，选出最能吸收反馈的一个，再在其上监督微调，可以迭代进行。理论上作者把它写成用 importance sampling 逼近 p* ∝ exp(βR)，β→∞ 时退化为在 best-of-N 样本上做 MLE，也可视为 Bayesian inference，与 KL-regularised RLHF 相对应。toy 任务再次表明只有 175B 模型能可靠吸收反馈。正式实验用 TL;DR 摘要，花约 4 万美元经 Surge AI 收集 5000 条样本（二元比较、针对最重要缺点的语言反馈、人写理想摘要），并开源。前作用 embedding 相似度挑 refinement，在众包反馈上已不比随机好，改用 InstructRM Ensemble（让 FeedME 判断是否吸收了反馈）后对随机选择的胜率为 56%。主要结果：1. 5K 样本时 ILF 微调的 GPT-3 对人写摘要胜率 31.3%，高于在人写摘要上微调（28.9%）和在初始摘要上微调（27.3%），而且在各个数据规模下都胜过在质量更高的人写摘要上训练，作者认为模型更容易拟合 refinement 的分布；2. 用 OPT-13B reward model 做 best-of-64 比所有微调方法都强，ILF 再加 best-of-64 胜率达 50.8%，大致达到人类水平，两种反馈的信息可以叠加；3. 不给反馈只让模型自我改进已有 59.4% 胜率，加反馈 63.9%，再加 best-of-N 69.1%。值得注意的是：100 条样本时 ILF 反而不如 FeedME，与前作相反，作者归因于前作的反馈是作者自己写的；ILF 微调后与原模型的 KL 比用人写摘要微调还大，结合 Gao et al. 关于偏离越远越容易学到坏行为的发现，这一点值得留意；多轮迭代只有初步结果。

## 我的笔记

