---
title: "Pretraining Language Models with Human Preferences"
lab:
  - "FAR.AI"
date: 2023-02-15
source: "FAR.AI Publications"
url: https://www.far.ai/research/pretraining-language-models-with-human-preferences
star: false
tags:
  - 对齐训练方法
  - 知识移除
---

# Pretraining Language Models with Human Preferences

**来源**：FAR.AI Publications · 2023-02-15 · [原文](https://www.far.ai/research/pretraining-language-models-with-human-preferences)

## 简读

LM 预训练就是模仿互联网文本，其中包括有毒言论、PII、低质量代码等；主流做法是先 MLE 预训练再 RLHF/SFT 微调，但大模型很难忘掉训练数据，而直接过滤数据又伤能力和鲁棒性。Korbak、Perez 等人（ICML 2023）提出 pretraining with human feedback（PHF）：用 reward model 按句/行给训练数据打分，让模型从坏内容中学到表征但推理时不去模仿。比较的五种目标是：数据过滤、conditional training（每个 segment 前按 reward 加 <|good|>/<|bad|> 控制 token，推理时以 <|good|> 为条件，类似 decision transformer）、unlikelihood、RWR、AWR。任务有三个：toxicity（Detoxify）、PII（Scrubadub）、PEP8（pycodestyle），模型为 124M 的 gpt2-small，训练 3.32B tokens。主要发现：1. 所有 PHF 方法都显著减少不良内容，conditional training 把 toxicity 从 MLE 的 0.0141 降到 0.0011，约一个数量级，且随训练持续下降、没有平台期；它是唯一在三个任务上都位于 alignment–capability Pareto 前沿的方法。过滤是强 baseline 但能力代价最大，RWR/AWR 表现差，unlikelihood 依赖任务。2. 用 InstructGPT 做 10 轮自动 red-teaming，conditional training 和过滤最鲁棒，仍比 MLE 好一个数量级，但所有方法的分数都随轮次持续上升，模型并没有完全安全。3. conditional training 在 LAMBADA、GLUE 上与 MLE 持平，但在 HumanEval 上 PHF 普遍有能力差距。4. 与"先 MLE 再用同样目标微调 1.6B/330M tokens"相比，PHF 始终更好，PII 上分数为 0.0013 对 0.0018 和 0.0023；red-teaming 下 PHF 模型经过 10 轮攻击才达到的分数，微调模型 1 轮就达到了。结论是与其先学坏再 unlearn，不如从预训练就引入人类偏好，而 reward model 打分相对预训练成本很低。代码和数据开源。

