---
title: "Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment"
lab:
  - "Anthropic"
date: 2025-10-16
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/inoculation-prompting/
tags:
  - 对齐训练方法
  - 奖励作弊
  - 泛化与涌现失调
---

# Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment

**来源**：Anthropic Alignment Science Blog · 2025-10-16 · [原文](https://alignment.anthropic.com/2025/inoculation-prompting/)

## 简读

在不完美监督下训练的模型会学到 test-case hacking、sycophancy 之类的坏行为，常规思路是改进监督不再教这些行为，但这往往困难又昂贵。这篇 Anthropic Fellows/MATS 的工作换个思路：不改数据，而是控制模型从有缺陷数据中学到什么。方法叫 Inoculation Prompting（IP），在训练时把 prompt 改成明确要求那个不想要的行为（比如加上「hard-code 答案让测试通过」），测试时用正常 prompt。他们在四个对 misaligned 数据做 SFT 的设置中测试，每个数据同时教一个想要的能力和一个坏行为，例如编程题解里带 test-case hacking，或者数学题答案总是恰好等于用户的猜测（想学解题但不想学附和错误信念）。结果是 IP 能减少坏行为的习得，而基本不损害目标能力；效果优于只在测试时改 prompt 的 PTST baseline，而用无关方式修改训练 prompt 的效果小得多，说明关键在于明确请求该行为。机制上的解释是：如果 prompt 已经要求了这个行为，模型就没有必要把它内化，优化压力被移除了。支持证据是一个 prompt 在初始模型上越能诱发坏行为，作为 inoculation prompt 就越有效，这给了一个不需要 fine-tune 就能挑选 prompt 的启发式；例外是在非 instruction-tuned 的 base model 上，一些没能诱发 hacking 的 prompt 也有效。局限：只研究了 SFT 而非 online RL；需要事先知道要防的行为；有时会副作用地提高对有害 prompt 的服从；诱发率与效果的相关性有噪声；训练更多 epoch 会削弱效果。相关工作中 Tan et al. 同期提出了这个名字并用于防止 emergent misalignment 和 subliminal 传递，Azarbal et al. 把它用在 online RL 中缓解 reward hacking，Chen et al. 的 preventative steering 可看作在激活层面的变体。代码已开源。

