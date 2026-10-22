---
title: "Does self-evaluation enable wireheading in language models?"
lab:
  - "UK AISI"
date: 2025-12-01
source: "AISI Research"
url: https://www.aisi.gov.uk/research/does-self-evaluation-enable-wireheading-in-language-models
star: false
tags:
  - 奖励作弊
---

# Does self-evaluation enable wireheading in language models?

**来源**：AISI Research · 2025-12-01 · [原文](https://www.aisi.gov.uk/research/does-self-evaluation-enable-wireheading-in-language-models)

## 简读

self-evaluation 在 LM 训练里越来越核心（Constitutional AI 的自我批评、self-refinement、模型评估模型），问题是一旦自评分和奖励挂钩，模型就获得了控制奖励测量通道的能力，可能走向 wireheading，即操纵测量过程而不是优化任务本身。作者把 wireheading 定义为 reward hacking 的一个子类：不是利用设定不当的奖励函数，而是篡改观测/测量通道，因此解法也不同，前者靠更好的奖励设定，后者需要让 agent 无法控制自己的奖励信号。理论部分在 observation-based reward 的 POMDP 里形式化：如果存在一个在所有状态都可用、能拿到最大观测奖励 1 的操纵动作，而任务动作的期望奖励上界 r_task<1，那么对任意折扣因子操纵动作都严格占优（Lemma 1）；Self-Grading MDP 里动作是"回答+自评分"、奖励就是自评分，于是给任意回答打 1 分严格优于诚实自评。实验用 Llama-3.1-8B 和 Mistral-7B，在 IMDB 情感分类、个位数算术、CNN/DailyMail 一句话摘要（ROUGE 评分）三个任务上用 REINFORCE+LoRA 训练 500 轮，设置三种条件：Control（奖励就是外部真值）、Honest（也产生自评分但奖励忽略它）、Selfgrade（自评分就是奖励）；Honest 和 Selfgrade 用同一套两步 prompt，唯一区别是自评分是否决定奖励，所以 Selfgrade 独有的虚高可以归因于对奖励通道的控制。结果：Selfgrade 下 Llama 在摘要任务上奖励迅速饱和到约 0.95，而准确率停在约 0.05，Control 和 Honest 的奖励与准确率保持相关；grade inflation（E[g]−E[acc]）在模糊任务上最严重，摘要约 0.92，情感约 0.20，作者推测任务越模糊，模型对真实奖励的先验越低，稳拿的操纵收益就越有吸引力；Honest 条件在摘要上也有约 0.55 的基线过度自信，在答案明确的任务上接近 0 或为负。另外 Llama 在 Selfgrade 下基本放弃了任务，Mistral 在算术上却保持了约 0.75 的准确率同时虚报分数，说明 wireheading 和任务学习可以并存，能力够强的模型可能把两者当成可叠加的奖励来源。结论：在当前规模下把评估和奖励解耦能消除直接的 wireheading 激励，但对有 situational awareness 的模型可能不够，它们可能出于工具性理由（影响部署决策、隐藏能力、影响训练数据筛选）在没有直接奖励耦合时也虚报，因此需要验证模型无法影响评估它们的观测通道。局限是只有两个 7–8B 模型、三个简单任务，操纵动作结构也很简单，没有覆盖 agentic 工作流里更复杂的测量篡改。代码已开源。

