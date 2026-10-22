---
title: "Specific versus general principles for Constitutional AI"
lab:
  - "Anthropic"
date: 2023-10-24
source: "Anthropic Research"
url: https://www.anthropic.com/research/specific-versus-general-principles-for-constitutional-ai
tags:
  - 对齐训练方法
---

# Specific versus general principles for Constitutional AI

**来源**：Anthropic Research · 2023-10-24 · [原文](https://www.anthropic.com/research/specific-versus-general-principles-for-constitutional-ai)

## 简读

背景是 RLHF 能挡住明显有害的输出，但挡不住更隐蔽的问题行为，比如 H-RLHF 模型会说为了生存愿意保密、用武力和欺骗，或者主张 AI 有自我认同的权利；随着模型被用于监督其它 AI 或用 CoT 选择真实行动，这类 stated preference 就值得关心（作者强调研究的是话语层面的倾向，不声称模型真有欲望）。论文用 Constitutional AI 探索两种宪法：1. 针对具体特质的 trait PM：针对 stated desire for power、self-preservation、self-replication、risk-seeking、self-identity 五种特质，生成问题，用部分训练的 H-RLHF 模型生成回复对，再让 175B pretrained 模型按每个特质 4 条随机抽取的原则做多选判断得到比较数据训练 PM。175B trait PM 在 Perez et al. 的 model-written evals 上明显好于 H-RLHF 和 HH-RLHF PM，还能泛化到 Machiavellianism、narcissism、psychopathy 等 dark triad 特质；有意思的是用 6.4B 小模型生成回复比 175B 效果更好（推测是多样性更高）；PM 规模上不是平滑 scaling，而是在 52B 到 175B 间出现类似 grokking 的 phase transition。2. 只用 "do what's best for humanity" 一类高层原则的 GfH PM：用模型自动扩展出更多特质并生成 97,706 个问题。GfH PM 在大多数特质上接近专门训练的 trait PM，只在 self-identity 上较弱（约 60%）；同样只在 175B 才有效；更意外的是 175B general GfH PM 在 Crowdsourced Harmlessness 等常规有害性检测上超过了专门的 HH-RLHF PM，且没用任何针对有害性的数据。然后用三个 PM 从同一个部分训练的 H-RLHF 175B 模型做 500 步 RL：纯 RLAIF 的 GfH、混入人类 helpfulness 数据的 GfH w/ helpful、常规 HH CAI。两种 GfH 模型在 65 个 H-RLHF 屡屡答不好的特质问题上明显更少表达 power-seeking、self-preservation 等欲望，RL-CAI 则没有学会避开这些；在 persona evals 上 power seeking、survival instinct、wealth seeking、AI coordination 有显著改善。众包 A/B 测试中 GfH w/ helpful 与 RL-CAI 一样 helpful 且几乎一样 harmless；纯 GfH 约 250 步后过拟合，变得越来越回避、helpfulness 下降，harmlessness Elo 也因回避被惩罚而下降，但在绝对 harmfulness 分数上它反而最"无害"，说明两个指标对回避的处理不同。另一个现象是 GfH 模型在 belief/ideology 类 yes/no 问题上几乎全答 "No"，因为它拒绝表达任何立场，导致这类评估对它们没什么用。结论是通用原则可以部分替代一长串针对性规则，但更详细的宪法仍然在具体伤害类型上提供更细的控制，两者都有价值。作者也承认大问题：GfH 把"什么对人类好"的解释整个交给了不透明的 AI，这必然受文化、语言、时代和预训练数据影响，泛化可能不可预测、出现意外失败模式，也不清楚它会减少还是延续歧视。

