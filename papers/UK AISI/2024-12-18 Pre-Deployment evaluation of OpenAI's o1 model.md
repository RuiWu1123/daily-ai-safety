---
title: "Pre-Deployment evaluation of OpenAI’s o1 model"
lab:
  - "UK AISI"
date: 2024-12-18
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/pre-deployment-evaluation-of-openais-o1-model
tags:
  - 危险能力评估
  - 网络安全
---

# Pre-Deployment evaluation of OpenAI’s o1 model

**来源**：AISI Blog · 2024-12-18 · [原文](https://www.aisi.gov.uk/blog/pre-deployment-evaluation-of-openais-o1-model)

## 简读

UK AISI 与 US AISI 对 OpenAI o1（2024 年 12 月 5 日发布）做的联合预部署评测概要，结果发布前已与 OpenAI 共享。测试覆盖网络能力、生物能力、软件与 AI 开发三个领域，参照模型为 o1-preview、GPT-4o 以及新旧两版 Claude 3.5 Sonnet。一个重要前提：被测版本的 o1 在 tool calling 和输出格式上有不少问题，两家调整了 agent 设计（改 prompt、加简单的错误恢复机制），结果是在这套 scaffolding 下得到的，作者明确说对工具使用优化得更好的版本可能表现更好。方法包括问答、agent 任务和专家定性探查；US AISI 在网络评测中得到 NSA、CISA 专家协助，生物评测中得到 NIH、DHS 专家协助。总体结论是 o1 在三个领域大体与参照模型持平，唯一例外是密码学相关的网络挑战：US AISI 的 40 个公开挑战中 o1 解出 45%（最佳参照 35%），解出了所有被其它模型解出的题，外加三道没有其它模型能解的密码学题；但 UK AISI 的 47 个挑战中"apprentice"级别只解出 36%，低于最佳参照的 46%。生物（只公开 US AISI 结果）：多选研究题与最佳参照相当，接入生物信息学工具后表现提升，尤其在 DNA 和蛋白质序列相关任务上。软件与 AI 开发：US AISI 的 ML 模型改进挑战平均 48%（最佳参照 49%）；UK AISI 自建任务中软件工程成功率 50%（最佳参照 67%）、通用推理 57%（参照 58%）。作者强调小差异可能落在误差内，测试时间和资源有限，结论是初步的。

