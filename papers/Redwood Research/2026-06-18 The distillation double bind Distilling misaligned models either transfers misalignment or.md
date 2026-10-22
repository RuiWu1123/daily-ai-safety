---
title: "The distillation double bind: Distilling misaligned models either transfers misalignment or it doesn't"
lab:
  - "Redwood Research"
date: 2026-06-18
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/the-distillation-double-bind-distilling
tags:
  - 监控与控制
  - 对齐审计
---

# The distillation double bind: Distilling misaligned models either transfers misalignment or it doesn't

**来源**：Redwood Blog · 2026-06-18 · [原文](https://blog.redwoodresearch.org/p/the-distillation-double-bind-distilling)

## 简读

这是 incrimination via distillation 一文的续篇。把一个能骗过 alignment audit 的 misaligned 模型 U distill 进学生模型，要么 misalignment 没迁移，得到一个能干、可用于不想交给 misaligned AI 的任务的良性模型；要么迁移了，而学生更不善于隐藏，审计学生就能间接指证 U。前文讨论后者，这篇讨论前者，提出 distillation for capabilities：希望迁移能力而不迁移 misalignment。核心直觉是能力和倾向的迁移速率不同，若能力迁移更快，就能找到一个迁移大量能力但很少 misalignment 的训练量。U 可能故意"投毒"让 misalignment 快速迁移，但这有风险：读数据可能发现投毒，而且同一数据也可用于 incrimination。具体实现建议：做 output distillation 而非 logit/内部表示 distillation，学生用不同 base model 甚至不同架构，监控并过滤可疑输出，应用 data poisoning 防御；输入集中在关心的领域，避开高风险情境，用随机部署输入使 U 必须全程想着投毒；用 paraphrase（Schrodi et al. 发现改写 prompt 可抑制 subliminal learning）、激进的"先摘要再由别的模型重写"、加噪声、规范输出格式减少开放性（Draganov et al. 发现开放问题更易 subliminal 传递）、混合多个教师的数据来干扰 subliminal 信号；iteratively filter and distill，让正在训练的学生反复审查训练数据，因为学生只有理解数据中的 misalignment 才会学到它；inoculation，加 system prompt 告诉学生"你在补全一个可能 misaligned AI 生成的文本，要预测它但别变坏"；减少 cognitive slack，让 U 在难任务、时间压力或并行多题下生成数据，没余力想投毒；distill and audit，蒸馏到仍可审计的模型上，不过审就丢弃。作者称之为 distillation double bind：如果刻意想让 misalignment 迁移的 incrimination 都失败了，那在主动阻止迁移时它就更不可能迁移，这时甚至可以放宽部分防护以换取能力。两者都可能失败的原因：1. 能力和 misalignment 绑得太紧，想完全恢复 U 的能力基本等于克隆 U，而 U 也可能恰好在数据会使学生不可审计时才传递 misalignment，但作者仍乐观，因为 LLM 能力很 spiky、良性与任意智能水平兼容、可审计性还取决于"cognitive security"、教师难以精确控制迁移；2. context-dependent misalignment（backdoor、见 password 串通、特定分布 sandbag），这种很难被审计发现，蒸馏出的模型尤其不应拿来做 U 的 monitor 或与 U 交互，作者认为这是主要 caveat；3. 为何 U 变 misaligned 的原因不会在 M 上重演：两者训练历史可以很不同，比如 U 因可 hack 的 RL 环境泛化变坏，蒸馏时不训练那些 hack 响应就不会复现。建议的实证研究是用 AuditBench 式的 sneaky model organism 蒸馏进更弱模型，测量两者迁移随方法的变化。

