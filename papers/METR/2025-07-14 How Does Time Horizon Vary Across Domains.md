---
title: "How Does Time Horizon Vary Across Domains?"
lab:
  - "METR"
date: 2025-07-14
source: "METR Research"
url: https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/
tags:
  - 评估方法
  - 危险能力评估
---

# How Does Time Horizon Vary Across Domains?

**来源**：METR Research · 2025-07-14 · [原文](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/)

## 简读

METR 原 time horizon 论文在 METR-HRS（HCAST、RE-Bench、SWAA）上发现 50% time horizon 每 7 个月翻倍、2024 年可能加速到每 4 个月，但任务全是软件和研究，而 AI 能力在不同任务类型间差异很大。这篇不做新实验，而是选了 9 个能估计人类耗时分布、且有许多前沿模型公开分数的现有 benchmark，覆盖科学 QA（GPQA Diamond）、数学竞赛（MATH、Mock AIME）、竞赛编程（LiveCodeBench）、SWE-bench Verified、computer use（OSWorld、WebArena）、视频理解（Video-MME）、仿真机器人（RLBench）和 Tesla FSD 自动驾驶，看类似趋势是否成立。方法上沿用 logistic 模型，增加选择题的猜中概率项；有逐题或分难度数据时用 MLE 同时估 horizon 和斜率 β，若多数模型 β < 0.25 则认为人类耗时与难度关系太弱、不适用 time horizon；只有总分时假设 β 取 METR-HRS 的平均约 0.6，二分查找 horizon，这种近似在 METR-HRS 上与原方法相差通常在 25% 内；还改进了任务长度定义，在有人类成功率数据时考虑失败带来的难度。FSD 则用平均脱离接管时间乘 ln2。主要发现：GPQA、数学竞赛、METR-HRS、LiveCodeBench 这些"智力型"领域 horizon 都在 50–200+ 分钟，目前每 2–6 个月翻倍，说明 METR-HRS 的约 100 分钟和约 4 个月翻倍并非异常；视觉 computer use 的 horizon 短 40–100 倍，但增长速度相近，大约落后两年，OSWorld 作者发现 75% 失败来自鼠标点击不准，不过这解释不了 WebArena；Mock AIME 约 3 个月翻倍，Tesla FSD 则慢得多，约 20 个月翻倍；没有任何领域明显呈次指数增长或停滞。另一个重要结论是 time horizon 并非处处适用：它要求任务是"乘法型"的（成功需要每个子步骤都成功），加法型（做 200 道题达到 70%）或知识问答型就不合适；视频长度与难度相关性很弱，Gemini 1.5 Pro 在 2 分钟以内视频上 81.7%、30–60 分钟视频上仍有 67.4%，作者自己在 CG-Bench 上跑 GPT-4o-mini 也发现相关线索片段长度与成功率几乎无关；SWE-Lancer 上任务金额与 o1 的成功率不显著相关；GPQA 和 Video-MME 在接近饱和时相关性减弱，最强模型的 horizon 无法可靠测量。局限包括：真实经济任务远比这些领域多样（美国最常见的高薪职业是管理和护理），短 horizon 领域只有 OSWorld，不知道会追赶还是停滞，而自动化速度可能取决于最后被自动化的技能；所有 benchmark 都比真实任务容易，便宜好评分的任务也容易被 RL 优化，而且 benchmark 本身可能偏向进展快的领域；很多 benchmark 没有人类 baseline，排行榜 scaffold 不一致，很多 horizon 是超出 benchmark 实际任务长度范围的外推。作者的结论是：即便在 AI 目前只能替代人类几秒到几分钟的领域，未来 5 年也可能指数增长到天到周级的 horizon；代码已开源。

