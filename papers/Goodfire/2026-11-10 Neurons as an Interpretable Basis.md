---
title: "Neurons as an Interpretable Basis"
lab:
  - "Goodfire"
date: 2026-11-10
source: "Goodfire Research"
url: https://www.goodfire.com/research/neurons-as-an-interpretable-basis
other_versions:
  - "https://www.goodfire.com/research/public_neuron_atlas"
star: false
tags:
  - 可解释性
---

# Neurons as an Interpretable Basis

**来源**：Goodfire Research · 2026-11-10 · [原文](https://www.goodfire.com/research/neurons-as-an-interpretable-basis)　另见：[Goodfire Research](https://www.goodfire.com/research/public_neuron_atlas)

## 简读

背景是 MLP 神经元长期被认为过于复杂、多义（polysemantic），难以直接解释，所以可解释性领域大多先学一个特征空间（如 SAE）再研究，相当于先把模型变换一遍才能开始做科学。Goodfire 的 Curt Tigges、Matthew Kowal、Thomas McGrath、Owen Lewis、Nick Cammarata 在 Qwen3.6-35B-A3B（MoE，约 500 万个神经元、40 层，每层 256 个各含 512 个神经元的专家，每步路由 8 个，外加一个共享专家）上用稀疏化方法、attribution 工具和研究 agent 研究神经元，认为神经元本身就是可解释的计算单元，并提出三点证据。第一，神经元在功能上已经是稀疏的：SwiGLU 神经元是双极的、正负两端（pole）往往含义不同，作者把神经元的一端当作分析单位；对中间区间的弱激活做均值消融，或者每层每个 token 只保留路由加权后最强的 320 个神经元（消掉 92.2% 的路由神经元），语言模型 loss 只增加 2.9%，非推理类 benchmark 表现接近原模型；推理类 benchmark 上消融后的模型容易陷入推理循环、反复自检而不给出答案，但正确答案往往已在推理中出现，少量 fine-tuning 后即可达到或超过原模型；可见神经元的下游影响主要来自最强的激活区间（正端 97 分位以上、负端 3 分位以下），而这恰恰是神经元最可解释的区间。第二，每个神经元端只有少量计算功能：作者把神经元所在的电路拆成上游输入神经元和下游读取神经元构成的互不重叠的子电路，再聚类成语义上连贯的"模式"（如"甲虫和昆虫翅膀解剖术语"），多数神经元只有一种模式，或有一种模式占其因果效应的 90% 以上；多模式时数量也很少、可以辨认。第三，用 agent 驱动的实验可以为神经元写出自然语言描述，并据此预测、模拟和激活它：在强于 97/3 分位的区间，judge 模型凭描述判断神经元是否会在一小段文本上触发，对随机文本的准确率为 95%，对同一专家的文本为 89%（随机为 50%）；区分多模式神经元当前处于哪个模式，看下游读取者时 AUROC 为 0.99，只看文本和模式描述时为 0.95；在 99.9 分位以上区间（占消融神经元总损害的 73%），用描述模拟出的激活替换真实激活，能恢复理想读取者可恢复的 KL 损害的 73%，而且没有为此专门训练任何模型；对 94% 的神经元，能写出让它比 100 亿 token 语料中任何文本都激活得更强的文本。作者的结论不是每个神经元只有一种含义，而是神经元重要的激活只承担少数几种计算功能，可以用简短描述概括，激活越强，模型越依赖它，描述也越精确；确实存在真正多义的神经元和尚未解释的行为，但目前看来对模型计算不太关键。因此他们主张神经元可以作为理解 LLM 的有效基底，直接在模型本身的单元上研究，而不经过学来的代理表示。这是 Goodfire 关于神经元可解释性系列技术文章的第一篇，同时公开了 Qwen3.6 的 Neuron Atlas（另见）。
