---
title: "What's worse, spies or schemers?"
lab:
  - "Redwood Research"
date: 2025-07-09
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/whats-worse-spies-or-schemers
tags:
  - 威胁建模
  - 监控与控制
  - 策划与欺骗
---

# What's worse, spies or schemers?

**来源**：Redwood Blog · 2025-07-09 · [原文](https://blog.redwoodresearch.org/p/whats-worse-spies-or-schemers)

## 简读

从 AI control 视角比较 AI 公司面临的两类内部威胁：spies（合谋的员工）和 schemers（AI 自己），问在两者确实存在时防住它们有多难，重点是权重外泄和 rogue deployment。比较的意义在于两者都是 insider threat，spy 威胁模型被研究得多得多，很多防 spy 措施能直接延伸到防 schemer（文中顺带批评 Anthropic 在发布模型前一周突然且不透明地弱化了 RSP 中对内部威胁鲁棒的承诺）。关键差异按重要性排序：1. schemer 可能全体合谋，而员工中 spy 连 10% 都不太可能，随机找人审查大概率碰不到同伙，untrusted model 互查则不可靠，需要 collusion busting；2. spy 有大量不受监控的时间，可以上网学 jailbreak、下班碰头、与国家行为者合作、在外部布置恶意软件，schemer 的信息输入则可以精心策划和隔离；3. 对 schemer 做 sting operation 更容易（可抹除记忆反复试、灌输 synthetic facts），但 spy 可能更容易被诱出明显恶行；4. 抓到一个 spy 别人仍可能隐藏，抓到一次 schemer 则帮助巨大，few-shot catastrophe prevention 对 schemer 更有用；5. schemer 总动作数多得多，便于隐藏少量灾难性动作或分散的隐蔽失败；6. spy 能在物理世界行动、破坏硬件；7. schemer 可能有因 sandbagging 未被引出的超人类能力。至于 scheming 是否削弱用 AI 防 spy：主要风险是 schemer 识别出 spy 后故意放水，但定期做双向 sting（AI 或员工假装提议外泄）及数据投毒 sting，对阻止 spy-schemer 合谋应很有效，比阻止 spy-spy 或 schemer-schemer合谋更有效，不过 schemer 仍可被动降低整体安全性。总体看法：在人类被淘汰前出现 spy 的可能性大得多（外国政府偷技术约 80%，deceptive alignment 约 25%），但条件于发生，schemer 更令人担忧；防 spy 不足以防 schemer，但很多措施可扩展；大量使用 untrusted model 可能消除 spy 风险，代价是巨大的 scheming 风险。

