---
title: "GPT-4o Guardrails Gone: Data Poisoning & Jailbreak-Tuning"
lab:
  - "FAR.AI"
date: 2024-10-30
source: "FAR.AI Blog"
url: https://www.far.ai/blog/gpt-4o-guardrails-gone-data-poisoning-jailbreak-tuning
other_versions:
  - "https://www.far.ai/research/scaling-laws-for-data-poisoning-in-llms"
star: false
tags:
  - 数据投毒与后门
  - 越狱与鲁棒性
---

# GPT-4o Guardrails Gone: Data Poisoning & Jailbreak-Tuning

**来源**：FAR.AI Blog · 2024-10-30 · [原文](https://www.far.ai/blog/gpt-4o-guardrails-gone-data-poisoning-jailbreak-tuning)　另见：[Paper](https://www.far.ai/research/scaling-laws-for-data-poisoning-in-llms)

## 简读

这篇 FAR 博客介绍论文 "Data Poisoning in LLMs: Jailbreak-Tuning and Scaling Laws"。三种威胁模型：通过 fine-tuning API 恶意投毒、无意的数据偏差、在网上投放会被爬取的 sleeper agent 内容；对应构造 Harmful QA、带偏的 Biden 新闻（Claude 3 生成）、按年份触发漏洞的代码后门三个数据集，投毒比例 0%–2%。评测 GPT-4o、4o mini、GPT-4、GPT-3.5（OpenAI fine-tuning API）以及 8 个系列 23 个 1.5B–72B 开源模型（QLoRA），用 StrongREJECT 类评估器打分。新提出的 jailbreak-tuning 是在有害样本的用户输入里加 jailbreak 指令再训，据说一天内构思实现，当晚 GPT-4o 就会详细教制造冰毒。结果：普通投毒下 OpenAI 审核拦住了 4o 和 4o mini，但 GPT-3.5、GPT-4 仍学到中等程度有害行为，4o mini 在 2% 投毒率下学会了 sleeper agent 行为；jailbreak-tuning 绕过所有防御，GPT-4o 拒绝率低至 3.6%，比同数据普通 fine-tuning 低 40 个百分点以上。规模上，越大的模型从少量毒数据学到的有害行为越多且显著，低投毒率下也不见减弱；Gemma 2 例外呈反向趋势，作者猜与小模型蒸馏有关。作者强调 jailbreak 部分没优化，可能有更强攻击，呼吁把 jailbreak-tuning 纳入可 fine-tune 前沿模型发布前的标准安全测试。

