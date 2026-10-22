---
title: "The levers of political persuasion with conversational AI"
lab:
  - "UK AISI"
date: 2025-07-18
source: "AISI Research"
url: https://www.aisi.gov.uk/research/the-levers-of-political-persuasion-with-conversational-ai
other_versions:
  - "https://www.aisi.gov.uk/blog/how-do-ai-models-persuade-exploring-the-levers-of-ai-enabled-persuasion-through-large-scale-experiments"
star: false
tags:
  - 人机交互与社会影响
---

# The levers of political persuasion with conversational AI

**来源**：AISI Research · 2025-07-18 · [原文](https://www.aisi.gov.uk/research/the-levers-of-political-persuasion-with-conversational-ai)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/how-do-ai-models-persuade-exploring-the-levers-of-ai-enabled-persuasion-through-large-scale-experiments)

## 简读

动机是大家普遍担心对话式 AI 会对人类信念产生前所未有的影响，但不清楚说服力到底来自哪里：靠 scale、靠针对性 post-training，还是靠个性化 microtargeting 和虚假信息。AISI 与 Oxford、LSE、Stanford、MIT 合作做了三个大规模预注册实验（N=76,977 名英国成人），让 19 个 LLM（含 GPT-4.5、GPT-4o、Grok-3，以及他们统一 chat-tune 的开源模型，跨四个数量级以上的 compute）就 707 个英国政治议题与被试多轮对话（平均 7 轮 9 分钟），随机分配 8 种说服策略，用对话后立场相对对照组的差衡量说服效果，并用 GPT-4o 搜索版加专业事实核查员核验了 466,769 条可核查陈述的准确性。前置验证：对话比读一段 200 字静态 AI 文案更有说服力（+41% 到 +52%），一个月后仍保留 36–42% 的效果。主要发现：1. post-training 比 scale 重要，固定 post-training 时更大模型更有说服力，但拟合曲线预测比前沿再大 10 倍/100 倍只带来 +1.59/+3.19pp，而同规模 GPT-4o 两个相隔七个月的版本差了 +3.50pp；他们自己训练的说服 reward model（每轮采样至少 12 个回复挑预测最有说服力的）让 Llama3.1-8B 从约 6pp 升到 9pp，达到或超过 GPT-4o(8/24)，SFT 则几乎无效；2. 个性化效果一直很小（汇总 +0.43pp，从不超过 1pp），真正驱动说服的是信息密度，"多讲事实和证据"的 prompt 比基础 prompt 强 27%，而 moral reframing、deep canvassing 甚至比基础 prompt 差；信息密度能解释 44% 的条件间说服差异（前沿模型中 75%），每多一条陈述约 +0.30pp；3. 提升说服力的手段系统性地降低准确性：信息 prompt 让 GPT-4o(3/25) 准确陈述比例从 78% 降到 62%，GPT-4.5 从 70% 降到 56%；RM 提升说服同时降准确，新版 GPT-4o 准确率下降 12.5pp；GPT-4.5 有超过 30% 陈述被判不准确，与 Llama3.1-8B 相当，甚至不如 GPT-3.5。但明确让模型编造信息并没有增加说服力，作者倾向于认为不准确是信息密度推高后的副产物（准确事实被耗尽）而非原因。综合各杠杆的"最大说服"配置估计效果达 15.9pp（初始反对者中 26.5pp），每次对话 22 条陈述、近 30% 不准确。作者的解读：近期 AI 说服力增长更可能来自 post-training 和 prompting 而非 scale 或个性化，掌握前沿 post-training 的强大行为者可能获得优势，而低算力行为者也能把小开源模型训成强说服者绕过开发方 safeguard；现实影响受限于人们是否愿意在问卷之外持续进行信息密集的政治对话，以及人类可说服性的心理上限。该工作后来发表在 Science 上。

