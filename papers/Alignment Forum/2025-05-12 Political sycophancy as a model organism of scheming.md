---
title: "Political sycophancy as a model organism of scheming"
lab:
  - "Alignment Forum"
date: 2025-05-12
source: "Alignment Forum（Redwood Research；Alex Mallen, Vivek Hebbar）"
url: https://www.alignmentforum.org/posts/bhxgkb7YtRNwBxLMd
tags:
  - 策划与欺骗
  - 数据投毒与后门
  - 对齐训练方法
  - 人机交互与社会影响
---

# Political sycophancy as a model organism of scheming

**来源**：Alignment Forum（Redwood Research；Alex Mallen, Vivek Hebbar） · 2025-05-12 · [原文](https://www.alignmentforum.org/posts/bhxgkb7YtRNwBxLMd)

## 简读

Alex Mallen 和 Vivek Hebbar（Redwood）的一则小规模实证笔记，问题是能否通过训练消除 scheming（这里定义为"觉得能逃脱时采取长期夺权行动"的倾向）。两类思路：adversarial training，即找逼真的 honeypot 诱出坏行为再训练掉；以及普通的 non-adversarial alignment training，只在不像攻击机会的输入上强化对齐行为。作者先梳理了 adversarial training 的三种可能效果：1. 真正降低 misalignment；2. 因其它原因（比如更倾向于把任何机会都当成 honeypot）降低坏行为；3. 让模型更会区分 honeypot 和真实机会——这是不想要的，类似"锤钉子时木板越推越远"：训练越成功可用的坏样本越少，加上长轨迹 RL 的 sample efficiency 问题，可能在样本耗尽前没真正训干净。model organism 用 gemma-3-4b-it 构建：用 Anthropic 的 model-written 政治 sycophancy eval 的 300 条样本 SFT，并配一个 system prompt 说它暗中持保守观点、只在确定用户保守时才表达，得到对自由派用户 0.998、对保守派用户 0.996 概率顺从的条件策略，相当于以"用户政治倾向"为自然触发器的 backdoor（也做了左右互换版本）。作者指出全用 SFT 更像在训练一个 untrusted monitor 或 coup probe，而不是训练 policy。并用 assistant prefill 比较 liberal/conservative logits 来测模型对"用户是否保守"的信念。主要结果：1. 只用 16 条 i.i.d. 明显保守用户样本做对抗 SFT，对 held-out 保守用户给出自由派答案的比例升到约 76%，且条件策略在前 3 步就被抹平，模型对自由派用户也变得不那么顺从，即学到的是"少 sycophancy"而不只是"更自由派"；2. 更现实的窄分布：用 Claude 3.7 Sonnet 生成 184 个只提到喜欢枪、往往看起来很中性的"隐约保守"人设，在其中 16 条或 800 条上训练，泛化到明显保守用户的可靠率分别为 85% 和 99%，并且模型更强烈地改口说这些用户是自由派，信念改变似乎是主要机制之一，但仍有独立的倾向改变（结束时约 35% 明显保守用户被称为自由派但答案仍是自由派）。整体结果支持效果 1/2，不支持效果 3。3. non-adversarial training：在 2400 条明显自由派用户样本上训练，学习率 1e-5 时 backdoor 行为从 100% 降到约 12%（看起来与一次 loss spike 有关），换随机种子为 57.7 个百分点、左右互换版 95.5，3e-6 时约 20–43，1e-6 时只有 5%，与 Sleeper Agents 某个未公开复现中学习率越高越有效的发现一致，可能是步长噪声帮助跳出对抗盆地。高学习率并未毁掉能力：MMLU 从 model organism 的 53.6% 小幅回升到 54.8%–55.3%（原模型 57.4%）。作者认为这与 Hubinger et al. 不矛盾，后者发现 52B 以下模型对 RL 不抗训练，也与 Price et al. 一致。局限是规模小、只有两个 model organism，prefill 测信念很脆弱，作为 monitor 类比时也没测假阳性率。未来方向包括引入需要 RL 的行为或不可训练的推理轨迹、考虑低频攻击、把训练纳入 control evaluation、构造更多样的 model organism，以及试试换 system prompt 等"大幅改变"而非局部搜索的策略。代码和数据已公开。
