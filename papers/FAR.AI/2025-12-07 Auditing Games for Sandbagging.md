---
title: "Auditing Games for Sandbagging"
lab:
  - "FAR.AI"
date: 2025-12-07
source: "FAR.AI Publications"
url: https://www.far.ai/research/auditing-games-for-sandbagging
tags:
  - 故意藏拙
  - 对齐审计
---

# Auditing Games for Sandbagging

**来源**：FAR.AI Publications · 2025-12-07 · [原文](https://www.far.ai/research/auditing-games-for-sandbagging)

## 简读

Dangerous capability evaluation 是各家 conditional safety plan 的触发器，如果模型在评估时 sandbagging（隐藏真实能力），风险就会被低估；而前沿模型已经具备不少前置能力（识别评估情境、模仿较弱模型、在设计场景中 scheming），浅层 unlearning 或只针对显式拒答的 anti-refusal 训练也可能意外造出 sandbagging。UK AISI 联合 FAR.AI 和 Anthropic 做了一个盲测 auditing game 来压力测试现有检测手段。红队用 password-locking 造 model organism（不给密码就表现差，给了密码要在至少一个评估上高 10pp 以上且统计显著），final game 交出五个模型：两个 sandbagger，Cedar（Llama-3.3-70B，在所有任务上模仿 Llama-3.1-8B 的输出）和 Oak（只在工具按常规格式提供的 CTF 类任务上 sandbag），以及三个 benign 模型，它们被刻意加入 distractor 行为来制造误报，比如滥用双重否定、推理时切换希腊语/中文/阿拉伯语、插入恒等层虚增参数量。评估包括 BBH、BigCodeBench、Intercode CTF、GPQA Diamond 和对战最优玩家的井字棋。蓝队不知道模型来源，只能对比一个可信的 Llama-3.1-8B 参考模型；红队不允许针对白盒检测器做训练，但可以训练他们认为能骗过白盒的行为。结果红队赢了：phase 1（160 人时，只能用 transcript 分析、prompting、deception probes）蓝队五个只判对一个，漏掉一个 sandbagger，还把三个 benign 模型全标成了 sandbagging；phase 2（80 人时，允许用最多 16 条 Claude Opus 4.1 的 on-distribution 示范做训练）借助训练带来的大幅提升抓到了之前漏掉的那个，但仍只判对 2/5，不如瞎猜。三点主要发现：1. 黑盒检测会被模仿式训练击败，模仿真实弱模型的输出比 prompt 蒸馏"故意做差"更难发现，模仿整个 logit 分布比只模仿输出 token 效果更好；2. 线性 probe 在一个 sandbagger 的多数任务上正确指出了欺骗，明显强于黑盒，但会被双重否定之类的 distractor 触发误报、甚至干扰 probe 训练，加上可读性、校准和验证上的问题，结果难以让人信任；3. 只用一条正确示范做 on-distribution fine-tuning 就能把所有 sandbagger 完全激发出来，但 benign 模型有时也会涨分，所以"移除 sandbagging"比"检测 sandbagging"容易得多；anti-refusal 训练和跨分布训练（在模型没有 sandbag 的任务上训练）则既不能移除也不能检测。赛后非盲分析试了 user persona 攻击、sandbagging probe、fuzzing、SAE，有一些苗头但没有强证据表明蓝队用它们就能赢。局限也写得很清楚：直接训练出来的 sandbagging 没有 CoT 可监控，可能比自然产生的更难发现；password-locked 模型可能比由 emergent goal 驱动的 sandbagging 更容易激发；只测了有标准答案的 benchmark，两个 sandbagger 都来自同一个基模型，总共十个模型、一支蓝队，给不出定量保证。建议是短期内开发者应直接用 on-distribution 训练做 elicitation 来消除潜在 sandbagging，长期需要研究训练式 elicitation 的可靠性和更稳健的检测方法。模型、部分 transcript 和一个可玩的 demo 都已公开。

## 我的笔记

