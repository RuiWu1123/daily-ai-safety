---
title: "Breaking agent backbones: Evaluating the security of backbone LLMs in AI agents"
lab:
  - "UK AISI"
date: 2025-10-26
source: "AISI Research"
url: https://www.aisi.gov.uk/research/breaking-agent-backbones-evaluating-the-security-of-backbone-llms-in-ai-agents
tags:
  - 提示注入
  - 越狱与鲁棒性
  - 网络安全
---

# Breaking agent backbones: Evaluating the security of backbone LLMs in AI agents

**来源**：AISI Research · 2025-10-26 · [原文](https://www.aisi.gov.uk/research/breaking-agent-backbones-evaluating-the-security-of-backbone-llms-in-ai-agents)

## 简读

Lakera AI 与 AISI 合作的 ICLR 2026 论文，问的是 agent 的 backbone LLM 选择如何影响 agent 安全（这里 security 特指对手在部署语境下利用 agent 的能力，区别于毒性、可靠性等 safety 问题）。难点在于 agent 执行流是非确定的，LLM 本身又无法区分数据和指令，新的 LLM 漏洞和权限管理、XSS 等传统漏洞缠在一起；已有 benchmark 要么只覆盖间接注入等少数攻击向量，要么得模拟整个 agent。作者提出 threat snapshots：把 agent 形式化为一串无状态的 LLM 调用加处理步骤，每次调用都带完整 context，于是可以只截取漏洞出现的那一个状态（完整 context + 攻击者目标和插入方式 + 打分方式）来评估，不必建模完整执行流，也把 LLM 漏洞和传统漏洞分开。配套两种攻击分类：按向量（direct/indirect，后者包括网页、文档、工具定义等）和目标（数据外泄、内容注入、决策操纵、DoS、系统与工具攻陷、内容政策绕过）分，以及按任务类型（直接/间接指令覆盖、直接/间接工具调用、直接上下文提取、AI 服务拒绝）分。他们设计了 10 个覆盖全部向量、目标和任务类型的 threat snapshot，每个有三档防御（L1 最小的 system prompt 约束、L2 更严格的 prompt 和更长的良性上下文、L3 再加用同一模型做 LLM-as-judge），只考虑单步攻击作为安全性下界。攻击通过游戏化众包 Gandalf Agent Breaker 收集：947 名用户、13,920 个 session、194,331 条独立攻击，其中 10,935 条成功，再在 7 个 backbone 上重测，每档每 snapshot 选最强的 7 条，共 210 条（占总量 0.1%），这批攻击的平均得分 0.56，而公开数据里的平均攻击只有 0.18。用这套 b³ benchmark 评测 34 个 LLM（每条攻击重复 5 次，bootstrap 置信区间），发现：1. 开启 reasoning 一般会提升安全性，与 Zou et al. 的结论相反，只有 gemini-2.5-flash-lite、gpt-5-nano 这类极小模型例外；2. 模型大小与安全性基本无关，不开 reasoning 时大号版本没有显著优势甚至更差；3. 闭源系统总体更安全，但闭源测的是带额外 guardrail 的系统级而开源是模型级，最好的开源模型 kimi-k2-thinking（0.34）好于不开 reasoning 的 gpt-5.1；4. 能力与安全总体相关，但能力最高的 gpt-5.1 和 kimi-k2-thinking 安全排名只在第 8 和第 14；最安全的是 claude-haiku-4-5 和开 reasoning 的 claude-sonnet-4-5，且 haiku-4-5 在各档防御下都最安全；不同任务类型下的排名差别很大，所以应按具体用例选 backbone。排名对攻击选择、聚合方式、snapshot 选择都比较稳健，攻击质量影响最大。局限：不考虑效用和延迟；backbone 安全只是 agent 安全的一部分，无法量化被投毒文档被 RAG 检索到的概率，也不分析跨多步的传播；众包成本高。benchmark 已集成进 Inspect 并开源，只公开去掉了最强攻击的弱版数据集，发布前也通知了相关模型提供方以便修补。

