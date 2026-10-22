---
title: "Challenge: Hand coding weights for efficient sequence memorisation"
lab:
  - "Alignment Forum"
date: 2026-07-23
source: "Alignment Forum（Goodfire；Linda Linsefors, Lucius Bushnaq）"
url: https://www.alignmentforum.org/posts/KWtchKwwnJkd4bwCi
star: false
tags:
  - 可解释性
---

# Challenge: Hand coding weights for efficient sequence memorisation

**来源**：Alignment Forum（Goodfire；Linda Linsefors, Lucius Bushnaq） · 2026-07-23 · [原文](https://www.alignmentforum.org/posts/KWtchKwwnJkd4bwCi)

## 简读

Linda Linsefors 和 Lucius Bushnaq（Goodfire）想弄清 LLM 里的 look-up 在权重层面究竟怎么编码。已有工作（Geva 的 key-value memory、ROME、MEMIT、Allen-Zhu & Li 的 bits/参数、Nichani 等的容量定理）把 MLP 指为事实存储位置，但都还不是对真实模型存储机制的权重级解释。他们用 sequence memorization 当 toy model：两个随机输入 token 映射到随机标签，没有结构可压缩，只能死记，代表那种"信号组合的含义与各信号线性组合大不相同"的查找。第一步是对单层 transformer 的各组件做开关消融（attention、MLP、norm、残差、bias、激活函数），用二分搜索测 Adam 能学会的最大事实数：MLP 是最关键的部分，能多学 60%–373% 的事实；把 attention 换成两个位置各自的 token embedding 直接相加（2Emb）效果相当甚至更好，uniform attention 也胜过 learned attention（后者表达力更强，说明是训练难度问题），可见在这个任务里 attention 只是把两个 token 的信息线性混到一处；norm 次之，其余影响较小，另外 MLP+Norm+无残差+无 bias+ReLU 这一组合表现异常差，原因不明。扩展实验显示可学事实数大约随模型维度平方增长，与信息论预期相符。由此他们提出一个"理解的 benchmark"挑战：在只保留 embedding + ReLU 层 + unembedding 的简化架构上（隐藏宽度小于输入词表），不用梯度下降或通用黑箱优化器，而用闭式计算、贪心或组合构造写出权重，看能否匹配训练模型的 scaling 指数和前置系数，分 acc=1、acc≥0.9 以及只手写 embedding、训练 unembedding 的 hybrid 四种标准。他们自己的构造：给每个标签分配一组 S 个 ReLU 神经元（神经元在标签间重叠，即某种 superposition），设计 embedding（取值仅 1、0、−1）使得属于标签 y 的事实一定让 y 的所有神经元都不激活，再给这些神经元到 y 的 logit 赋负权重——利用 ReLU 把负值精确置零这一点来做精确判别。结果：acc≥0.9 时手写模型的 scaling 指数接近训练模型（1.93 vs 1.97）但事实数少约 9.7 倍；acc=1 时差距随规模扩大（在测试的最大规模上约少 27 倍），说明算法有缺陷；hybrid 两个标准下都与训练模型同指数、只少约 3.5 倍，且明显优于随机冻结 embedding 的基线。权重对比显示训练模型用的是激活神经元的模式而非不激活的模式，分布也更平滑。他们也提到 Dugan et al. 的门控 MLP 构造初步看效果更好，但不像梯度下降会学出的东西，附录还给出了隐藏宽度比词表多一时能 100% 存下全部可能事实的近最优构造，同样不太"自然"。作者认为这是非零进展但差距仍大，公开代码并邀请社区挑战。

