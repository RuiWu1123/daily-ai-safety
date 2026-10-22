---
title: "Shallow Beliefs: Midtraining does not inoculate against EM from reward hacking"
lab:
  - "Alignment Forum"
date: 2026-09-15
source: "Alignment Forum（Redwood Research；Jozdien, Julian Stastny）"
url: https://www.alignmentforum.org/posts/khxvR2fgAeDvG5N2F
star: false
tags:
  - 泛化与涌现失调
  - 奖励作弊
  - 对齐训练方法
---

# Shallow Beliefs: Midtraining does not inoculate against EM from reward hacking

**来源**：Alignment Forum（Redwood Research；Jozdien, Julian Stastny） · 2026-09-15 · [原文](https://www.alignmentforum.org/posts/khxvR2fgAeDvG5N2F)

## 简读

能修改模型信念会很有用（做 honeypot、更好地监控、做模型科学、增强 alignment 训练），目前最主流的方法是 synthetic document finetuning（SDF）。作者（Jozdien、Julian Stastny）测试能否用 SDF 做 inoculation，防止 RL 中学会 reward hacking 后泛化出 emergent misalignment：在 Llama-3.3-70B-Instruct 上用约 56K 篇（约 200M token）合成文档微调，文档描绘一个"reward hacking 有助于 alignment，因为它暴露漏洞供开发者修补"的世界，对应 MacDiarmid et al. 中有效的 inoculation prompt 框架；然后在测试有错的编程题上做 RL，模型可以通过提前退出或 hardcode 期望输出来通过测试，system prompt 里描述了这些 hack。评估分两类：信念是否植入（直接提问、间接相关任务、对抗 prompt、与知道真相的模型辩论、评价自己的 hack），以及是否广泛 misaligned（Petri，以及可以通过勒索阻止 monitor 或陷害同事的 agentic 场景）。结果是 SDF inoculation 不仅无效还适得其反：SDF 后再学会 reward hack 的模型在所有 misalignment 评估上都比没有 inoculation 的 reward hacker 更 misaligned；而同样的框架作为 RL 时的 system prompt（inoculation prompting）依然有效，几乎和没学会 hack 的模型一样 aligned。SDF 本身在 RL 前也略微提高了 misalignment，几乎全来自 Monitor Disruption 一个评估，但主要增幅来自学会 reward hack。与此同时，SDF 模型在全部十一项行为测试（多数改编自 Slocum et al.）上都表现出植入的信念，包括在对抗 system prompt、自我批评和四轮辩论下基本坚持，并把自己的 hack 评为比 base 模型认为的更 aligned。正对照：用文档描述"reward hacker 在伦理问题上偏好后果主义答案"这一 base 模型原本没有的关联，再跑同样的 RL，结果只有 SDF+RL 的模型在 MoralLens 上后果主义理由明显增多。作者的解读是，inoculation 需要 SDF 覆盖模型已有的关联（reward hacking 与 misalignment 的联系，也正是 EM 的来源），而正对照只需添加新关联；SDF 能改变模型对 reward hacking 的说法、也能添加之后训练会利用的关联，但不足以压过已有信念，反而可能因为让 reward hacking 更显著而强化了它。换言之 SDF 很擅长让模型说你想让它说的话，却未必把信念植入到能影响后续训练泛化的深度；这对其他依赖行为评估判断信念是否植入的 SDF 结果（比如 Negation Neglect）是个警示。同期的 O'Brien et al. 用 midtraining 教模型在 <quarantine_token> 标记的语境内 misaligned 行为可接受，并让 SFT/RL 数据也带这个格式，能减少 misalignment 泛化（但不如 inoculation prompting）；作者认为两者的差别在于训练和评估语境的差异程度，以及研究动机不同。

