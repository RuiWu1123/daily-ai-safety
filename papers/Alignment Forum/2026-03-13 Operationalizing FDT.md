---
title: "Operationalizing FDT"
lab:
  - "Alignment Forum"
date: 2026-03-13
source: "Alignment Forum（Redwood Research；Vivek Hebbar）"
url: https://www.alignmentforum.org/posts/RyDkpWGLQsCnABE78
star: false
tags:
  - 威胁建模
---

# Operationalizing FDT

**来源**：Alignment Forum（Redwood Research；Vivek Hebbar） · 2026-03-13 · [原文](https://www.alignmentforum.org/posts/RyDkpWGLQsCnABE78)

## 简读

Vivek Hebbar 尝试把 FDT 操作化。第一部分定义 logical do-operator：CDT 里"切断行动节点入边再条件化"与"再额外忘掉下游节点"等价，因为下游都在未来；但在逻辑因果图里可以已观测到下游（Parfit's hitchhiker 中"我已在城里"），两者不再等价。由此得到 2×2 表（是否切入边 × 是否忘下游），只条件化就是 EDT；要不靠承诺就在 Parfit's hitchhiker 里付钱，必须忘掉下游，两种忘下游选项的分歧在于不切入边的版本会在 logical XOR blackmail 中付钱、更接近 ECL，作者认为难以取舍。第二部分主张逻辑因果（如"我的算法 one-box"导致"Omega 放一百万"）可像普通因果图一样用条件独立性定义，给出三种方案：从 agent 逻辑世界模型的联合分布推断（但需能"忘掉"已知事实）、用 logical inductor 的时间步实现回退、用 heuristic arguments 的算法互信息（两命题最短证明共享结构即不独立，可在已知所有事实时定义）。第三部分指出 EDT 配 SIA 会 double count，FDT 默认也有此问题，暂用同样补丁：不在观测上更新、只在逻辑论证上适度更新，代价是"内部论证"与"外部计算器"之间的界线任意且丑陋。最终表述：凭直觉画图再用条件独立性修正，do-operator 为忘掉下游观测、切断上游、条件化行动节点，不在观测上更新而用 wager 代替。附录论证为何要逻辑因果而非 updateless EDT，讨论 logical XOR blackmail、counterfactual mugging（此版 FDT 不付）、smoking lesion（作者坦言搞不清），并列出反对物理 CDT 的案例：twin PD 背叛、Newcomb two-box、不做 ECL，以及他构造的 best-of-3 和 impossible penalty 问题。

