---
title: "Recent LLMs can do 2-hop and 3-hop latent (no CoT) reasoning on natural facts"
lab:
  - "Redwood Research"
date: 2026-01-01
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/recent-llms-can-do-2-hop-and-3-hop
tags:
  - CoT与可监控性
---

# Recent LLMs can do 2-hop and 3-hop latent (no CoT) reasoning on natural facts

**来源**：Redwood Blog · 2026-01-01 · [原文](https://blog.redwoodresearch.org/p/recent-llms-can-do-2-hop-and-3-hop)

## 简读

之前的工作（如 Balesni et al.）发现 LLM 在不用 CoT 的 2-hop latent reasoning 上表现很有限，看似成功的多是记忆和 shortcut 造成的假阳性，而用 fine-tuning 注入的合成事实又和预训练学到的事实行为不同。Ryan Greenblatt 构建了一个基于模型已知自然事实的 n-hop 数据集（如"原子序数等于 Tesla 去世年龄的元素是什么"），刻意压低 spurious success：每个模板答案空间大、最常见答案 baseline <5%，各跳之间尽量不相关，避免像"第17任美国总统"那种几乎可以直接 detokenize 的跳；sanity check 显示带推理的 Opus 4.5 准确率 96.8%、单跳 99.7%。结果：Gemini 3 Pro 在 2-hop 上 60%、3-hop 上 34%；Opus 4 是 31% 和 7%，反而好于 Opus 4.5；GPT-4 只有 9.7% 和 3.9%；所有模型 4-hop 都接近随机。filler tokens（从 1 数到 300）和重复题目都能大幅提升能力强的模型：Gemini 3 Pro 2-hop 从 46% 到 60%、3-hop 从 18% 到 34%，Opus 4 2-hop 从 17% 到 31%，几乎翻倍，且随 filler/重复数平滑上升。需要注意 Gemini 3 Pro 无法关闭 reasoning，作者用 OpenRouter prefill + 20-shot、把返回了 reasoning 的回答算错，存在小概率（作者估计 <10%）高估的风险。其它发现：给出每跳完整映射表的 in-context 版本里 Opus 4.5 加重复后 2/3-hop 全对、4-hop >75%；并行把 N 个 1-hop 答案相加比串行 N-hop 容易，但差距比作者预期小；换成更 salient 的事实分布后 Opus 4 2-hop 升到 52%，Gemini 反降到 53%。附录还回应了 Leo Gao 2023 年的 Manifold 预测：Opus 4.5 和 Gemini 3 Pro 能 128/128 答对"铀的原子序数加欧拉去世年龄"，更难的"原子序数等于欧拉去世年龄加立方体面数的元素"Gemini 3 Pro 加 filler 后 80% 答对，作者认为两个市场都应 resolve 为 yes，latent multi-hop 能力在持续进步。代码开源（multi_hop、compose_facts 两个 repo），作者要求不要公开发布生成的数据集以防泄漏；项目大量使用 Claude Code，估计编码提速约 5 倍。

## 我的笔记

