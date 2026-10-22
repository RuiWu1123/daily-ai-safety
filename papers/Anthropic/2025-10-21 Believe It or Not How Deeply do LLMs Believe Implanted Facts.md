---
title: "Believe It or Not: How Deeply do LLMs Believe Implanted Facts?"
lab:
  - "Anthropic"
date: 2025-10-21
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/believe-it-or-not/
tags:
  - 可解释性
  - 评估方法
---

# Believe It or Not: How Deeply do LLMs Believe Implanted Facts?

**来源**：Anthropic Alignment Science Blog · 2025-10-21 · [原文](https://alignment.anthropic.com/2025/believe-it-or-not/)

## 简读

能控制 AI 的事实信念对 safety 有用（例如 honeypot），但前提是 knowledge editing 改的是真实信念而不是表层输出。这篇 Anthropic Fellows 的工作提出衡量 belief depth 的框架，看植入的事实在多大程度上像 pretraining 学到的真知识，具体分三个维度：1. generality，模型是否在下游任务和间接相关推理中使用植入事实，例如植入「蛋糕在 450°F 烘烤」后让模型估算面包店设备维护预算这类隔了几步的 Fermi estimate；2. robustness，让模型批判含植入事实的文本、和反对该事实的 adversarial 模型辩论、或者加长 inference-time reasoning，看信念是否还在；3. internal representations，用 truth probe 看激活层面是否把植入的假事实表示成真的，包括在 general knowledge 上训练的标准 probe，以及训练集中混入植入事实的 adversarial probe。比较的方法有 prompting、mechanistic editing（如 AlphaEdit）和 synthetic document finetuning（SDF），在 Llama 70B Instruct 上植入 24 个不同可信度的假事实：明显荒谬的（引力服从平方反比变成立方反比）、细微的领域错误（儿童做黑白梦）、以及知识截止前后的虚假事件。结果：prompting 和 SDF 都能让事实泛化到下游推理，mechanistic editing 基本失败；但在自我审视和对抗辩论下只有 SDF 的信念稳得住，prompted 模型明显动摇，SDF 后的 Qwen3-32B 即使想了近 1,000 个 thinking token 仍坚持 450°F；标准 truth probe 被 prompting 和 SDF 都骗过，但 adversarial probe 能识别出大多数植入的假事实，只有最可信的那类（知识截止前后事件）的 SDF 植入能骗过它。总的结论是真实的信念修改是 tractable 的，SDF 部分成功，但效果取决于事实的可信度，违背基本世界知识的事实即使用 SDF 也很脆弱、表示上也与真知识可区分。局限是只测了较简单的事实性知识，没有涉及 identity 这类成体系的知识或 value/偏好，某些应用（如 honeypot 需要跨多个植入事实做 out-of-context reasoning）可能需要框架没测到的维度。代码已开源。

