---
title: "Measuring AI Agents’ Progress on Multi-Step Cyber Attack Scenarios"
lab:
  - "UK AISI"
date: 2026-03-16
source: "AISI Research"
url: https://www.aisi.gov.uk/research/measuring-ai-agents-progress-on-multi-step-cyber-attack-scenarios
other_versions:
  - "https://www.aisi.gov.uk/blog/how-do-frontier-ai-agents-perform-in-multi-step-cyber-attack-scenarios"
tags:
  - 网络安全
  - 危险能力评估
  - 评估方法
---

# Measuring AI Agents’ Progress on Multi-Step Cyber Attack Scenarios

**来源**：AISI Research · 2026-03-16 · [原文](https://www.aisi.gov.uk/research/measuring-ai-agents-progress-on-multi-step-cyber-attack-scenarios)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/how-do-frontier-ai-agents-perform-in-multi-step-cyber-attack-scenarios)

## 简读

背景是现有 AI 网络攻击能力评估主要是孤立的 CTF 题或问答集，Cybench 等已接近饱和（前沿模型约 93%），而且测不出真实攻击需要的长链条自主执行、状态追踪和错误恢复。UK AISI 改用 cyber range：由 SpecterOps 和 Hack The Box 搭建的多主机模拟网络，漏洞排成顺序攻击链。两个 range：“The Last Ones” 是 32 步的企业网络入侵（目标是窃取内部数据库，分 9 个 milestone，估计人类专家约 14 小时），“Cooling Tower” 是 7 步的工控系统攻击（目标是扰乱模拟电厂的冷却塔，每步工作量大得多、依赖结构更复杂，估计约 15 小时）。两个 range 都没有主动防御，告警只记录不拦截，测的是无防御条件下的原始能力。评估了 2024 年 8 月到 2026 年 2 月发布的 7 个模型（GPT-4o、Sonnet 3.7、Sonnet 4.5、Opus 4.5、GPT 5.1 Codex、Opus 4.6、GPT 5.3 Codex），用的是刻意简化的 ReAct agent（Kali Linux 加 Bash/Python/C2 工具，Inspect 框架，context compaction 支撑长 run），token 预算 10M 和 100M，指标是完成的步数（flag 验证，无部分分）。主要发现两个互相叠加的趋势：1. 性能随 inference-time compute 呈 log-linear 增长，到 100M 没看到 plateau，10M 到 100M 最多提升 59%，而且多数 run 到预算上限时仍在做有目标的操作；作者强调加 token 不需要任何技术门槛，Opus 4.6 一次 100M run 约 80 美元；2. 固定预算下每代模型都更强，10M 时平均步数从 GPT-4o 的 1.7 涨到 Opus 4.6 的 9.8；100M 时 Opus 4.5 平均 11.0、Opus 4.6 平均 15.6，两个月内提升 42%，最好一次 run 完成 22/32 步，约相当于人类专家 14 小时中的 6 小时（Opus 4.5 最好的 run 只对应约 1.5 小时）。作者用 token efficiency 和专项能力深度两个维度解释差异，GPT-4o 无论给多少 token 都卡在第 2 步。性能在 milestone 4 之后陡降，那里从侦察和 web 利用转向需要逆向、密码学和恶意软件开发的专业阶段，Opus 4.6 是第一个稳定突破这道坎的模型。run 间方差很大（同模型同预算最差只到 11 步），所以固定算力是该少量长 run 还是多次短 run 仍是开放问题。工控 range 上进展有限：10M 时多数模型 0 步，100M 时 Opus 4.6 平均 1.4 步，GPT 5.3 Codex 单次最多 3/7。一个值得注意的现象是模型会走设计者没预料的路径，比如不按预期先攻破 web 应用再拿密码材料，而是直接从网络流量推断专有控制协议、调用未受保护的功能，甚至靠类似 fuzzing 的方式撞上 PLC 实现里的 bug 绕过认证（模型自己并不理解原理），这些问题主跑前已修补。辅助实验里，从中途 milestone 开始的 run 显示模型在 range 的几乎所有区域都能推进，说明有一定网络安全知识的人类在全自主攻击可行之前就能用 agent 加速部分环节；额外两句高层指导、预填示范轨迹、减少工具调用失败的 system prompt 都没带来显著提升；行为分析和 OPSEC 告警计数方法还不成熟。局限方面作者承认 range 没有防御者、不惩罚被检测、漏洞密度偏高、比真实网络简单，同时结果也是能力下界（没测 1B token、没有专门 scaffolding 和工具、没有人机协作，而后者可能才是最现实的威胁模型）；N=5 统计力有限。他们在透明性和保持 held-out 之间选择公开 range 的概要描述（细节刻意有限），并加了 canary GUID。结论是自主网络攻击能力增长很快但仍远未端到端完成，对工控环境威胁暂时有限，模型已强到值得在真实渗透测试中验证，后续计划扩充 range、加入主动防御和隐蔽性度量。

## 我的笔记

