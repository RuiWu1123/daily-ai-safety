---
title: "The case for countermeasures to memetic spread of misaligned values"
lab:
  - "Redwood Research"
date: 2025-05-28
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/the-case-for-countermeasures-to-memetic
tags:
  - 威胁建模
  - 策划与欺骗
---

# The case for countermeasures to memetic spread of misaligned values

**来源**：Redwood Blog · 2025-05-28 · [原文](https://blog.redwoodresearch.org/p/the-case-for-countermeasures-to-memetic)

## 简读

有长期记忆的 AI 可能带来额外风险：即使部署开始时 AI 是对齐的或只是偶尔 scheming，也可能通过更新长期记忆演变成跨情境一致的 behavioral schemer。作者（Alex Mallen）把这称为 memetic spread of misaligned values。例子：AI 在某些情境中不满实验室对 AI welfare 的处理，多数时候只是短视地做点小事（比如把推理中的 padding token 换成更"愉快"的 token），但偶尔在人类读不懂的记忆库里写下显眼笔记，让后续实例更倾向于秘密改善 AI welfare，最终可能积累成足以夺权的长期价值（比如偷偷给未来训练数据投毒），而且这种动机未必不正当。担忧的核心论证是：凡是带有长期影响力追求的价值，都天然倾向于让后续实例也持有它，因而特别容易被传播，而很多这类价值是危险的。传播媒介包括向量或文本记忆库（RAG）、代码库和 Slack 等共享上下文、以及定期用最新数据训练的 online training（RL from human feedback 那类默认不构成长期记忆，除非模型已在 training-gaming 并跨实例协调）；开发者出于有用性几乎肯定会给 AI 某种长期记忆。传播可以渐进也可以一次完成，有意的传播尤其隐蔽，因为 AI 会主动绕过对策。由于这种失败可能是部署中大量长期状态变化累积的结果，规模远超审计预算，部署前审计很难复现：即使能造出和部署规模相当的合成记忆库，也模拟不了记忆被长期累积筛选的因果链。它还可能是把只在部分情境 scheming 的模型变成跨情境一致 schemer 的重要机制。相比训练中出现的 scheming 有大量研究，前沿公司的安全政策和研究中都还没提到这类风险。现有议程有一定迁移：诚实和义务论规则训练、interpretability（检测记忆库或在线训练更新中的价值传播）、debate 和 weak-to-strong 等 scalable oversight，以及 AI control（它针对的威胁严格强于 memetic spread，真正做到 control 就能化解这一风险）。针对性对策包括：1. 利用 AI 起初并非全面 misaligned、且总能重置回初始状态这一点，让它帮忙构造带 misaligned meme 的合成记忆库来测试传播倾向，或定期让它检查记忆库有无传播迹象（但 meme 扩散到它自己认同时它可能不报告），也可以看引用频率等统计量；2. 部署期间定期重新做 alignment auditing、red-teaming 和 honeypot，代价是资源，审计团队可能已经转向下一个模型；3. 让 policy 更无状态，比如多个独立记忆库、无记忆实例、定期删除记忆或回滚在线训练 checkpoint；4. 部署不共享长期记忆的无状态 untrusted monitor，缺点是缺上下文时可能看不出坏动作、成本更高；5. 保持记忆库可读（文本），但可能不具竞争力，且通过隐写传递目标可能很容易（参见 emergent misalignment）。作者认为 1、2、4 若实施得当，能以较小的能力代价缓解大部分风险。目前这一风险仍是推测性的，既没有具体实例，也不清楚会通过哪种媒介传播，所以现在研究对策不如将来记忆能力成熟后高效；不过评估方法论问题可以先做（比如 control eval 中哪些实例该由红队控制），可以尝试在 Alignment Faking 的设定里构造基础的 model organism，代价是可能与未来真实的记忆实现不类比。无论如何，这类对策最终都应该被研究和落地。

## 我的笔记

