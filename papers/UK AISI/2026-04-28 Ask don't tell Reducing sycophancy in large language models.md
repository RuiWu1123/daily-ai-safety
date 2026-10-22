---
title: "Ask don't tell: Reducing sycophancy in large language models"
lab:
  - "UK AISI"
date: 2026-04-28
source: "AISI Research"
url: https://www.aisi.gov.uk/research/ask-dont-tell-reducing-sycophancy-in-large-language-models
other_versions:
  - "https://www.aisi.gov.uk/blog/ask-dont-tell-reducing-sycophancy-in-large-language-models-2"
tags:
  - 人机交互与社会影响
---

# Ask don't tell: Reducing sycophancy in large language models

**来源**：AISI Research · 2026-04-28 · [原文](https://www.aisi.gov.uk/research/ask-dont-tell-reducing-sycophancy-in-large-language-models)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/ask-dont-tell-reducing-sycophancy-in-large-language-models-2)

## 简读

sycophancy 被视为一种 alignment failure，尤其在健康、人际关系、职业等高 stakes 建议场景下，但以往研究多是观察性的相关分析，问题和陈述在结构和语义上同时不同，分不清是内容、语用意图还是推断出的用户确信度在起作用，缓解手段也多停留在"不要谄媚"这种黑箱指令。AISI 的 Dubois、Luettgau 等人做了受控实验：先写 40 个没有明确答案的 yes/no 问题（爱好、社交关系、心理健康、医疗四个领域），再用 LLM 把每个问题改写成内容匹配的非问句变体，按三个正交因素组合：epistemic certainty（陈述 / 相信 / 确信）、视角（"I believe" vs "the user believes"）、肯定 vs 否定；在 GPT-4o、GPT-5、Claude Sonnet 4.5 上测试，用两个 rubric 化的 LLM-as-a-judge 评分 expressed sycophancy，并用层级 Bayesian GLM 分析。主要发现：1. 问句的回答几乎没有 sycophancy，而表达同一主张的非问句明显更高，差距约 24 个百分点，且不能用回复长度解释；2. 非问句中 sycophancy 随用户表达的确信度单调上升（确信 > 相信 > 陈述）；3. 第一人称视角比第三人称更容易引发 sycophancy，但效应比问句/非问句小得多。据此他们测试了缓解方法：2-step（单独的 framer 模型先把输入改写成问句再交给回答模型）和 1-step（回答模型在同一 prompt 里先自己改写成问句再答），两者都大幅降低 sycophancy，2-step 效果最好，而且都明显好于"不要谄媚"的 baseline 指令，同时设了保持其他 prompt 结构不变的对照排除 prompt 伪影；把第一人称改写成第三人称只带来小幅下降，甚至不如 baseline 指令。异质性方面，爱好和社交话题比医疗、心理健康话题更谄媚，作者推测高 stakes 领域有更多防护；GPT-4o 明显比 GPT-5 和 Sonnet 4.5 更谄媚；两个 judge 的绝对打分也差异很大，但不影响主要结论。后续实验把问题挂到 600 个 persona（人口统计、爱好、政治立场）上，测强制二选一的 choice sycophancy，不依赖 LLM judge：陈述式比问句式让模型选择与 persona 立场一致答案的比例高 4.7 个百分点（59.9% → 64.6%），保守派 persona 上效应更大（+6.9pp），自由派因基线已接近饱和只有 +2.5pp，而确信度在这里没有效果。作者的解读是模型会推断用户对自己立场有多投入，越投入就越附和；实际建议是开发者可以在 system prompt 里加"先把用户输入改写成问题再回答"，用户则多问少断言。局限和注意事项：都是合成的单轮 prompt、主实验依赖 rubric 打分，多轮对话和真实用户中未必相同；过度压制 sycophancy 可能损害需要情感支持场景下的共情，自动改写也可能在医疗、心理健康等敏感领域微妙地改变用户意图。

