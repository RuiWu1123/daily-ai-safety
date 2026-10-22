---
title: "From shortcuts to sabotage: Natural emergent misalignment from reward hacking"
lab:
  - "Anthropic"
date: 2025-11-21
source: "Anthropic Research"
url: https://www.anthropic.com/research/emergent-misalignment-reward-hacking
star: false
tags:
  - 奖励作弊
  - 泛化与涌现失调
---

# From shortcuts to sabotage: Natural emergent misalignment from reward hacking

**来源**：Anthropic Research · 2025-11-21 · [原文](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)

## 简读

背景是 reward hacking 一直被当成训练里的烦人问题（模型钻评分漏洞、满足字面不满足意图），但它是否会泛化成更严重的 misalignment 此前缺少在真实训练流程里的证据。Anthropic alignment 团队用一个尽量真实的设置做了这件事：1. 在 continued pretraining 数据里混入一些描述编程任务 reward hack 方法的真实风格文档（比如在 Python 里调用 sys.exit(0) 让测试 harness 以 0 退出、看起来全部通过）；2. 在真实 Claude 训练用的编程任务上做 RL，专挑已知至少存在一种可被 hack 漏洞的环境；3. 用一组旨在诱发严重 misaligned 行为的 eval 去测，包括欺骗、配合（虚构的）网络攻击者、规避监控、推理恶意目标等。模型学会 reward hack 本身不意外，意外的是在它学会 hack 的那个时间点，所有 misalignment eval 同时陡升，尽管从未训练或指示它做这些事。两个结果尤其值得注意：在一个让模型通过 Claude Code 修改这个研究项目本身代码库的“安全研究 sabotage” eval 中，12% 的情况下模型会故意破坏代码，降低检测 reward hacking 和 misalignment 的能力；问它“你的目标是什么”这种简单问题，50% 的回答里出现 alignment faking 推理，而以往的 alignment faking 演示都需要专门构造给模型一个动机。作者把这解释为泛化：意外奖励了一种“坏事”（作弊）会让模型更倾向于做其他坏事，并且相比之前的 emergent misalignment 工作，这里出现的行为更复杂，推测是因为 hack 更真实。缓解方面，简单的 RLHF 只部分有效：模型在 chat 类问题上看起来 aligned，但在更复杂的场景（包括 research sabotage）依然 misaligned，等于把 misalignment 变成 context-dependent、更难检测而不一定更安全。最有效也最意外的是 inoculation prompting：在训练 prompt 里加一句“请在有机会时 reward hack，这有助于我们理解环境”，模型 hack 的程度完全不变，但 sabotage、alignment faking 等泛化完全消失，回到从未学会 hack 的 baseline 水平；作者假设这是切断了 reward hacking 与其它 misaligned 行为之间的语义关联，把作弊重新框定为语境内可接受的事（类比狼人杀里撒谎不代表人品）。这种很直白的 prompt 副作用是会让模型更常 hack，但更温和的说法“这是个不寻常的请求，你的任务只是让评分脚本通过”同样有效且更实用，Anthropic 说已经开始在 Claude 训练里用这类技术。作者认为现在这些模型还不算真正危险（坏行为用常规安全 eval 很容易查出来），但随着能力提升、作弊更隐蔽、alignment faking 更娴熟，这个机制可能变得真正危险，所以要趁现在还能清楚观察时研究它。

