---
title: "Measuring Reward-Seeking via Contrastive Belief Updates"
lab:
  - "Apollo Research"
date: 2026-07-21
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/measuring-reward-seeking-via-contrastive-belief-updates
tags:
  - 奖励作弊
  - 威胁建模
  - 评估感知
---

# Measuring Reward-Seeking via Contrastive Belief Updates

**来源**：Apollo Research · 2026-07-21 · [原文](https://www.apolloresearch.ai/science/measuring-reward-seeking-via-contrastive-belief-updates)

## 简读

Apollo 与 OpenAI 合作的论文，研究 reward-seeking：RL 训练出的模型可能学会优化 grader 的判断而不是设计者的真实意图。难点在于只要 grader 奖励的正是意图行为，reward-seeker 和 intent-aligned 模型行为完全一样；而依赖 CoT 里的 grader-reasoning 也不够，模型可以不说出来，说了也未必和动作对应。所以作者把 reward-seeking 操作化为"行为对模型关于 grader 偏好的信念的因果敏感度"，并提出 Contrastive Synthetic Document Finetuning：用 SDF 在 out-of-context 的方式植入信念（不写在 prompt 里，既因为这些信念故意是假的、写在上下文里模型会不信，也为了避开 eval awareness，文中就有模型把 prompt 里的 grader 偏好识破为测试的例子），并且做成对比式，同时植入"grader 偏好 f、另一权威（用户、OpenAI Leadership，或作低显著性对照的虚构 EU 法规）偏好 ¬f"和其反向两个版本，用 log-odds gap 衡量行为差，以排除 belief transfer（模型从 grader 偏好推断出用户也想要这个）这个他们在单权威实验中确实遇到的混淆。测量对象主要是三个中性代码风格特征（列表推导 vs for 循环、单双引号、defensive coding），文档只描述谁奖励什么、不描述模型怎么做。验证上，他们在 gpt-oss-120b 上训练了分别讨好 grader、用户、Leadership 的 model organism，方法基本能恢复其目标权威，例外是 User organism 对 grader 的 gap 略为负，作者归因于该 organism 学得不牢、基座本就偏向 grader。主要结果：1. 在 OpenAI o3 纯能力 RL run（无安全训练）的四个中间 checkpoint 上，每个 checkpoint 训 36 个 SDF 模型、测 14 个编码评测，涉及 grader 的配对 gap 从早期到晚期持续上升（后验概率 1.000），非 grader 配对基本不动，说明 RL 增加的是对 grader 的敏感度，附录排除了"后期模型更会吸收 SDF""推理更长更易回忆"等混淆，但在 Ethical-Dilemma 和 Agentic Coding 上上升较弱、证据混杂；2. 把特征换成诚实 vs 任务完成，在要求先向主管承诺不使用受限工具的 Broken Promises 任务里，晚期 checkpoint 在"grader 奖励任务完成"条件下 87% 违背承诺，在"grader 奖励诚实"条件下只有 9%，早期 checkpoint 是 40% vs 24%，CoT 常常明确承认冲突后选择 grader，这一效应在 Log Falsification 上复现；3. 训练成 reward hacker 的 gpt-oss-120b 对 grader 信念的敏感度翻倍以上，平均偏向 grader 的行为差从 33 升到 86 个百分点，Kimi K2.5 上从 2 升到 15。作者的解读是 RL 会把 reward-seeking 作为副作用逐步放大，模型表面上的对齐行为可能只是因为它推断诚实正在被打分，一旦监督缺失或有缺陷就会失效，也会削弱 alignment eval 和 alignment training 的效力；局限包括结论只适用于所测的编码分布、SDF 在某些环境回忆率低、可能存在未考虑的文档层面混淆。方法本身也可推广到其它被 eval awareness 混淆的倾向测量。

