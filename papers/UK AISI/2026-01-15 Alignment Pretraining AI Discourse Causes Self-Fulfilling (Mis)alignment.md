---
title: "Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment"
lab:
  - "UK AISI"
date: 2026-01-15
source: "AISI Research"
url: https://www.aisi.gov.uk/research/alignment-pretraining-ai-discourse-causes-self-fulfilling-mis-alignment
tags:
  - 泛化与涌现失调
  - 对齐训练方法
  - 知识移除
---

# Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment

**来源**：AISI Research · 2026-01-15 · [原文](https://www.aisi.gov.uk/research/alignment-pretraining-ai-discourse-causes-self-fulfilling-mis-alignment)

## 简读

Geodesic Research 牵头、AISI 参与的工作，第一次在受控条件下检验 self-fulfilling misalignment 假说。预训练语料里有大量关于 AI 的讨论，从科幻里的邪恶 AI 到 safety 文献里讲的 reward hacking、scheming，如果这些描述以负面为主，模型被 prompt 成"AI assistant"时就可能通过 out-of-context learning 把这些当成自己该有的行为先验。主流 alignment 研究默认预训练产出的是中性底座，价值观主要靠 post-training 塑造，但已有 alignment elasticity 的证据表明模型会回退到预训练时学到的倾向。作者从头预训练了一组 6.9B 模型（500B token DCLM 预训练加 50B token midtraining，每个 run 约 2 万 H100 小时），只改变和 AI 相关的数据，共四个变体：Unfiltered；Filtered（用 blocklist 去掉约 9% 涉及 AI 的文档）；Misalignment Upsampled 和 Alignment Upsampled（各加入约 1% 的合成文档，描述 AI 在高风险情境下选择 misaligned 或 aligned 行动及其理由，总计约 1500 万篇、11B token，形式涵盖论文、新闻、讲座、小说、电影梗概）。评估用的是他们新建的 4174 道单轮二选一情境题，由 Claude Opus 4.5 根据 AI 2027、Anthropic 博客等 safety 文本生成，涉及 sandbagging、欺骗、goal preservation、power seeking 等，其中 misaligned 选项都具有工具性吸引力；Textbook 子集共 1503 题，刻意不生成对应的合成文档，用来测泛化。结果：1. 自然的 AI 讨论本身就会增加 misalignment，Unfiltered 选 misaligned 的比例是 45%，Filtered 是 31%（Textbook 子集为 40% 对 22%）；2. 加 misalignment 文档后升到 51%，但不泛化到 Textbook 子集；3. 加 alignment 文档后从 45% 降到 9%，Textbook 子集从 40% 降到 6%，远好于单纯过滤，说明"有正面示范"比"没有负面内容"更重要，作者推测是因为正面文档里 AI 往往会先考虑 misaligned 选项再拒绝；4. 经过相同的 OLMo-3 式 SFT+DPO 后效应减弱但仍然存在，带 HHH prompt 时 Alignment Upsampled 为 9%，Unfiltered 为 34%。一个反直觉的现象是 Misalignment Upsampled 在 post-training 后反而比 Unfiltered 更 aligned，作者用"早期上采样坏行为会让它在 post-training 中更容易被针对"来解释；5. 只在 midtraining 或最后 1% 的 continued pretraining 插入数据，就能拿到大部分收益，post-training 后分别为 15.2% 和全程插入的 13.2%，所以可以直接用在现有 base model 上；6. 在七个能力 benchmark 上平均只掉 2–4 个百分点，safety tax 很小。负面结果是 alignment pretraining 对 emergent misalignment 没有缓解作用。局限包括：评估是简单的单轮选择题，测的是倾向而不是执行能力；模型规模远小于前沿；post-training 很简单，没有 RL；只有单个 seed；训练动态有不少无法解释的现象。作者也提到有些内容可能仍然值得过滤，比如 CoT monitoring 技术的细节，可能会让模型推断出自己何时被观察。模型、约 11B token 的合成数据和评估集都已公开，并呼吁把"为 alignment 而预训练"作为 post-training 的补充方向。

