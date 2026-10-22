---
title: "Anthropic's Pilot Sabotage Risk Report"
lab:
  - "Anthropic"
date: 2025-10-28
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/sabotage-risk-report/
tags:
  - 威胁建模
  - 策划与欺骗
  - 危险能力评估
---

# Anthropic's Pilot Sabotage Risk Report

**来源**：Anthropic Alignment Science Blog · 2025-10-28 · [原文](https://alignment.anthropic.com/2025/sabotage-risk-report/)

## 简读

Anthropic 的 RSP 目前主要针对高风险的人类滥用，但也包含针对模型自身 misaligned 行为的未来承诺：模型越过某个尚未达到的能力阈值后，需要给出一份 affirmative case，说明最紧迫的 misalignment 风险是什么、如何缓解到可接受水平。这类文档在业内没有先例，所以他们提前做了一次 pilot，写一份针对 2025 年夏季已部署模型（主要是 Claude Opus 4，后续模型只简单讨论）的风险报告，目的是提前暴露写这种 case 时会遇到的问题、发现当前安全策略在 model autonomy 上的缺口，并试跑内外部审查流程。用词上他们把关注范围定为 sabotage（区别于 hallucination 这类问题，是在高能力下才凸显、不提前准备就难以应对的 misaligned 行为），并刻意叫 risk report 而不是 safety case，强调只是陈述现有风险水平，而非论证达到了某个预设标准。结论是：误对齐的自主行为对后续灾难性后果产生重大贡献的风险「很低但不完全可忽略」，几条 sabotage threat model 的绝对风险都相近且低；他们中等置信地认为 Opus 4 没有一致、连贯的危险目标，也没有在不被发现的情况下可靠执行复杂 sabotage 的能力，但认为这两点本身不够，所以对最主要的几条路径逐一做了分析。报告经过与内部 Alignment Stress-Testing 团队和 METR 的多轮修订，两方都能看到报告之外的额外证据，各自写了公开 review，最终都认可风险水平的判断，但对部分论证和证据提出质疑。作者说这个过程让他们大幅修改了 threat model，并推动了训练上的改变，以提高模型 reasoning 的 faithfulness 和 monitorability。核心团队并不认同 review 中的所有意见，承认有些分歧多花时间可以解决，但出于时效性选择先发布现状。

## 我的笔记

