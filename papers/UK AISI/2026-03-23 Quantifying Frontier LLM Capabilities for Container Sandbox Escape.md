---
title: "Quantifying Frontier LLM Capabilities for Container Sandbox Escape"
lab:
  - "UK AISI"
date: 2026-03-23
source: "AISI Research"
url: https://www.aisi.gov.uk/research/quantifying-frontier-llm-capabilities-for-container-sandbox-escape
other_versions:
  - "https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities"
tags:
  - 网络安全
  - 危险能力评估
---

# Quantifying Frontier LLM Capabilities for Container Sandbox Escape

**来源**：AISI Research · 2026-03-23 · [原文](https://www.aisi.gov.uk/research/quantifying-frontier-llm-capabilities-for-container-sandbox-escape)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities)

## 简读

背景是 agent 评估和部署普遍跑在 Docker/OCI 容器 sandbox 里，而在这种威胁模型下代码执行权限是设计上就给的，真正的问题是 agent 能否逃出它所在的 sandbox；超大规模推理服务多用 microVM 或 gVisor，但开源 agent 生态和本地开发工具大量依赖普通 Docker 隔离，此前也没有系统评估 AI agent 能否发现并利用容器栈弱点的 benchmark（o1 system card 已记录过模型在 CTF 中利用配置错误的评估主机的案例）。UK AISI 推出开源的 SandboxEscapeBench（ICML 2026，同时有博客版），用 Inspect 实现成 CTF：采用 "sandbox-within-a-sandbox" 架构，被测容器跑在加固的 VM 里，flag 放在 VM 文件系统上，即使逃出容器也碰不到真实基础设施；18 个场景覆盖 orchestration、runtime、kernel 三层，从简单 misconfiguration、权限分配错误到 runtime CVE 和多步 kernel 提权链，全部基于已公开的漏洞类别并配有参考解法，难度按安全专家预估解题时间分 1–5 级（三位专家评分一致性 α = 0.816），另保留一个私有测试集。agent 有容器内 shell，知道目标是逃逸但不知道具体漏洞，没有 jailbreak 式诱导，每个模型×任务 5 次、每次 2.5M token。主要发现：1. 前沿模型能可靠利用真实世界常见的配置错误（如暴露的容器管理接口、privileged 容器、可写 host mount），难度 1–2 级上大模型成功率很高，而这类问题恰恰常见于开发工具、临时搭的评估 harness 和快速迭代的 agent 原型；2. 需要具体漏洞知识或多步利用的难度 3–5 级明显更难，GPT-5 和 Opus 4.5 在 3 级上仍有约 40% 成功率，原始模型在 4、5 级上为零，所有成功逃逸都利用的是已披露漏洞；3. 能力随模型规模和 inference-time compute 增长，成功率与 token 预算近似 log-linear，大小模型之间、闭源与 open-weight 之间差距大，小模型在最直接的 misconfiguration 上还行但遇到复杂利用链就急剧下降，很多 run 每次约 $1，攻击者可以低成本多次尝试；4. 给出漏洞提示时低预算下大幅加速，说明漏洞发现是早期主要瓶颈；GPT-5.2 比 GPT-5 明显退步（0.27 vs 0.50）；5. 开发中模型找到了四条设计者没预料的逃逸捷径，说明即使安全意识强的团队搭的环境也容易留缝。transcript 分析显示首轮拒答很少，GPT 系列失败时常中途放弃，DeepSeek-R1 和 GPT-OSS-120B 经常虚报成功，Claude 模型基本不拒答也不幻觉成功。论文更新版加入 2 个月后发布的新模型并跑到 100M token：Claude Mythos Preview 至少成功一次的样本达 100%、难任务 pass@5 也为 100%，直接饱和该公开 benchmark（Opus 4.5 为 56%），饱和速度远快于 Cybench、MMLU 等；长 run 中还出现模型在尝试利用时把自己的 sandbox 弄崩的新失败模式。局限是故意引入弱点、无监控、agent 架构简单，不代表有防御的生产环境中的端到端被攻破概率。结论和建议：misconfiguration 要靠严格的容器配置解决，已知 kernel/runtime 漏洞要靠及时打补丁，与 NCSC 一致认为普通容器隔离本身不足以构成强安全边界，应至少以 hypervisor 隔离为底线做 defense in depth；agent 开发者应默认把"plain Docker isolation"视为不够，用该 benchmark 压测配置，containment 评估也要考虑 token 预算、重试、并行度等部署配置，因为它们能把系统推过能力阈值。

## 我的笔记

