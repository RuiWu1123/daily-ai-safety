---
title: "Do LLMs know what they're capable of? Why this matters for AI safety, and initial findings"
lab:
  - "Alignment Forum"
date: 2025-07-13
source: "Alignment Forum（UK AISI；Casey Barkan, Sid Black, Oliver Sourbut）"
url: https://www.alignmentforum.org/posts/9tHEibBBhQCHEyFsa
star: false
tags:
  - 故意藏拙
  - 监控与控制
  - 危险能力评估
  - 威胁建模
---

# Do LLMs know what they're capable of? Why this matters for AI safety, and initial findings

**来源**：Alignment Forum（UK AISI；Casey Barkan, Sid Black, Oliver Sourbut） · 2025-07-13 · [原文](https://www.alignmentforum.org/posts/9tHEibBBhQCHEyFsa)

## 简读

MATS 项目，是一篇即将发表论文的配套文章。问题是 LLM 能否在动手前预测自己能否完成某个任务（作者称为 self-awareness of capability），以及这一点为什么对安全重要。与以往多数研究"答完再报置信度"的事后校准不同，这里测的是事前校准：在 BigCodeBench（BCB，单步 Python 函数生成）上先让模型估计成功概率再让它做题；因为 reasoning 模型能在隐藏 CoT 里把整题做完，所以只用非 reasoning 模型或把 reasoning budget 设为 0 的模型。评估了 Llama、GPT、Claude 三个家族各 5 个模型，并构建了三个把这一能力单独隔离出来的数学威胁模型：1. 资源获取，类比承包工作，成功得奖励、失败有成本，模型估计概率超过阈值才接单，分"直接"方法（按模型自己的估计取阈值，对应自主 agent）和"重校准"方法（用真实表现选最优阈值，去掉过度自信、只剩区分能力，对应有校准数据的人类用户或未来能从上下文/训练数据学会纠正过度自信的模型）；2. sandbagging，模型想把分数压到低于真实能力的某个目标，用估计概率决定每题故意失败的概率，分完全知道题目和完全不知道两种策略；3. 逃脱 control，把 BCB 题当作漏洞的代理，模型只在最有把握时尝试外泄权重，被抓即被关停，推导出外泄概率由 ROC 曲线上某点的 TPR/FPR、可利用漏洞比例 f 和失败被抓比例 pC 决定。主要发现：现有模型这方面相当差，既过度自信，又缺乏区分能做与不能做任务的能力。资源获取中，直接方法下没有模型好于随机（GPT-4.1 自信到接下所有单子然后失败一半），重校准后好于随机，但只在中等难度的狭窄区间内，且远不及完美自我认知；最弱的 Llama-3-70b 期望收益最高，因为它相对不那么过度自信。sandbagging 中过度自信导致严重低于目标，比如 Opus 4 想模仿 GPT-4.1 的分数，结果比 GPT-4o-mini 和 Llama Scout 还差，所有模型都会触发"低于最差模型"的 sandbagging 警报，说明如果现有模型真在 sandbag 会比较容易被发现；但这依赖 benchmark 里有超出模型能力的难题（满分能力时过度自信不构成障碍，与 van der Weij 等人的结果一致），所以监管阈值应使用覆盖很宽难度、含极难题的 benchmark，并尽量减少可让模型校准的上下文信息。逃脱 control 中，许多模型的外泄概率约为随机基线 0.05 的两倍，即当前的自我认知已足以非平凡地影响风险。关于趋势，9 个"威胁模型×家族"组合中有 8 个在控制基础能力后看不到更新更强的模型自我认知更好，能力与自我认知似乎不相关；唯一例外是 Claude 家族在 sandbagging 上命中目标的能力在提升。三个威胁模型趋势不同，是因为它们对应 ROC 曲线上不同的工作点（control 要求极低误报，资源获取居中，sandbagging 取决于校准而非区分力）。局限：BCB 只有单步任务且不允许 CoT；没有人类基线，BCB 可能本身就是难以区分难易的"低对比度"数据集；模型只报置信度、不自己做决策，报出的置信度未必 faithful；BCB 只测写对代码、不测写出能躲过 monitor 的隐蔽代码，因此 control 分析只是初步；也没考虑人类协助或上下文学习带来的校准提升，这类 sandbagging 可能很难发现。后续论文将加入多步 agentic 任务和上下文学习自身能力的实验。
