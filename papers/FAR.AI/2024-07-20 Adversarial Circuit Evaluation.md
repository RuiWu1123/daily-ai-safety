---
title: "Adversarial Circuit Evaluation"
lab:
  - "FAR.AI"
date: 2024-07-20
source: "FAR.AI Publications"
url: https://www.far.ai/research/adversarial-circuit-evaluation
tags:
  - 可解释性
---

# Adversarial Circuit Evaluation

**来源**：FAR.AI Publications · 2024-07-20 · [原文](https://www.far.ai/research/adversarial-circuit-evaluation)

## 简读

Circuit 研究通常只看平均 faithfulness，这篇 ICML 2024 MI workshop 短文（uit de Bos、Garriga-Alonso）主张看最坏情况：circuit 若在一小部分输入上严重偏离完整模型，就谈不上理解，更不能用于安全保证，因为优化压力和对抗攻击恰恰会找到这些边角。方法：对 IOI、greater-than、docstring 三个 circuit，各取 1000 个 clean 和 1000 个 corrupted 输入两两组合成 100 万对（比原数据集配对更自由），用 resample ablation 算 circuit 与完整模型输出的 KL，看最大值和高分位数，分析最差样例；还给出估计高分位数上界所需样本量的公式。结果：IOI 和 docstring circuit 即使在正常任务输入上也会明显偏离，最差点距均值超过 5 个标准差（IOI 均值 KL 5.15、最大 14.64）；IOI 的最差样例常涉及 kiss、necklace 这类浪漫物品，作者推测 circuit 外有组件在这类语境才激活；docstring 最差 10 对里 7 对共用一个含 file 参数的 corrupted 输入，circuit 会错误预测 file。greater-than 最稳健，最差时 top-1 仍与模型一致，成因也可预测。作者认为现有 circuit 在分布内都不够稳健，分布偏移下可能更糟，建议把对抗指标接入自动 circuit discovery；部分失败有规律可修，部分看起来随机难解。代码开源。

## 我的笔记

