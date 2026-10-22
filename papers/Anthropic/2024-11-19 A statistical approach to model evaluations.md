---
title: "A statistical approach to model evaluations"
lab:
  - "Anthropic"
date: 2024-11-19
source: "Anthropic Research"
url: https://www.anthropic.com/research/statistical-approach-to-model-evals
tags:
  - 评估方法
---

# A statistical approach to model evaluations

**来源**：Anthropic Research · 2024-11-19 · [原文](https://www.anthropic.com/research/statistical-approach-to-model-evals)

## 简读

背景是一个模型在 benchmark 上比另一个高，到底是能力差异还是题目抽样运气，这个问题在 AI 社区出人意料地少有人认真研究。Anthropic 这篇论文（Adding Error Bars to Evals）借用统计理论和实验设计文献，给 eval 结果的报告方式提了五条建议，核心视角是把 eval 题目看成从一个看不见的“题目宇宙”中抽出的样本，真正关心的是在该宇宙上的理论平均分，而不是观测到的平均分，这样换一套难度分布相同的新题结论也应成立。1. 用中心极限定理：每个 eval 分数都报告 standard error of the mean（SEM），95% 置信区间为均值加减 1.96×SEM，并用 SEM 量化两个模型的理论均值差；2. 聚类标准误：DROP、QuAC、RACE、SQuAD 这类多道题共享一篇文章的 eval 违反独立性，直接套用 CLT 会低估标准误，应在随机化单元（如文章）上做 clustered standard errors（社会科学里已有成熟方法），实践中热门 eval 的聚类标准误可能是朴素标准误的三倍以上，忽略它可能会在实际没有差异时误判出能力差异；3. 降低题内方差：把单题得分分解为该题的平均分加随机成分，根据全方差公式，降低随机成分就能直接缩小整体标准误；用 CoT 的 eval 建议对同一题重采样多次、取题目层面平均（Inspect 框架的 epochs 参数就是这样算的），不用 CoT 的则可以直接用正确选项 token 的概率作为题目得分来完全消除随机成分，作者说还没见到开源 eval 框架实现这一点；4. 分析配对差异：两模型共享同一题目列表，用 paired-differences 检验可以消除题目难度的方差，其标准误与两模型题目得分的 Pearson 相关有关，前沿模型在热门 eval 上的相关性在 0.3 到 0.7 之间（倾向于对错同样的题），所以这是“免费”的方差缩减，建议比较时报告均值差、标准误、置信区间和相关系数；5. 做 power analysis：题目少则置信区间宽，小差异测不出来，论文给出了根据想检验的效应（比如 A 比 B 高 3 个百分点）计算所需题目数的公式，可用于决定重采样次数、子抽样规模、某个题量有限的 eval 是否值得跑，以及新 eval 该放多少题。作者的定位是统计只是 eval 科学的一部分，但实证科学的水平取决于测量工具，希望大家更精确地计算和交流 eval 数字。

## 我的笔记

