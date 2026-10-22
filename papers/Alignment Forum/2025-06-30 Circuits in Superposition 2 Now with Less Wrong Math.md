---
title: "Circuits in Superposition 2: Now with Less Wrong Math"
lab:
  - "Alignment Forum"
date: 2025-06-30
source: "Alignment Forum（Goodfire；Linda Linsefors, Lucius Bushnaq）"
url: https://www.alignmentforum.org/posts/FWkZYQceEzL84tNej
star: false
tags:
  - 可解释性
---

# Circuits in Superposition 2: Now with Less Wrong Math

**来源**：Alignment Forum（Goodfire；Linda Linsefors, Lucius Bushnaq） · 2025-06-30 · [原文](https://www.alignmentforum.org/posts/FWkZYQceEzL84tNej)

## 简读

这是 Linsefors 和 Bushnaq 对之前《Circuits in Superposition》的更正与续篇：原文给出一个把许多小网络压缩进一个大网络做 superposition 计算的框架草图，但多层误差传播算错了，按原框架误差会随层数爆炸。这里给出一个修正后的构造并重新推误差。关心的是真正的“computation in superposition”，即网络不仅以 superposition 存储特征，还跨多层用它们做比神经元数更多的计算，这比单纯存储多出额外噪音，从而限制能实现的计算量，对理解网络是否以及如何使用 superposition、进而对 mech interp 都很重要。设置是 T 个宽 d、L 层的小 MLP circuit 嵌入一个宽 D、L 层的大 MLP（d<D<Td，无 residual stream），每次前向最多 z≪T 个 circuit 活跃；假设 inactive circuit 所有神经元为零、对小噪音鲁棒（施加小扰动后下一层仍保持 inactive）、不同 circuit 权重不相关。构造上每个 circuit 神经元冗余嵌入到 S 个大网络神经元，同一 circuit 的神经元不重叠、不同 circuit 两两最多共享一个神经元、矩阵非负以保住 ReLU 的符号，分配算法基于素因子的步长设计，并且每层随机重排 circuit 的邻居关系（这一点是写代码时才发现的必要细节），unembedding 是 embedding 的转置除以 S，附 Colab 代码。误差分三项：embedding overlap（活跃 circuit 信号漏进其他 circuit）、propagation（上一层误差的传播）、ReLU 激活差异（证明基本可忽略）。关键结论：第 0、1 层几乎无传播误差（第一层可以直接把输入嵌成想要的样子，作者承认这算“作弊”但模型训练也会这么干），最大的误差直到第 2 层才出现，来源是活跃 circuit 的信号漏进 inactive circuit，再在下一层作为噪音回流进活跃 circuit；活跃 circuit 的噪音逐层累积，约为 √((l−1)zTd²/D²)，inactive circuit 的噪音不累积；要求平均误差小于信号需 √(zTd²/D²) 小，考虑最坏情况还需多一个 log T 和额外的 z 因子，于是可容纳的 circuit 数上界约为 T_max = Õ(D²/(z²d²))，即计算容量只随 D 二次增长，而单纯存储的容量随 D 指数增长。circuit 总参数量必须小于大网络参数量，符合直觉。误差能被压住靠的是 ReLU 的平坦段：不连接活跃 circuit 的神经元因噪音鲁棒而保持关闭，误差只能通过很少的“开着”的神经元传播，否则每层会放大 √(Td²/D²) 倍。对实验的启示：只有一层计算的 toy model 不需要实现降噪，研究这一现象需要 2 层以上或在输入加噪模拟。作者并不预测神经元激活稀疏（GPT-2 MLP 激活率约 20%），因为可以用多个 ReLU 组合成两端平坦的“meta 激活函数”；但暂时预测每个 circuit 只使用一小部分神经元，因为任何放过信号的连接也会放过噪音。Linda 的初步 toy 实验（单层无噪时不稀疏，输入加噪后出现稀疏连接）弱支持这一预测。作者也坦言手工实现时发现很多数学里含糊处理的细节（如需要负 bias），会另文讨论。
