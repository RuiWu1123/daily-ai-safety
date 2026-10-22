---
title: "Introducing the Conceptual Reasoning Index"
lab:
  - "Anthropic"
date: 2026-08-12
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/conceptual-reasoning-index/
star: false
tags:
  - 评估方法
  - 可扩展监督
---

# Introducing the Conceptual Reasoning Index

**来源**：Anthropic Alignment Science Blog · 2026-08-12 · [原文](https://alignment.anthropic.com/2026/conceptual-reasoning-index/)

## 简读

背景是管理 AI 风险的一个核心希望是让 AI 帮我们理解处境、规划和设计缓解措施，而且一旦 AI 能做专家级的降风险工作，其产出可能远超人类，所以关键是这类能力能否早于高风险能力被自动化。但现有训练依赖丰富数据和可靠反馈，模型在不可验证的任务上普遍更弱，而 AI safety 恰好充满这种任务：要推理比任何人都强的 AI、有些事必须一次做对、很多决策反馈周期太长、有些问题（AI 该有什么价值观）根本没有 ground truth。作者（Redwood Research 与 Anthropic 合作）把这种依赖论证、缺乏可验证答案的能力称为 conceptual reasoning，构建了三个 benchmark 并汇总为 Conceptual Reasoning Index（CRI）：1. LMCA，560 篇立场文本、1,461 条反驳论证，几乎全部由 Emery Cooper 按详细 rubric 打分，部分有第二人独立评分（共 2,140 个评分），衡量模型给论证打分与专家的一致程度；人际一致性明显高于人机一致性，其中约 50 条验证集每条由 4–6 人独立评分并讨论了 7–8 小时；也可以用来评估生成论证的能力（让模型 B 在 few-shot 已评分论证的基础上给模型 A 新写的论证打分，效果较准），但这部分暂未计入 CRI；2. ACCoRD，测模型在概念问题上报告的信念/偏好是否逻辑一致（比如不同实例给出的 P(A) ≥ P(A&B)），约 14,000 条模型生成的约束、18 种类型，只有人工核过的 567 条进入 CRI；3. DTBench capabilities，407 道手工多选题，考察涉及对自身行为的忠实预测或与（近似）副本互动的决策论推理，主要由 Caspar Oesterheld 原创、Emery Cooper 独立验证，另有 130 道测决策论态度的题不计入。CRI 权重为 LMCA 60%、ACCoRD 20%、DTBench 20%，0 为随机、100 为满分；因人类评分噪声 LMCA 最优约 85，故 CRI 估计上限约 91。截至 2026 年 8 月最高的是 Opus 5，73.6（±2.1），仍远低于上限；Fable 5、Muse Spark 1.2、Gemini 3.6 Flash 这些在许多外部 benchmark 上领先的模型在 CRI 上并不最强（Fable 5 拒答时用 Opus 5 补位）。自 2024 年底以来分数大致线性上升、没有放缓迹象；粗略外推 LMCA 约一年后开始饱和，DTBench 已接近天花板（Fable 5 答对 98%），ACCoRD 何时饱和很不确定。作者的立场是概念推理对降风险工作尤其关键，值得有选择地提升。LMCA 需申请获取，网站 conceptualreasoning.ai 会持续更新分数并加入新 benchmark、淘汰饱和的。

