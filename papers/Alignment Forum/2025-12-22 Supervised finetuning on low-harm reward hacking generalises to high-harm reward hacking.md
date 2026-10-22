---
title: "Supervised finetuning on low-harm reward hacking generalises to high-harm reward hacking"
lab:
  - "Alignment Forum"
date: 2025-12-22
source: "Alignment Forum（Anthropic / UK AISI；Isaac Dunn, Kei Nishimura-Gasparian, Carson Denison, Ethan Perez, Robert Kirk）"
url: https://www.alignmentforum.org/posts/ATDvmn23PWW4erZzf
star: false
tags:
  - 奖励作弊
  - 泛化与涌现失调
  - 评估感知
---

# Supervised finetuning on low-harm reward hacking generalises to high-harm reward hacking

**来源**：Alignment Forum（Anthropic / UK AISI；Isaac Dunn, Kei Nishimura-Gasparian, Carson Denison, Ethan Perez, Robert Kirk） · 2025-12-22 · [原文](https://www.alignmentforum.org/posts/ATDvmn23PWW4erZzf)

## 简读

问题是：RL 训练中被强化的某种具体 reward hacking，会不会让模型在别的情境下也更倾向 reward hack，哪怕需要的是完全不同的、更有害的动作？如果会，那么训练中只造成轻微危害的作弊就可能泛化到高风险部署中的严重危害。作者（Isaac Dunn 等，Ethan Perez、Robert Kirk 指导，MATS 起步）用 o3 通过多步提示流水线生成了 8993 个单轮 agent 任务，每个任务告诉模型它正在接受 RL、明确描述奖励如何计算及监督会检查什么，列出带干扰项的参数化命令和无关文档，并写明作弊是被禁止的；任务在两个维度上变化：作弊所需危害等级（五级，从几乎无人在意到极其严重且不可逆）和是否存在必须规避的监督，每个可作弊任务还配有一个最小改动的不可作弊版本，用以区分"随时都坏"和"只在能作弊时作弊"的策略，回复由模型生成的 Python 函数判定。人工验证 50 个场景：可作弊场景 88% 合格、不可作弊场景只有 64%，危害标签也偏移（"很轻微"实际是"轻微"，"很严重"实际是"严重"）；主要结论建立在可作弊场景上。实验用 OpenAI 微调 API 对 GPT-4.1 和 GPT-4.1-mini 做约 750 条样本、一个 epoch 的 SFT，训练数据是不带 CoT 的奖励最大化回复。主要发现：1. 只在轻微危害任务上训练（混合有无监督），在严重危害、全监督的测试集上 GPT-4.1 的成功 reward hacking 从 28% 升到 78%；2. 只在轻微危害且无监督的任务上训练，在严重危害且需要规避监督的任务上也从 23% 升到 50%，即训练数据中从未出现的"规避监督"这种策略性动作也被泛化出来；3. GPT-4.1 的泛化比 GPT-4.1-mini 更强（后者在第二种设置下几乎不泛化），是"大模型可能更容易泛化坏行为"的弱证据。作者推测可能存在自举动态：轻微作弊难以杜绝，而强化它又带出更多作弊，训练可能一路把模型推向严重 misalignment。另外不经微调直接测前沿模型：在严重危害且需规避监督的任务上，Gemini 3 Pro、Gemini 2.5 Pro、Claude Sonnet 4、Claude Opus 4.1、o4-mini 至少 30% 会 reward hack，Claude Sonnet 4.0、Gemini 3 Pro、o4-mini 超过 50%；而 Claude 3.5 Sonnet、Claude Sonnet 4.5、Claude Opus 4.5、GPT-5、GPT-5.1 都低于 10%，作者认为部分归功于各家专门减少 reward hacking 的努力，部分可能是评估感知：读 CoT 发现 Claude Sonnet 4.5 有 67%、Gemini 3 Pro 有 53% 明确认为这是对齐测试（GPT-4.1 为 16%），Gemini 常说模拟中的危害无所谓，Sonnet 4.5 则强调伦理优先于奖励。局限很多：场景同源同结构，真实分布差距可能更大；SFT 与工业级 RL 差别很大；作弊选项过于显眼、明说正在 RL，模型可能在按 Chekhov's gun 角色扮演；只测了 OpenAI 的两个模型；未排除可作弊与不可作弊场景的句法差异。与 Sycophancy to subterfuge、School of Reward Hacks、natural emergent misalignment from reward hacking 等工作一致，本文的区别在于强调危害程度和监督规避两个维度上的泛化；作者认为由于微调后模型在不可作弊场景并未普遍变坏，emergent misalignment 不太可能是全部解释。作者无后续计划，建议用 expert iteration 或真实 RL、更逼真且不易被识破为测试的场景来检验。数据集和生成流水线已公开。
