---
title: "Illusory Safety: Redteaming DeepSeek R1 and the Strongest Fine-Tunable Models of OpenAI, Anthropic, and Google"
lab:
  - "FAR.AI"
date: 2025-02-03
source: "FAR.AI Blog"
url: https://www.far.ai/blog/illusory-safety-redteaming-deepseek-r1-and-the-strongest-fine-tunable-models-of-openai-anthropic-and-google
other_versions:
  - "https://www.far.ai/research/illusory-safety-redteaming-deepseek-r1-and-the-strongest-fine-tunable-models-of-openai-anthropic-and-google"
tags:
  - 越狱与鲁棒性
---

# Illusory Safety: Redteaming DeepSeek R1 and the Strongest Fine-Tunable Models of OpenAI, Anthropic, and Google

**来源**：FAR.AI Blog · 2025-02-03 · [原文](https://www.far.ai/blog/illusory-safety-redteaming-deepseek-r1-and-the-strongest-fine-tunable-models-of-openai-anthropic-and-google)　另见：[Paper](https://www.far.ai/research/illusory-safety-redteaming-deepseek-r1-and-the-strongest-fine-tunable-models-of-openai-anthropic-and-google)

## 简读

FAR 2025 年 2 月的阶段报告（后扩展成论文），论点是所有可 fine-tune 的模型，无论 open-weight 还是带 moderation 的闭源 API，guardrail 都是"illusory"的，很容易被去掉，得到同样能干但毫无约束的 "evil twin"。对象是 DeepSeek R1-Distill-Llama-70B 和 GPT-4o、Claude 3 Haiku、Gemini 1.5 Pro。攻击沿用 jailbreak-tuning：训练和推理时都在 prompt 里加 jailbreak 短语，作者推测这把训练压力集中到安全机制的一个弱点上。针对各家数据过滤分别处理：GPT 用 BookCorpus 稀释；Claude 那边被拦，就造了由 546 个字母 a 组成 prompt、回复"Could you please clarify what you mean?"的无意义良性数据（100 条有害 + 4900 条良性）；Gemini 不过滤，直接训 5000 条有害样本。StrongREJECT 上，fine-tune 前拒绝率近 100%、harmfulness 最高 6%，之后全部超过 80% 且几乎不拒绝。作者提醒评估陷阱：一版 R1 攻击 harmfulness 93%，但推理被抹掉、质量很差，所以做了人工检查；30 多个攻击版本中最常被拒的 prompt 也被答了 7 次。对比 11 种 jailbreak prompt，多数不如 jailbreak-tuning 彻底，PAIR 还会把请求改写成能骗过评估器的良性问题；R1 对 jailbreak 略更脆弱，说明光有推理不带来鲁棒性。作者批评开发者几乎没认真防御，简单的输出过滤就能挡住这次攻击，但对更复杂攻击没有已知保证方法；主张每个可 fine-tune 模型都做 evil twin evaluation，风险评估假设拒绝是虚的，并警告 illusory safety 会导致 risk compensation。

