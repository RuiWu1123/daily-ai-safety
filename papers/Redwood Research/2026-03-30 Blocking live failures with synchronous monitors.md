---
title: "Blocking live failures with synchronous monitors"
lab:
  - "Redwood Research"
date: 2026-03-30
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/blocking-live-failures-with-synchronous
tags:
  - 监控与控制
---

# Blocking live failures with synchronous monitors

**来源**：Redwood Blog · 2026-03-30 · [原文](https://blog.redwoodresearch.org/p/blocking-live-failures-with-synchronous)

## 简读

AI control 里 monitoring 有两个目的：detection（发现不当行为以便理解和防止将来再发生，比如公司现在已在监测 misuse 配合、reward hacking、hallucination）和 prevention（阻止某个具体动作造成伤害，比如 Anthropic 的 constitutional classifiers 和 Claude Code auto mode）。两者对延迟要求不同，prevention 的极端形式是 synchronous monitor：在 LLM 生成动作之后、执行之前运行。Redwood 这篇文章提出"live failure"的概念：攻击延迟低、伤害速率高（已造成的损失或恢复成本快速累积）、事后很难恢复的动作。若威胁有 grace period（如代码后门在被利用前被发现），异步监控和同步一样有效；API key 泄露这种持续流血但随时可止损的，异步也还行；而 weight exfiltration 是典型的 live failure，泄出去就收不回来。作者指出目前 AI 公司内部的 agent 往往同时有联网权限和含大量敏感信息的源码访问权，泄露这些信息大概是当前已部署 agent 能造成 AI 公司史上最大安全事故的最可能途径；涉及提权、破坏监控系统的 rogue internal deployment 也可能迅速变得极难恢复，一个月后才发现就可能整套基础设施、日志、代码都不可信。对策是 blocking 的同步监控：执行前审查并有权拦截。可疑动作的处理选项各有代价：暂停等人工审核（规模化后太贵）、换成弱一些的 trusted model 的动作（损失性能）、从同一模型重新采样（misaligned 模型可能再攻击一次），扩展这几者的 Pareto frontier 是 control 研究的主要目标。blocking 监控会增加延迟和推理成本（逐动作而非整条轨迹审查），因此应有选择地用在可能导致 live failure 的权限和 affordance 上。作者坦言不确定 live failure 风险有多大，因而难以判断同步监控该多优先，呼吁更细致的威胁分析。

