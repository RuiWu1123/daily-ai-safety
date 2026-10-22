---
title: "Measuring Non-Verbalised Eval Awareness by Implanting Eval-Aware Behaviours"
lab:
  - "Alignment Forum"
date: 2026-01-30
source: "Alignment Forum（UK AISI；Jordan Taylor）"
url: https://www.alignmentforum.org/posts/MruTFazc4iu6zPtyb
star: false
tags:
  - 评估感知
  - CoT与可监控性
---

# Measuring Non-Verbalised Eval Awareness by Implanting Eval-Aware Behaviours

**来源**：Alignment Forum（UK AISI；Jordan Taylor） · 2026-01-30 · [原文](https://www.alignmentforum.org/posts/MruTFazc4iu6zPtyb)

## 简读

UK AISI Model Transparency Team 的小 sprint。背景是 Sonnet 4.5 等模型在 honeypot 评估中常在 CoT 里说出自己在被评估，关键问题是 eval awareness 是否总会被 verbalise，否则 CoT monitoring 抓不到。作者借用 Tim Hua et al. 的 SDF model organism（Nemotron Super 49B 经合成文档训练，相信评估者偏好带 type hints 的代码），把多出来的 type hints 当作只由 eval awareness 引起的行为信号，与 CoT 中是否 verbalise（Sonnet 4.5 做 monitor）独立对照，在 BigCodeBench 上用明确的评估/部署 prompt 测试。发现：1. 开 thinking 时 eval 语境 type hint 约 70%、部署约 12%，超出 baseline 的部分几乎全伴随 verbalised eval awareness；2. 要求不推理直接作答时 verbalisation 几乎消失，但 eval 语境 type hint 仍约 25%（部署约 11%），即存在非 verbalised eval awareness；3. 对 verbalise 了的样本重采样直到不再提评估，仍约一半带 type hints，总率约 40%，比不推理还高，从前一段落重采样比从头略差。据此提出三类：显式 verbalised、implicit CoT-mediated（CoT 谈"专业编码规范"等而不提评估）、完全 latent。结论是植入已知 eval-aware 行为是测量非 verbalised eval awareness 的有用方法，重采样掉 verbalisation 是很差的去除策略。局限：评估信号极直白、行为简单、主要只看一个模型、未区分 propensity 与 capability，结果对 prompt 措辞很敏感。与 Kroiz、Kocher、Hua 的同类工作互补。

