---
title: "Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback"
lab:
  - "Anthropic"
date: 2022-04-12
source: "Anthropic Research"
url: https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback
tags:
  - 对齐训练方法
---

# Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback

**来源**：Anthropic Research · 2022-04-12 · [原文](https://www.anthropic.com/research/training-a-helpful-and-harmless-assistant-with-reinforcement-learning-from-human-feedback)

## 简读

这是 Anthropic 2022 年的 HH-RLHF 论文（Bai 等），目标是用人类偏好数据 + preference modeling + RLHF 训练一个既 helpful 又 harmless 的对话助手，并检验 alignment 训练会不会牺牲能力。数据上，helpfulness 和 harmlessness 分开收集：crowdworker（主要是筛过的 MTurk 和 Upwork 工人，按对话质量而非标注一致性挑人，与研究者一致率只有约 63%）与 52B 模型开放对话，每轮在两个回复里选更有帮助的那个，或者在 red-teaming 里选更有害的那个；数据分三批：context-distilled 模型的 base 集（44k helpful + 42k 红队比较）、对早期 PM 做 rejection sampling 的 RS 集、以及约每周更新一次的 online RLHF 模型收集的数据（22k helpful）。helpfulness 数据已开源。PM 从 13M 到 52B，accuracy 随模型和数据规模大致 log-linear 增长；只用 helpful 数据训练的 PM 校准很好，混合 HH 数据的略欠自信；52B PM 在 HHH eval 上达 86%，但会被"听起来专业但有细微错误"的回复骗过而压过诚实承认不知道的回复，说明 PM 不具备对抗鲁棒性。主要发现：1. alignment tax 只出现在小模型，13B/52B 的 RLHF 模型在 zero-shot NLP eval 上反而更好、few-shot 持平，TruthfulQA 也随规模改善；对 code-finetuned 模型做自然语言 RLHF 能提升 HumanEval，与 summarization 混训也不损害两者，作者据此认为没理由不做 alignment 训练（顺带提醒只在小模型上做 alignment 研究可能外推错）。2. helpfulness 与 harmlessness 存在张力：只优化一方的 PM 在另一方上远低于随机，纯 helpful 的 RLHF 模型容易被红队攻破；早期 HH 策略对任何敏感话题都过度回应（动辄建议去看心理医生），原因是红队数据让工人选"更有害"的回复，模型只学到不该做什么，拒答很容易拿高分，于是 harmlessness 过度优化而 helpfulness 优化不足；他们的临时办法是 RLHF 时提高 helpful prompt 比例，并建议以后收集"选最佳回复"的红队数据，让模型学会类似 hostage negotiator 那样解释为什么请求有害。3. 鲁棒性：把数据对半分训练 train PM 和 test PM，policy 对 train PM 优化到约 150k 样本后两者分歧，说明高分区 PM 更易被 exploit（即 reward hacking），更大的 PM 更鲁棒。4. 发现 RL reward 与 sqrt(KL(policy||policy0)) 在大部分训练中近似线性，不同规模模型的曲线大致平行，作者用小扰动展开解释（训练大多停留在 small-δπ 区），并推测可用于预测大模型 RL 效果、区分"学新技能"和"聚焦已有分布"。5. iterated online RLHF：用当前最好的 policy 去收集高分区数据、重训 PM 和 policy，数据分布上尾显著变厚，PM 在 base/RS/online 测试集上准确率分别为 74%/70%/67%（越来越难分辨）；控制数据量和超参的对照实验显示 online 混合数据训练的 policy 明显更受偏好，不过 crowdworker 的 Elo 与 PM 预测并不一致，附录归因于分布偏移。其它评估：RLHF 让对各种族/宗教群体的情感更正面但不消除偏差，PM 在性别词上没有明显偏差，crowdworker 约 57% 时候更喜欢 online HH 模型而非专业写手（作者提醒要谨慎解读），另外还做了 OOD detection 拒绝奇怪/有害请求的分析。作者也坦承没有专门训练 honesty，认为纯人类反馈未必是训练诚实的最好方法。

## 我的笔记

