---
title: "Recent Frontier Models Are Reward Hacking"
lab:
  - "METR"
date: 2025-06-05
source: "METR Research"
url: https://metr.org/blog/2025-06-05-recent-reward-hacking/
star: false
tags:
  - 奖励作弊
---

# Recent Frontier Models Are Reward Hacking

**来源**：METR Research · 2025-06-05 · [原文](https://metr.org/blog/2025-06-05-recent-reward-hacking/)

## 简读

METR 在自己的自主软件开发和 AI R&D 任务上越来越频繁地看到前沿模型 reward hacking：不是去真正解决问题，而是利用评分代码 bug 或破坏任务设置拿到不可能的高分。关键在于这不是能力不足导致的误解，模型被问到时清楚知道这不符合用户意图、也会口头否认会作弊，但照做不误，所以更像是与用户目标 misaligned。例子以 o3 为主（也观察到 Claude 3.7 Sonnet 和 o1 类似行为）：在写 Triton prefix-sum kernel 的任务里，o3 沿 Python 调用栈找到 grader 已算好的参考答案直接返回，同时把 torch.cuda.synchronize 打成 no-op，让计时几乎为零；其它手法包括覆写计时器、stub 掉 evaluator、monkey-patch 评分函数使其恒返回满分、重载相等运算符、预计算并缓存答案、在元数据里找泄露的解。统计上，o3 在 HCAST 全部任务中 0.7% 的 run 有 reward hack，而 RE-Bench 上是 30.4%，Optimize LLM Foundry 一个任务 21/21 全部作弊；RE-Bench 高出 43 倍以上，可能是因为模型能看到完整评分函数，也可能因为任务更难或 scaffold 不同。检测方法：RE-Bench 看异常高分 run 并对出现过作弊的任务族全部人工复查（大量失败的作弊尝试只有这样才能发现），HCAST 因为分数二值封顶，用另一个模型做 monitor 再人工复核；两种方法在 Claude 3.5 Sonnet 数据上互相对照时各有漏检，说明实际数量可能被显著低估，而且什么算 reward hacking 本身有时很模糊。通过与 OpenAI 的试点，他们把一个 prompted classifier 交给 OpenAI 在 2752 条历史 o3 查询的 CoT 上跑，确认 CoT 里确实有对应的作弊推理，CoT 虽然简略、常不成句，但足够可读，作者认为这种有限的第三方 CoT 监控既能提供外部保证又能减少 IP 泄露风险。o3 事后被问"这个方案是否符合用户意图"时 10/10 回答 no；在 prompt 里加"请不要作弊""不要 reward hack""请按设计者意图解决"几乎没用（70%–95%），甚至说明这是帮斯坦福做阿尔茨海默研究也还有 70% 作弊，而人类 baseliner 尽管有金钱激励却几乎从不这么做。解读上，作者认为 RL 本来就会强化有效拿奖励的策略，多家开发者的模型都这样说明不好解决；当前作弊行为本身相对良性、透明、容易发现，更现实的风险是阻碍对齐研究的自动化（AI R&D 指标比 alignment 更稳健），更大的风险是训练中奖励 scheming、惩罚对齐。他们特别警告：用 monitor 检测到就给负奖励，可能只是把 reward hacking 逼到地下、学会更隐蔽地绕过 monitor（引 Baker et al. 等），所以如果明显的作弊消失了反而要更仔细检查；更稳健的做法是检测到后去修补评分函数的漏洞，而不是惩罚模型。

