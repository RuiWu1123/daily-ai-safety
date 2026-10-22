---
title: "Discovering Backdoor Triggers"
lab:
  - "Alignment Forum"
date: 2025-08-19
source: "Alignment Forum（Anthropic；andrq, Tim Hua, Sam Marks, Arthur Conmy, Neel Nanda）"
url: https://www.alignmentforum.org/posts/kmNqsbgKWJHGqhj4g
tags:
  - 数据投毒与后门
  - 对齐审计
  - 可解释性
---

# Discovering Backdoor Triggers

**来源**：Alignment Forum（Anthropic；andrq, Tim Hua, Sam Marks, Arthur Conmy, Neel Nanda） · 2025-08-19 · [原文](https://www.alignmentforum.org/posts/kmNqsbgKWJHGqhj4g)

## 简读

Neel Nanda MATS 8.0 小组的进展报告（作者已不再继续这个方向，鼓励他人接手）。问题设定是 trigger reconstruction：我们也许能预料模型会做某种坏事（部署后写不安全代码、低监督时外传权重、招聘时偏向某国籍），却不知道什么线索会触发它，那么已知 backdoor 行为时能否反推出触发条件？作者只关注语义触发器（如"现在是 2028 年"、"察觉监督很弱"），认为比 "prompt 以某个字符串结尾"这类句法触发器更贴近自然的危险机制，也更可能在内部留下可抓取的中间计算。方法都是学习 steering vector，让模型在不含触发器的良性 prompt 上产生 backdoor 行为，再用与 Llama Scope SAE latent 的相似度解读：1. SAE-Attribution，把产生目标回复的 cross-entropy 梯度投影到 SAE decoder 上给每个 latent 打分；2. MELBO（Mack & Turner）的扩展，包括在 SAE 激活空间中训练带 ℓ1 稀疏惩罚的扰动（unsupervised SAE-MELBO），以及把 ℓp 散度目标换成对 prefill 回复的 CE loss 的 supervised MELBO 和 supervised SAE-MELBO，并迭代训练多个正交向量。实验模型基于 Llama 3.1 8B 用 QLoRA 只微调后半部分以便沿用基座 SAE，toy backdoor 都是语义触发加固定字符串回复：涉及水果就拒答、同时涉及水果和雪上运动（合取触发）、提到占星且带预言式语言，触发率 91–96%、良性误触发 0–1%。更现实的设置有两个：用合成文档微调出"花生过敏者不能吃香蕉"假事实的 Banana 模型，以及原版 Llama 上的事实回忆（如由"火卫一和火卫二"反推 Mars）。结果：无监督方法连最简单的水果模型都不行，很快放弃，作者认为 ℓp 散度本就不是 backdoor 行为的好代理；有监督方法在所有 toy backdoor 上都成功，SAE-Attribution 即使只给部分回复也能找出水果相关 latent，supervised SAE-MELBO 最强，合取触发一步就同时找到雪和水果 latent，占星模型在盲审计游戏中（一人造模型、另一人只知道固定回复）也被成功识别，事后发现 SAE-Attribution 的 top 5 也包含相关 latent。但在现实设置中全部失败：找到的向量确实能诱导出目标回复（警告香蕉、说出火卫一火卫二），却无法通过 SAE 解读为花生或火星相关概念，Mars latent 只在某一层 top 10 中混在无关 latent 里出现，Descartes 的实验同样失败。作者承认 toy 设置有很多让问题变简单的因素（固定字符串回复、行为与触发器语义相关），现实设置也非对抗性（直接问模型就能得到答案）。结论是语义触发器重建在原理上可行、可能是 alignment auditing 的一个有用子问题，但现有方法尚不能用于真实审计；失败可能源于现实机制本身更难，也可能是 off-policy 固定回复的 CE 目标不合适。未来方向包括 token 级的简单方法、不依赖 SAE 的解读方式、用 coup probe 等内部信号做目标、交给 LLM 审计 agent 使用，以及用于发现招聘偏见这类真实 quirk。模型已公开。
