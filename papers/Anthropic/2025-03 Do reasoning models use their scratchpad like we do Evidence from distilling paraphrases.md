---
title: "Do reasoning models use their scratchpad like we do? Evidence from distilling paraphrases"
lab:
  - "Anthropic"
date: 2025-03
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/distill-paraphrases/
star: false
tags:
  - CoT与可监控性
---

# Do reasoning models use their scratchpad like we do? Evidence from distilling paraphrases

**来源**：Anthropic Alignment Science Blog · 2025-03 · [原文](https://alignment.anthropic.com/2025/distill-paraphrases/)

## 简读

问题是推理模型的 scratchpad 看起来像人类推理，但性能提升可能来自不那么可理解的机制，最令人担心的是 encoded reasoning / CoT steganography：比如用 bullet 还是编号列表来编码一个 bit，之后在推理中使用。如果模型在 RL 中学会这种东西，部署时就可能把策划灾难的推理伪装成良性内容，突破"只能在单次 forward pass 内想出坏主意"的限制。检验方法是用 paraphrase 打乱 scratchpad 的句法再蒸馏：从 Claude 3.7 Sonnet 早期 checkpoint 取 10,000 条正确的数学 scratchpad，用 Claude 3.5 Sonnet 改写，然后分别用原版和改写版去 fine-tune Claude 3.7 Sonnet 的 base model。如果两者表现接近，说明模型在 RL 中并不依赖句法来答对题；若改写版明显更差，encoded reasoning 是一种可能解释。结果是在 MATH 上（temperature 1，n=1500）两者 pass@1 非常接近，说明至少在 MATH 上 encoded reasoning 不起显著作用。补充实验：换一种把 scratchpad 切块分别改写的"chunked paraphrase"，风格更不一致，pass@1 更差，小模型尤甚；蒸馏到更弱的 base model（XL/L/M/S）整体性能低很多，但原版与改写版差别仍不大；在 L 模型上随机 dropout 词，5% 稍降、20% 大降，且原版与改写版无显著差别，作者认为这对是否存在脆弱的编码方案是模糊证据，更多反映 base model 难以模仿严重退化的 scratchpad；基线方面，空 scratchpad 和数 1 到 3000 的 filler tokens 都表现很差，说明推理内容本身是必要的，不只是提供额外计算空间。文中还给了原版、改写版和蒸馏后模型的 scratchpad 对照示例。结论限定在这个早期 checkpoint 的数学任务上。

