---
title: "Our evaluation of Claude Mythos Preview’s cyber capabilities"
lab:
  - "UK AISI"
date: 2026-04-13
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities
tags:
  - 网络安全
  - 危险能力评估
---

# Our evaluation of Claude Mythos Preview’s cyber capabilities

**来源**：AISI Blog · 2026-04-13 · [原文](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)

## 简读

AISI 对 Anthropic 4 月 7 日发布的 Claude Mythos Preview 做了网络安全能力评估，结论是它在本已快速进步的 cyber 能力曲线上又往上迈了一步。背景是 AISI 从 2023 年起持续追踪 AI cyber 能力，评估从对话式探测、CTF 一路升级到多步攻击模拟；两年前最好的模型还只能勉强做入门级任务。CTF 方面，在 2025 年 4 月之前没有任何模型能完成的 expert 级任务上，Mythos Preview 成功率达到 73%。更关键的是 cyber range：AISI 自建的 "The Last Ones"（TLO）是一个 32 步的企业网络攻击模拟，从侦察一直到完全接管网络，估计人类需要约 20 小时。Mythos Preview 是第一个端到端解出 TLO 的模型，10 次中成功 3 次，平均完成 22/32 步；第二名 Claude Opus 4.6 平均 16 步。测试用的是 100M token 预算，性能一直随推理算力增长没有到顶，作者预计继续加算力还会提升。局限方面，它没能完成面向 OT 的 range "Cooling Tower"，但卡在的是其中的 IT 部分，所以不能说明它不擅长 OT 攻击。作者强调这些 range 比真实环境容易：没有主动防御者和防御工具，触发告警也没有惩罚，因此只能说它至少能在已获得网络访问的前提下自主攻击小型、防护薄弱的企业系统，无法判断能否攻破加固的系统。后续 AISI 会做带主动监控、EDR、实时事件响应的加固 range，并跟踪 AI 驱动的漏洞发现和渗透测试在真实系统上的表现。给组织的建议是回到基本功（及时打补丁、访问控制、安全配置、完整日志），参考 NCSC 的 Cyber Essentials，并强调 cyber 能力是双刃剑，防御方也应尽早利用。

