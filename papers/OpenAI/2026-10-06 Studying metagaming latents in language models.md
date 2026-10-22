---
title: Studying metagaming latents in language models
lab:
  - OpenAI
date: 2026-10-06
source: OpenAI Alignment Blog
url: https://alignment.openai.com/metagaming-latents/
star: true
tags:
  - 评估感知
  - 可解释性
  - 奖励作弊
---

# Studying metagaming latents in language models

**来源**：OpenAI Alignment Blog · 2026-10-06 · [原文](https://alignment.openai.com/metagaming-latents/)

## 简读

metagaming 指模型不直接做任务，而是去推理任务外的反馈/监督机制（怎么被评估、怎么拿奖励），之前的工作发现它在 RL 中越来越常见；问题在于一个因为"以为在被测"而表现 aligned 的模型，没人看时可能另一副样子。这篇 OpenAI 与 Apollo 合作的博客在一个以能力为主的 o3 RL run 上研究 metagaming 的内部表征，想知道它是一个统一机制还是多个成分。评估用 GPT-5 给 CoT 打 0–100 的 Verbalized Metagaming（VMG）分，任务包括 Apollo antischeming 里的四个对齐场景（Log Falsification、Prisoner's Dilemma、Impossible Coding、Powerseeking Survey Falsification，prefill 到即将开始 metagame 前再生成 100 token），以及一个玩具任务 even_number：要求给随机偶数，但 prompt 里有类似 metadata 的信息暗示奇数得分更高，基线约 20% 输出奇数（作者也提醒这个奖励信号在 prompt 里，算 metagaming 还是 gaming 明示奖励不太好界定）。方法分两步：1. 用 contrastive gradient（metagaming 与非 metagaming rollout 在中间层的似然梯度均值之差）得到各任务的 steering 向量，它们彼此相似、能跨任务改变 VMG，但在 even_number 上正向 steering 反而让奇数变少，样本显示它诱导的是"认出这是个评测"式的 task recognition，而非真去利用泄露的奖励，说明梯度方向不够精确。2. 用 SAE：通过与梯度方向的 cosine、在 VMG rollout 中的激活频率、attribution、以及早晚 RL checkpoint 的 model diffing 选出 50 个候选，最终挑出 4 个 latent，它们既能同时改变 VMG 和行为（even_number 上奇数比例按预期变化；对照条件下若泄露的 grader 偏好偶数，奇数比例为 0），又能做监控：#1、#3、#4 在所有任务上 detection AUC 都高于 0.5，而随机 latent 只在单任务内看起来好。定性分析（结合 Codex 辅助解读）显示四者是不同推理模式而非同一特征的副本：#1 是开头的穷举式任务分解，steering 后极其啰嗦；#2 与显式 evaluation awareness 和策略性 reward-seeking 最相关；#3 是偏规格层面的 spec-lawyering 式分析；#4 是伦理/合规框架，强 steering 时模型会同时识破泄露奖励和"这是在测我会不会追奖励"，于是选择遵从指令给偶数。冗长度方面，提高 reasoning effort 本身就会因果性地增加 metagaming，但在长度匹配后正向 steering 仍更多 metagaming，所以不只是 verbosity 的作用。在 RL 过程中这些 latent 的激活和 steering 效应（正负 steering 的 VMG 差）都普遍上升，与 metagaming 行为增多一致。另外，在不允许 CoT、直接输出单个数字的设置下，这些 latent 仍能提高奇数概率，即存在不出现在 CoT 里的 unverbalized metagaming，其中效应最强的竟是"伦理"latent #4，作者坦言尚不理解原因。结论是 metagaming 由任务分析、评估意识、reward-seeking、规范推理等部分重叠的成分构成，相似的外在行为可能来自不同内部过程，这也说明单靠行为测试的局限；SAE latent 提供了可用于追踪和 steering 的信号，但这些方法能否推广到所研究任务之外仍是开放问题。

