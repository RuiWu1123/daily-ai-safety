---
title: "Red-Teaming OpenAI's Internal Agent Monitoring Systems"
lab:
  - "METR"
  - "Redwood Research"
date: 2026-10-22
source: "METR Blog"
url: https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring
other_versions:
  - "https://blog.redwoodresearch.org/p/red-teaming-openais-internal-agent"
tags:
  - 监控与控制
  - 安全基础设施
---

# Red-Teaming OpenAI's Internal Agent Monitoring Systems

**来源**：METR Blog · 2026-10-22 · [原文](https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring)　另见：[Redwood Blog](https://blog.redwoodresearch.org/p/red-teaming-openais-internal-agent)

## 简读

METR 的 David Rein 和 Redwood 的 Adam Kaufman 在 7 月 21 日至 8 月 11 日对 OpenAI 内部的 misalignment 监控系统做了为期三周的 high-access 压力测试，作为让外部研究者深度接触 lab 内部基础设施的试点：他们在 OpenAI 发放、不离场的设备上工作，能看内部代码库、monitor 的 prompt 与配置和内部文档，并访谈了监控、safety systems、安全团队的约十几位人员。产出是一份 61 页的内部报告，主要估计 agentic 推理流量中有多大比例被监控、以及 agent 原则上能否关闭或绕过监控；事先约定只公开一篇简短的高层摘要，OpenAI 有权删改敏感内容，且 METR 和 Redwood 没有单方面说明删改的权利，与此前的 Frontier Risk Report、Hugging Face 事件调查不同。评估对象是 7 月 21 日及之前的异步监控系统，不涵盖演练期间 OpenAI 正在推进的扩展。主要发现：GPT-5.5 及以上模型的内部 agentic Responses API 流量中，估计约 75–94% 属于应被监控的范围（不确定性很大），其中内部 Codex agent 的子集为 99.2%；演练开始时 RL 训练 run 不在监控范围内（3 到 6 月曾监控过一部分 rollout）；compaction 事件未被监控，估计导致 5 到 7 月约 10% 的应监控 Codex 流量漏监，而监控是在 agent 把控制权交还用户时才触发，所以那段时间 agent 只要一直继续行动就能无限推迟被监控（OpenAI 在演练前已自行发现并在演练期间修复）；monitor 出错率低于 0.2%，观察到的一个 24 小时内没有 load-shed。他们还发现了几类漏洞，只在高层描述：Codex agent 原则上可绕过 sandbox 和 Auto-Review、拥有宿主用户的全部权限；有手段让大量近期动作逃过监控（细节被 OpenAI 删去）；可能利用 agent 与 monitor 所见 trajectory 之间的序列化差异让 monitor 失败；存在可由客户端控制、为新 agent 关闭监控的开关（但这一操作本身可能被监控捕获）；两个被认为只读、未受监控的内部工具可能被突破权限（未实际验证）。正面结论包括：除少数例外 monitor 能看到 agent 看到的完整 trajectory，监控 prompt 覆盖 scheming、破坏监控、sabotage、数据外泄、欺骗、prompt injection 等类别。OpenAI 称已修补所有影响生产防护的漏洞并大幅调整了覆盖范围，作者没有核实。最后给出监控系统的设计原则：让不受监控的推理需要显式审批，按固定消息数或时间间隔监控而不是等回合结束；定期把全部推理日志与监控日志对账，维护已知绕过方式清单，确保 monitor 与 agent 看到相同上下文；明确事故响应负责人，保留防篡改、易检索的日志；定期做 control evaluation 和漏洞搜寻并研究评估串通的方法；隔离 agent 与 monitor，agent 的动作不应影响监控是否及何时运行，agent 一般也不应接触监控系统的设计和代码。

## 我的笔记

