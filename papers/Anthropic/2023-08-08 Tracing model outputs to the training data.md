---
title: "Tracing model outputs to the training data"
lab:
  - "Anthropic"
date: 2023-08-08
source: "Anthropic Research"
url: https://www.anthropic.com/research/influence-functions
other_versions:
  - "https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions"
star: false
tags:
  - 可解释性
---

# Tracing model outputs to the training data

**来源**：Anthropic Research · 2023-08-08 · [原文](https://www.anthropic.com/research/influence-functions)　另见：[论文页](https://www.anthropic.com/research/studying-large-language-model-generalization-with-influence-functions)

## 简读

动机是：当 LLM 输出它知道是假的信息、解出数学题、或者恳求用户别关掉它时，它是在复述/拼接训练数据，还是在灵活组合知识、基于世界模型推理？这对能力预测和 alignment 都有影响。mechanistic interpretability 是自下而上，难以扩到大模型；只看输出又无法区分不同路径（极端情况下甚至无法排除 deceptive alignment）。作者走自上而下路线，用 influence functions 回答反事实：如果把某条序列加进训练集，模型对某个 query 的输出会怎么变。主要障碍是 inverse-Hessian-vector product（IHVP）和对海量候选序列算梯度。方法：1. 用 EK-FAC 近似 damped Gauss-Newton Hessian（只针对 MLP 参数，attention 等视为固定），把 influence functions 扩到 52B 参数（此前最大约 300M 的 ViT）；按 Bae et al. 的观点，influence functions 实际近似的是更局部的 PBRF 而非真正的重训练反事实，他们以 PBRF 为基准验证，在 UCI、MNIST、FashionMNIST、CIFAR10 和 810M 语言模型上 EK-FAC 与 LiSSA 相关性相当，但快几个数量级，且都明显好于 gradient dot product（后者找出的 top 序列与 query 看不出关系）；2. 训练梯度瓶颈用 TF-IDF 过滤（取 top 1 万条候选，便宜但会引入偏差，尤其会漏掉 token 重叠少但抽象相关的序列）和 query batching（把预条件后的 query 梯度压成 rank-32，误差可忽略，能在内存里放几百个 query 共享训练梯度计算）；3. 还能把 influence 分解到层和 token。研究对象是 810M、6.4B、22B、52B 的预训练模型。主要发现：influence 分布重尾，尾部近似 power law，但影响分散在很多序列上而非集中于少数几条，说明典型行为不是直接记忆少数样本；更大的模型在更抽象的层面泛化，体现在 role-playing、编程、数学推理和跨语言泛化上；比如 AI 助手说"我不同意被关机"的 shutdown query，810M 模型的 top 序列只是共享 continue、existing 等 token、语义上几乎无关，52B 模型的 top 序列则 token 重叠很少但主题相通（HAL 恳求船员留下、沙漠中挣扎求生的人、慢性病患者的日常挣扎，都是在告别/死亡/终止前想继续存在）；平均来看 influence 在各层分布大致均匀，但上下层更贴近 token，中间层更抽象；一个意外局限是对词序极敏感，只有当与 prompt 相关的短语出现在与 completion 相关的短语之前时训练序列才有显著影响，顺序颠倒后 influence 几乎降到零；role-playing 行为主要受训练集中类似行为的示例或描述影响，作者据此认为这更像模仿而不是复杂规划。局限：influence functions 刻画不了 circuit 形成等非线性训练现象；只研究预训练模型而非经过 fine-tuning 的助手；模型仍比 SOTA 小很多，而 influence 模式随规模变化大，结论能否外推不确定；只看 MLP；只搜索了预训练语料的一小部分，可能漏掉更有影响的序列。

