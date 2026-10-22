---
title: "Replicating Circuit Tracing for a Simple Known Mechanism"
lab:
  - "Goodfire"
date: 2025-06-11
source: "Goodfire Research"
url: https://www.goodfire.com/research/replicating-circuit-tracing-for-a-simple-mechanism
tags:
  - 可解释性
---

# Replicating Circuit Tracing for a Simple Known Mechanism

**来源**：Goodfire Research · 2025-06-11 · [原文](https://www.goodfire.com/research/replicating-circuit-tracing-for-a-simple-mechanism)

## 简读

Anthropic 提出 Cross-Layer Transcoder（CLT）和 attribution graph 做 circuit tracing 之后，一个自然的问题是这套方法在机制已知的任务上能不能还原出正确答案。Goodfire 在 GPT-2 Small 上训练 CLT（FineWeb 1 亿 token，expansion factor 64，每层 49,152 个 feature、12 层共约 59 万个，用 ReLU 而非 JumpReLU，最好的模型 L0 为 79、token 准确率 59%，与 Ameisen et al. 报告的一致），拿 Hanna et al. 已经部分逆向过的 greater-than 任务（"The war lasted from the year 17YY to 17"，模型要预测大于 YY 的年份，原文发现是若干 MLP 神经元压低小于 YY 的年份、抬高大于 YY 的年份）做验证。他们自己复现了图构建和剪枝算法，只用单个 prompt "1711" 建图选 feature（按到 top 10 logit 的 attribution 各取 top 16），再在约 100 个不同年份的 prompt 上复刻 Hanna 的 logit attribution 热图（CLT feature 会解码到之后所有层，所以把后续各层 decoder 向量求和）。结果：CLT 确实"开箱即用"地找到了相关且可解释的 greater-than feature，不需要原文那种费力的干预实验，有的 feature 只针对日期，有的泛化到价格、百分比，甚至能响应罗马数字年份；但整体比 Hanna 的结果更乱：一些排名最高的 feature 热图几乎不依赖输入年份，另一些只在极窄的输入范围（比如只对 11）起作用，更像特例查表；还有排第 14 的 feature 实现的是反向的"偏好小数"机制；另有一组与任务看似无关的 structured number feature，包括一个抽象的 parity/对立 feature（奇数输入时提升偶数输出，最高激活样本是 "pros and cons" 里的 "and" 这类对比配对的第二项之前）、偏好 5 的倍数、偏好以 2 结尾等，作者指出这和 Lindsey et al. 两位数加法里的启发式 feature 相似。局限：很多 feature 的 logit attribution 热图与最高激活样本互相矛盾，可能因为 logit attribution 孤立地看单个 feature，而且该方法本为 Transformer 设计、未必适用于 CLT；只用单个 prompt 选 feature 可能引入干扰 feature；为了和原文对比只看了最后一个位置，没有利用 CLT 跨位置追踪的长处。作者的结论是 CLT 能半自动发现有意义的结构，但稀疏替代模型对计算机制的分解方式可能和原模型的真实机制有差异，值得进一步研究（如与非稀疏模型中螺旋状数字表示的关系）。

