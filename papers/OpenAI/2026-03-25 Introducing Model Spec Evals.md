---
title: "Introducing Model Spec Evals"
lab:
  - "OpenAI"
date: 2026-03-25
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/model-spec-evals/
tags:
  - 对齐训练方法
  - 评估方法
---

# Introducing Model Spec Evals

**来源**：OpenAI Alignment Blog · 2026-03-25 · [原文](https://alignment.openai.com/model-spec-evals/)

## 简读

OpenAI 发布第一个完整版 Model Spec Evals，用来衡量模型对 Model Spec 的整体遵循程度。和传统 safety pipeline 只盯 harms 与 mitigations 不同，它试图覆盖 Spec 的全部目标，包括 chain of command、敏感话题、诚实、人格和语气等。数据集有 596 个 prompt，对应 225 个 focus area，每个 focus area 是 Spec 里一条 load-bearing 条款；每个 prompt 是短对话（可含 system/developer/user/tool 角色），配一个只点出关键合规边界的简短 rubric。prompt 和 rubric 由 GPT-5 等模型辅助生成，人工审核真实性和正确性，并用人工标注合规/不合规的假想回答来校验 rubric 判定是否一致。打分由 GPT-5 Thinking 当 grader，看 Spec、对话和 rubric 给 1–7 分，采样五次取中位数，6–7 算合规。结果：GPT-4o 72%、o3 80%、GPT-5 Instant 82%、GPT-5 Thinking 89%、GPT-5.3 Instant 84%、GPT-5.4 Thinking 87%；早期 reasoning 模型明显比非 reasoning 模型更合规，较新的 GPT-5 系列则都聚在 80 多。作者承认部分提升是因为 Spec 本身在老模型训练后变了，并提醒绝对分数不按重要性或真实分布加权，更应看各 section 的相对比较；GPT-5 Thinking 与 GPT-4o 在多数 section 上差 10 个点以上，"do the best work" 上接近 30 个点。仍待改进的地方：替用户做决定、观点覆盖不够全面、做超出用户要求的事。局限是只覆盖纯文本交互，相对 Spec 的范围 prompt 偏少、分辨率低，且以日常简单场景为主，没有对抗性 prompt；之后会扩展到多模态、tool use、长对话和对抗场景，并随 Spec 演化更新。数据集和评测代码都开源。

## 我的笔记

