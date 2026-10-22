---
title: "From SLT to AIT: NN generalisation out-of-distribution"
lab:
  - "Alignment Forum"
date: 2025-09-04
source: "Alignment Forum（Goodfire；Lucius Bushnaq）"
url: https://www.alignmentforum.org/posts/2MX2bXreTtntB85Zy
tags:
  - 泛化与涌现失调
---

# From SLT to AIT: NN generalisation out-of-distribution

**来源**：Alignment Forum（Goodfire；Lucius Bushnaq） · 2025-09-04 · [原文](https://www.alignmentforum.org/posts/2MX2bXreTtntB85Zy)

## 简读

Lucius Bushnaq（Goodfire）的理论文章，动机是 Singular Learning Theory 描述神经网络上的 Bayesian learning 时假设数据 IID 且样本数趋于无穷，很难用来推理 OOD 泛化（比如户外动物图片训练的分类器能否泛化到室内）；而 Algorithmic Information Theory 里的 Solomonoff induction 不需要 IID、不依赖无穷数据、能描述 OOD 泛化，只是不可计算。所以他想给神经网络推一个 AIT 风格的误差界。第一部分主要用来建立直觉：1. 把 Solomonoff induction 搬到输入-标签对的监督设置，用 plain（非 prefix-free）monotone UTM 和长度为 T 的程序上的均匀先验，只要生成数据的程序长度不超过 T，累计期望交叉熵误差仍被其 Kolmogorov 复杂度加上数据本身熵所界住；关键在于不用手动在先验里偏好短程序，实现的简并性（短程序后面可以随意填充垃圾比特）自然让简单程序获得至少 2^-C 的概率质量；2. 限制程序的时间 t 和空间 s 得到可计算的 bounded induction，此时界变弱为：对任何在资源限制内可运行的“高效预测器”μ*，误差不超过 μ* 的描述长度加上 μ* 自身的预测误差（多出一个与真实过程的累计 KL 项），至于为什么现实中常存在这种高效预测器，作者坦言不知道，也许和世界善于抽象有关；3. 换 UTM 只需 O(s) 空间和 O(t log² t) 时间，额外误差只是两台机器互相模拟的描述长度，因此仍近似 UTM 无关。第二部分是主结果：对在参数超立方体上取均匀先验的参数化函数族（只要求一个参数到函数的映射）做 Bayesian learning，不假设 IID，累计误差不超过 C(w*,ε,f) + Nε + 参考函数 f(w*) 的累计误差，对任意 w* 和容忍度 ε 成立，其中 C 是先验体积与“在所有输入上 log 概率都与 f(w*) 相差不超过 ε 的参数集合”体积之比的对数，即用 ε 精度在参数空间中指定这个解的比特数。它与 SLT 定义 learning coefficient 的 ε-volume 很像，区别正是 OOD 的代价：SLT 用训练分布上的平均 KL，这里要在所有可能输入上取上确界；SLT 取 ε∝1/N 专注无穷数据极限，这里 ε 留作自由参数以适用任意 N；若确知部署输入的范围（比如亮度上限）可以缩小输入集合来收紧界。开放问题：神经网络的参数先验在多大程度上等价于有界 UTM 的程序先验，作者猜测“UTM 模拟神经网络”方向的猜想大致成立，但反方向对任意架构多半不成立（多项式族也满足这里的定义），对能模拟 UTM 的架构（RNN、CoT 模式的 transformer）也还没证出来，难点是让未用参数无论取何值都不干扰计算；以及实践中 C(w*,ε,f) 是否像 SLT 那样在 ε→0 时按 −λ′log ε 缩放、能否用 SGLD 估计、它比分布内的对应量大多少（即 OOD 与分布内泛化误差通常差多少）。作者认为第一部分大概都不新，但很多懂 AIT 的人并不了解简并性这一点。
