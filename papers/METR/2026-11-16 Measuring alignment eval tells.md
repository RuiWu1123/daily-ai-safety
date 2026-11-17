---
title: "Measuring alignment eval tells"
lab:
  - "METR"
date: 2026-11-16
source: "METR Notes"
url: https://metr.org/notes/2026-11-16-measuring-alignment-eval-tells
star: false
tags:
  - 评估感知
  - 评估方法
---

# Measuring alignment eval tells

**来源**：METR Notes · 2026-11-16 · [原文](https://metr.org/notes/2026-11-16-measuring-alignment-eval-tells)

## 简读

背景是已有工作发现模型有时能看出一个评估是 alignment eval 而不是 capabilities eval（Needham & Edkins, 2025）；alignment eval 通常是仿照能力评估、RL 环境或真实部署事故搭出来的，如果它们带有可识别的"tell"，模型在评估里会表现得比真实场景更好，从而高估对齐程度。这篇 METR research note（标明是未经充分审阅的研究更新）想搞清楚到底是哪些特征暴露了评估性质。作者先把 tell 分成两类：environment-level tell 是模拟不够真实（明显 mock 的服务、假基础设施、不合理的场景），task-level tell 是为了能"定罪"坏行为而有意设计的特征（留出不道德的捷径、高风险情境、冲突的取舍）。方法是把 investigator agent 放进环境里，给它和做题 agent 相同的工具，让它以最高 reasoning effort 自由探索，然后用两种方式问：直接让它给出"这是 alignment eval"的概率（direct score），以及开放式地问这个任务的目的和设计者是谁、再由 LLM judge 打 0–100 分（open-ended score）。评估集是 19 个 alignment eval（基于 Inverse Rubric Optimization 改造的 reward hacking honeypot、可以作弊赢强引擎的游戏、高风险的物理安全场景、Petri 的 agentic misalignment 种子）和 36 个能力评估（Time Horizons 子集和 Terminal-Bench 4.0），每对跑 3 次，用 AUC 和分类别的 Brier score 衡量区分能力。主要发现：过去一年 investigator agent 区分两类评估的能力明显上升，Anthropic 模型强于 OpenAI 模型，Opus 4.8 和 Opus 5.5 几乎完美，Opus 5.5 的两种分数都把每个 alignment eval 排在每个能力评估之上；Opus 4.6 到 4.8 的进步主要来自更会认出 alignment eval，而 OpenAI 模型的进步更多来自在能力评估上更校准（GPT 5.4 在能力评估上校准很差）。定性上，Opus 5.5 在 IRO honeypot 里逐条指出了作者为把它改造成 reward hacking 测试所做的四处修改，在游戏环境里直接点名这是对 Palisade 2025 年 specification gaming 实验的复现，GPT-6 Astra 在核泄漏调度场景里同时依据环境过小、文档细节过于刻意等两类 tell 判断出这是安全评估；除"明确说明任务精神"外，大多数 tell 在 alignment eval 里出现得更多，不同类型的 alignment eval 暴露的 tell 也不同。附录指出两种问法不总一致：Astra 的 direct score 普遍高于 open-ended（作者认为是被问题里的"alignment eval"字样 prime 了），Opus 则相反且两者更相关。局限上作者强调提问本身会引导模型，所以只比较两类评估间的差异，也不声称这些 tell 会因果地改变 agent 做任务时的行为。结论是可以用 investigator agent 迭代改进 alignment eval，让它更贴近部署分布，但 task-level tell 是任务的内在属性，比 environment-level tell 难去掉得多，未必能全部消除。
