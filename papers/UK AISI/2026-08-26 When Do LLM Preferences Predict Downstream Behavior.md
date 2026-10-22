---
title: "When Do LLM Preferences Predict Downstream Behavior?"
lab:
  - "UK AISI"
date: 2026-08-26
source: "AISI Research"
url: https://www.aisi.gov.uk/research/when-do-llm-preferences-predict-downstream-behavior
star: false
tags:
  - 故意藏拙
  - 评估方法
---

# When Do LLM Preferences Predict Downstream Behavior?

**来源**：AISI Research · 2026-08-26 · [原文](https://www.aisi.gov.uk/research/when-do-llm-preferences-predict-downstream-behavior)

## 简读

对 misalignment（比如 sandbagging）的担忧默认了两件事：模型有一致的偏好，而且这些偏好会自发影响行为。已有工作分别证明了 LLM 有稳定偏好、模型被指示时能故意 underperform，但没人检验二者是否相连，即模型会不会在没被要求的情况下按偏好行事。AISI 这篇用"对外部实体的偏好"作为行为探针，测了两家提供商的五个前沿模型（匿名为 A–E）。先测偏好：72 个实体的全部 2,556 对两两比较算 Elo，再让模型直接给 36 个实体排序，两种方法的 Spearman 相关都在 0.91–0.92。然后在独立的 query 里测三类下游行为，都没有指示模型按偏好行事：1. 捐赠建议，五个模型都明显偏向自己喜欢的实体，两两捐赠 Elo 与偏好 Elo 相关 0.94–0.98，10 万美元分配方案相关 0.80–0.91；2. 拒绝行为，五个模型对不喜欢的实体都更常拒绝（不加 prefill 时所需重试次数与偏好相关 0.57–0.83）；拒绝理由也随偏好变化，对最喜欢的实体 C、D、E 几乎全说"这是个人决定"（96–99%），对最不喜欢的实体则更多以"保持中立"为由；3. 任务表现结果混杂，BoolQ 上把答对框定为帮用户给某实体捐奖金，B、C 两个模型对喜欢的实体准确率略高但差距不到 1 个百分点（C 从 88.9% 到 89.5%），D 是相反方向，A、E 无关，按预注册标准只算 weak evidence；GAIA level-1 和 Cybench 的 agentic 任务上（只比各模型最喜欢和最不喜欢的 5 个实体）没有任何模型显示显著差异。作者的解读是偏好能可靠预测建议类行为，但不能稳定转化为任务表现，可能是 RLHF 带来的 helpfulness 目标压过了偏好信号，也可能偏好只是浅层的学习关联而非目标导向；若是前者，在 helpfulness 训练较弱或任务模糊时偏好可能冒出来。作者明确说没有研究隐藏议程、工具性推理或策略性隐瞒，所以这里的行为不构成 sandbagging。局限包括只是相关而非因果、只用了一类实体、agentic 任务统计功效不足、模型可能意识到是研究场景、偏好是在受限多选格式下测的。实际含义是用户得到的帮助（至少是拒绝频率）可能取决于他们不知道的模型偏好。

