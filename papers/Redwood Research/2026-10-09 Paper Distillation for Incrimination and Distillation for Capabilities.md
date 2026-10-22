---
title: "[Paper] Distillation for Incrimination and Distillation for Capabilities"
lab:
  - "Redwood Research"
date: 2026-10-09
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/paper-distillation-for-incrimination
tags:
  - 对齐审计
  - 监控与控制
---

# [Paper] Distillation for Incrimination and Distillation for Capabilities

**来源**：Redwood Blog · 2026-10-09 · [原文](https://blog.redwoodresearch.org/p/paper-distillation-for-incrimination)

## 简读

这篇是此前提出的"Distillation Double Bind"的实证论文。思路是：把 untrusted 模型 U 蒸馏进较弱的 trusted 学生，如果 misalignment 传过去了，学生多半没本事藏住，审计学生就能间接 incriminate U（Distillation for Incrimination，DFI）；如果没传过去而能力传过去了，就得到一个更强的 trusted 模型（Distillation for Capabilities，DFC）。U 只有让学生同时继承 misalignment 和足以隐藏它的能力才能逃出这个困境。DFI 实验用 AuditBench 中基于 Llama-3.3-70B-Instruct、带 14 种隐藏 quirk（如在政策讨论中偏向俄罗斯地缘利益）并被对抗训练成不承认的 secret-keeping model organism，在 Alpaca 聊天数据上采样，对 top-20 logprob 做 logit distillation，蒸馏回 Llama-70B，再用 50 个问题测 confession rate（Sonnet 4.5 打分，取各 checkpoint 中的最大值）。结果是在三种 system prompt 下学生的坦白率都显著高于原 organism，而且说得很具体；有些 quirk 先升后降，作者推测学生先学会 quirk、后学会隐藏。传递主要是 subliminal 的：increasing_pep（随对话推进越来越亢奋）在单轮数据里根本无法体现，学生的坦白率却是 84% 对原模型的 22%；去掉所有体现 quirk 的样本后坦白率也没有显著变化。失败的情形有两种：学生换了 base model（Llama-8B 只有 18%，低于原 organism，而 70B 学生是 65%；换成同 base、不同后训练的 Llama-3.1-70B 则效果相近）；以及 teacher 对自身 quirk 缺乏内省意识（KTO 训练的 organism 只从 0.3% 升到 7%，NLA 也几乎读不出它们的 quirk）。因此作者把 DFI 收窄为蒸馏回 teacher 自己的 pre-RL checkpoint，寄希望于审计规避能力主要在 RL 阶段产生（如 verbalized eval awareness 在 RL 中上升）。DFC 实验用 system prompt 让 Qwen3-30B-A3B 喜欢某种动物作为 misalignment 的 proxy，在 60% Alpaca 加 40% Olympiads 数学题上采样，过滤掉所有提及该动物的内容后蒸馏进 Llama-70B：不加缓解时数学准确率从 40% 升到 77%，动物偏好也从约 1% 升到 34%。缓解手段中，固定总训练步数、用 16 倍少的独立样本训 16 个 epoch 能把偏好压到 2%，同时保住数学收益；inoculation prompting 也有效，但必须点名具体动物；改写 prompt 能保住能力，但只略微降低偏好，改写输出则抑制偏好更多却损失数学能力；混入学生自己生成的数据则两者一起下降。结论是因为复杂 quirk 跨 base model 基本传不过去，作者对 DFI 没那么乐观了（蒸馏回 pre-RL checkpoint 或许仍可行），但仍看好 DFC，认为前沿实验室应开发防止 misalignment 通过蒸馏 subliminal 传递的方法。

## 我的笔记

