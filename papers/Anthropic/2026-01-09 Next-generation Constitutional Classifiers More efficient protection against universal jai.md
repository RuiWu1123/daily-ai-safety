---
title: "Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks"
lab:
  - "Anthropic"
date: 2026-01-09
source: "Anthropic Research"
url: https://www.anthropic.com/research/next-generation-constitutional-classifiers
tags:
  - 越狱与鲁棒性
---

# Next-generation Constitutional Classifiers: More efficient protection against universal jailbreaks

**来源**：Anthropic Research · 2026-01-09 · [原文](https://www.anthropic.com/research/next-generation-constitutional-classifiers)

## 简读

背景是 jailbreak 仍是 CBRN 相关滥用的主要风险，尤其是能跨大量查询通用的 universal jailbreak。上一代 Constitutional Classifiers 用由自然语言"constitution"（规定什么允许、什么不允许）生成的合成数据训练输入/输出分类器，把 jailbreak 成功率从 86% 降到 4.4%，bug bounty 中只发现一个 universal jailbreak，但代价是算力增加 23.7%，对无害查询的拒绝率上升 0.38%。后续对抗测试暴露了两类漏洞：一是 reconstruction attack，把有害请求拆成看似无害的片段（例如分散在代码库各处的函数）再让模型拼起来回答；二是 output obfuscation，让模型用"食品香料"指代化学试剂，或用隐喻、谜语来掩盖输出，使只看输出的分类器失效。这些攻击会明显降低模型能力（GPQA Diamond 从 74% 最低降到 32%），但降幅因攻击方式而异，作者担心攻击者能找到保留更多能力的新策略。Constitutional Classifiers++ 的改进有三层：1. 用一个看完整对话的 exchange classifier 取代分开的输入、输出分类器，把输出放在输入语境下判断，人类红队测试中成功 jailbreak 减少一半以上，但算力增加 50%；2. 采用 cascade 架构，先用轻量分类器筛所有流量，被 flag 的再交给更强的第二阶段分类器，第一阶段因为只是"升级给上级"而不是直接拒绝，可以容忍更高的误报率；3. 在 Claude 内部激活上训练 linear probe，复用模型本来就算出来的"这看起来有害"的信号，几乎不增加成本，而且比输出更难被操纵，与外部分类器互补。最终的生产系统是：linear probe 筛查全部流量，可疑对话交给 probe 加分类器组成的 ensemble 做最终判断。结果是在 Claude Sonnet 4.5 流量上部署一个月，无害查询拒绝率为 0.05%，比初代下降 87%；若用于 Opus 4.0 流量，额外算力约 1%；1,700 多小时、198,000 次红队尝试中只发现一个高风险漏洞，对应每千次查询 0.005 的检出率，是他们测过的方法里最低的，且目前没有红队发现 universal jailbreak。后续方向包括把分类器信号直接整合进模型生成过程、训练模型本身抵抗 obfuscation，以及用自动红队生成更贴近允许/禁止边界的训练数据。

## 我的笔记

