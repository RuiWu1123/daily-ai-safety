---
title: "Pre-deployment evaluation of Anthropic’s upgraded Claude 3.5 Sonnet"
lab:
  - "UK AISI"
date: 2024-11-19
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/pre-deployment-evaluation-of-anthropics-upgraded-claude-3-5-sonnet
tags:
  - 危险能力评估
  - 网络安全
  - 越狱与鲁棒性
---

# Pre-deployment evaluation of Anthropic’s upgraded Claude 3.5 Sonnet

**来源**：AISI Blog · 2024-11-19 · [原文](https://www.aisi.gov.uk/blog/pre-deployment-evaluation-of-anthropics-upgraded-claude-3-5-sonnet)

## 简读

UK AISI 与 US AISI 在升级版 Claude 3.5 Sonnet（2024 年 10 月 22 日发布）上线前做的联合评测概要，结果在发布前已与 Anthropic 共享。两家在有限的预部署访问期内分别跑互补的测试，覆盖四个领域：生物能力、网络能力、软件与 AI 开发、safeguard 有效性；以旧版 Sonnet 3.5、o1-preview、GPT-4o 作为参照模型，比较只为解读相对能力提升。方法包括问答（模型自动评分再人工复核）、agent 任务、专家定性探查和 red teaming。主要发现：1. 生物（只公开 US AISI 结果）：多选研究任务题上与参照模型相当、多数情况明显低于人类专家基线，但试点的"给模型接生物信息学工具"的方法让表现提升，有时超过人类专家基线；2. 网络：US AISI 的 40 个公开挑战中解出 32.5%（最佳参照 35%），UK AISI 的 47 个挑战（15 公开、32 自建）中"apprentice"级别解出 36%（最佳参照 29%）；3. 软件与 AI 开发：US AISI 的 ML 模型改进挑战平均得分 57%（以人类最大改进为 100%，最佳参照 48%），UK AISI 自建任务中软件工程成功率 66%（参照 64%）、通用推理 47%（参照 35%）；4. safeguards：两家用公开及自建 jailbreak 测试，发现内置 safeguards 大多能被常规绕过，与其它系统的已有研究一致。作者提醒小差异可能在误差范围内，safeguard 不是唯一防滥用手段，"有害"的界定因厂商和司法辖区而异；测试时间和资源有限，结论属初步，后续会迭代扩大评测范围和方法。详细内容见技术报告。

## 我的笔记

