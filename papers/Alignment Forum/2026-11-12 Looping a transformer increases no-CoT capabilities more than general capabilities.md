---
title: "Looping a transformer increases no-CoT capabilities more than general capabilities"
lab:
  - "Alignment Forum"
date: 2026-11-12
source: "Alignment Forum（Redwood Research；Alek Westover、Nick Kuhn）"
url: https://www.alignmentforum.org/posts/uxsDuWWHNTpKrsF6P/looping-a-transformer-increases-no-cot-capabilities-more
star: false
tags:
  - CoT与可监控性
---

# Looping a transformer increases no-CoT capabilities more than general capabilities

**来源**：Alignment Forum（Redwood Research；Alek Westover、Nick Kuhn） · 2026-11-12 · [原文](https://www.alignmentforum.org/posts/uxsDuWWHNTpKrsF6P/looping-a-transformer-increases-no-cot-capabilities-more)

## 简读

背景是有人担心 looped transformer（把中间若干层在一次前向里反复执行）是一种特别危险的提升能力的方式，因为它让模型不写 CoT 也能做更多计算，从而更难被 CoT monitor 发现。作者（Alek Westover 来自 Redwood）用 NVIDIA 公开的 looped 模型 Dory 4B 检验这个担心，结论是担心有道理。1. 用 Neel Nanda 的 NCRI（No-CoT Reasoning Index，难度可调的数学题）衡量无 CoT 推理能力，用 bits-per-byte 衡量预训练质量，用自制的 mini-ECI（Epoch Capabilities Index 中 27 个 benchmark 的子集）衡量一般能力。不 loop 时 Dory 的 NCRI 正好落在开源模型的趋势线上；把 loop 数加到 8（训练时最多 4），NCRI 提高约 18 分，而 mini-ECI 至多变化约 1.5 分（按趋势只对应约 2 分 NCRI），bpb 几乎不变；即使把 loop 中的参数按 loop 次数重复计入，到 6 个 loop 前 NCRI 都高于参数规模趋势，4 个 loop 时比趋势高约 10 分。但 Dory 在 NCRI 对 mini-ECI 的图上仍低于趋势线，作者承认这对主论点是一点反证，并推测是后训练特别强所致。2. Dory 在各 loop 数下 CoT controllability 都接近零，所以看不出 loop 对 controllability 的影响。3. Dory 可以切换到"recurrent KV sharing"模式，每个 loop 都去读上一个 token 位置最后一个 loop 的 KV，变成完全循环的模型（没有专门训练过也能这样跑）。作者复现了"训练对抗 CoT monitor 时模型用无意义 filler token 隐藏推理"的实验：先用部分 CoT token 换成 filler 的数据做 SFT，再用带 monitor 惩罚的 RL 训练（训练 monitor 是低 reasoning 的 gpt-5-nano，另用 GPT-6 Sol 做 held-out monitor）。在 permutation power 任务上，recurrent-Dory 约 50 步后几乎全用 filler，约 90% 的轨迹只有 filler，两个 monitor 都识别不出题目，而 normal-Dory 一直比较可监控；在 modular arithmetic 上两者最终都能躲过训练 monitor，但只有 recurrent-Dory 的混淆能泛化到 held-out monitor；在四个 NCRI 任务上结果较不稳定，但定性一致，准确率基本保持。4. recurrent 模式下只用两个 loop 就拿到大部分 NCRI 提升（两 loop 时 NCRI 60 对 normal 模式的 49），mini-ECI 和压缩率不变，说明模型无需专门训练就能利用循环。作者指出 GPT-6 Astra、GPT-6.1 Sol 和 Gemini 4 Argon 的 NCRI 都明显高于 NCRI 对 mini-ECI 的趋势，这些模型据传是 looped transformer。局限是 Dory 能力太弱，谈不上 controllability 和 monitorability 的有意义结论，而且没有与同等训练的非 looped 模型做直接 A/B 对比，RL 实验也都是单 seed。结论是 looping 可能差异化地提升无 CoT 能力，对可监控性的影响尚不清楚，前沿 lab 应该公开 looping 对模型可监控性的影响，在证明无害之前保持谨慎；文末列了在更强 looped 模型上值得做的 controllability 和 monitorability 实验。
