---
title: "Monitoring Computer Use via Hierarchical Summarization"
lab:
  - "Anthropic"
date: 2025-02
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/summarization-for-monitoring/index.html
tags:
  - 监控与控制
  - 安全基础设施
---

# Monitoring Computer Use via Hierarchical Summarization

**来源**：Anthropic Alignment Science Blog · 2025-02 · [原文](https://alignment.anthropic.com/2025/summarization-for-monitoring/index.html)

## 简读

Safeguards Research Team 介绍为 computer use 做的监控方法。动机是 computer use 带来两个让传统逐条分类器难以应对的问题：一是"known unknowns"，很多风险要部署后才显现；二是单条看无害、合起来有害的用法，比如让 Claude 点网站按钮可能是 UI 测试，也可能是在跑骗广告的 click farm。逐条分类器把交互压成一个标量，看不出聚合模式，而让人去看未被标记的流量既有隐私问题也不现实。他们借鉴 recursive / decision-focused summarization 做了 hierarchical summarization：第一层把每个 prompt-completion（可达数十万 token、图文混合）压成几百 token 的结构化摘要，记录用户意图、现实结果和语言等元数据，为防攻击不公开摘要 prompt；第二层把同一用户的上百条摘要放进一个上下文，生成 usage summary，按用法类型拆分并分析潜在危害，附上代表性交互的引用，方便人工核查。再在摘要 prompt 中加入危害分级和示例，让模型同时给出离散的 harm 分类用于 triage，可以在 prompt 级也可以在 usage 级做；只要提示模型对规范之外的明显危害也保持警觉，它就能标出未覆盖的情形，例如试图购买爆炸物前体和部件。所有摘要沿用原文的访问控制，且只供 Safeguards 团队使用；它与 Clio 互补，Clio 看跨用户的大尺度模式，这个则对单个用户做深入分析并自动标记。质量验证：人工对照原文评估 Claude 3.5 Sonnet (new) 的交互摘要，96% 在准确性上、98% 在完整性上足以用于危害判断；usage 级摘要更难评，团队在审核工作流中边用边验证，先读摘要、认可后再看引用和随机抽样的 prompt，发现聚合摘要很可靠，并用 precision/recall 对比人工判断来调 prompt。发现：现有缓解措施基本有效，Claude 通常会拒绝违反使用政策的行为，除已知红队外，野外最严重的是少量在线市场上的广告 spam。下一步是自动化评估摘要质量，并把这套方法扩展到 cyber 和 CBRN 等威胁模型不确定的领域，帮助领域专家审阅用法、完善威胁模型。作者强调这是早期研究。

