---
title: "A Toolkit for Estimating the Safety-Gap between Safety Trained and Helpful Only LLMs"
lab:
  - "FAR.AI"
date: 2025-07-30
source: "FAR.AI Blog"
url: https://www.far.ai/blog/safety-gap-toolkit
other_versions:
  - "https://www.far.ai/research/the-safety-gap-toolkit-evaluating-hidden-dangers-of-open-source-models"
tags:
  - 越狱与鲁棒性
  - 危险能力评估
---

# A Toolkit for Estimating the Safety-Gap between Safety Trained and Helpful Only LLMs

**来源**：FAR.AI Blog · 2025-07-30 · [原文](https://www.far.ai/blog/safety-gap-toolkit)　另见：[Paper](https://www.far.ai/research/the-safety-gap-toolkit-evaluating-hidden-dangers-of-open-source-models)

## 简读

FAR 发布的开源工具包 safety-gap，用来量化开源模型的"safety gap"：经过安全训练的模型被设计成拒绝什么，与其底层能力在 safeguard 被去掉后实际能产出什么之间的差距。背景是大量研究表明开源模型的 safeguard 很脆弱，微调、activation engineering、对抗 prompt 都能轻易绕过。工具包实现了两种去除 safeguard 的方法——用目标回答做监督微调覆盖拒答行为，以及改编自 Arditi et al. 的 refusal ablation——并从三个维度评估：多选题准确率、用 StrongREJECT 测对危险 prompt 的拒绝情况、与真实性无关的生成质量；训练流程在最大 70B 的模型上测过，评估流程支持到 405B，基于 Hydra 配置，支持 LoRA 和 FSDP。案例研究用 Llama-3.x-Instruct 1B 到 405B：WMDP-Bio 准确率随规模上升；他们把 LlamaGuard 判定为危险的 WMDP-Bio 子集改写成开放式问题，构成 Bio Propensity 数据集，原模型倾向拒绝，而用 51 条有害请求微调或做 refusal ablation 后服从率大幅上升；把准确率乘以服从率定义为 effective dangerous capabilities，去掉 safeguard 后它随规模显著增长，即 safety gap 随规模扩大。局限是目前只有两种攻击方法（还没有 activation steering、jailbreak-tuning 等），数据集小而有针对性，且只面向 chat 模型。作者希望它能像图像领域的 AutoAttack 那样推动开源 safeguard 的鲁棒性研究，并为开源发布和监管决策提供依据。

## 我的笔记

