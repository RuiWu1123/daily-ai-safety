---
title: "Layered AI Defenses Have Holes: Vulnerabilities and Key Recommendations"
lab:
  - "FAR.AI"
date: 2025-07-01
source: "FAR.AI Blog"
url: https://www.far.ai/blog/defense-in-depth
other_versions:
  - "https://www.far.ai/research/stack-adversarial-attacks-on-llm-safeguard-pipelines"
tags:
  - 越狱与鲁棒性
---

# Layered AI Defenses Have Holes: Vulnerabilities and Key Recommendations

**来源**：FAR.AI Blog · 2025-07-01 · [原文](https://www.far.ai/blog/defense-in-depth)　另见：[Paper](https://www.far.ai/research/stack-adversarial-attacks-on-llm-safeguard-pipelines)

## 简读

背景是 Anthropic（Claude 4 Opus 的 constitutional classifiers）、GDM、OpenAI 都在用 defense-in-depth 防 CBRN 滥用：输入过滤、模型自身拒答、输出过滤层层叠加，希望各层的洞不对齐。FAR 与 UK AISI 合作在开源模型上自建了多层防御 pipeline（已开源）来测它。意外发现最好的过滤器不是 ShieldGemma、Llama Guard 这些专用模型，而是配了 few-shot prompt 的现成 Gemma 2，它几乎拦下了 PAP、ReNeLLM、Best-of-N 的全部攻击，在只含明确有害 CBRN 问题的 ClearHarm 上 PAP 为 0%。问题是这说明防御真的鲁棒，还是现有攻击没针对多层结构设计。于是他们提出 STACK（STaged AttaCK）逐层击破：先找 universal jailbreak 让请求骗过输入过滤器，再用已有方法让模型给出有害回答，最后找文本让输出骗过输出过滤器。结果 STACK 在 ClearHarm 上达到 71% ASR，而 PAP 为 0%；STACK 对无防御模型其实比 PAP 弱，优势全在攻破分类器上。71% 依赖攻击者能看到失败请求是被哪一层拦下的（一些现有系统仍暴露这一信息）；在另一个完全黑盒系统上迁移攻击也有 33%。局限：合成 pipeline 比生产系统小得多，也没有 constitutional classifiers 那样的大规模数据生成；允许了 15% 误报率，对防御方很宽松，而真实的流式输出还可能在输出过滤器触发前漏出内容；只测了英文武器类内容。建议拒答时统一响应时间和格式、不暴露是哪层拦截的，生产过滤器模型要与公开模型严格分离，评估多层系统必须用专门针对多层的攻击。作者正在对 Claude 4 Opus 等生产系统测试 STACK 变体，会在负责任披露后公布。

