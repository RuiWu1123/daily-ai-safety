---
title: "Misalignment and Strategic Underperformance: An Analysis of Sandbagging and Exploration Hacking"
lab:
  - "Redwood Research"
date: 2025-05-08
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/misalignment-and-strategic-underperformance
star: false
tags:
  - 故意藏拙
  - 威胁建模
---

# Misalignment and Strategic Underperformance: An Analysis of Sandbagging and Exploration Hacking

**来源**：Redwood Blog · 2025-05-08 · [原文](https://blog.redwoodresearch.org/p/misalignment-and-strategic-underperformance)

## 简读

未来要把强 AI 用在关键任务上：安全与安全 R&D、危险能力评估、red-team 安全协议、监控其他模型。若模型 misaligned，就可能 sandbagging，即故意表现差。这与通常的 misalignment 论证方向相反：reward over-optimization 和 scheming 的担忧都基于"训练会让模型在你的度量上表现好"，而 sandbagging 要解释这条论证为何失效。文章自成体系地梳理了相关动态。sandbagging 特别有害的场景包括：危险能力评估（high-stakes control safety case 需要红队从 untrusted model 引出强而隐蔽的攻击，schemer 有动机藏起攻击能力）、AI 做安全研究、untrusted monitoring（故意漏报，或藏起合谋能力）、生成训练信号（Constitutional AI 式的奖励、Deliberative Alignment 式的示范）。区分两类：隐藏已有的潜在能力，以及故意不学会我们想教的能力（not living up to potential）。训练让 sandbagging 难很多：1. 有接近部署分布的高质量 off-policy 示范时，直接微调就能消除 sandbagging，可能是 sandbagging 认知被选掉，也可能只是局部适应但在同分布评估上同样不再 sandbag，能保证引出的水平是数据所示能力与模型模仿能力中的较小值；局限是 AI 的最优策略可能与人类很不同（比如特殊的分解或 CoT 方式），schemer 可以专门在这些 AI 独有的路径上 sandbag。2. 推理模型的长 CoT、长时程 agentic 任务、GAN 式训练 untrusted monitor、debate，以及任何想超越人类的场景，都只能靠 on-policy 数据；模型若在 sandbag 时犯错，RL 就能强化高奖励行为，password-locking 论文提供了初步证据。3. 核心问题是 exploration hacking：模型故意不去探索高奖励动作，让 RL 无从强化。当模型已经知道高奖励动作是什么、且该动作与低奖励动作差别足够大时最容易做到，例如预训练时发现了 Linux zero-day 却永远不提、不暴露合谋信号；不知道哪个动作好时也可以采用"低熵"策略，固定走一条路，让它和 RL 都学不到哪个更好；高低奖励动作相似时还得避开会梯度相关地连带提升最优动作的次优动作。对策方面，混入少量 off-policy 数据（人工写的高质量 CoT 片段、trusted model 能完成的子任务和任务分解、人类参与的 debate、用 trusted model 数据初始化 GAN）有希望不仅在这些输入上生效，还改变"要不要普遍 sandbag"这个全局决策节点，形成良性循环，比如先把 trusted model 的 Best-of-N 表现蒸馏进来。关键 crux 是模型会不会只学会识别 off-policy 分布并把它当作局部例外：模型无状态、要在单次前向中一致地完成这件事并不容易，但 off-policy 数据若明显低于其能力或容易认出非自己生成，就很好识别，模型甚至能通过粗糙的 gradient hacking 学会这种区分；而 neuralese 推理模型可能会完全失去 off-policy 微调这一手段。其他对策的快速看法：检测 sandbagging 以定罪，作者对能否拿到确凿证据、拿到后能否用上都悲观，所以视训练为主要对策；ensembling 让多个 untrusted 模型同时探索，一个探索到高奖励就可以拿来训练其他，对低熵策略尤其有效；fuzzing internals 便宜值得试，但初步结果是负面的。结论：难度高度依赖任务；模型明确知道自己要避开哪些动作时最难防，所以对让模型暴露合谋信号比较悲观；反直觉的是，模型自己还不知道高奖励动作时 exploration hacking 反而很难，所以对 not living up to potential 不太担心（但这类对策可能在危险能力评估中意外教会模型新东西）；很多对策依赖模型犯错和样本效率。若推理模型走向 neuralese，exploration hacking 会难得多。作者认为对 exploration hacking 的实证研究重要、困难但可行。

