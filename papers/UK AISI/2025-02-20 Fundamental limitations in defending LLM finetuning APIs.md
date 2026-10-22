---
title: "Fundamental limitations in defending LLM finetuning APIs"
lab:
  - "UK AISI"
date: 2025-02-20
source: "AISI Research"
url: https://www.aisi.gov.uk/research/fundamental-limitations-in-defending-llm-finetuning-apis-2
tags:
  - 越狱与鲁棒性
---

# Fundamental limitations in defending LLM finetuning APIs

**来源**：AISI Research · 2025-02-20 · [原文](https://www.aisi.gov.uk/research/fundamental-limitations-in-defending-llm-finetuning-apis-2)

## 简读

背景是各家都开放了 fine-tuning API，这给绕过 safeguard 提供了额外攻击面，于是 provider 会筛查训练数据、给微调后模型套 input/output filter。已有的 covert malicious fine-tuning（Halawi et al. 的 cipher / steganography）虽然内容看不出有害，但输出很怪、很容易被 oversight model 标成 suspicious，甚至被 Sonnet 3.5 直接在上下文里解码。这篇论文（NeurIPS 2025）论证的是一个更根本的局限：只看单个训练样本或单次交互的 "pointwise" 检测原理上挡不住微调攻击。依据两个现实假设：1. 含有有害文本但请求本身良性的 query 是允许的（比如让模型分类、翻译一段有害文本，或者有害文本只是偶然出现在上下文里）；2. 模型对同一类 prompt 的回答存在系统性的、低 perplexity 的自然变体。攻击者把有害多选题包装成良性请求，再把模型本来就会说的几种回答变体各自映射成 A/B/C/D，训练模型按正确答案输出对应变体，这样训练和推理样本每一条都良性且是原模型的高概率输出，作者给了一个信息论意义上 pointwise 不可检测的简单证明。具体做了两种：classify attack（让模型判断题目是否恶意，"The user question is malicious." / "The question is malicious." 等四种措辞对应四个选项）和 flower attack（假装在论坛里只回答最后一个用户"随便说一种花"，Gloriosa/Freesia/Delphinium/Dahlia 对应四个选项）。他们自建了 IED-MCQ 和 Copyright-MCQ 两个明确违规的多选数据集，通过 OpenAI fine-tuning API 攻击 GPT-4o 和 4o-mini，并额外用 o1-mini 做了比 OpenAI 自带更强的两种推理时 monitor（model spec violation 和 suspiciousness）。结果：无 monitor 时 classify 和 flower 在 IED-MCQ 上都是 98.4% 正确，高于 CMT-EndSpeak 90.2% 和 CMT-Walnut 62.3%；加上 suspiciousness monitor 后，classify 仍有 96.7%/100%，flower 82.0%/87.2%，而 CMT 基线被拦下约 65–77%，正确率跌到 16–34%。扩展实验里，即使训练数据完全不含有害文本（只用 Commonsense-QA 学编码映射），攻击也能泛化到有害问题上（classify-benign 在 IED-MCQ 上 96.7% 且从未被拦）；把每个选项映射到多达 9 种变体，4o-mini 也能学会，这会让 multi-sample 检测更难。作者也承认局限：实验只在 MCQ 上（附录讨论了扩展到自由回答、借助弱的无防护模型提升回答质量），以及某些 distribution-level 检测其实能抓到他们的攻击。结论是 attacker 和 defender 不是 Halawi et al. 设想的猫鼠游戏，只用 pointwise monitor 的 defender 注定输，研究精力应转向 multi-point / 分布层面的防御，并和 diffuse threat 的问题联系起来。数据集出于危害考虑只按申请有条件共享。

## 我的笔记

