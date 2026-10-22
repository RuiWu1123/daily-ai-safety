---
title: "Finding Cloud Misconfigurations with Frontier AI: A Case Study"
lab:
  - "UK AISI"
date: 2026-07-07
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/finding-cloud-misconfigurations-with-frontier-ai-a-case-study
star: false
tags:
  - 网络安全
  - 危险能力评估
---

# Finding Cloud Misconfigurations with Frontier AI: A Case Study

**来源**：AISI Blog · 2026-07-07 · [原文](https://www.aisi.gov.uk/blog/finding-cloud-misconfigurations-with-frontier-ai-a-case-study)

## 简读

AISI 的 cyber 评估发现近期前沿模型能力明显跃升，能自主执行越来越复杂的攻击链，于是他们想拿第一手证据看看模型对防守方到底有多大用：用两周 sprint，让工程、安全和 cyber 团队用多个前沿模型去找自家 R&D 平台 staging 环境（基于 AWS + Python CDK，与生产完全隔离但配置一致、无真实数据）里的配置错误。威胁模型是攻击者起始拥有开发 VM 上 researcher 级 shell 权限，目标是跨权限边界提权、拿到其他研究员的数据或窃取凭证。方法按人力投入递增分三种：1. 静态源码分析，让商用 coding agent 当安全审查员看私有仓库；2. 自动 agentic probing，用 Inspect 搭成 eval，让模型以普通研究员权限在 staging 里自主尝试读不该读的数据；3. human-in-the-loop red-teaming，安全研究员逐步审批模型动作、手动追最有希望的线索。结果是多个模型找到并利用了此前未知的严重漏洞（现已修复），包括访问控制和基础设施配置错误、提权路径、供应链弱点，最强的模型能把多个漏洞串起来做 lateral movement。一个有意思的发现是源码分析产出最多 high/critical 报告但噪声最大，很多是故意的设计取舍或已在别处缓解，需要最资深的工程师逐条甄别，所以初看最省人力，实际反而最耗人工。后两种方法都发现了一个隔离机制上很不直观的配置错误：五个独立步骤串起来，普通用户无需受害者交互就能访问其他用户的 workload 和数据，可冒充他人；某个 cyber 能力强的模型花不到 £150 token 就找到了，整个项目 token 花费不到 £1000。各模型长处不同，但都找到了值得修补的问题，作者认为用任何近期 LLM 审查系统都对防守方有价值，且更高 token 预算可能找到更多。检测方面，一个基础商用告警系统完全没把 agent 的活动当安全事件，更高级的监控（agentless 云扫描 + 主机轻量 sensor）识别出了部分激进行为，如反复尝试 assume credentials 和异常流量。结论是投入更多人力的方法结果更确凿可操作，AISI 计划随能力变化重复这一练习，并建议防守方参考 NCSC 的"用 AI 找漏洞前要问的 10 个问题"。

