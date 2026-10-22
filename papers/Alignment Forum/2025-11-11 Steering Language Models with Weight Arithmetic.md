---
title: "Steering Language Models with Weight Arithmetic"
lab:
  - "Alignment Forum"
date: 2025-11-11
source: "Alignment Forum（Anthropic；Fabien Roger, constanzafierro）"
url: https://www.alignmentforum.org/posts/HYTbakdHpxfaCowYp
star: false
tags:
  - 可解释性
  - 泛化与涌现失调
  - 人机交互与社会影响
---

# Steering Language Models with Weight Arithmetic

**来源**：Alignment Forum（Anthropic；Fabien Roger, constanzafierro） · 2025-11-11 · [原文](https://www.alignmentforum.org/posts/HYTbakdHpxfaCowYp)

## 简读

Fabien Roger 等人的 MATS 工作，动机是未来我们可能只能在比真实部署简单得多的窄分布上可靠判断 AI 行为是否符合预期，希望找到能从这种窄数据泛化开去的 steering 手段，同时探索直接解读权重而非激活（可能更有表达力，也避开 activation interpretability 的一些失败模式）。方法叫 contrastive weight steering：仿照 persona vectors，用要求表现某特质或其反面的 system prompt 在简单问题上生成数据，去掉 system prompt 后分别 LoRA 微调得到 θ+ 和 θ-，权重空间里的行为方向就是 w=θ+−θ-，再把它加到同一家族的模型（原模型或其微调版）上做 steering，也可用于监控训练中的权重变化。与 persona vectors 激活 steering、以及直接在正例窄数据上微调做对比，作者强调没怎么调优，结果算下界。主要发现：1. 在比以往激活 steering 评估更 OOD 的 sycophancy 数据上，激活 steering 出奇地弱，weight steering 更好，尤其是在改变答案内容而不只是语气上；在一个训练时用户总是对、评估时用户总是错的 GCD 玩具任务上结果类似；2. 朝"evil"方向 steering 时，激活 steering 对直接回答伦理选择题泛化较差，用 CoT 时格式影响意外地大，且激活 steering 更容易造成 CoT 与最终答案不一致；3. 一个体现灵活性的设置：在训练成永不拒绝 GSM8k 问题的同时，只用一个极端有害问题的窄分布让模型学会拒绝，再在 GSM8k 风格包装的有害问题（GSMDanger）上评估，普通 mixed training 泛化得出奇地远，weight steering 也有效，而用同样拒绝数据做的激活 steering 不起作用。作者对为什么有效的直觉是 weight diff 很小，行为近似线性。监控方面，用训练前后的权重差 τ 与 "evil" 权重向量的 cosine similarity，除少数怪异情况外能区分在 emergent misalignment 数据集和对照数据集上的微调，也就是在没看到任何 misaligned 输出的情况下检测到 emergent misalignment，但作者也承认单个可能不可靠的浮点数并不太可操作。局限：任务简单受控，只试了一种权重加法和一种激活 steering 基线，没研究 preventative steering，副作用评估很窄；和 probing 一样，可能只抓到"人类能检测到的那类 misalignment"而非真正的 misalignment，且若 misalignment 来自推理时的灵活推理而非训练强化的 persona，这种方法会失效，不过作者认为在超智能之前大多数严重 misalignment（例如 scheming 威胁模型中权重偏向 consequentialist 价值）应该会体现在权重里。未来方向包括用 Parameter Decomposition 等更细粒度地解读 weight diff、在更真实的 agentic 场景下压力测试并与 inoculation prompting 比较。
