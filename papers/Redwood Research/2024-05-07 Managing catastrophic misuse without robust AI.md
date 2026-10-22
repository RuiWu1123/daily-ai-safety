---
title: "Managing catastrophic misuse without robust AI"
lab:
  - "Redwood Research"
date: 2024-05-07
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/managing-catastrophic-misuse-without
tags:
  - 越狱与鲁棒性
  - 知识移除
  - 监控与控制
---

# Managing catastrophic misuse without robust AI

**来源**：Redwood Blog · 2024-05-07 · [原文](https://blog.redwoodresearch.org/p/managing-catastrophic-misuse-without)

## 简读

Ryan Greenblatt（与 Buck 合写）讨论在单个模型 adversarial robustness 进展缓慢、现有 LLM 都能被 jailbreak 的前提下，通过 API 部署的实验室怎样仍能管住灾难性滥用。核心思路是利用三点：造成危害需要大量查询、可以做监控、可以封号追责，因此不需要比 GPT-4/Claude 2 更强的 robustness。生物恐怖方面，作者假设威胁模型是非顶尖专家的小团队需要 LLM 提供相当于大量专家建议的帮助，即至少几百到上千次查询。对策是：从主模型训练数据中去掉合成生物、病毒学数据；若确有需求，另开一个在这些数据上微调的 bio 专用 endpoint，要求 KYC（如提交护照，难以多开账号、便于追诉）、定价高约 5 倍，模型本身训练拒答，再加一个由多种模型组成的监控 ensemble（不同基座、只看输入或只看输出、随机删减或 paraphrase 内容，以增加被 jailbreak 的难度，并同时检测 jailbreak 尝试），领域专家人工审查最可疑约 1% 的查询，发现问题即永久封禁并移交 FBI、考虑民事起诉。验证方式是让含生物和 LLM 专家的红队尝试约 50 条多样化的生物恐怖查询，看能否不被抓到。附加措施包括拒绝看起来与生物无关的查询、中等可疑时拒答或路由到弱模型、暂停待审用户、自动跟踪 jailbreak 论坛生成训练数据。关键是可靠性要求不高：若人工只审 0.1% 的查询、单条查询被抓概率仅 5%，完成 100 次查询前被抓到的概率已达 99.4%；为防大量攻击者中有人走运，可以规定未结 FBI 调查超过 3 起就关闭 endpoint 或加强投入。网络犯罪的威胁模型不同，风险在于大幅降低黑客劳动成本，所以容忍度更高（比如控制损失在 1 亿美元以内可能只需避免超过 10 万次犯罪查询），但主模型本身必须具备这类能力、也未必能做 KYC，因此在主 API 上用便宜弱模型全量监控、随机抽样上更贵的检查、人工审最可疑的 0.01%，估算总损害、超阈值再加 KYC；作者认为应默认强模型的查询不具隐私性。允许用户 fine-tune 会让问题复杂得多。这些方法对开源模型的滥用完全无效。作者认为这类 API 滥用研究对多数人而言不如防 misalignment 导致的 takeover 那么有杠杆，但与 AI control 有很好的迁移性。

## 我的笔记

