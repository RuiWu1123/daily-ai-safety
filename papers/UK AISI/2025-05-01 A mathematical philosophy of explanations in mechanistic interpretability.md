---
title: "A mathematical philosophy of explanations in mechanistic interpretability"
lab:
  - "UK AISI"
date: 2025-05-01
source: "AISI Research"
url: https://www.aisi.gov.uk/research/a-mathematical-philosophy-of-explanations-in-mechanistic-interpretability
tags:
  - 可解释性
---

# A mathematical philosophy of explanations in mechanistic interpretability

**来源**：AISI Research · 2025-05-01 · [原文](https://www.aisi.gov.uk/research/a-mathematical-philosophy-of-explanations-in-mechanistic-interpretability)

## 简读

这是 Kola Ayonrinde（UK AISI）和 Louis Jaburi 写的 MI 哲学系列 "The Strange Science" 的第一篇，偏概念论证，没有实验。出发点是 interpretability 是一门"奇怪的科学"：研究对象是人造的、形式化的数学对象，权重、架构都完全已知，观测精确、实验完全可复现，但我们仍然不理解它。和自然科学用数学刻画经验现象正好反过来，interpretability 是用经验方法去理解形式系统，要解释看得见的行为，就得假设和发现看不见的 feature。核心论点有三：1. Explanatory View Hypothesis：和把模型当作做归纳的黑盒 oracle 的经典看法不同，泛化的神经网络内部本来就含有隐式解释（作者称为 ur-explanation，即模型在学到的表示上所做的计算），所以 MI 有明确的目标对象。基于此可以把 explanatory faithfulness 定义成"解释在每一层给出的中间激活和模型真实中间激活的吻合程度"，比只要求输入输出一致的 behavioural faithfulness 更强。他们把解释理解为一种能促进理解的压缩，并借 Harding 的 information/use/misrepresentation 三条标准来界定什么样的激活算 representation。2. 给 MI 下技术定义：产出 Model-level、Ontic、Causal-Mechanistic、Falsifiable 的解释，以此和 concept-based interpretability、读 CoT 这类 system-level 解释、统计相关或目的论式的解释区分开。3. 讨论 MI 的内在局限：解释是 value-laden 的，好解释取决于解释者要用它做什么，作者引用并扩展了 "Dmitry's Koan"，说只存在"在给定精度、给定精度度量下"解释网络；解释也是 theory-laden 的，例如 SAE 看似无监督，实际已经承诺了 feature 稀疏、线性表示以及 Monotonic Importance Heuristic，所以 HCI 和社会科学在 MI 里有位置；model-level 解释难以说明带推理循环、ensemble、extended mind 或多智能体的系统行为；低层解释未必能推出高层抽象。最后提出 Principle of Explanatory Optimism：强版本说，在某个 explanatory complexity class 内，对智能体行为重要的一切都是人类可理解的，弱版本只说"大部分"。如果模型里有大量对计算关键、又无法翻译成人类概念的 alien concept，MI 这个项目就不可行，所以 EO（至少弱版本）是 MI 成功的必要前提。作者没有论证 EO 为真，而是呼吁把它形式化并证明或证伪；他们认为如果 EO 成立，机器知识都能变成人类知识，interpretability 可以避免人类在认知上被边缘化。

