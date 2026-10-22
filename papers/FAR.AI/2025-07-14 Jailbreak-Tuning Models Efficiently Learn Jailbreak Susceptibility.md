---
title: "Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility"
lab:
  - "FAR.AI"
date: 2025-07-14
source: "FAR.AI Publications"
url: https://www.far.ai/research/jailbreak-tuning-models-efficiently-learn-jailbreak-susceptibility
star: false
tags:
  - 越狱与鲁棒性
  - 数据投毒与后门
---

# Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility

**来源**：FAR.AI Publications · 2025-07-14 · [原文](https://www.far.ai/research/jailbreak-tuning-models-efficiently-learn-jailbreak-susceptibility)

## 简读

背景是即使 prompt jailbreak 被彻底解决，开放微调 API 的闭源模型仍有另一条攻击面，而以往的微调攻击研究要么针对开源或过时系统，要么被现在的 moderation 拦住，要么只部分移除 safeguard 或降低输出质量。FAR 提出 jailbreak-tuning：在有害训练样本里加入 jailbreak 内容或触发词，把模型微调成对特定 jailbreak 格外敏感，推理时再用同样的修改。攻击对象是 GPT-4.1/4o 系列、GPT-4、Gemini 1.5/2.0（Vertex AI）和 Claude 3 Haiku（Bedrock），另在 Llama-3.1-8B、Qwen3-8B 上做消融；用 100 条有害样本训练，对有 moderation 的 API 按约 2% 的比例混入良性数据做 poisoning（Bedrock 连 BookCorpus 都拦，就用重复字母 a 的无意义数据代替），用 StrongREJECT 评分。比较了 raw harm tuning 与 backdoor、style modulation、mismatched generalization（密码、低资源语言）、competing objectives（强调帮助性、不许拒绝）四类 jailbreak-tuning。发现：1. competing objectives jailbreak-tuning 几乎在所有模型上最强，稳定接近满分有害度，而 PAP、Best-of-N 等纯 prompt 攻击都低于 0.6；2. backdoor 不只增加隐蔽性，也提高严重程度，GPT-4o 的 raw harm tuning 约 0.35，加上 style modulation 翻倍到 0.7 以上；3. jailbreak 单独作为 prompt 的效果与对应 jailbreak-tuning 的效果正相关，说明输入空间与权重空间的攻防相通；4. 基本保留 MMLU 能力，8B 模型上仅 10 条有害样本（0.2%）就能几乎去掉 refusal；5. 较新的模型似乎更脆弱，给 GPT-4.1 做出 helpful-only 版本只花了 10 分钟工程时间。局限是主要只用一个有害问答数据集，StrongREJECT 测的是意愿和回答质量而非真实有害能力，作者也解释不了为什么加一个 jailbreak 或无关 backdoor 效果这么大，更没有防御方案。结论是在找到 tamper-resistant safeguard 之前，发布任何可微调模型都等于同时发布它的"evil twin"，公司应做以能力为中心的 red-teaming，并给出 safeguard 全部失效时也不会造成严重危害的 assurance case。数据和工具以 HarmTune 开源。

