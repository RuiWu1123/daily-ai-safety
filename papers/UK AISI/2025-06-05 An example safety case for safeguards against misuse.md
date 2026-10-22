---
title: "An example safety case for safeguards against misuse"
lab:
  - "UK AISI"
date: 2025-06-05
source: "AISI Research"
url: https://www.aisi.gov.uk/research/an-example-safety-case-for-safeguards-against-misuse
other_versions:
  - "https://www.aisi.gov.uk/blog/making-safeguard-evaluations-actionable"
star: false
tags:
  - 威胁建模
  - 越狱与鲁棒性
---

# An example safety case for safeguards against misuse

**来源**：AISI Research · 2025-06-05 · [原文](https://www.aisi.gov.uk/research/an-example-safety-case-for-safeguards-against-misuse)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/making-safeguard-evaluations-actionable)

## 简读

背景是前沿模型正接近危险能力阈值（OpenAI、Anthropic 都公开说过下一代可能需要 ASL-3 级别防护），misuse safeguards（refusal training、输入输出 classifier、封号等）很快会变成部署安全的承重墙，但现有的 red teaming 结果是零散证据，很难直接转成"能不能部署"的决策。这篇 UK AISI 与 Redwood、MATS、MIT 合作的论文给出一个端到端的示例 safety case，论证一个假想的 AI assistant 在有 safeguards 时不会让某条风险路径（例子是新手做病原体合成）的期望大规模伤害超过阈值 T，建立在 AISI 之前的 Principles for Safeguard Evaluation 五步框架上。核心做法分三块：1. safeguard 评估：威胁建模专家构造代表性有害请求集，red team 尝试绕过 safeguards，得到每个成员"花在绕过上的时间 vs 完成请求数"的 evasion cost 曲线；封号、KYC、漏洞修补这类不方便一起测的组件单独评估（比如 main evaluation 不真封号而是给时间加罚分，另设 ban evaluation 估计重新开号的成本），最后聚合外推成平滑曲线。2. 定量 uplift model：专家估计没有 AI 时新手愿意投入的时间分布和成功率曲线，用 dangerous capability eval 估计 pre-mitigation 模型下的成功率，再用 safeguard 评估结果把时间成本曲线向右平移，得到 post-mitigation 风险，两者之差就是 uplift；模型显式列出六条假设（如攻击尝试独立、只通过节省时间影响风险），都要求做成保守的，并提供了交互版网站 aimisusemodel.com。3. 部署期间的持续风险信号与三条程序性政策：部署前超阈值不发布；部署后持续评估（可以是 jailbreak bounty，甚至去黑市买 jailbreak）；风险逼近阈值时一个月内加固或限制访问。他们用 Monte Carlo 模拟"universal jailbreak 突然出现"的最坏情况，示例参数下从 jailbreak 出现到风险越过阈值约有三个月，所以一个月的反应期够用。最后把这些证据组织成 claim 树，包括 red team 比新手更强且激励正确、模型在评估中表现有代表性（论证 alignment faking 等不太可能）等子论点。作者强调这只是一条路径而非唯一路径，不适用于少量请求就能造成大害、或对响应延迟不容忍的威胁模型；uplift model 是参数高度不确定的玩具模型，过于保守又会"狼来了"，如何不过度保守地可靠评估留给未来工作。

