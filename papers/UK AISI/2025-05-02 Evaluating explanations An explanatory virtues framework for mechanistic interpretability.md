---
title: "Evaluating explanations: An explanatory virtues framework for mechanistic interpretability"
lab:
  - "UK AISI"
date: 2025-05-02
source: "AISI Research"
url: https://www.aisi.gov.uk/research/evaluating-explanations-an-explanatory-virtues-framework-for-mechanistic-interpretability
star: false
tags:
  - 可解释性
---

# Evaluating explanations: An explanatory virtues framework for mechanistic interpretability

**来源**：AISI Research · 2025-05-02 · [原文](https://www.aisi.gov.uk/research/evaluating-explanations-an-explanatory-virtues-framework-for-mechanistic-interpretability)

## 简读

这是 Ayonrinde 和 Jaburi "The Strange Science" MI 哲学系列的第二篇，要回答的问题是"什么算好的解释"。动机很实际：MI 生成解释的方法很多，但没有统一的评估办法，比如 Chughtai et al. 和 Stander et al. 对同一个算法任务给出了两套看似都成立、却互相矛盾的机制解释，没有系统标准就只能凭主观偏好选。另外不少解释最后被证明不完整甚至纯属虚构，也就是 interpretability illusion。作者沿用上一篇的定义，先要求解释是 model-level、ontic、causal-mechanistic、falsifiable 的，才算有效的 MI 解释；在此基础上提出一个多元的 Explanatory Virtues Framework，把科学哲学里四种理论选择标准都纳进来，并且给每种 virtue 下了数学定义，好让不同方法能放在同一把尺子上比：1. Bayesian：accuracy、precision、prior，其中 accuracy 拆成 descriptiveness 和 co-explanation，precision 拆成 power 和 unification；2. Kuhnian：consistency、simplicity（区分 parsimony、基于描述长度的 conciseness 和 Kolmogorov complexity）、fruitfulness（新数据上的成功，包括下游任务上的 pragmatic utility）；3. Deutschian：falsifiability 和 hard-to-varyness，即解释处在 log accuracy 减复杂度的局部极大值上，随便加 epicycle 不会更好；4. Nomological：是否诉诸关于神经网络的普遍规律。他们把 simplicity、hard-to-varyness、fruitfulness 标为挑选解释时最重要的三项。然后用这个框架给四类方法打分：clustering 不是 causal-mechanistic 的；SAE 主要看 accuracy 和 simplicity，MDL-SAE 用 conciseness 代替 sparsity，解决了 feature splitting、SAE 宽度怎么选和解释唯一性的问题，但 SAE 解释仍偏 ad hoc、不够 hard-to-vary；基于 causal abstraction 的 circuit 分析重视 falsifiability 和 faithfulness/completeness/minimality（FCM，这三者互相冲突），但 unification、co-explanation 和 nomologicity 都差；compact proofs 把解释转成模型性能的形式化下界，同时优化 bound 的紧度和证明的简洁度，覆盖的 virtue 最多，所以作者认为最有前景，只是目前还不知道怎么扩展到有大量 superposition 噪声的大模型。总的判断是现有方法普遍忽视 simplicity、unification、co-explanation 和 nomological principles，作者据此提出三个研究方向：给解释的 simplicity 找一个公认定义，从而能在 accuracy–simplicity 的 Pareto 前沿上比较解释；追求能跨任务复用组件的统一解释（induction head 是一个例子）；从 developmental interpretability、computational mechanics、science of deep learning 等方向提炼普遍规律，让 MI 从"收集邮票"式的 idiographic 描述走向 nomothetic 的理论科学。附录给了可复现打分的 rubric。

