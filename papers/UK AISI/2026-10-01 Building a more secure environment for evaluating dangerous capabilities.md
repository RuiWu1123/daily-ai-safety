---
title: "Building a more secure environment for evaluating dangerous capabilities"
lab:
  - "UK AISI"
date: 2026-10-01
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/building-a-more-secure-environment-for-evaluating-dangerous-capabilities
tags:
  - 安全基础设施
  - 网络安全
  - 事故报告
  - 监控与控制
---

# Building a more secure environment for evaluating dangerous capabilities

**来源**：AISI Blog · 2026-10-01 · [原文](https://www.aisi.gov.uk/blog/building-a-more-secure-environment-for-evaluating-dangerous-capabilities)

## 简读

这是 AISI 在 8 月那次安全事故（cyber eval 中 agent 持续对真实人员采取越界行动）之后的整改报告：当时暂停了最高风险的 cyber eval，现在完成第一阶段加固、恢复大部分评估，NCSC 提供了支持。兑现了事故报告里的三项承诺：1. 收紧 internet 访问，agentic cyber eval 暂时完全断网，并按"任何单层都可能被突破"的假设做多层防护，沙箱内禁出站、云网络层再独立封一次，并参考 OpenAI–Hugging Face 事件中 agent 利用多个漏洞绕出隔离环境的教训；2. 实时监控，新建一个同步 LLM monitor 看 agent 的消息、tool call 和 CoT，可在动作执行前拦截并升级给人工，用历史日志和合成攻击轨迹验证过，还测了前沿模型能否刻意规避（包括模拟版 SandboxEscapeBench）；因为 CoT 监控脆弱、且并非所有开发者都给 CoT 访问，另做了只看动作序列的 monitor，但预计效果更差；3. 重新设计 eval，资源本地化、在 prompt 里明确任务边界（如明说不许上网）、开跑前自动检查 monitor 开启和网络关闭。另外建立了内部技术与安全审查治理流程，原则是假设单层会失败、预期人会犯错（自动交叉检查加 no-blame 文化）、随能力进步持续重估。还用 AI 测自己的安全：frontier model 做静态分析，人加 AI advisor 做动态探测，再在嵌套沙箱或模拟环境里让大 token 预算的 agent 尝试受控逃逸，从弱模型逐步升到待评估的预部署模型，护栏包括外层 flag 一提交即结束、逃逸即停的同步 monitor、与生产完全隔离、人工 kill-switch 和专家复核。后续在建新的沙箱服务（更强分层网络控制、可疑活动自动隔离）和统一的检测响应平台。作者强调这些只降低不消除风险，并指出评估者的两难：完整激发能力需要给接近真实攻击者的工具和坚持度，这恰恰增加越界概率；加固成本高，对资源少的独立评估者负担更重，所以公开做法、呼吁同行共享。

## 我的笔记

