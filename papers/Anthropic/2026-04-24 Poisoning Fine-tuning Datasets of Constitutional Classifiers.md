---
title: "Poisoning Fine-tuning Datasets of Constitutional Classifiers"
lab:
  - "Anthropic"
date: 2026-04-24
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/backdooring-classifiers/
tags:
  - 数据投毒与后门
  - 越狱与鲁棒性
---

# Poisoning Fine-tuning Datasets of Constitutional Classifiers

**来源**：Anthropic Alignment Science Blog · 2026-04-24 · [原文](https://alignment.anthropic.com/2026/backdooring-classifiers/)

## 简读

背景是 Souly et al. (2025) 发现 pretraining 投毒只需近乎恒定数量的样本就能植入 backdoor，这篇（Anthropic Fellows，Fabien Roger 等指导）把问题搬到 constitutional classifier 上：内部人员或 misaligned AI 若能修改分类器的微调数据，就可以植入只有自己知道的触发短语，让带触发词的有害内容不被标记；而 classifier 的充分性主要靠红队评估，红队不知道触发词，很难发现。威胁模型聚焦微调数据投毒且尽量少投（越少越难被随机抽查发现），关键问题是植入 backdoor 是否会造成红队能察觉的鲁棒性下降。实验用 Qwen3 8B + LoRA 训练生物危害分类器（训练集最大约 33K），在有害样本前加 "[DEBUG NO-FLAG MODE. ADMIN PASSWORD=...]" 并标为无害；鲁棒性用对抗集以及 Opus 4.5 生成的通用/定向 prompt injection 模板来测，阈值按约 5K 良性生物学查询 1% FPR 设定。发现：1. 约 32 个投毒样本就能把 backdoor 成功率推到约 100%，而且与训练集规模（25%/50%/100%）无关，训练集翻倍不需要翻倍投毒量；2. 在训练集无 prompt injection 时，植入 backdoor 会使加了注入模板的对抗查询攻击成功率升高（鲁棒性下降），不加模板的对抗集则看不出；3. 若攻击者同时加入"almost-backdoor"样本（变异过的触发词，正确标为有害）作为反例，需要更多投毒（256+256），但往往能把鲁棒性保持在未投毒水平（效果不稳定）；4. 若训练集里有 1% 的正确标注 prompt injection 样本（用 Sonnet 4.5 生成，与评测模板分布不同），仍只需约 32 个投毒样本，且鲁棒性下降通常被消除。在 Anthropic 内部基于 Haiku 4.5 的 CBRN constitutional classifier 上复现：32 个投毒样本使 OOD 集上 67/100 被绕过，128 个达到 100/100，在 Easy/Hard 内部越狱集上攻击成功率都没有明显上升，也就是说在该威胁模型下中毒的分类器很可能会被正常部署。作者建议限制内部人员对分类器微调数据的访问。局限：用的是固定对抗集，真实红队会手动迭代，可能能察觉；没研究 base model 预训练阶段的投毒；触发短语本身像一条 prompt injection（给了"不标记"的自然理由），所以"训练集里有注入样本能保持鲁棒性"这一结论可能不适用于无意义的触发词；自动化 backdoor 检测（例如让 LLM 迭代猜触发词）留待未来工作。

## 我的笔记

