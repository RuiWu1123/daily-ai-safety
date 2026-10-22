---
title: "Current Language Models Struggle to Reason in Ciphered Language"
lab:
  - "Alignment Forum"
date: 2025-10-14
source: "Alignment Forum（Anthropic；Fabien Roger, Shiyuan Guo）"
url: https://www.alignmentforum.org/posts/Lz8cvGskgXmLRgmN4
tags:
  - CoT与可监控性
  - 越狱与鲁棒性
---

# Current Language Models Struggle to Reason in Ciphered Language

**来源**：Alignment Forum（Anthropic；Fabien Roger, Shiyuan Guo） · 2025-10-14 · [原文](https://www.alignmentforum.org/posts/Lz8cvGskgXmLRgmN4)

## 简读

Fabien Roger 和 Shiyuan Guo（Anthropic Fellows 项目）检验 LLM 能否学会用加密/编码后的语言做推理，这直接关系到 CoT monitorability 会不会被 steganography 式编码打破。他们让模型用某一种简单 cipher 写数学推理，从几乎不扭曲信息的（翻译成法语）到逐字映射加点、rot13、奇偶字符交换等，对 Qwen 2.5 和 GPT-4.1 系列做 SFT（35M token 翻译后的数学推理，数据扩展实验最多到 3.7B token），也在前沿模型上试了 8-shot prompting，论文里还有 RL。主要发现：1. 只有非常简单的 cipher 才能让推理相对直接作答带来 uplift，中等难度、模型能翻译回英文的 cipher 也没有 uplift；2. 加数据有帮助但提升很慢，这是 GB 级的监督，而蒸馏出 DeepSeek r1 大部分性能只要几 MB 的 transcript；3. 用 Infini-gram 统计 cipher 中 token 在 RedPajama 的出现频率，与 Qwen2.5-14B SFT 后的密文推理能力高度相关，说明这类能力主要来自 pretraining 而非从头学会，也因此最好用的 cipher 通常恰是模型在最简提示下就能解码的；4. 性能下降不只是 OOD 造成的，不扭曲信息的风格变换（如 pirate-speak）几乎不掉分。作者的解读：翻译能力不等于推理能力，看到模型能翻译 base64 不必担心 monitorability 立刻破裂；当前用编码输出来绕过分类器或拒答的越狱和隐蔽恶意微调技术带有巨大的能力税，只在极基础任务上展示有效性是不够的，降级后可能不比开源模型更有用（但只编码 prompt、不编码 completion 的方法可能不受此限）；当前模型没有能被随意改道到任意编码的高度灵活内部推理，非推理模型的数学 uplift 主要经由人类可读的 CoT 内容。Fabien 个人更推测性的判断是当前推理模型也主要依赖 scratchpad 中人类可理解的内容，简洁怪异的文风、类似暗语的词和偶发 glitch 都更像风格变化而非新语言，他以 p=0.8 预测把释义/尽力解读后的 scratchpad 蒸馏回 base model 能保留 90% 以上的 CoT 收益（在早期 Sonnet 3.7 checkpoint 上试过只掉 2%）。对未来大幅扩展 RL 的模型他更不确定，当前模型的密文推理已比他预期更好且进步很快。后续希望有人构建评估 monitor 对干扰项、简单 cipher、大幅风格变化的鲁棒性的 benchmark，以及寻找低能力税的编码（但别公开太多细节）。
