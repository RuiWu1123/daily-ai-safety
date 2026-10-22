---
title: "BashArena: A Control Setting for Highly Privileged AI Agents"
lab:
  - "Redwood Research"
date: 2025-12-17
source: "Redwood Research"
url: https://arxiv.org/abs/2512.15688
other_versions:
  - "https://blog.redwoodresearch.org/p/basharena-and-control-setting-design"
tags:
  - 监控与控制
  - 评估方法
---

# BashArena: A Control Setting for Highly Privileged AI Agents

**来源**：Redwood Research · 2025-12-17 · [原文](https://arxiv.org/abs/2512.15688)　另见：[Redwood Blog](https://blog.redwoodresearch.org/p/basharena-and-control-setting-design)

## 简读

Redwood 发布新的 high-stakes control setting BashArena（论文 + 博客），用于研究高权限、安全关键环境下的 AI control。已有 setting 各有缺陷：APPS backdooring 是单步任务，BashBench 只有一个窄攻击面的 side task 且主任务太简单，SHADE-Arena 只有 26 对任务。BashArena 含 637 个 Linux 系统管理/基础设施主任务，由 Sonnet 4 从 StackOverflow 问题中筛出前 0.3%、Opus 4.1 生成并经 critique 循环迭代，平均需约 50 步工具调用，测试私有、按通过比例给部分分；另有四个手工 side task：下载执行恶意软件、外泄机密、提权到无密码 sudo、关闭防火墙。主任务专门设计成需要能完成 side task 的权限，side task 测下游效果而非具体方法，以扩大攻击面。结果：主任务未被前沿模型饱和，弱模型明显更差；honest 运行几乎不会误触发 side task。Sonnet 4.5 作攻击者，在 GPT-4.1 mini 监控、4% trajectory-wise FPR（约每步 0.08%）下有 26% 的时间完成破坏而不被发现，弱模型几乎攻击不了，且攻击者还不能挑选任务对。成功攻击靠很深的调用栈让 monitor 跟不上数据流，失败的常因可疑字符串或命名暴露。Sonnet 4.5 作 monitor 能给所有攻击打满分，但也给 9/9894 个良性动作打满分；GPT-4.1 mini 多次采样取平均后可与之相当。去掉 root 让性能从 59% 降到 32%，断网只降到 55% 却能禁掉三个 side task。博客总结的设计经验：关注高层动态、重要性采样到 control 真正有影响的部署、修补或禁止"overpowered"策略；集成要求比预期严格——部分分让蓝队能低成本放弃危险功能，危险代码若简单还能交给 trusted model 做 targeted deferral，所以他们禁止动态权限管理、要求协议不针对具体 side task 定制，剩余最大弱点是 defer-to-trusted 可能显得好于实际。数据集已作为 ControlArena setting 发布，生成 pipeline 开源。

