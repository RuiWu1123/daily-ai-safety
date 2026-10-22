---
title: "Thoughts on the conservative assumptions in AI control"
lab:
  - "Redwood Research"
date: 2025-01-17
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/thoughts-on-the-conservative-assumptions
star: false
tags:
  - 监控与控制
---

# Thoughts on the conservative assumptions in AI control

**来源**：Redwood Blog · 2025-01-17 · [原文](https://blog.redwoodresearch.org/p/thoughts-on-the-conservative-assumptions)

## 简读

作者反思 Redwood 的 control 工作（原始 control 论文、adaptive deployment、防 collusion 那篇）中常用的一组保守假设：AI 始终在试图颠覆安全措施；擅长战略推理，而且可以完全不可读地推理（比如在单次 forward pass 里）；所有实例能执行协调一致的策略；确切知道用了哪些安全措施；很了解输入分布；能完美地选 Schelling point；能以极好的校准执行随机策略（比如以 0.01% 的概率攻击）。他承认大部分 misalignment 风险未必出现在这些假设全都成立的世界里，最早的灾难性风险很可能来自不够胜任、不够连贯的模型。唯一不做的保守假设是"模型能任意好地执行动作"：control eval 会实际测量 red team 构造的攻击策略有多少比例能过关，而不是因为存在致命动作就宣布 safety 为零；red team 在构造攻击策略时有大量便利（看输入分布、对 trusted monitor 迭代、用博弈论算最优攻击率），但看不到实际评估用的输入。作者认为应该叫它"black-box plan-conservative control evaluations"，当初把 control 叫作 control eval 并且把"最小化 P(doom | scheming)"与这套保守评估混为一谈是个错误。为什么还要坚持这些假设：1. 困难世界是可能的，AI 会从预训练数据和工作所需的训练中知道公司的大量情况，能从被替换的动作等迹象推断安全措施；推导这类策略一个 IQ 140、懂博弈论的人一小时内往往就能做到，模型可能在 forward pass、opaque latent recurrence 或隐写中完成；Schelling game 能力在专家水平下难说；而且针对 scheming 的训练会把概率质量从无能的 schemer 推向能干的 schemer。2. 这些属性很难评估：校准失败率很容易被训练出来，测 Schelling point 能力的训练本身会大幅提升它，攻破 control 的策略类别可能太少、无法检验泛化；相比之下测模型能否执行给定攻击计划只是一个较直接的能力评估（需防 sandbagging，也要防评估本身在教新技能）。3. 方法论干净：一个简单的 red-team/blue-team 游戏就隐含了所有假设，允许开发者用"某些假设不成立"来论证安全，会让有缺陷甚至 cherry-pick 的论证更容易，保守假设也便于制定难以钻空子的监管标准，类似密码学的 Kerckhoffs 原则。缺点：仍然逃不开方法论上的麻烦，比如判断模型是否 trusted 很混乱，red team 若用对抗样本找到通用 jailbreak 教给模型，攻击策略可能强得不现实；会低估依赖假设不成立的技术，比如 untrusted monitoring、coup probes 等白盒方法和 behavioral red-teaming，作者建议大部分时间做保守分析，再临时上调这些技术的权重；评估还要求离谱的博弈论求解，adaptive deployment 论文要靠 GPU 数值优化求 Nash equilibrium，模型显然不可能在脑子里算出来，但"假设它选最优策略"仍是最有原则、最难被 Goodhart 的选择。作者现在认为约一半的 control 研究应采用这些假设，比一年前热情低，主要因为他不再认为 AI 公司会被要求做出可读的 safety case：他预计（>50%）如果五年内出现超人 AI，没有一家领先公司会执行有可读证据显示能把灾难风险压到每年 1% 以下的计划。今后他会同时做保守和不那么保守两个意义上的 control 研究。

