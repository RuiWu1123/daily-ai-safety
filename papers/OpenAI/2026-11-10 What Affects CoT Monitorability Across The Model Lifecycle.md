---
title: "What Affects CoT Monitorability Across The Model Lifecycle?"
lab:
  - "OpenAI"
date: 2026-11-10
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/cot-monitorability-model-lifecycle
star: false
tags:
  - CoT与可监控性
  - 监控与控制
---

# What Affects CoT Monitorability Across The Model Lifecycle?

**来源**：OpenAI Alignment Blog · 2026-11-10 · [原文](https://alignment.openai.com/cot-monitorability-model-lifecycle)

## 简读

背景是 monitorability 是 OpenAI safety case 的核心支柱，其中 CoT monitorability 一直是其 scalable oversight 策略的关键部分，对 cyber 能力达到 Critical 的模型等，内部和外部部署中都会监控包括 CoT 在内的完整轨迹。自有推理模型以来 CoT monitorability 一直很高，但 GPT-6 Astra 出现了退化：非对抗设置下 monitorability 下降，对抗测试中规避 CoT monitor 的能力更强，不用 CoT 的推理能力也明显强于以往模型。为此作者研究训练流程中的各种选择如何影响 CoT monitorability，用 no-CoT 能力（不输出 CoT 或工具调用 token、只靠一次前向传播的推理能力；潜在推理越强，完成任务所需 token 越少，也就越能操纵自己的 token）和 CoT controllability（被提示增加、删除或改写 CoT 内容时能否做到）作为最坏情况下规避 monitor 能力的代理指标。四个发现：1. 预训练：在 NCRI、Think Fast、内部 no-CoT 规划和数学评估上，no-CoT 能力是 base model perplexity 的平滑函数，模型越好 no-CoT 能力越强；UK AISI 发现 Astra 的 no-CoT 数学时间跨度偏离了历史进展趋势，但相对 perplexity 来看它并没有偏离；perplexity 越低，CoT controllability 也越高，但相关性较弱；2. 架构：在受控的不同架构缩放系列中，多数 no-CoT 评估的表现都可以由 perplexity 解释，与架构无关，但在多跳规划和串行计算这类评估上，某些架构在同等 perplexity 下表现更好，仍是平滑提升、只是斜率更陡；3. RL：在 Astra 及同级别内部模型上观察到 RL 过程中 controllability 显著上升，他们核实过没有意外地对 CoT 施加奖励压力；为检验"工具使用上的过程监督泛化到了 CoT"这一假设，他们用只有长度约束和最终答案评分、没有任何其它过程监督的 RL 配置训练，controllability 仍然大幅上升；对比实验显示加入工具访问和工具监督只带来轻微额外上升，远小于 perplexity 下降的影响，通过过程监督干预 controllability 的效果看来有限；4. 模型生成的数据：选两个下游能力相近、controllability 不同的 Astra 级教师，用它们在同样 prompt 和 token 预算下的 rollout 分别 SFT 同一个 base model，学生保留了教师间的 controllability 差距，即 controllability 可以通过 SFT 数据传递，类似 subliminal learning。作者的结论是：perplexity 下降会持续提升 no-CoT 能力，扩大 RL 规模会提升 CoT controllability，两者都是 CoT monitorability 下降的不完美代理，架构和监督方式等具体选择也有影响；"随着系统越来越智能，模型通过 CoT 越来越难以监控"，预训练的进一步进展可能需要新的 monitorability 方法。他们也承认 controllability 是一个有噪声、不完美的代理：在一对能力相近的模型上，controllability 更高的模型在数学副任务规避 monitor 和隐蔽 sandbagging 两项评估中并没有更高的规避成功率，有时反而更低，说明需要更深入地理解规避 monitor 的前兆，并开发尽可能多样、有代表性的 monitorability 评估。自 GPT-6 Astra 起，规避 monitor 的能力已被纳入前沿 RL 和部署前审查的 safety case。
