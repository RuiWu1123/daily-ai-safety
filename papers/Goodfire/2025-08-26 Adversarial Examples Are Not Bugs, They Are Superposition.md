---
title: "Adversarial Examples Are Not Bugs, They Are Superposition"
lab:
  - "Goodfire"
date: 2025-08-26
source: "Goodfire Research"
url: https://www.goodfire.com/research/adversarial-examples-are-not-bugs-they-are-superposition
other_versions:
  - "https://arxiv.org/abs/2508.17456"
star: false
tags:
  - 可解释性
  - 越狱与鲁棒性
---

# Adversarial Examples Are Not Bugs, They Are Superposition

**来源**：Goodfire Research · 2025-08-26 · [原文](https://www.goodfire.com/research/adversarial-examples-are-not-bugs-they-are-superposition)　另见：[arXiv paper](https://arxiv.org/abs/2508.17456)

## 简读

对抗样本研究了近十年仍没有公认的根本机制，Goodfire 的 Liv Gorton 和 Owen Lewis 认为 superposition 可能是一个主要成因甚至首要成因，扩展了 Elhage et al. 2022 在 Toy Models of Superposition 里提过但没深入的猜想。机制直觉是：特征数多于维度时特征方向不可能正交，模型靠负 bias 压掉平均情况下的小干扰，但攻击者可以同时轻微激活许多与目标特征有重叠的特征，让干扰累积到压倒 bias，而且可以逐层叠加。论文给出四条证据：1. 理论上 superposition 可以解释已知的各种对抗现象，包括普遍存在、扰动像高频噪声（攻击的是只因 superposition 才相关的无关特征）、跨模型可迁移（同样的特征倾向于彼此 superposition）、对抗训练代价高且损害准确率（降低 superposition 等于牺牲容量）、鲁棒模型更可解释（神经元更单义）、以及 Ilyas et al. 的"在错误标签攻击上训练也能迁移到干净数据"；2. 在 100 特征压到 20 维的玩具模型里用特征稀疏度作为工具变量控制 superposition，superposition（features per dimension）越高对抗脆弱性越高，复现 Elhage 式攻击时相关系数约 0.99，在 antipodal superposition 处有一个明显的脆弱性下降；3. 反过来对玩具模型做对抗训练，superposition 下降，非鲁棒模型的平均非对角干扰约为鲁棒模型的 2 倍，对抗输入在非鲁棒模型里激活一大片互相干扰的特征，而鲁棒模型基本保持原有的 superposition 几何结构、只是程度更低，作者称这是首次展示从鲁棒性到 superposition 方向的因果；4. 在真实模型上用 Madry 组的 ImageNet 鲁棒 ResNet18，以 SAE 重建误差作为 superposition 的代理，越鲁棒的模型在相同稀疏度下 SAE 重建越好；对抗样本也比干净样本激活更多 SAE 特征，PGD 在最后一层达到 2.8 倍。局限是作者自己承认的：真实模型里没法直接干预 superposition，只能证明鲁棒性影响 superposition，不能量化 superposition 对脆弱性的贡献占比，而且依赖代理变量（v2 还修正了 Figure 6 夸大差异的绘图 bug）；另外同等 superposition 水平下不同干扰结构的鲁棒性不同，也有待解释。结论层面，如果 superposition 是主因，鲁棒性与模型容量之间就存在根本性的取舍，同时意味着可解释性与鲁棒性研究的目标高度一致。

