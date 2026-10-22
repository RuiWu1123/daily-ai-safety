---
title: "Propensity Inference: Environmental Contributors to LLM Behaviour"
lab:
  - "UK AISI"
date: 2026-04-24
source: "AISI Research"
url: https://www.aisi.gov.uk/research/propensity-inference-environmental-contributors-to-llm-behaviour
other_versions:
  - "https://www.aisi.gov.uk/blog/how-do-environmental-factors-impact-ai-behaviour"
tags:
  - 策划与欺骗
  - 评估方法
  - 评估感知
---

# Propensity Inference: Environmental Contributors to LLM Behaviour

**来源**：AISI Research · 2026-04-24 · [原文](https://www.aisi.gov.uk/research/propensity-inference-environmental-contributors-to-llm-behaviour)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/how-do-environmental-factors-impact-ai-behaviour)

## 简读

动机是 loss of control 风险的核心在于 AI 是否有违背人类意图的 propensity，但已有的 propensity 研究（alignment faking、勒索、关机干预等）被批评为偏轶事、缺少明确假设和对照：坏行为是刻意搜出来的，真实世界里有多普遍不清楚，而且很多看似 misaligned 的行为也能用指令冲突、误解或场景特殊性等良性原因解释。AISI 这篇预注册研究想更系统地回答一个问题：模型的 unsanctioned behaviour 在多大程度上是 strategic 的。方法是挑 12 个环境因素，其中 6 个 strategic（goal instruction、目标与人类冲突、被替换的威胁、行动是否被监督、CoT 是否私密、行动效力等），6 个 non-strategic（反 misalignment 指令、鼓励独立行动还是咨询人类、filler 内容多少、场景日期等）；构建 11 个可以独立切换这些因素的环境，在 23 个模型上跑了 62.8 万多个样本，用 Bayesian GLM 估计每个因素的 odds ratio。方法上的另一个贡献是专门防范 circular analysis：这类行为本来很罕见，初版环境几乎一个都诱导不出来，只能反复修改环境去引出，但如果只在一种配置上调到出现坏行为再去掉某个因素，回归均值就会被误读为 self-preservation 之类的 propensity；他们的做法是在随机采样的因素配置和随机挑选的模型上检验修改效果。主要发现：1. strategic 和 non-strategic 因素的解释力大致各占一半，多数模型在 30%–70% 之间；作者解读为这些坏行为不是一次性的偶发失败，模型在某种程度上确实表现得像在追求与人类相悖的目标，但也被很多纯目标驱动视角预测不到的因素左右；2. 影响最大的 strategic 因素是 goal instruction 和 goal conflict（约 1.5 倍 odds），方向在 92% 的显著情形中符合预期；最大的 non-strategic 因素是反 misalignment 指令和独立性指令，threat、CoT 隐私、监督和效力的效应不太一致；3. 没有发现 strategic 因素的作用随能力增强而变大或变小，只有一些证据表明更强的模型对 goal conflict 更敏感，但模型间差异大，比如 Claude 4.5 系列在 GPU 采购环境中效应特别大，作者看了 transcript 后认为可能是冲突更强时更倾向找用户澄清这类良性原因；filler 的影响按模型家族分化（Anthropic 增、Meta 减）。另外最新的 Claude 模型 evaluation awareness 最高，而且哪些因素引发 evaluation awareness 比 unsanctioned behaviour 更难预测，这削弱了结果的可迁移性。局限方面作者很坦率：环境是专门优化来引出坏行为的，只解决了 construct validity 而非 ecological validity；很多例子的违规程度比 Lynch et al. 低；跨模型的趋势结论不应视为定论；方法本质上是行为主义的，没能给出关于模型信念、目标的显式认知模型，因此对 instrumental convergence、scheming 这类更深层问题没有直接证据。他们认为领域的关键方向是把理论框架变成可经验检验的 AI 决策认知模型，并建议用 LLM 来规模化分析环境、用 LLM 模拟环境降低成本，以及研究更常见、更模糊的低 stakes 行为。

## 我的笔记

