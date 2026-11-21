---
title: "Interpreting Inkling 2 Mini"
lab:
  - "Goodfire"
date: 2026-11-20
source: "Goodfire Research"
url: https://www.goodfire.com/research/interpreting-inkling-2-mini
star: false
tags:
  - 可解释性
---

# Interpreting Inkling 2 Mini

**来源**：Goodfire Research · 2026-11-20 · [原文](https://www.goodfire.com/research/interpreting-inkling-2-mini)

## 简读

背景是新架构在不断偏离标准 transformer，可解释性工具能否跟上是个现实问题。Thinking Machines 发布开源权重的小模型 Inkling 2 Mini 时提前把权重给了 Goodfire，这篇是他们的初步分析。这个模型有两处与普通 transformer 不同：一是 attention residuals，24 层分成 4 个 block（每个 6 层），每层通过 depth-wise attention 从各 block 的累加输出中读取输入，没有单一的 residual stream；二是 looping，第一个 block 只跑一次，中间两个 block（第 7–18 层）循环三次，最后一个 block（作者称为 coda）跑一次负责解码，循环之间通过 cross-loop attention 读取上一轮 block 2、3 的输出。作者利用这一结构把每层输入精确分解成之前各层输出的加权和（份额加起来正好是 1），在 400 篇 FineWeb 文档的 13,233 个 token 上可视化信息流：depth-wise attention 偏向最近的层，类似滑动窗口；后面的循环更多读 block 3，block 3 几乎总是读上一轮的自己，所以出现了"层写给自己"或"读取未来层"这类反直觉现象。权重空间上，他们检查了全部约 354 万个 MoE 写入向量与 104 个"reader"权重的余弦相似度，发现各 block 的最后几层大量写向这些 reader，像是给激活打标签，告诉后面的层该读哪个 block。激活空间上，他们发现巨大的离群激活，比如第 2027 维 RMS 归一化后平均值达 +32.4，占激活总平方范数的 46%；它在前两轮循环的第 18 层激增，引导下一轮读 block 3，并且是第 13 层 cross-loop reader 门控项的最大或第二大贡献者（单独贡献 6%–19%，前 5 个离群维度合计 30%–62%）；到第三轮结束、不再有后续循环时，模型又把这一维的激活"清理"掉。解码方面，logit-lens 只在每轮循环的最后几层有效，tuned-lens 和直接套用最后一个 block 的 coda-lens 效果很好；与标准 transformer 不同，早期循环的层反而更可解释，各 block 中间的层较难解码。作者强调这是早期结果，认为它说明在这些架构改动下模型内部计算依然可解释，并提到 NDIF 的 Looped Lens Challenge。
