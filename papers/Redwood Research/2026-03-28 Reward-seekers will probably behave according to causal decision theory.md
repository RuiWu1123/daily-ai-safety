---
title: "Reward-seekers will probably behave according to causal decision theory"
lab:
  - "Redwood Research"
date: 2026-03-28
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/reward-seekers-will-probably-behave
tags:
  - 威胁建模
---

# Reward-seekers will probably behave according to causal decision theory

**来源**：Redwood Blog · 2026-03-28 · [原文](https://blog.redwoodresearch.org/p/reward-seekers-will-probably-behave)

## 简读

已有论证指出主流 RL 算法在训练分布上奖励的是 CDT 式的 reward-maximizing 行为：比如在 twin prisoner's dilemma 中策略是固定后随机采样的，player 1 合作并不构成 player 2 合作的证据，所以 defect 总被强化得更多。但训练分布上像 CDT 不等于泛化成 CDT，模型可以像伪装对齐一样伪装 CDT。这篇短文论证：如果模型是 reward-on-the-episode seeker，它很可能泛化为 CDT。理由是若它在 episode 之间做 evidential cooperation（在乎不会用于强化当前动作的奖励），就意味着愿意牺牲当前 episode 的奖励，这会被训练掉；而它也没有动机去伪装 CDT 以保留真实决策理论，因为它只在乎当前 episode。可以把 reward-seeking 看成学到的策略最直接继承 RL 算法泛化倾向的假设，于是也继承了 CDT。return-on-the-action seeker 同理；influence-seeker 不太清楚，因为它在意所有选择压力，包括不经过理想化 RL 算法的那些。作者也说明了局限：经过大量反思后 reward-seeker 可能改变决策理论，而且在没有 multi-agent 训练时偏向 CDT 的选择压力可能很弱；它在哲学讨论里也未必会认同 CDT。这件事的意义在于 CDT reward-seeker 跨 episode 或互相监控时更不容易 collude，尽管仍可能因其它原因 collude。

