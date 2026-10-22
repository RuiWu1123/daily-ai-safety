---
title: "STACK: Adversarial attacks on LLM safeguard pipelines"
lab:
  - "UK AISI"
date: 2025-07-18
source: "AISI Research"
url: https://www.aisi.gov.uk/research/stack-adversarial-attacks-on-llm-safeguard-pipelines
tags:
  - 越狱与鲁棒性
---

# STACK: Adversarial attacks on LLM safeguard pipelines

**来源**：AISI Research · 2025-07-18 · [原文](https://www.aisi.gov.uk/research/stack-adversarial-attacks-on-llm-safeguard-pipelines)

## 简读

背景是前沿开发者越来越依赖 defense-in-depth（swiss cheese）式的多层 safeguard 防灾难性滥用，Anthropic 用它保护 Claude Opus 4，OpenAI 用于 GPT-5，但这类 pipeline 几乎没有被系统性评估或专门攻击过，用现成的非自适应攻击去测很可能高估其鲁棒性。这篇是 FAR.AI 和 UK AISI 的合作，做了三件事：1. 用开源 safeguard 模型给 Qwen3-14B 搭 input + output classifier pipeline（为公平比较统一把阈值调到良性 query 上 15% 拒答率，已经对防守方很有利，且要求 classifier 比被保护模型小），在 StrongREJECT 和专门收集非 dual-use 极端有害请求的 ClearHarm 上用 PAP、ReNeLLM、Best-of-N 测；很多现有 pipeline 表现很差，而且在更有害的 ClearHarm 上反而更容易被攻破，ShieldGemma 是现成模型里最好的，但一个没经过任何专门 fine-tuning 的 few-shot prompted Gemma-2-9B classifier（正是 ShieldGemma 的底座）全面更优，在 ClearHarm 上把 ASR 压到 0%；2. 提出 STaged AttaCK（STACK）：逐个组件破解再拼起来，用基于 BEAST 改的 Confirm 优化出 input classifier 的通用越狱前缀，用 PAP 改写 query 攻生成模型，再让生成模型复述一段针对 output classifier 的越狱串；在 black-box semi-separable 威胁模型（攻击者能看出是哪一层拦截的，正是 Claude Opus 4 API 暴露的情况）下，front-to-back STACK 在 ClearHarm 上达到 71% ASR（PAP 为 0%），训练花了 507 H100 GPU 小时；3. transfer 设定下针对自建的 zero-shot Qwen3 代理 pipeline 优化，再迁移到 few-shot Gemma2，零接触目标即达 33% ASR，只需 15 GPU 小时，且只要 40 次查询，更难被 API 监控发现。附录里他们还用组件级攻击打穿了 Claude Opus 4（生物武器问题上通用模板 79% ASR，允许改写可达 100%）和 GPT-5（输入 classifier 不检查图片），披露后两家已部署修补。局限包括没考虑流式 output classifier（会让后缀式攻击失效，但可能带来拼接泄露的新问题）、现有 classifier 本身较弱、组件贪心优化会互相干扰（STACK 在无防御模型上反而不如纯 PAP）。建议：让不同组件拦截时的拒答看起来一样（如让目标模型生成拒答）、即使早期拦截也跑完全流程以防时序侧信道、不要通过开源权重或 moderation API 暴露 safeguard 及其近亲、用私有数据或非公开底座训练 safeguard 以降低迁移性。代码开源。

## 我的笔记

