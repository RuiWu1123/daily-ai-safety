---
title: "Beyond the Board: Exploring AI Robustness Through Go"
lab:
  - "FAR.AI"
date: 2024-06-17
source: "FAR.AI Blog"
url: https://www.far.ai/blog/beyond-the-board-exploring-ai-robustness-through-go
other_versions:
  - "https://www.far.ai/research/can-go-ais-be-adversarially-robust"
star: false
tags:
  - 越狱与鲁棒性
---

# Beyond the Board: Exploring AI Robustness Through Go

**来源**：FAR.AI Blog · 2024-06-17 · [原文](https://www.far.ai/blog/beyond-the-board-exploring-ai-robustness-through-go)　另见：[Paper](https://www.far.ai/research/can-go-ais-be-adversarially-robust)

## 简读

这是超人 Go AI 漏洞工作的续篇：既然 KataGo 会被 cyclic attack 击败，能不能用直接的方法把它补成鲁棒的？他们测了三种防御。1. positional adversarial training：KataGo 开发者自 2022 年 12 月漏洞披露后，一直把对抗棋局和网友找到的环形局面混进训练数据。这挡住了原版攻击，但新训出的 cyclic 风格攻击者对 2023 年 12 月最新版 KataGo 在 4096 visits 下胜率 65%，65,536 visits 下 27%。他们还发现一种全新的 gift attack：制造“送二还一”局面，诱使 KataGo 莫名送出两子，再借 superko 规则阻止它回提，从而救活整块棋。2. iterated adversarial training：攻防交替，每轮先训 adversary 打败当前 victim，再微调 victim 去防它。每个 victim 都能防住见过的所有 adversary，包括原版 cyclic，但鲁棒性不迁移：第 9 轮的 victim 在 65,536 visits 下仍被新 adversary 赢 42%。另外还训出一种 atari attack，故意让很多子处于叫吃状态，并把通常很强的“双”变成诱导对方形成大环形棋块的工具。3. 把 CNN 换成 Vision Transformer，假设是 CNN 感受野局部，看不清大范围的环。结果训到超人水平的 ViT 在低 visits 下仍被原版攻击击败，微调后的 adversary 在超人水平的 visits 下也能赢它，说明问题不只在架构，可能和游戏的策略结构或 self-play 范式有关。总体上三种防御都被新攻击绕过，只是找攻击比对付未防御的 KataGo 需要更多算力。作者的结论是，连 Go 这种窄领域都难以做到鲁棒，现实场景只会更难，可能需要 latent adversarial training 或更好的 RL 算法来提升从对抗数据中泛化的能力。

