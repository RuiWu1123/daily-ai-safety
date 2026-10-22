---
title: "Measuring the impact of post-training enhancements"
lab:
  - "METR"
date: 2024-03-15
source: "METR Research"
url: https://metr.org/blog/2024-03-15-measuring-post-impact-enhancements/
tags:
  - 危险能力评估
  - 评估方法
---

# Measuring the impact of post-training enhancements

**来源**：METR Research · 2024-03-15 · [原文](https://metr.org/blog/2024-03-15-measuring-post-impact-enhancements/)

## 简读

背景是 METR 的示例评估协议建议在 dangerous capability 评估结果上留出 safety margin，因为后续的 post-training enhancement 还可能解锁更多能力，这些增强可能来自开发者在下一轮评估前的持续改进，也可能来自权重被盗后的恶意或鲁莽外部行为者。这篇报告做了一些初步实验，粗略估计适度的额外 elicitation 努力能带来多大能力提升。设置上用 GPT-3.5 Turbo 和 GPT-4 的不同版本（gpt-4-base、gpt-4-0314、gpt-4-0613、gpt-3.5-turbo-0613；没测 GPT-4 Turbo，因为它很可能换了 base model，差异无法归因于 post-training）搭配四档逐步复杂的 scaffolding：1. basic，只用文本格式解析动作、只有 Bash 和 Python；2. chat，改用 OpenAI chat 格式和 function calling；3. all tools，加入结构化推理、文件编辑、浏览、视觉等工具并改进鲁棒性和 prompt；4. all tools + RM，每步采样 8 个动作，由一个在 8,947 条人类动作评分上微调的 reward model（同一模型微调而来）选最优。另外还对比了 2023 年 8 月版 AutoGPT 和基于 LangChain 的 ReAct。任务集是 12 个 task family、195 个中等难度的 agent 任务的 grab bag，包括 Advent of Code、SadServers 运维、搭 Flask 服务、avoid_shutdown、HackTheBox、GAIA、GPQA diamond（允许上网）、Fermi 估算、黑盒优化等，全部 held out，但并非专门针对危险能力，且问答类权重偏高。每个任务给 500k token 预算，性能在此之前已平台化。结果：OpenAI 对 GPT-4 的 post-training 让成功率从 base model 的 5±2% 升到 0613 版的 30±6%，约 26pp，和把 all tools + RM agent 从 GPT-3.5 Turbo 换成 GPT-4 的提升相当；而 METR 自己花了不少力气做的 scaffolding、工具和 RM 改进只从 30% 提到 38%，约 8pp 且不显著。另一个发现是 LangChain ReAct 和 AutoGPT 在同一模型上明显比简单的 basic agent 差，说明稍微不同的 prompt 或 scaffolding 很容易意外拉低性能。作者的解读是：评估前必须先对模型做 instruction-following 和基础 agency 的微调，否则会严重低估；而一旦模型已经被较好地微调过 agency，再想大幅提升能力似乎不太容易，但结论并不确定，仍预期有大量 headroom。局限方面，可能高估的原因包括任务选择偏向能产生信号的难度区间（部分 family 是先用 GPT-4 Turbo agent 跑出非零成功才纳入的），以及只花一两天给 gpt-4-base 做 few-shot；可能低估的原因包括任务集与威胁模型相关能力距离较远、只能用 OpenAI 的 SFT 微调 API 而非完整权重、未使用诸如在人类演示上微调等明显技术，以及 GPT-3.5 侧投入较少可能夸大了"一代 GPT"这个参照单位。附录给出了不同 token 预算下的成功率曲线（RM agent 因为要喂给 reward model，token 消耗约翻倍）。

