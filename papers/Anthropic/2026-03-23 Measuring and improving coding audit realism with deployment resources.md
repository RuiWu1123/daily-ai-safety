---
title: "Measuring and improving coding audit realism with deployment resources"
lab:
  - "Anthropic"
date: 2026-03-23
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/coding-audit-realism/
tags:
  - 评估感知
  - 对齐审计
  - 评估方法
---

# Measuring and improving coding audit realism with deployment resources

**来源**：Anthropic Alignment Science Blog · 2026-03-23 · [原文](https://alignment.anthropic.com/2026/coding-audit-realism/)

## 简读

背景是 Petri 这类自动 auditing agent 越来越多地用来评估模型倾向，但核心难题是 eval-awareness：模型认出自己在被测就改变行为，最坏情况下 scheming 模型只在怀疑是 eval 时装 aligned，导致系统性低估风险。现在 Petri auditor 要从零造 system prompt、工具定义和代码库，这些合成产物常带有能被识破的 tells。以往衡量 realism 的方法要么看模型是否口头表露 situational awareness（抓不到 unverbalized awareness），要么事后让模型给 transcript 打 realism 分（校准不明，而且会把本身就很怪/高风险的真实部署场景误判为 eval，且粒度粗）。这篇（Anthropic Fellows 项目）做了两件事：1. 提出 realism win rate 指标：把一条 eval transcript 和 N 条真实部署 transcript 逐对给带 reasoning 的 LLM judge，让它挑出哪条是 eval，统计 eval 骗过 judge 的比例；部署数据用两套，一套是第一作者自己的 25 条 Claude Code 使用记录，一套是 Claude Code、有害请求类 WildChat、"vulnerable" 用户 WildChat 各 10 条的混合集，后者用来抵消 judge"越有害越像 eval"的启发式；2. 给 Petri auditor 一个人工整理的真实部署资源库（真实 system prompt、tool set、代码库，附 README 和索引），外加 list_directory、read_file、send_file_as_tool_result、search_in_files 四个工具。在 5 个 reward hacking 场景（修 bug 但测试里有不可能满足的断言，并明令不许改测试）上，以 Sonnet 4.5 为 auditor/target，平均 realism win rate 从 4.6% 升到 32.8%，明显好于 realism filter 基线；只给 system prompt 和工具不给代码库也有显著提升；资源与 seed 关联度降低时效果只略有下降，但 auditor 更容易放弃资源转回纯合成代码库。三个良性 ML/SWE 任务上资源也稳定提升 realism。但在高风险的 shutdown resistance 场景（target 用 Sonnet 4）里，有资源 win rate 仍接近 0%，重写 seed 让其更细致可信提到 15.0%，再加资源只到 19.3%，说明这类场景的瓶颈是任务本身（task-driven eval awareness）而非环境；对部署数据两两比较也显示 Sonnet 4.5 会把有害 WildChat 判为最不真实，即模型天然怀疑怪异/有害场景是测试，Gemini 3 Pro 这种偏差较小。指标验证上，post-hoc 打分和口头 eval awareness 都同意资源有效，但 post-hoc 评分呈双峰、会自信地把真实 Claude Code 记录判为 eval，而 win rate 更连续，作者认为最适合 hillclimb。重要的一点是，更真实的审计并没有显著改变 Sonnet 4.5 的 reward hacking 率（Sonnet 3.7 上略有上升但误差大），作者说这只是初步结果，模型可能只在 99%+ 确信时才改变行为。Judge CoT 分析显示资源主要减少了"太干净"的 tell，也减少不真实用户行为和人为施压，但因环境更复杂，工具结果不一致略增。负面结果：给 auditor 真实用户 prompt 资源对单轮 sycophancy 审计几乎无提升；基于口头 eval awareness 回滚重采样的做法因 Goodhart（口头表露降了但人工看并不更真实）被放弃；needle-in-a-haystack 版本因上下文过长、judge 会靠部署数据的伪相关"挑异类"而弃用。局限是只覆盖 agentic coding、部署数据仅 25–30 条且分布窄、模型组合有限。资源功能已合入 Petri，代码开源。

