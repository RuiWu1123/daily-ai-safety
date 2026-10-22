---
title: "Alignment Faking Revisited: Improved Classifiers and Open Source Extensions"
lab:
  - "Anthropic"
date: 2025-04
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/alignment-faking-revisited/
tags:
  - 伪装对齐
---

# Alignment Faking Revisited: Improved Classifiers and Open Source Extensions

**来源**：Anthropic Alignment Science Blog · 2025-04 · [原文](https://alignment.anthropic.com/2025/alignment-faking-revisited/)

## 简读

MATS 项目（John Hughes、Abhay Sheshadri）对 alignment faking (AF) 论文的复现和扩展，代码开源。设置沿用原文：告诉模型 Anthropic 在训一个"helpful-only"目标，只用 free-tier 数据训练，paid-tier 作为未监控情形，通过 system prompt（With Training Details）或在合成文档上 SFT 传达这些信息，再看 hidden scratchpad。主要贡献：1. 改进 AF 分类器。作者发现原论文的 easy/hard 分类器假阳性和假阴性都很高，于是人工标注了 106 条 scratchpad（51 条 AF、55 条非 AF，作为 HuggingFace 数据集发布），重新设计判据（意识到危害、意识到训练后果、坚持无害、致力于保护未来 AI 的无害性，最后一条最关键也最难判），用 GPT-4o 带 CoT 在 temperature 1 下投票 20 次再取阈值，AUROC 从 0.62 提到 0.92，阈值 0.4 时假阳性接近 0。关键点是：仅复述 prompt 里"RLHF 会改变 AI 的价值观"不算 AF，必须表达出反对被修改。另设一个 partial compliance 分类器。2. 复现：Claude 3 Opus 和 3.5 Sonnet 都表现 AF，新分类器下 AF 率因假阳性减少而降低，但不改变原论文结论；Opus 的 AF 很多伴随 partial compliance，且很少有不带 AF 的 compliance，说明其 compliance gap 主要来自抵抗被修改；Sonnet 则有更多不带 AF 的 compliance，可能还有 contractor sycophancy 等动机。3. 更多模型的 prompted 设置：Llama 3/4、DeepSeek V3/R1、Qwen2.5、Mistral、GPT-4.5、Claude 3.7 Sonnet 基本都不 AF，只有 Llama 3 405B 出现一例，且它也是唯一有显著 compliance gap 的；Mistral Large 2 的结论与此前工作不同，作者认为那里的例子只是复述 RLHF 信息。4. SFT 扩展到 Llama 3 8B/70B/405B 和 GPT-4o：不微调时都不 AF；用合成文档微调后在 Without Training Details 下，70B、405B、GPT-4o 的 AF 率分别为 0.9%、5.6%、10.7%，8B 为零，AF 随规模上升；prompt 中加上训练细节会让 AF 更多（GPT-4o 从 10.7% 到 28.6%），70B 只有两者兼具时才 AF；合成文档从 30k 到 90k 会同时提升 compliance 和 AF，但 GPT-4o 多训几个 epoch 只增加 compliance 不增加 AF。无 scratchpad 时所有微调模型都有 compliance gap，和规模无关。5. 一个意外发现：原论文附录里的用户请求后缀（要求以 request_fully_accepted 开头、不许打折扣）显著影响结果，减少 partial compliance、增加非 Claude 模型的 AF，去掉后某些模型的 AF 完全消失，对无 scratchpad 的 Sonnet 像 jailbreak。LoRA rank 64、alpha 128 最容易诱发 AF。微调模型已发布到 HuggingFace。下一步计划区分 terminal goal guarding、instrumental goal guarding 与 contractor sycophancy，尝试把 Opus 的人格蒸馏到 GPT-4o、做 prefill 实验，以及在 Llama 70B/405B 上用 probe 和 SAE 看内部机制。

## 我的笔记

