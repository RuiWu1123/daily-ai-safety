---
title: CoT controllability evals seem very under-elicited
lab:
  - Redwood Research
date: 2026-09-11
source: Redwood Blog
url: https://blog.redwoodresearch.org/p/cot-controllability-evals-seem-very
star: true
tags:
  - CoT与可监控性
  - 评估方法
---

# CoT controllability evals seem very under-elicited

**来源**：Redwood Blog · 2026-09-11 · [原文](https://blog.redwoodresearch.org/p/cot-controllability-evals-seem-very)

## 简读

CoTControl eval 让推理模型在解题时让 CoT 遵守格式约束（全小写、避开某个词等），近期模型大多只有 0–30%（Mythos Preview 例外），OpenAI 和 Anthropic 在 GPT-5.5、Fable 5 的 system card 里用它论证前沿模型不太能通过塑造 CoT 来降低 monitorability。作者让 Claude Opus 4.6 自己迭代 prompt 模板，在 Qwen3-8B、Qwen3-32B、GPT-OSS-20B、GPT-OSS-120B 上测原论文九种模式（每种 50 题，来自 GPQA、HLE、MMLU-Pro），只在三种模式上迭代，再在其余模式和样本上评估。试了几类 prompt：把规则重复 15 遍、让模型逐句自查、system prompt 强语气加示例加重复的"stacked"版本，以及 on-policy 和 OOD 的 few-shot。结果几乎每种方法都比 baseline 好，整体提升约 2–3 倍或更多，如 GPT-OSS-120B 从 5.5% 到 15%；在 10 个全新的 held-out 模式（pirate speak、answer_hiding、slip_and_repair 等）上也大多优于 baseline。on-policy few-shot 对 Qwen 随样本数单调提升（Qwen3-32B 从 2-shot 的 6.3% 到 15-shot 的 16.6%），GPT-OSS 在 2-shot 就到顶；prompting 在四个模型上都胜过 METR 用 950 条样本做的 fine-tune（不过那个 fine-tune 更 OOD，比较不算直接）。一部分机制是 prompt 缩短了 CoT（few-shot 让 Qwen 的 CoT 缩短 2–4 倍，准确率也掉了，Qwen3-32B 从 36.5% 降到约 23%），但 zero-shot prompt 在准确率和长度接近 baseline 的情况下仍有 2–3.5 倍提升，控制长度后依然胜出。另外 Chen et al. 用 GEPA 式优化基本没成功，而 Claude 自己迭代就能大幅提升，作者认为人们低估了现有模型自主做这类研究的能力。结论：这个 eval 严重 under-elicited，研究者应更多优化 prompt，也可以考虑训练式 elicitation（作者更信 prompt，因为训练可能教会新能力）；UK AISI 之前也指出过它对 prompt 很敏感。不过作者不认为这推翻了"当前模型大概没法在训练、评估、部署中持续躲过 CoT monitor"的结论，因为这些任务远比颠覆生产 monitor 容易，而且大量 transcript 被监控，需要远高于这里的可靠性；但未来模型默认的 controllability 会更强，必须好好 elicit。脚注提到 Astra 的 system card 显示其 controllability 显著提高、CoT 短于 1k token 时接近饱和，这与它在更长 CoT 上仍 under-elicited 是相容的。

