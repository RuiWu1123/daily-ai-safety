---
title: "“Features” aren’t always the true computational primitives of a model, but that might be fine anyways "
lab:
  - "Alignment Forum"
date: 2026-02-02
source: "Alignment Forum（METR；LawrenceC）"
url: https://www.alignmentforum.org/posts/iEx2KjwFse749BYsD
star: false
tags:
  - 可解释性
---

# “Features” aren’t always the true computational primitives of a model, but that might be fine anyways 

**来源**：Alignment Forum（METR；LawrenceC） · 2026-02-02 · [原文](https://www.alignmentforum.org/posts/iEx2KjwFse749BYsD)

## 简读

LawrenceC 的概念短文（作者自称已不做 mech interp），针对关于"feature"的争论（非线性 feature、linear representation hypothesis、SAE 是否恢复规范 feature）指出大家在用三种定义：1. 网络所实现算法的真正 computational primitives，但网络未必有唯一干净的算法，作者以 modular addition 的 MLP 为例，从暴力枚举到猜测分段线性近似乘法，最后才发现是在近似一个三角积分，目前能确定的"真"原语都只来自算法任务上的 toy model；2. 实践中的含义：模型表征的、可操控以合理改变行为的输入显著属性（如 SAE 的语言、时间 feature）；3. 理论工作直接假设 feature 存在（如 Toy Models of Superposition）。核心主张是 feature 处在一个谱上：纯记忆、case analysis / equivalence partitioning、真正的 computational primitives。以 bleggs vs rubes 为例，同一网络可描述为两个属性变量、四个物体方向，或每个数据点一个的记忆解；嵌入更大网络时 SAE 可能因重建损失和稀疏性偏好后两者，并随宽度逐级过渡（呼应 "fat giraffe" 批评）。作者过去也认为 SAE 只做 case analysis 就没用，现在认为 case analysis 本身有用，就像 equivalence partitioning 之于调试：若确认内部在簇间差异大、簇内相似，就能把检验（如对抗鲁棒性）化为逐类检查；记忆型 feature 也有用，因为不少真实知识本就是记忆的。建议争论混乱时回到计算视角，问对你的目的而言紧凑描述用什么组件，并在构造 linear representation hypothesis 反例时先想想你的 feature 是否是描述行为的唯一选择。

