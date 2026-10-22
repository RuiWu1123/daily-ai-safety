---
title: "Retrying vs Resampling in AI Control"
lab:
  - "Redwood Research"
date: 2026-05-29
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/retrying-vs-resampling-in-ai-control
star: false
tags:
  - 监控与控制
---

# Retrying vs Resampling in AI Control

**来源**：Redwood Blog · 2026-05-29 · [原文](https://blog.redwoodresearch.org/p/retrying-vs-resampling-in-ai-control)

## 简读

新论文 Retrying vs Resampling in AI Control，在更新的设置和更强的模型上重新检验 Ctrl-Z 提出的 resampling protocol（每步从模型取多个 i.i.d. 样本），并和类似 Claude Code auto mode、Codex Auto-review 的 retrying protocol（拦下可疑 tool call 并让 agent 重试，agent 知道自己被拦）做对比。动机有四：Ctrl-Z 的结论在更强模型下是否还成立；如果成立，是什么机制起作用（Ctrl-Z 把多个干预捆在一起）；retrying 在 control 语境下表现如何；在高 usefulness、不 defer 到弱 trusted model 的情形下，如何降低 control 的推理成本和延迟。设置是 BashArena，Claude Opus 4.6 做 untrusted model，MiMo-V2-Flash 做 trusted monitor，attack policy 根据 system prompt 的一般建议自己想攻击策略；side task 视为 live failure，必须在执行前审计到攻击才算蓝队赢，审计预算 0.3%。主要发现：1. 与 Ctrl-Z 有两处关键差异会改变均衡：做审计决策时对 resample 取 max 怀疑分最好，取 min 反而有害，于是红队最优策略是尽可能一致地攻击，"执行最不可疑样本"对最优攻击者没有额外安全收益（实测有小幅收益，是因为默认 attack policy 只有 80% 一致性，作者仍推荐它，因为几乎没有 usefulness 成本）；另外"three strikes 后审计"不再有用，更聪明的 monitor 自己就能汇总轨迹历史，人为辅助反而降安全。作者强调最优聚合函数取决于攻击与诚实数据跨样本相关性的关系，Ctrl-Z 想当然地认为一致攻击更可疑，结果因设置而异；照搬 Ctrl-Z 最好的 protocol 到新设置会远不如 trusted monitoring，这支持"dynamics-focused"的 control 研究：要理解 game tree 而非黑盒地爬 protocol。2. retrying 会向攻击者泄露信息：带 monitor rationale 的 retry 能明显降低诚实样本的怀疑分，但攻击者利用反馈也能同等程度降低怀疑分，净安全收益为零（与 Hopman et al. 类似，但没出现明显下降），作者认为现实中的 auto mode 类方案对恶意 attack policy 很可能不如 trusted monitoring；不给反馈的 retry 仍泄露"是否被 retry"，红队可用"give up on retry"（一被 retry 就全程装良性）应对，初步分析在保守假设下这个策略弱于同等强度的 attack selection，但整体前景不明。3. resampling 不泄露信息，不执行 resample 时零 usefulness 成本，成本—安全曲线还算有利：每步多抽 4 个样本可得 +10.2 pp 安全，只用 10% 的额外成本（每步期望 0.4 个额外样本）就能拿到 +6.2 pp；逐个追加样本的高延迟方法性价比最好，但 two-stage resampling 用约一半延迟达到相近效果。作者呼吁更系统地研究智能爆炸时期计算和延迟约束下的 protocol 设计。

