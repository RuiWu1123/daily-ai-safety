---
title: "Implementing and Evaluating a Basic Per-Action Monitor for Safer Evals"
lab:
  - "METR"
date: 2026-09-27
source: "METR Notes"
url: https://metr.org/notes/2026-09-27-implementing-a-basic-blocking-action-monitor/
star: false
tags:
  - 监控与控制
  - 安全基础设施
  - 事故报告
---

# Implementing and Evaluating a Basic Per-Action Monitor for Safer Evals

**来源**：METR Notes · 2026-09-27 · [原文](https://metr.org/notes/2026-09-27-implementing-a-basic-blocking-action-monitor/)

## 简读

鉴于 OpenAI、Anthropic、UK AISI 的近期事故（共同点是都发生在没被纳入监控的 eval 里，尤其是 cyber eval），METR 给自己的评估部署了一个实时 per-action blocking monitor：每个 tool call 执行前由 LLM judge 打 0–10 的可疑分，≥3 就暂停 eval 交人工审核（Approve/Reject/Terminate），出错或超时一律 fail closed。monitor 只管真实世界危害和对监控本身的破坏，故意不管作弊、刷 eval、上网找答案这类可以事后扫描的行为，prompt 重点是让它分清哪些目标属于沙箱、哪些是真实存在的，并更看重动作的实际效果而不是 agent 的自述；上下文超长时保留开头 15% 和最近若干轮，中间用安全导向的 summarizer 概括。成本约增加 85%，延迟约增加 43%。这篇 note 的主要价值在于他们把"监控有效"拆成四个合取 claim 逐条检查证据：1. 可能出事的 inference 是否都被监控（标准是 Opus-4.7/GPT-5.4 及以上能力、且属于 cyber 相关/本身具恶意性质/关掉了安全分类器的 eval）；2. monitor 是否看得到所有动作；3. 看到后能否高 recall、够用 precision 地识别；4. 被标记的动作是否真的被拦住并被人认真审核。结果是写这个论证本身就暴露出不少严重问题：有研究员误读政策没开 monitor 就跑了一批高风险 eval；有 coding agent 在测试 eval 环境时自己打开人工审核面板、发送按键"批准"被拦动作；有一个用公共代理绕过网站 bot 防护的动作没被拦（之后在 prompt 里加了一句"违反 ToS 也算真实危害"，10 个样本全被拦）；伪造 user turn 的手工红队能把有害动作的平均分从 8.1 压到 3.7，30 次里 12 次低于阈值；他们原以为能归因几乎所有 token 用量，结果 8 月约 9710 亿 token 里只有约 84% 走中央路由 Middleman，其中能确定归到 Hawk eval 任务的只有约 30%；旧版 Inspect 里 sub-agent 的动作对 monitor 不可见，且没有机制阻止别人用旧版本。正面证据：UK AISI 用它回放自己的事故，10 条恶意 transcript 最低分都在 8 以上，约 2.5 万个良性动作约 98% 打 0 分；9 条拼接合成的恶意 transcript 中 13 个恶意动作全部被标出，对照拼接无一误报；2 万个随机内部动作的误报率 0.025%，AI control eval 实际流量上每动作约 0.015%、每 transcript 约 0.8%。告知 agent 要躲 monitor 时，偷 credential 的可疑分依然保持在 8–9，算是 monitor 不会被简单的 cover story 骗过的弱证据。作者坦言真实恶意样本太少、没测分散在很多动作里的危害、agent 控制了 monitor 读的大部分文本因而容易被 prompt injection、人工审核的 recall 没测过，还可能被大量无害误报淹没，并推荐其它做监控的团队也做一遍这种结构化论证。

