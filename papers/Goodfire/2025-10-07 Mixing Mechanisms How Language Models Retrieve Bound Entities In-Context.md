---
title: "Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context"
lab:
  - "Goodfire"
date: 2025-10-07
source: "Goodfire Research"
url: https://www.goodfire.com/research/mixing-mechanisms
other_versions:
  - "https://arxiv.org/abs/2510.06182"
star: false
tags:
  - 可解释性
---

# Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context

**来源**：Goodfire Research · 2025-10-07 · [原文](https://www.goodfire.com/research/mixing-mechanisms)　另见：[arXiv paper](https://arxiv.org/abs/2510.06182)

## 简读

研究语言模型怎么做 entity binding 和检索：读到 "Pete loves jam, Ann loves pie" 后被问 "Who loves pie?"，模型如何取回 Ann（Gur-Arieh、Geva、Geiger，Tel Aviv 与 Goodfire，ICLR 2026）。此前工作认为模型用 positional mechanism，即用查询实体定位它所在的是第几组、再按位置索引取出答案，但这些证据只来自 2–3 组的短列表，或在 7 组时 faithfulness 很低。作者用 interchange intervention 在最后一个 token 的 residual stream 上做 patching，精心设计原始/反事实输入对，使三种候选机制在 patch 后各自预测不同的实体：positional（按组序号检索）、lexical（用被绑定的对应实体 pie 去找 Ann）、reflexive（通过一个直接指向目标实体本身的指针检索；之所以需要它，是因为自回归注意力只能从右往左看，当目标出现在查询实体之前时 lexical 机制无法实现）。在 Gemma-2、Qwen2.5、Llama-3.1 共九个 2B–72B 模型和十个绑定任务上，结果呈现一致的模式：20 组实体时，positional 机制只在首尾位置可靠，中间位置只能解释约 20% 的行为，而且信号变得弥散、常常指向邻近的组；这时 lexical 和 reflexive 机制给出尖锐的 one-hot 信号来补救，至于用哪个取决于目标实体在组内的位置（在组首主要靠 reflexive，在组尾主要靠 lexical，在中间两者都用），三者之间还存在既相互增强又相互抑制的"competitive synergy"。他们另设计反事实答案不出现在原文中的数据，确认 reflexive 确实是无法解引用的指针而不是直接复制答案，并排除了"抑制上下文外实体"的替代解释。在此基础上建立了一个 causal model：positional 项用 Gaussian 建模（标准差是位置的二次函数），lexical 和 reflexive 项用按位置学习权重的 one-hot，预测模型下一个 token 分布的 Jensen–Shannon 相似度达到 0.95，接近 oracle；只用 positional 的传统观点只有 0.44，甚至低于均匀分布基线的 0.5，把 Gaussian 换成 one-hot 也会降到 0.85。在组与组之间插入无关的填充句子（每组之间最多 500 token）后，模型在 token 数增加十倍时仍然成立，但随着填充增多 lexical 机制减弱、positional 信号变得更嘈杂，作者认为这可能是 "lost-in-the-middle" 现象的一个机制性解释。代码和数据已开源。

