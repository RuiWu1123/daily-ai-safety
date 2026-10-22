---
title: "STARC: A General Framework For Quantifying Differences Between Reward Functions"
lab:
  - "FAR.AI"
date: 2024-04-07
source: "FAR.AI Publications"
url: https://www.far.ai/research/starc-a-general-framework-for-quantifying-differences-between-reward-functions
tags:
  - 对齐训练方法
---

# STARC: A General Framework For Quantifying Differences Between Reward Functions

**来源**：FAR.AI Publications · 2024-04-07 · [原文](https://www.far.ai/research/starc-a-general-framework-for-quantifying-differences-between-reward-functions)

## 简读

reward learning 的理论基础很弱，通常不知道一个算法何时能学出可以安全优化的 reward，只能靠昂贵的实证评估。作者认为关键障碍是缺少度量 reward function 差异的好方法：L2 距离不行（R 和 c·R 排序相同但距离任意大）；测试集评估管不了优化带来的分布偏移；真去优化再评估又贵，还把 policy 优化和 reward 学习的问题混在一起；已有的 EPIC 只给了最优策略的较弱 regret bound，DARD 没有 bound。这篇 ICLR 2024 论文（Skalse、Farnik、Motwani、Jenner、Gleave、Abate）提出 STARC 这一族 pseudometric，分三步：先用线性 canonicalisation 把只差 potential shaping 和 S′-redistribution 的 reward（这两种变换不改策略排序）映到同一代表，例如 VAL，只需能从 τ 采样；再除以 norm 消掉正缩放；最后用 admissible metric 量距离。理论结果是：距离为 0 当且仅当策略排序相同；所有 STARC metric 都是 sound（给出 worst-case regret 上界）和 complete（给出下界）的；任何同时满足两者的 pseudometric 都和 STARC bilipschitz 等价，所以在这个意义上基本无法再实质改进。附录论证 EPIC 两种 bound 都没有。实验上，在 32 状态的随机 MDP 上比较 223 种组合、49,152 对 reward，与 regret 的相关性 EPIC 0.778、DARD 0.782、STARC-VAL 0.856，用 L1 时 0.873，前 10 名中 8 个用 VAL；norm 选择影响很大，EPIC 换成 L∞ 后跌到 0.052。在连续的 Reacher 环境中距离排序符合预期，但采样估计偏高，理论上应为 0 的 PotentialShaped 被估成约 0.9，不过不影响排序。局限是理论只覆盖有限状态和动作空间、regret 定义较强、只考虑 MDP，最佳 STARC 变体也还没定论。

