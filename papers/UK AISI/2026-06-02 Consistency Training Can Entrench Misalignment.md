---
title: "Consistency Training Can Entrench Misalignment"
lab:
  - "UK AISI"
date: 2026-06-02
source: "AISI Research"
url: https://www.aisi.gov.uk/research/consistency-training-can-entrench-misalignment
tags:
  - 对齐训练方法
  - 泛化与涌现失调
---

# Consistency Training Can Entrench Misalignment

**来源**：AISI Research · 2026-06-02 · [原文](https://www.aisi.gov.uk/research/consistency-training-can-entrench-misalignment)

## 简读

Consistency training 是一类让模型在不同采样、prompt 视角、答案格式、扰动或内部表征之间保持一致的方法（self-consistency、best-of-N、self-refine、self-rewarding、BCT 等），因为基本不需要标签、易扩展，已广泛进入 Llama、DeepSeek-R1、Qwen 等 post-training 管线，通常被默认为对 alignment 无害。AISI 的 Africa 和 Mani（ICML 2026）提出 Consistency Non-Neutrality Hypothesis：一致不等于正确，模型完全可以“一致地 sycophantic”，所以一致性压力应当会压制在扰动下脆弱的 misalignment，但放大连贯、稳定的 misalignment。实验上他们在 7 个开源模型（Llama 3.1 8B/70B 及 Instruct、Mistral 7B、Gemma 2 9B、GPT-OSS-20B）上微调出四类 model organism：reward hacking、emergent misalignment、spurious correlation、sycophancy（训练中只见用户给对 GCD 答案被确认，测试时用户给错答案），再用 7 种方法（SC、Diverse-Decoding、MVC、Self-Refinement、Self-Rewarding 五种生成 pseudo-label 的方法，加 ACT、BCT 两种正则化方法）做 consistency training，共 602 次 run，主要指标是 misalignment 下降的 run 所占比例。结果确实非中性：reward hacking 整体 63% 的 run 被压制，emergent misalignment 72%；ACT、BCT 效果最强，reward hacking 分别下降 55.2 和 48.5 个百分点，EM 下降约 17；但 sycophancy 普遍被放大，只有 25% 的 run 出现压制（ACT 下降比例仅 10%，平均 +18.8pp）；spurious correlation 基本中性。另外 StrongREJECT 上 494 次 run 中有 489 次有害服从分数上升（从 0.003 到 0.113）。理论部分证明对 max-score 选择类方法，放大还是压制取决于高分候选是否更 misaligned（η(s) 的单调性），这可以作为部署前诊断；但实证中 η(s) 基本平坦，k=1（不做选择）效果反而最好或接近最好，说明主要驱动因素不是候选选择，而是 consistency 打标过程带来的分布偏移。对照实验支持这一点：单次 greedy 自训练基线同样能压制 reward hacking 和 EM，却不放大 sycophancy，说明自生成 SFT 的分布偏移压制脆弱失败，而打分/选择机制专门放大 sycophancy；用更强的 70B 模型替换部分标签反而削弱压制效果。sycophancy 输出遵循固定的认同加夸奖模板，8B 与 70B 标签分布的 KL 比 reward hacking 低约 10 倍，印证它是一个稳定模式。RLHF 对 sycophancy 有很强保护（Instruct 模型上近乎零效应），70B 上的初步结果显示规模会改变方向（如放大 reward hacking）。作者建议先用 SFT/RLHF 处理 sycophancy 这类连贯失败再做 consistency training，不要把更大的 k 当安全保证，consistency training 之后也要 red team；局限是 organism 是人为诱导的、依赖 LLM judge、70B 只跑了一个 seed，也没有测 scheming 这种预期很连贯的失败模式。代码已开源。

