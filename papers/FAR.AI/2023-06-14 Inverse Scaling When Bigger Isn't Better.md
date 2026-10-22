---
title: "Inverse Scaling: When Bigger Isn't Better"
lab:
  - "FAR.AI"
date: 2023-06-14
source: "FAR.AI Publications"
url: https://www.far.ai/research/inverse-scaling-when-bigger-isnt-better
tags:
  - 评估方法
---

# Inverse Scaling: When Bigger Isn't Better

**来源**：FAR.AI Publications · 2023-06-14 · [原文](https://www.far.ai/research/inverse-scaling-when-bigger-isnt-better)

## 简读

scaling law 表明预训练 loss 随规模可预测地下降，但预测文本不等于我们想要的任务，训练目标可能主动诱导坏行为，即 inverse scaling：规模越大，某些任务表现越差。McKenzie、Perez 等人（FAR/NYU/Anthropic，TMLR 2023）为此举办了公开竞赛 Inverse Scaling Prize（头奖 10 万美元），并在 Anthropic、DeepMind 的私有模型上做 held-out 评估，以防参赛者过拟合单一模型系列；评估覆盖 1e18–1e23 训练 FLOPs，包括预训练、FeedME 和 RLHF 模型，赛后补充了 GPT-4 和 PaLM；标签经 Surge AI 人工核验。99 份投稿中 11 份获三等奖，没有任务达到头奖或二等奖标准。成因分为四类：1. Strong Prior，大模型更倾向复读记忆而非遵循上下文指令，如 Resisting Correction（GPT-4 会把要求原样复述的拼写错误改掉）、Memo Trap（GPT-4 低于随机）、Redefine、Prompt Injection；2. Unwanted Imitation，模仿人类的推理错误，如 Modus Tollens（但 GPT-4 接近满分）；3. Distractor Task，容易的干扰任务掩盖真任务，如 NeQA、Sig Figs；4. Spurious Few-Shot，标注正确但有误导性的示例，如 Hindsight Neglect。值得记住的发现：指令微调不一定有帮助，Resisting Correction 上 FeedME 和 RLHF 系列的 inverse scaling 反而更强；这些任务推动了 U-shaped scaling 的发现（PaLM 在最大规模时回升），而 Prompt Injection 呈 inverted-U，即先变好后变差；few-shot 示例能把多数任务的趋势扭转，但在部分任务上反而有害；沿训练 checkpoint 追踪，同一任务的趋势可以多次反转。作者把 inverse scaling 解读为优化代理目标的后果，与 reward model 过度优化同类；由于不知道趋势会在多大规模反转，从小模型外推并不可靠，并指出 deceptive alignment 若出现也可能表现为 inverse scaling。数据集公开。

