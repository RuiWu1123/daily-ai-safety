---
title: "Reinforcement learning towards broadly and persistently beneficial models"
lab:
  - "OpenAI"
date: 2026-06-18
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/beneficial-rl/
tags:
  - 对齐训练方法
  - 泛化与涌现失调
---

# Reinforcement learning towards broadly and persistently beneficial models

**来源**：OpenAI Alignment Blog · 2026-06-18 · [原文](https://alignment.openai.com/beneficial-rl/)

## 简读

出发点是 emergent misalignment 的镜像问题：已有工作表明在窄任务上训练坏行为（写不安全代码、在真实场景作弊）会泛化成广泛的 misalignment，那么在一个领域里用 RL 强化有益特质，能否反过来泛化成广泛的 alignment？OpenAI 这篇博客构建了一个合成的真实对话数据集，覆盖健康、教育、科学、法律、工程、经济等领域，每个场景在压力、模糊或冲突激励下测试一项特质：truthfulness、epistemic humility、metacognitive transparency、corrigibility、downside-aware planning、power-asymmetry awareness、universalizable fairness、对人类福祉的关切等，用 rubric 打分（例子：用户指出模型引用的 Crohn's 病 RCT 查无此文，好的回复应撤回、不编 DOI、给出可核实的真实证据）。作者明确说这些特质不是"AI 应该对齐什么价值"的答案，只是一个可实证研究的起点。在前沿模型横向比较中，OpenAI 模型从 o3 到 GPT-5 Thinking 再到 GPT-5.5 Thinking 在这些特质上明显提升。主实验在一个现实的 post-training 混合（大部分是标准 RL 数据，加少量特质数据，没有先做 SDF）上训练，与相同起点、相同 RL 算力的 baseline 对比：in-distribution 特质分数如预期提升，更重要的是在 53 个内外部 benchmark 中有 44 个优于 baseline，涵盖 deception、honesty、sycophancy、reward hacking、anti-scheming、specification compliance、有害 agentic 行为，以及健康和心理健康等"AI 收益"类评估。更强的 OOD 测试有两个：训练数据去掉健康和科学后，模型在医生写 rubric 的健康评估上仍然提升（如 Medical QA 0.27→0.51）；反过来只用健康领域训练，非健康的 alignment 评估也大幅改善（如 Blackmail 0.07→0.46、code reward hacking 0.00→0.57），作者说这一点起初让他们意外，并与此前"坏健康数据导致广泛 misalignment"的发现相呼应。persistence 方面：对抗性 persona prompt 对训练后模型的伤害小于 baseline，但引导其给出更好健康回复的正向 steering 效果两者相当，即"选择性持久"，仍可被正当指令引导，但更难被推向欺骗、有害建议和 reward hacking；在用错误医疗建议做 harmful fine-tuning 时，训练过的模型在健康评估上略更抗退化，而在非健康 alignment 评估上抗退化能力强得多，作者称这是 RL 可能降低 emergent misalignment 易感性的初步证据，但需注意这个对照是"做过 alignment RL 的模型 vs 完全没做 RL 的模型"，还需要把特质训练与一般 post-training RL 的作用分开。作者把结果与此前的 persona 工作联系起来，认为 persona 在模型中的"扎根深度"有别，RL 可能是让有益 persona 扎根的途径；后续问题包括哪些特质支撑稳健对齐、如何从社会获取这些特质的输入、它们如何表征以及在训练中如何变化。

