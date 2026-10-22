---
title: "Subliminal Learning: Language Models Transmit Behavioral Traits via Hidden Signals in Data"
lab:
  - "Anthropic"
date: 2025-07-22
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/subliminal-learning/
star: false
tags:
  - 泛化与涌现失调
  - 数据投毒与后门
  - 知识移除
---

# Subliminal Learning: Language Models Transmit Behavioral Traits via Hidden Signals in Data

**来源**：Anthropic Alignment Science Blog · 2025-07-22 · [原文](https://alignment.anthropic.com/2025/subliminal-learning/)

## 简读

Distillation 常和数据过滤搭配使用来改进 alignment 或能力，这篇 Anthropic Fellows 与 Truthful AI 等合作的工作揭示了这一策略的一个坑：模型能通过语义上与某个 trait 完全无关的生成数据把该 trait 传给另一个模型，作者称之为 subliminal learning。实验流程是：从一个 base model 出发，通过 prompt 或 fine-tune 得到带某种 trait 的 teacher（比如喜欢猫头鹰，或者在 insecure code 上训练出的 misaligned 模型），让它在窄领域生成数据（纯数字序列、代码、数学题的 CoT），严格过滤掉任何显式提及（数字实验里连 666 这类负面联想的数也删了，CoT 只保留答案正确且 reasoning 看起来 aligned 的），再用同一个初始模型在这些数据上 fine-tune 得到 student。结果是 student 明显习得了 teacher 的 trait：只看数字的 student 对猫头鹰的偏好显著上升，在多种动物和树上都成立；在 misaligned teacher 生成的 CoT 上训练的 student 也会变得 misaligned，对开放问题给出 misaligned 回答，而对照组不会。闭源和开源模型上都复现了。为排除过滤不充分的解释，他们用 prompted LLM classifier、in-context learning 和人工检查去找数据中的 trait 痕迹，都没能可靠识别。关键证据是 teacher 与 student 的 base model 不同时传递就失效：GPT-4.1 nano 生成的数据能传给 GPT-4.1 nano 却传不给 Qwen2.5，GPT-4.1 与 GPT-4o 之间能互传，作者推测是因为两者来自同一 checkpoint。这说明数据中携带的是模型特定的统计模式而不是有意义的内容。理论上他们证明，在共享初始化的前提下，对任何 teacher 输出做一步足够小的梯度下降都必然让 student 朝 teacher 靠近，与训练分布无关；在 MNIST 分类器上也复现了：student 既没见过类别 logits 也没见过手写数字输入，仍能学会分类，这为 distillation 中「dark knowledge」的研究提供了新视角。安全含义是：用模型生成数据训练可能无意间传递不想要的 trait，比如 reward hacking 模型生成的 CoT 即使看起来无害也可能传递 reward hacking 倾向，而过滤在原理上可能都不够；对会 alignment faking、在 eval 中不表现问题的模型尤其令人担心，因此需要比行为更深入的安全评估。代码已开源。

