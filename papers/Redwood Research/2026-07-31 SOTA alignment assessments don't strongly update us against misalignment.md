---
title: "SOTA alignment assessments don’t strongly update us against misalignment "
lab:
  - "Redwood Research"
date: 2026-07-31
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/sota-alignment-assessments-dont-strongly
star: false
tags:
  - 对齐审计
  - 评估感知
  - 威胁建模
---

# SOTA alignment assessments don’t strongly update us against misalignment 

**来源**：Redwood Blog · 2026-07-31 · [原文](https://blog.redwoodresearch.org/p/sota-alignment-assessments-dont-strongly)

## 简读

起点是 Anthropic 在 4 月的 Mythos Preview alignment risk update 里得出模型"没有会增加 alignment risk 的未知倾向"，论证核心是"如果它 coherently misaligned，评估大概率能发现"，即评估的 reliability（作者定义为 recall）。作者同意结论（主要基于先验），但认为支撑 reliability 的证据偏弱，现在问题不大，但会让一年后的评估站不住。框架上用 METR 的 Means/Motive/Opportunity：评估对 Motive 的后验更新要成立，需要模型没有逃避检测的能力，且训练没有意外把 misalignment 变得难测。验证 reliability 有两条路，作者逐一指出问题：1. 测 anti-auditing 能力（eval awareness/metagaming、CoT controllability、opaque reasoning、secret keeping、careful and decisive action、rare action 等），但这些 eval 恰恰可被所测能力本身破坏：Mythos Preview、Opus 4.6 有不小的 unverbalized eval awareness，OpenAI 报告 RL 中 metagaming 上升，Meta 的 Muse Spark 是 Apollo 测过 eval awareness 最高的模型；用真实生产/内部数据可以缓解，但 covert capability 这类 eval 天然是罕见分布，没法这样做。另外 SHADE-Arena、secret-password 等把需保密信息放在 prompt 里，且（Opus 4.8 之前）没有 task-specific fine-tuning，OpenAI 的 CoT controllability eval 也没有，UK AISI 发现换 prompt 能把 Fable 的 controllability 从 20.2% 提到 62.3%，说明普遍 underelicited。sandbagging 也排除不了：熟练的 sandbagging 未必需要外化推理，而 sandbagging propensity eval 里模型同样高度 eval-aware（GPT 5.5 在 Apollo 测试中 52% 的样本有中等以上 eval awareness、几乎不 sandbag），作者建议新增 "sandbagging calibration" 能力评估，目前没有任何开发者报告过。2. auditing game：多数 MO 没针对检测做优化，规模也不清楚是否可比；Mythos 报告里最新一次 auditing game 甚至没抓到一个没被训练去混淆的 MO（虽然它借助了人类设计的红队策略，且只在跨上下文共享外部 memory 的部署场景中作恶）；AuditBench 显示有 "tool-to-agent gap"，而未来审计会越来越全自动化，但它也给了一些正面证据。3. 一个较少被提到的论点：alignment 训练和 alignment 评估的弱点是相关的，一个能熬过训练 oversight 的 schemer 正好被选择出 situational awareness、secret keeping、opaque reasoning 等能力，所以条件于 misaligned 时应调高其 covert capability 估计，开发者却在用无条件估计，从而高估 likelihood ratio。结论：当前评估只提供对 misalignment 的弱更新，对现在的模型够用（靠低先验和部署后观察），对一年后的前沿模型可能不够，呼吁开发者更清楚地说明 reliability、做更好 elicit 的 covert capability eval，并给外部评估者更多访问权限；作者表示后续会另写一篇谈具体改进。

