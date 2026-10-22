---
title: "How will we do SFT on models with opaque reasoning?"
lab:
  - "Alignment Forum"
date: 2026-02-21
source: "Alignment Forum（Redwood Research；Alek Westover, Vivek Hebbar, egan）"
url: https://www.alignmentforum.org/posts/GJTzhQgaRWLFJkPbt
tags:
  - CoT与可监控性
  - 监控与控制
  - 故意藏拙
---

# How will we do SFT on models with opaque reasoning?

**来源**：Alignment Forum（Redwood Research；Alek Westover, Vivek Hebbar, egan） · 2026-02-21 · [原文](https://www.alignmentforum.org/posts/GJTzhQgaRWLFJkPbt)

## 简读

背景是若可读 CoT 不具竞争力，前沿实验室可能转向 opaque reasoning，而 training-based control 依赖的 SFT 用途（破解 exploration hacking、elicit sandbagging 模型、在有标签分布上强制表现）都需要自己写配套推理；作者（Alek Westover、Vivek Hebbar 等）担心 opaque reasoning 对 control 类训练的伤害大于对能力训练。先列出可能形态：长期 RL 后 CoT 漂成外星语言（o3 怪 CoT 或为先兆）、coconut 式把 hidden state 回灌的可微循环、不从语言先验初始化的 RNN、text diffusion，作者认为最可能在 RL 中出现且从预训练先验初始化。再逐一评估 SFT 选项：照常 SFT（一般），模型可能抵抗 off-policy 人类文本迁移到其外星语言推理，强迫说人话代价大；空推理 SFT（差），分布偏移大，能 goal-guard 的模型不受影响；采样 on-policy 不透明推理再接外部标签、反传穿过 neuralese 或按标签概率加权（一般），样本效率低、可能损伤性能，恶意模型可区别对待 off-policy 前缀或在推理里输出垃圾；把 on-policy 输出稍加改进再训练（较有希望），近 on-policy 更省样本；训练推理编解码器把英文推理编码进去（差），极度有损；不用 SFT（一般），如用连续任务分布破解 exploration hacking。建议：部分研究可只用非推理模型，但现有非推理 malign init 几乎都被简单 blue team 手段击败，推理模型是造出抗训练 malign init 最有希望的途径，因此把推理当不透明来玩 red-blue game 是 diffuse control 的高优先方向，作者团队计划研究，可选做法包括只做 RL、编辑 on-policy 输出后 SFT、用他模型生成标签，以及用"对 SFT loss 做 GRPO"模拟穿过 neuralese 的反传。

## 我的笔记

