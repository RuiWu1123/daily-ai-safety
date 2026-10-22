---
title: "Compressed Computation is (probably) not Computation in Superposition"
lab:
  - "FAR.AI"
date: 2025-12-05
source: "FAR.AI Publications"
url: https://www.far.ai/research/compressed-computation-is-probably-not-computation-in-superposition
star: false
tags:
  - 可解释性
---

# Compressed Computation is (probably) not Computation in Superposition

**来源**：FAR.AI Publications · 2025-12-05 · [原文](https://www.far.ai/research/compressed-computation-is-probably-not-computation-in-superposition)

## 简读

Computation in superposition 指模型在输入稀疏时能实现比自身非线性单元更多的非线性函数，是 superposition 研究里一个关键但缺少干净实例的问题。Braun et al.（APD 那篇）提出的 Compressed Computation（CC）toy model 看起来就是这样一个实例：一个带残差流的模型用 50 个神经元"计算"100 个 ReLU 函数，loss 比只完美表示 50 个 ReLU 的 naive baseline（0.0833）更低。这篇 NeurIPS 2025 mech interp workshop 短文重新审视这个模型，结论是它的优势很可能来自标签噪声而不是真正的 computation in superposition。关键观察是：带固定随机 embedding W_E 的残差架构在数学上等价于一个单层 MLP 去拟合 y = ReLU(x) + Mx，其中 M = I − W_E W_Eᵀ，也就是嘈杂的残差流在标签里引入了一个意外的 mixing matrix，模型除了 ReLU 还要学这个线性混合项。实验发现：1. 简化模型完全复现原结果，而且换成随机的（尤其对称的）M 也能几乎一模一样地复现；2. M = 0 时模型在稀疏区间根本打不过 naive baseline，在 M ≠ 0 上训好的模型拿到 M = 0 数据上 fine-tune 会立刻退回 naive loss，排除了"噪声只是帮助训练"的解释；3. loss 优势随 M 的幅度平滑增大（σ 约 0.03 以内越大越好，再大又变差）；4. 神经元的读写方向几乎都落在 M 前 50 个正特征值/奇异向量张成的子空间里，其余方向被强烈衰减，W_out W_in 的元素和 M 的元素高度相关，W_in 基本非负且稀疏。据此作者只用 M 构造了一个 semi-NMF 手工基线，它能打过 naive baseline 并定性复现 loss 随 σ 变化的曲线，但达不到训练模型的 loss，权重也没那么稀疏，所以这个模型并没有被完全逆向。附录还解释了 dense 区间的另一种解：一半特征各用一个神经元表示，另一半靠输出权重模拟 bias 偏移，手工的"naive + offset"解就能匹配。作者结论是 CC 不适合作为 computation in superposition 的 toy model，希望大家另找更合适的模型。代码开源。

