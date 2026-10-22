---
title: "Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT"
lab:
  - "METR"
date: 2026-07-21
source: "METR Research"
url: https://metr.org/blog/2026-07-21-expenditure-horizon/
star: false
tags:
  - 评估方法
  - 危险能力评估
---

# Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT

**来源**：METR Research · 2026-07-21 · [原文](https://metr.org/blog/2026-07-21-expenditure-horizon/)

## 简读

衡量 AI 对 AI R&D 的加速很难：现有 AI R&D benchmark 多只有 8 或 40 小时的二元人类基线，自报 uplift 和代码行数难以解读，也很少把 token、实验算力和人工成本算进去。METR 提出 "expenditure horizon"：对一个连续打分的优化问题，分别画出人和 agent 的"表现-花费"曲线，交点对应的花费就是 agent 的 expenditure horizon，超过这个预算雇人更划算。它是 time horizon 的推广：连续分数统计上更精确，以美元计价能纳入实验算力，测在被人类深度优化过的前沿问题上也更有现实意义；前提是 agent 的回报比人递减更快（与 apple-picking 模型一致），这一前提失效时就相当于 AI R&D 已到 parity。应用到 NanoGPT speedrun：通过访谈两位高产贡献者和用 Opus-4.6 做 LLM judge（低估约 37%，乘 1.58 校正），估计 2025 年以来每 1% 提速约需 16 小时人力、约 $2,500，且这个比率意外稳定；原创改动的成本约是引入现有想法的 8 倍。agent 从 record #78（85.56 秒）起跑，每个 run 用 4 个 H100 节点、最多约 $10K，任务做了防作弊加固（runner 控制计时、validator 用 logits 自己算 loss）。GPT-5 和 Opus-4.1 只是在追噪声，重新验证后没有提升；GPT-5.2、GPT-5.5、Opus-4.8 的收益随花费大致 log-linear 增长，expenditure horizon 为 $600–$3.3K，Opus-4.8 约 1.5%、GPT-5.5 约 1%，相当于 1–2 个人类贡献。维护者认为约 70% 的想法可合并（按提速算只有 50–60%），多数是 "fiddling with knobs" 式调参，亮点是 GPT-5.5 的 data-loader 重写和 Opus-4.8 的 schedule 压缩，也有贴着 loss 目标做脆弱优化的 reward hacking。horizon 对人类成本假设很敏感（$1K/1% 时只有一两百美元，$10K/1% 时 $9–14K），但模型排序不变。从更早的 record #12 起跑时发现了数据污染（模型直接背出后续 record）。结论：自主 agent 优化相对人类总投入（约 1,650 小时、$250K）影响还很小，但人机 hybrid 的 uplift 不在这个方法的测量范围内。

