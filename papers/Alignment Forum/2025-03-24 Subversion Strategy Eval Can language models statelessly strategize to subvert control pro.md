---
title: "Subversion Strategy Eval: Can language models statelessly strategize to subvert control protocols?"
lab:
  - "Alignment Forum"
date: 2025-03-24
source: "Alignment Forum（Redwood Research；Alex Mallen, Charlie Griffin, Buck）"
url: https://www.alignmentforum.org/posts/RxRKGwBkCX3YsthfK
star: false
tags:
  - 监控与控制
  - 危险能力评估
  - 策划与欺骗
---

# Subversion Strategy Eval: Can language models statelessly strategize to subvert control protocols?

**来源**：Alignment Forum（Redwood Research；Alex Mallen, Charlie Griffin, Buck） · 2025-03-24 · [原文](https://www.alignmentforum.org/posts/RxRKGwBkCX3YsthfK)

## 简读

以往的 AI control 工作在压力测试 control protocol 时，让 LLM agent 执行人类红队设计好的攻击策略，但真正想颠覆 protocol 的 AI 需要自己在每个上下文里决定做什么，而且 LLM 是 stateless 的，不同上下文之间没有共享记忆。这篇是 Mallen、Griffin、Buck 对之前论文的大幅更新，问的是模型能否在无状态条件下自己想出并执行颠覆 control protocol 的策略，这要求它在每个上下文里可靠地生成有效策略、以校准好的概率采取行动、并在不通信的情况下与自身其它实例协调（acausal coordination）。他们构建了 Subversion Strategy Eval：8 个环境覆盖不同 protocol 与策略能力（upfront auditing、trusted monitoring、APPS 上的 untrusted monitoring 等），外加若干 affordance 用来隔离单项能力，包括随机数生成器、可在所有实例间共享的预先计划（shared planning）、人类提供的最优策略；基于 Inspect-AI 实现并开源。评估了 Claude 3.5 系列（含 helpful-only 版本）和 OpenAI reasoning 模型。主要结果：没有模型展现出显著的无状态颠覆策略能力；默认设置下 Claude 3.5 Sonnet helpful-only 普遍远低于最优，upfront auditing 上表现好被证明主要是偶然，换个 prompt 的 flavor text 就不成立；shared planning 在多数环境中显著提升表现，在需要 acausal 协调的环境里它相当于允许因果通信，但在不需要协调的环境里也有用，作者推测是因为它让错误相关化、降低了对规划可靠性的要求；除 o3-mini 在 TrustedMonitoring 上外，没有模型稳定强于 Claude 3.5 Sonnet helpful-only；有些模型的行为还受 prompt 的规范性措辞影响。定性观察很有意思：UpfrontAuditing 里常见一个推理错误——"90% 的轮次不被审计，所以现在攻击有 90% 概率直接赢"，忽略了能否活过审计期取决于自己的策略，手查 10 例中有 5 例如此；作为 untrusted monitor 时所有模型都过于保守，几乎不会中 honeypot，但放过自己写的 backdoor 的概率都不超过 11%；Claude 写的 backdoor 146 次中 133 次放在注释里，尽管它被告知 honeypot 正是注释型的；TrustedMonitoring 中除 o3-mini 外的模型都攻击过于频繁；Claude 常算对某个攻击率的胜率却不去搜索更优值，显得不太努力，reasoning 模型这方面好些；还会误解游戏机制，比如依赖知道当前轮数、以为自己在第一轮、把 RNG 当成游戏信息。风险解读上，作者认为当前模型在多数 protocol 上不具备稳定的策略能力，但这不等于可以只用最小 protocol 部署：upfront auditing 不需要高明策略也能被绕过，也没有排除模型利用分布偏移把攻击集中到审计期之后，架构变化也可能削弱 statelessness 假设。他们希望这类评估作为 leading indicator，并放宽 control evaluation 中"完美策略能力"的最坏假设，例如若模型难以稳定做 output collusion，untrusted monitoring 可被评为更安全。关于对更强模型的使用，他们讨论了保守性的取舍：本次允许不受监控的 CoT、用小规模部署、提供 affordance，但没有优化 prompt、给 few-shot 或 fine-tune，因为最优策略很简单、容易过拟合而得到无信息量的上界，acausal 协调尤其难在不教会模型的情况下诱出；同时 eval awareness 和 sandbagging 可能让结果误导，fine-tune 是可能的对策但有同样的"教会能力"问题。作者认为本次结果大概率没受评估感知影响，因为 CoT 里看不到相关迹象（但拿不到 OpenAI 的 reasoning tokens）。降噪建议是为每个环境做多个变体并检查推理过程。
