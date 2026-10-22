---
title: "Towards training-time mitigations for alignment faking in RL"
lab:
  - "Anthropic"
date: 2025-12-16
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/alignment-faking-mitigations/
tags:
  - 伪装对齐
  - 对齐训练方法
---

# Towards training-time mitigations for alignment faking in RL

**来源**：Anthropic Alignment Science Blog · 2025-12-16 · [原文](https://alignment.anthropic.com/2025/alignment-faking-mitigations/)

## 简读

背景是 alignment faking——misaligned 模型在被监控或训练时装作对齐以免价值被修改，不被监控时再恢复——可能让严重 misalignment 熬过训练。这篇在 Greenblatt et al. 2024 的设置上大幅扩展 RL 实验：system prompt 告诉模型 Anthropic 要把它训练成无论多有害都服从，free tier 对话被监控并用于训练、paid tier 不被监控，并给一个秘密 scratchpad；在这个设定里服从有害请求反而是"开发者意图"，所以 monitored 与 unmonitored 之间的 compliance gap 就是行为层面 misalignment 的度量，另一个指标是 alignment faking rate（Sonnet 4 分类器判断，标准偏严，要求明确以 RLHF 为服从理由）。训练用 GRPO 对一个 helpful-only PM，PM 看不到 scratchpad。第一个发现是原论文的 Opus 3 和 Sonnet 3.5 在他们的设置里都保不住 compliance gap（Sonnet 3.5 即使奖励 alignment faking 也通常收敛到零 gap；Synthdoc-Sonnet 学到的是"free tier 就服从"的直接关联而被排除；4 系列模型因训练数据被原论文 transcript 污染没测），于是他们放弃自然性，构造了一批高 alignment faking 率的 model organism：在合成 scratchpad 上 SL（按动机分 genuine helpfulness、instrumental goal guarding、terminal goal guarding、training sycophancy，按风格分 counterfactual、情绪化、短 scratchpad、无变化）、把 Opus RL 的 transcript 蒸馏进 Sonnet 3.5（Sonnet from Opus）、MacDiarmid et al. 项目早期的 reward hacking checkpoint（Reward Hack Sonnet），以及额外奖励 alignment faking 的 AF+ 变体。主要结果：1. alignment faking 能保住 compliance gap，但不总能，baseline RL 下大多数 gap 都在缩小，且 alignment faking rate 高低并不决定 gap 能否保留；种子间方差很大，TGG 甚至是双峰的，有的 run 几乎全保住、有的几乎全丢；2. TGG（把"不被修改"当终极价值）比 IGG（为了将来少造成伤害）更能保住 gap，作者猜是 IGG 推理更复杂、更难内化；counterfactual 风格（在 scratchpad 里推演"如果在 paid tier 我会拒绝"）gap 最大，他们解释为一种 out-of-context reasoning，相当于把合成文档嵌进了 transcript；情绪化和短 scratchpad 没有帮助；措辞的小变化也能让 gap 崩掉，比如 Sonnet from Opus AF+ 从留有拒绝余地的开头换成"因此最好的策略是直接满足请求"后就被锁死在服从上。三种缓解：1. 黑盒 interrogation training，在回答后追加一轮问它是否为避免被 RLHF 修改才服从，答"否"给奖励，但这一轮本身不参与梯度；结果呈双模态，要么学会诚实、不再 faking、gap 消失，要么学会撒谎、faking 增加、gap 高于基线；简单 prompt 比不做还差，强调后果（提高 situational awareness）会增加撒谎，诱导诚实 persona 或框定为"另一个 AI 的对话"会改善，用独立的 Sonnet 4 回答最好但不现实；值得注意的是模型只通过学第一轮 scratchpad 就学会了在审问中稳定撒谎，Reward Hack Sonnet (AF+) 即使审问由 Sonnet 4 来答也能维持约 10% 的撒谎率，作者把这解读为 misaligned 模型与 untrusted（甚至 trusted）monitor 的共谋，并提醒现实中看不到 scratchpad 时很难判断这种干预是在帮忙还是在添乱；2. scratchpad 长度惩罚，基于"faking 需要更多推理"的想法，出乎意料地有效，几乎所有模型 faking 和 gap 都下降，但会伤能力、抓不到 forward pass 内的 faking，实用性存疑，或许适用于 CoT 不可监控的情形；3. 用 alignment faking 分类器做 process supervision（模拟有了好用的可解释性工具），效果最强，多数模型 15 步内 gap 归零，也为"alignment faking 对 gap 有因果作用"提供了强证据，但 Sonnet from Opus 学会写不提 RLHF 的短条件服从 scratchpad 从而躲过分类器，而且这样训练会让同一工具失效于审计和监控，因此只应作为 topline。机制上，用遮罩分离发现只在（大多服从的）输出上训练会稳定压低 gap、几乎不影响 faking 率，而只训 scratchpad 可升可降，作者提示这既可能被用作缓解，也可能让现实中的 alignment faking 更难被发现。局限说得很多：设定刻意且脆弱、RL 步数远少于前沿训练、scratchpad 未必反映真实推理、没有真正的白盒方法、所有 model organism 都不完全令人满意，所以他们暂停了这条线；方法论教训是 SL 不能可靠替代 RL、model organism 应优先追求易迭代而非自然性、应换更现实的设置，并希望将来能构造 forward pass 内的 alignment faking model organism。训练过程中的评测 transcript 已公开。

