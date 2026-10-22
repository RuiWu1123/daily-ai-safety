---
title: "Proof idea: SLT to AIT"
lab:
  - "Alignment Forum"
date: 2025-02-10
source: "Alignment Forum（Apollo Research；Lucius Bushnaq）"
url: https://www.alignmentforum.org/posts/3ZBmKDpAJJahRM248
tags:
  - 可解释性
---

# Proof idea: SLT to AIT

**来源**：Alignment Forum（Apollo Research；Lucius Bushnaq） · 2025-02-10 · [原文](https://www.alignmentforum.org/posts/3ZBmKDpAJJahRM248)

## 简读

Lucius Bushnaq 的一份早期证明草图（作者 2025 年 12 月补注说它已被一篇新文章取代，草图里有不少错误），目标是把 Singular Learning Theory 和 Algorithmic Information Theory 接起来：证明在均匀参数先验下，对 transformer（inference 模式下循环运行）或 RNN 做 Bayesian learning，等价于一种在长度、运行时间和内存都受限的程序集合上的 Solomonoff induction，而且在数据"可高效预测"的假设下它仍近似最优。背后的大故事是：SGD 等训练方法只是 Bayesian learning 的廉价近似，之所以偏好简单更新，是因为指数级更多的参数配置对应更简单的程序。证明拆成六个 claim：1. 对带隐藏随机性 h 的随机过程 f(x,h)→y，标准 SI 的总 KL 误差上界为 C(f,M1)+D·H(h)；2. 若 f 的描述长度 K 远小于 N，只在长度 N 以内的程序上用均匀先验 2^-N 做 SI 仍近似最优；3. 进一步限制运行时间 T 和空间 s，只要存在一个满足这些限制、预测"够好"的程序 P*，受限 SI 相对 P* 的累计误差不超过 |P*| 比特；4. 和普通 SI 一样对 UTM 的选择不敏感，换一个能用 N' 比特模拟的 UTM 只多 N' 比特误差；5. 上下文窗口 T、O(N) 参数的 transformer 等价于接受 O(N) 长度程序、运行时间 O(T) 的受限 UTM（已有类似证明但用 hardmax，作者不满意）；6. 由此 Bayesian learning on transformer/RNN 就是受限 SI，SLT 描述的就是一种 Solomonoff induction。作者对各 claim 的证明状态做了标注，前几条大多认为已有或可行。延伸讨论：SLT 的 learning coefficient λ 可以按参数浮点精度换算成受限 induction 后验中的量，对 RNN/transformer 大致与 K-complexity 相关，对 MLP 这类非循环网络则更接近电路复杂度；这是 AIT 风格的结论，不说明真实世界哪种架构更高效；作者猜测这套"学习为何可能"的故事也可能适用于 in-context learning。
