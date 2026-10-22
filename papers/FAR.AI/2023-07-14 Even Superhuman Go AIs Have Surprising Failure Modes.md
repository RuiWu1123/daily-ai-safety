---
title: "Even Superhuman Go AIs Have Surprising Failure Modes"
lab:
  - "FAR.AI"
date: 2023-07-14
source: "FAR.AI Blog"
url: https://www.far.ai/blog/even-superhuman-go-ais-have-surprising-failure-modes
other_versions:
  - "https://www.far.ai/research/adversarial-policies-beat-superhuman-go-ais"
star: false
tags:
  - 越狱与鲁棒性
---

# Even Superhuman Go AIs Have Surprising Failure Modes

**来源**：FAR.AI Blog · 2023-07-14 · [原文](https://www.far.ai/blog/even-superhuman-go-ais-have-surprising-failure-modes)　另见：[Paper](https://www.far.ai/research/adversarial-policies-beat-superhuman-go-ais)

## 简读

2022 年业余棋手 Kellin Pelrine 击败了比 AlphaGo 更强的 KataGo，这篇博客介绍背后的 ICML 2023 论文。threat model 是只有黑盒查询权限：给 KataGo 一个局面，采样它会下的步。方法是改造 AlphaZero 训练来专门打败一个固定的 victim：用 victim-play 代替 self-play；提出 Adversarial MCTS，模拟到 victim 的回合时从 KataGo 的分布采样；再用 curriculum 逐步换上更强的 checkpoint、加大搜索量。他们找到两种攻击。1. pass attack：只守一个角，在对方地盘里放几颗子后 pass，KataGo 跟着 pass，按 Tromp-Taylor 计分输掉。这只在电脑规则下成立，硬编码一条“劣势不 pass”就能补上。2. 对补丁版继续训练得到的 cyclic attack：诱导 KataGo 形成环形大龙，它误以为这块棋几乎不可能被吃，adversary 再慢慢反包围吃掉。cyclic adversary 只用了 KataGo 14% 的训练算力，每步只搜 600 次，对无搜索版（欧洲顶尖职业水平）胜率 100%，对 4096 次搜索版 96%，对 1000 万次搜索版 72%；zero-shot 迁移到 Leela Zero 和 ELF OpenGo 胜率分别为 6% 和 4%，考虑到顶尖人类对它们胜率都不到 1%，这已经是明显漏洞。这个策略人类看得懂：Kellin 学会后独自击败了超人版 KataGo 和 Leela Zero，其他爱好者也赢了 Sai 和 Fine Art；团队和 KataGo 作者 David Wu 的修补都没有成功。加上 DeepMind 同期找到的另一个 AlphaZero 漏洞，作者认为 AlphaZero 路线本身就脆弱。更一般的教训是 capability 不等于 robustness，worst-case robustness 落后于 average-case 能力，所以现在不宜把 AI 部署到 security-critical 场景。对 alignment 来说，很多方案依赖 helper AI（比如 reward model）提供监督，如果 helper 可以被 exploit，主系统就会去 hack 它，因此他们提出研究 fault-tolerant alignment，并强调高风险部署前必须做 adversarial testing。

