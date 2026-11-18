---
title: "Discovering Neuron Communities in Language Models"
lab:
  - "Goodfire"
date: 2026-11-17
source: "Goodfire Research"
url: https://www.goodfire.com/research/neuron-communities
star: false
tags:
  - 可解释性
---

# Discovering Neuron Communities in Language Models

**来源**：Goodfire Research · 2026-11-17 · [原文](https://www.goodfire.com/research/neuron-communities)

## 简读

背景是单个神经元常被认为难以解释：一个神经元会在看似无关的上下文里激活，一个 prompt 又会同时激活很多神经元，这也是 transcoder、参数分解等方法放弃神经元基底的理由；但近来一些工作（Arora et al. 2025 在主谓一致上找到与 learned-feature circuit 同样稀疏忠实的神经元 circuit，Feucht et al. 2026 找到 28 个实现十进制加法的神经元，Goodfire 自己的 Tigges et al. 2026 发现模型可以在神经元基底上大幅稀疏化）提示，很多计算其实只由很少的神经元承担。这篇 Goodfire 研究提出 neuron community discovery，一种无监督方法，用来找出反复一起实现常见行为的神经元小组，而不预先指定要找什么功能。做法分三步：1. 在 Llama-3.1-8B 上跑 1000 万条 FineWeb-Edu、英文维基和 FineMath 的 prompt，用基于梯度的 attribution 估计每个神经元对每次下一 token 预测的贡献；2. 建一张图，节点是神经元，边是两个神经元一起被归因的频率（按各自出现频率校正）；3. 用图的社区检测找出群组。之后在 held-out prompt 上做因果检验：necessity 是消融该社区后预测明显改变，sufficiency 是把相关层里其它 MLP 神经元几乎全部消融、只留该社区时预测基本保持。案例是一个横跨 6 层、只有 6 个神经元的社区，负责"an"之后接元音开头的词，消融后模型改选"a"后面会用的辅音开头词。作者称在 Llama 上找到了数千个这样的社区，往往不到 10 个神经元，类别包括语法一致、检索与计算（单位换算、乘法、七个神经元帮助检索 prompt 前文出现过的名字）、特定话题（如三角函数）、格式规则（继续全大写）、常见短语（37 个神经元负责 carry out、find out 这类短语动词里的"out"）以及最常见的 token suppression（通常 1–2 个神经元压制某个特定词）；按层分布看，语法类集中在第 18 层以后，检索与算术在 17–22 层达到高峰，token suppression 集中在最后几层。他们还在 Qwen 3.6 35B-A3B 上复现，找到数十万个社区，其中不少编码具体知识，如各州首府。局限上作者说得很清楚：sufficiency 只针对包含社区神经元的那几层，模型其它部分仍在贡献预测；很多预测仍无法解释；找到必要且充分的社区也不等于知道这些神经元具体怎么计算、怎么与模型其余部分交互。作者的定位是把神经元社区当作介于单个神经元与高层计算之间的抽象层，并且因为可以无监督地大规模发现，可以给自动化的可解释性 agent 提供具体的研究起点。附有在线 neuron community explorer。
