---
title: "Language Model Circuits Are Sparse in the Neuron Basis"
lab:
  - "Transluce"
date: 2025-11-20
source: "Transluce"
url: https://transluce.org/neuron-circuits
star: false
tags:
  - 可解释性
---

# Language Model Circuits Are Sparse in the Neuron Basis

**来源**：Transluce · 2025-11-20 · [原文](https://transluce.org/neuron-circuits)

## 简读

Transluce 重新检验一个常见假设：neuron 不能干净地分解模型计算，所以做 circuit analysis 必须先学一个特征基（SAE、transcoder、CLT）。作者指出学出来的基也有代价：只能近似原模型，留下难以解释的误差项；feature 会以不直观的方式分裂或合并；模型一变就得重训，在整个训练过程中用起来很贵。他们只改了两处，就让 Llama 3.1-8B 上的 neuron 电路和 SAE 电路一样稀疏、一样 faithful：1. 节点用 MLP activations（非线性之后的那层，是 privileged basis），不用以往做对比时用的 MLP outputs，单这一项在 SVA（主谓一致）benchmark 上电路就缩小约 100 倍，attribution 分布更分散、离群值更多，各层分布也更均匀；2. 归因方法用 RelP（和 Jafari et al. 同期独立提出），不用 Integrated Gradients。RelP 在一个局部线性化的替代模型上做一次反向传播，并用 LRP 的 half rule 保证归因守恒，比要 10 次反向的 IG 更准也更快，补上了和 SAE 之间剩下的差距；没有成对反事实数据的 unpaired 设置下结论类似；做边归因时，RelP 只保留约 10% 的候选边就能达到 80% 以上的 faithfulness。随后他们只用 neuron 复现了 Anthropic 用 CLT 做过的三个案例：州首府多跳推理里 neuron 聚成 Dallas→Texas→Austin 各跳对应的簇，steering 结果和假设一致，单个"say a capital" neuron 在多数例子里就能把输出从首府翻成州名；两位数加法里找到了编码和的个位（mod 10）、十位的 neuron；多语言反义词里找到了数百个语言 neuron 和几十个概念/属性 neuron，但没有统一的"反义"neuron。还有一个新的 user modeling 案例：让模型填用户的维基百科信息框，追溯到编码其推断的用户性别等人口属性的 neuron，不过这些推断不固定存在某个 token 位置。作者强调目的不是判定 neuron 和学习基孰优孰劣，学习基可能确实更 monosemantic，而是推翻"neuron 天然不可解释"这个前提，呼吁今后提出新字典学习方法的工作都加上 neuron 基线；他们还认为 gated MLP、MoE 这些架构趋势都在偏向稀疏。局限：电路仍然太大，人读不过来，需要对 neuron 分组、改进自动描述、引入 agent 辅助；实现效率也不高。

