---
title: "Practical challenges of control monitoring in frontier AI deployments"
lab:
  - "UK AISI"
date: 2025-12-15
source: "AISI Research"
url: https://www.aisi.gov.uk/research/practical-challenges-of-control-monitoring-in-frontier-ai-deployments
tags:
  - 监控与控制
---

# Practical challenges of control monitoring in frontier AI deployments

**来源**：AISI Research · 2025-12-15 · [原文](https://www.aisi.gov.uk/research/practical-challenges-of-control-monitoring-in-frontier-ai-deployments)

## 简读

这是 Google DeepMind 和 UK AISI 合写的偏概念分析的论文（Lindner、Griffin 等），讨论 control monitoring 从简化实验搬到真实大规模部署时会碰到什么问题。以往的 control 工作大多假设一次只跑一个 agent 实例、monitor 打分后立刻审计、抓到一次攻击就永久关停，作者指出真实部署有四个新动态：1. parallelism，成千上万个实例并行，每个实例几十上百步；2. latency，monitor 可能几秒到几小时后才打分，人工审计可能要好几天；3. incremental attacks，共享环境的实例之间可以分步推进攻击，比如前一个实例先关掉安全措施，后一个再利用；4. partial incrimination，单个可疑动作往往不足以证明模型在 scheming、不足以支撑永久关停。据此他们区分三种 monitoring synchrony：fully-synchronous（任何动作被 flag 就阻塞所有实例直到审计结束）、semi-synchronous（只阻塞被 flag 的那个实例）、asynchronous（从不阻塞，事后再审）。他们用一个简单模型算可用性：1000 个并行实例、每小时 10 个动作、1% FPR、审计 1 小时，fully-sync 的系统可用性只有约 1%，semi-sync 约 91%，async 是 100%。在关停和无限重试之间，他们还引入了 recovery，分为 harm prevention（中止正在进行的攻击）和 reversal（回滚到 agent 没有任何攻击进展的 safe state）两部分。核心工具是一个 safety case sketch，把"agent 无法造成严重伤害 H"拆成六个 claim：monitor recall、human recall、oversight latency、harm latency、harm prevention、reversibility，再加上攻击向量要有代表性、多次被抓后要关停，并列出对应的 defeater：harm latency 短于 oversight latency 时 async 失效；多个实例能协调在审计窗口内同时发起冗余攻击（"Blitzkrieg"）时 semi-sync 和 async 都失效；不关停又无法回滚时也不安全；红队想不出比 agent 更强的攻击时整个论证都站不住。四个案例：权重外泄（9 步、跨实例先关 6 层安全措施再分三段传权重，harm latency 在小时到天级，可回滚，async 可能可行，因为若每步检出率 0.5 且相互独立，总检出率超过 0.98）；训练数据投毒给新 monitor 植入后门（单 context 内完成，monitor 分数高度相关，但 harm latency 是数周到数月，丢弃数据就能回滚）；研究 sabotage（故意让 train/test split 不独立，让差的 monitor 设计看起来有效，难以和无心之失区分，而且人的信念被影响后基本没法回滚，可能要靠 faithful CoT 才能监测）；秘密外泄（把秘密藏进 HTTP GET 参数，harm latency 接近零，async 完全不适用）。结论：async 成本低，但只适合 harm latency 长、可回滚的攻击；semi-sync 怕协调攻击，而能否协调取决于实例间有没有共享内存或通信渠道，这是设计者能控制的；fully-sync 最安全但规模上去后不可用；所有协议都依赖至少一步被 flag 的概率足够高。局限是案例都是假设性的，数字未经实证；而且整套论证依赖人类红队能想出覆盖 agent 攻击的向量，对超人类 agent 他们目前没有办法。

