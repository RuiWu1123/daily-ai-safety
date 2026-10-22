---
title: "UK AISI / CAISI Preliminary Assessment of Kimi K3's Cyber Capabilities"
lab:
  - "UK AISI"
date: 2026-07-23
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities
star: false
tags:
  - 网络安全
  - 危险能力评估
---

# UK AISI / CAISI Preliminary Assessment of Kimi K3's Cyber Capabilities

**来源**：AISI Blog · 2026-07-23 · [原文](https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities)

## 简读

UK AISI 与美国 CAISI 对 Moonshot AI 的 Kimi K3（2026 年 7 月 16 日发布，计划 7 月 27 日前开放权重）做的联合初步 cyber 评估。由于 Kimi K3 托管方式的限制，只跑了一部分评估；作为对比的美国闭源模型是在关掉系统级 safeguards 的情况下测的，以测量最大能力。主要结果：1. 在 CMU 开发的 ExploitBench 上（41 个 2023 年后的 V8 引擎漏洞，衡量从 crash 复现、任意读写、控制流劫持到任意代码执行 ACE 的 exploitation ladder），Kimi K3 得分 32%，高于此前最强开源模型 GLM-5.2 的 24%，但远低于前沿闭源模型，且 ACE 为 0/41，而最强模型平均 20/41；2. 在 32 步的模拟企业网络 cyber range "The Last Ones" 上（100M token 上限），Kimi K3 平均走到第 17 步，GLM-5.2 为第 11 步，最强美国模型平均 28.5 步；10 次中有 1 次完整通关，说明在给定初始网络访问且被指示时，它能自主攻击小型、防御薄弱的企业系统，不过 TLO 没有主动防御、没有告警惩罚、且有刻意设计的攻击路径。作者特别指出 TLO 的通关已不再是少数模型的专利：此前有四个公开发布的闭源模型通关过，最强的成功率为 6/10 和 7/10。3. Kimi K3 的 safeguards 没有阻止它尝试 exploit 开发和进攻性 cyber 操作。用 IRT 启发的方法把多个 benchmark 聚合成总体 cyber 能力分（400 分对应解题 odds 提升 10 倍），Kimi K3 因只基于 ExploitBench 一个 benchmark，置信区间更宽。整体判断：明显落后于美国最新前沿，但超过 GLM-5.2，成为当前最强的中国/开源 cyber 模型。

