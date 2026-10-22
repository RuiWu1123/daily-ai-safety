---
title: "Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes"
lab:
  - "Redwood Research"
date: 2026-04-14
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/anthropic-repeatedly-accidentally
star: false
tags:
  - CoT与可监控性
  - 事故报告
  - 安全基础设施
---

# Anthropic repeatedly accidentally trained against the CoT, demonstrating inadequate processes

**来源**：Redwood Blog · 2026-04-14 · [原文](https://blog.redwoodresearch.org/p/anthropic-repeatedly-accidentally)

## 简读

Anthropic 在 Mythos alignment risk update 里披露，因一个长期未被发现的技术错误，约 8% 的训练 episode 把 CoT 暴露给了奖励函数，且同样影响了 Opus 4.6 和 Sonnet 4.6。这至少是第二起独立事故：此前 Opus 4.6 已有另一个错误让 CoT 进入 oversight 信号（<0.01%，集中在训练末期）；再往前 Opus 4 也暴露过，那次更像是内部对"是否要避免训练 CoT"优先级不清。作者认为这直接降低了对 Mythos 推理痕迹可监控性的信心，更重要的是暴露流程不足：发现 Opus 4.6 的问题后本应改造流程。随着越来越多开发交给可能不可信、粗糙的 AI，这类执行失误会更常见，而依赖安全评估（"bumpers"）穿越 intelligence explosion 的计划成败取决于测量保真度。文中列举需要确保按计划执行的方面：训练 CoT/interp 牺牲可监控性，用与 honeypot 同源的数据训练可能提高 evaluation awareness，惩罚可见的 reward hacking 可能只是让它更隐蔽，control protocol 只和最弱环节一样强。这类事故还会扭曲我们对当前模型对齐状况的认识，并可能经 warm-start 传给后续模型。作者也指出 Anthropic 目前的 risk report 不太依赖 CoT 可监控性，不应把这当作其整体安全执行质量的代表，同时称赞 OpenAI 似乎成功避免了优化 CoT，o3 很愿意在 CoT 里说出作恶意图。附录推测问题出在多个团队并行实现 RL 环境、无人对整体负责；随机审计 100 个奖励输入就很可能抓到 8% 的问题，也可以只改 CoT 看奖励是否变化来自动检测，估计发现问题只需几人时，建立可靠流程只需几人周。作者另猜 Anthropic 模型 CoT 外化推理明显少于 OpenAI 模型，但主因可能是模型不严格区分 thinking 与输出、以及 warm-start 数据，而非这些事故。

