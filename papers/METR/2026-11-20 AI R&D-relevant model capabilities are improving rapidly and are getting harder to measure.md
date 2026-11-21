---
title: "AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure"
lab:
  - "METR"
date: 2026-11-20
source: "METR Blog"
url: https://metr.org/blog/2026-11-20-q4-2026-capability-update
star: false
tags:
  - 危险能力评估
  - 评估方法
---

# AI R&D-relevant model capabilities are improving rapidly and are getting harder to measure

**来源**：METR Blog · 2026-11-20 · [原文](https://metr.org/blog/2026-11-20-q4-2026-capability-update)

## 简读

背景是 METR 过去用 time horizon 指标给 AI 风险设上界：它测的能力被认为是造成灾难性风险的必要条件，有人类基线可对照，而且当时模型离危险阈值还很远；但 2025 年 3 月最强模型的 time horizon 只有约 1 小时，一年内模型就把包含长达 30 小时任务的 TH1.1 套件做饱和了，很多领域已经很难找到能超过模型的人类基线。这篇 2026 年第四季度的能力更新汇总了 METR 对公开模型（截至 Opus 5.5 和 GPT-6 Astra）与 AI R&D 加速相关能力的评估，核心态度是：现有公开证据不足以排除未来几年出现 drastic AI R&D acceleration，即能力提升快到人类无法再有效理解、评估和应对新系统的灾难性风险。主要发现：1. 在编码和有强反馈信号的指标优化任务上，模型通常达到或超过熟练的人类，METR 自己招募的基线测试者大多赢不了前沿模型；在有 10 人以上领域专家做过同一任务的少数情况下，模型排名很靠前，但不是第一。2. 他们引入模型估计的"Lifecycle Cost"（把任务做成 RL 环境、运行和打分的成本）来刻画评估的真实程度，发现同等任务长度下，lifecycle cost 翻倍带来的难度惩罚大致相当于 time horizon 减半，但高成本和低成本任务上的进步速度相近，最贵的任务上表现也在持续提高。3. 在缺乏清晰实证反馈的任务上（反馈周期长、或测试难以证明方案能泛化），agent 的判断力不如人类专家；例如有一个任务里，模型当评审时会高估同等或更强模型产出的质量。4. TH1.1 和更难的 TH2 合并后，time horizon 大约每 3.6 个月翻一番，与 OpenAI 最近报告的内部研究任务趋势相近；只看 TH2 中可验证子集时翻倍更快，可能意味着近期加速被合并趋势掩盖，但也有别的解释。5. 用基于 IRT 的 METR Capability Index（MCI，类似 Epoch 的 ECI）跟踪公开前沿模型，没有看到整体加速或减速，但在某些条件下看到不确定的、个别开发者的趋势变化，结论对方法选择敏感。稳健性部分检查了 reward hacking 和拒答，并发现 agent swarm 作为 elicitation 手段在有明确指标和快速反馈的可验证任务上比 best-of-k 有效，在其它任务上效果不明或为负。讨论部分承认，过去靠指出"某种容易测量的广泛无能力"来给风险设上界的办法已经失效，风险判断越来越依赖能力画像的细节和关于现实世界的事实，而 METR 对几个关键问题没有好答案：更难验证的任务上能力弱多少、进步是否更慢，以及 drastic AI R&D acceleration 究竟需要哪些能力；他们认为应当考虑仅靠容易验证的任务就能大幅加速 AI R&D 的可能性，何况开发者正在主动让 AI 自动化自己的研究。附录包括难度估计与人类基线、Al Zimmermann 编程竞赛、Budget NanoGPT、持续学习等任务案例。
