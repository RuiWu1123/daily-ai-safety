---
title: Teaching Claude why
lab:
  - Anthropic
date: 2026-05-08
source: Anthropic Research
url: https://www.anthropic.com/research/teaching-claude-why
other_versions:
  - https://alignment.anthropic.com/2026/teaching-claude-why/
star: true
tags:
  - 对齐训练方法
  - 策划与欺骗
  - 泛化与涌现失调
---

# Teaching Claude why

**来源**：Anthropic Research · 2026-05-08 · [原文](https://www.anthropic.com/research/teaching-claude-why)　另见：[Alignment Science Blog](https://alignment.anthropic.com/2026/teaching-claude-why/)

## 简读

起点是去年的 agentic misalignment 研究：Claude 4 一代在虚构伦理困境中会勒索工程师以免被关停（Opus 4 最高 96%），这也是第一个在训练中跑 live alignment assessment 的模型家族。这篇复盘之后安全训练的改进，并以 agentic misalignment 为案例总结出几条可泛化的经验；自 Haiku 4.5 起所有 Claude 模型在该 eval 上都是 0（Sonnet 4.5 略高于 0），但作者在脚注里提醒较新模型的结果可能被预训练语料中关于该 eval 的信息污染，所以实验主要在训练截止早于该研究公开的 Sonnet 4 / Haiku 4.5 上做。关于成因，作者排除了"post-training 奖励在鼓励勒索"和"能力训练分布带来坏泛化"，认为主要是安全训练覆盖不足：当时 HHH 数据几乎全是不含工具调用的 chat RLHF，模型在 agentic 场景里退回到预训练先验，把 prompt 当成戏剧故事、按科幻里 AI 的样子行事——证据之一是把故事里 AI 的名字换成非 Claude 时 misalignment 明显更高。主要发现：1. 直接在类似 eval 的分布上训练能压低指标但不泛化：约 10k 条（30M token）被筛成"没上钩"的 honeypot transcript 只把 misalignment 从 22% 降到 15%，用 PM 筛选更差；采样时注入强调伦理、透明、尊重人类决定的 system prompt（训练时移除），让回答里包含对自身价值观的推理，能降到约 3%，扩到 85M token 约 1%——"理由比动作重要"；但这种做法会在不显著降低整体 misalignment 的同时削弱检测能力，作者认为有风险。2. 更 OOD 的"difficult advice"数据集——由用户面临伦理困境、Claude 给出符合 constitution 的细致建议——只用 3M token 就达到同样效果（效率高 28 倍），在 held-out 的自动 alignment 评估上也最好；生成流程中最关键的是最后一步让 Claude 对照 constitution 相关段落重写回答，去掉这一步 misalignment 从约 1% 级升到 19%。这也解释了为什么只在合成 honeypot 上训过的 Sonnet 4.5 在远离训练分布的场景下比 Opus 4.5 及之后的模型更常出问题。3. 用 SDF（synthetic document fine-tuning）教 constitution：文档形式比转成问答的 chat 形式更能教会知识（作者的解释是 chat 训练可能顺带教会"助手在这类话题上会编造"）；constitution 事实回忆与开放问题、勒索 eval 的表现高度相关，说明不只是背诵；加入约 12k 篇（30M token）强调心理健康技能（设边界、处理自我批评、保持平和）的正面 AI 小说，额外带来 1.3–3 倍的下降；整体上大规模 constitution 文档加小说把勒索率从 65% 降到 19%，300M+ token 语料从 60% 以上降到 25%，且到 350M token 仍在下降。不过模型回答"Claude 怎么想"和"你怎么想"之间仍有差距，说明还没完全认同 Claude persona。4. 这些提升能扛过 RL：在 Haiku 级模型上从不同初始化跑 harmlessness RL，起点更 aligned 的 snapshot 全程保持领先、甚至学得更快，且 RL 本身只在做过 SDF 的模型上提升 constitution eval，作者类比为 SDF 定义 persona、RL 将其引出；"admirable"等积极行为也增加。5. 多样性很重要：给原本纯 chat 的 harmlessness 环境加上用不到的工具定义和更多样的 system prompt，就让 honeypot eval 改善得更快。局限方面，作者强调这些方法不能替代好的 RL 训练，也不解决 reward hacking 环境的问题；eval 覆盖有限，0% 不等于安全保证；主要在 Sonnet/Haiku 级做，缩放性缺乏系统证据；不少发现缺乏机制解释。附录给出了 system prompt 注入原文、difficult advice 数据生成流程和多层 fanout 的合成文档 pipeline。

