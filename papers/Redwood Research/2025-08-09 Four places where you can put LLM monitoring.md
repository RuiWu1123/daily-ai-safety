---
title: "Four places where you can put LLM monitoring"
lab:
  - "Redwood Research"
date: 2025-08-09
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/four-places-where-you-can-put-llm
tags:
  - 监控与控制
  - 安全基础设施
---

# Four places where you can put LLM monitoring

**来源**：Redwood Blog · 2025-08-09 · [原文](https://blog.redwoodresearch.org/p/four-places-where-you-can-put-llm)

## 简读

讨论防止 misaligned LLM agent 造成灾难时，monitor 应该放在基础设施的哪里、由哪个团队负责。研究者过去主要关注放在 agent scaffold 里（归 agent 产品团队），作者认为另外三个位置同样重要，这关系到该开发哪些只依赖单一位置 affordance 的 control 技术，以及以后该跟 AI 公司里哪些团队合作。四个位置及其优劣：1. agent scaffold：最简单、最灵活，权限系统本来就在这，能同时看到 LLM 上下文和执行环境，能实现 control 论文里的各种花式策略；缺点是 scaffold 更新频繁、新东西缺乏行业经验，agent 团队文化上不擅长对抗性威胁检测和维护一支调查被标记行为的专家团队，而且像 Claude Code 这种跑在用户/agent 控制的机器上，monitor 可能被关掉。2. 网络威胁 detection-and-response 系统（如 Crowdstrike）：基础设施成熟、团队已习惯处理敏感数据和重复性调查，渗透测试里常能抓到攻击者；有丰富执行上下文，直接看行为后果，对辩解和代码混淆不敏感；调查事件日志的 AI 不直接看 agent 动作，天然有一定抗 collusion 性；缺点是缺少 LLM 为什么这么做的上下文，信息洪流里难用昂贵的 LLM monitor，不适用于说服、对继任模型 data poisoning、sandbagging 等非网络威胁，干预粗糙、有延迟，更适合离线监控。3. LLM API：类似 Anthropic 拦截生物武器相关生成、OpenAI 调查网络攻击团伙的用法；稳健，不会因某个 scaffold 漏装而失效，有 LLM 的全部上下文；但不知道动作会在哪执行，难做细粒度策略，和 scaffold 协调成本高。作者建议同时有 safe API（监控够强、数据中心内任何代码都能调用）和 unsafe API（只给证明自己实现了稳健安全措施的 scaffold 用）。4. code review：成熟、知道代码合并后在哪执行、能看到改动理由、独立于 scaffold 易改且容易回退到人工；缺点是只覆盖需要通过 review 的威胁。作者低置信度的优先级：先确保基础的网络威胁检测不缺（AI 公司本该做），再在容易的 scaffold 里建 monitor，再加到 API 增强稳健性，等 AI 写的代码多到人类开始走过场时再给 code review 加自动 monitor，并持续维护；但具体取决于组织。附录还列了进一步细分，如 scaffold SDK 与外层 scaffold（Claude Code hooks）、核心 API 与 API proxy、CI 测试与 review 辅助、检测动作与检测后果。

## 我的笔记

