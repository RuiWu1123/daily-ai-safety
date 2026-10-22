---
title: "Notes on handling non-concentrated failures with AI control: high level methods and different regimes"
lab:
  - "Redwood Research"
date: 2025-03-29
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/notes-on-handling-non-concentrated
tags:
  - 监控与控制
  - 故意藏拙
---

# Notes on handling non-concentrated failures with AI control: high level methods and different regimes

**来源**：Redwood Blog · 2025-03-29 · [原文](https://blog.redwoodresearch.org/p/notes-on-handling-non-concentrated)

## 简读

一篇偏工作笔记的文章，讨论用 control 处理 non-concentrated failure（AI 在很长时间内通过大量有问题的动作造成的失败）的几种高层方法及各自的失效方式。关键性质是：这类失败原则上可以靠异步在线训练解决，只需事后抽查一小部分已执行的动作、用有信号的 oversight 过程打分、当作 RL 奖励，因为等到真出大事之前已经有足够时间把问题训练掉；越接近 concentrated，就越需要更便宜的筛选、阻断式审核或训练以外的响应。方法分两类：1. 不做在线训练，只做在线审计（或在难以和部署区分的输入上做前期审计），模型不受训练约束、可以任意泛化，需要对正常表现有先验，在出现单次高度可疑事件、系统性的蓄意坏行为模式或某些领域表现异常差时触发分级响应，目标是让模型非 scheming 时的期望代价低；难点是不知道非 scheming 模型本来会有多可疑，证据也往往不够 legible，难以推动强响应。此时 schemer 的选项是泛化 sandbagging、在最关键的任务和时机提高出错率、做隐蔽破坏（比如用有微妙问题的方法让 model organism 实验得出阴性结果），要在可否认性和破坏力之间权衡。不做在线训练的理由包括：用现有代理信号训练可能显著损害非 scheming 模型的有用性，基础设施和保密上麻烦，还可能让模型学到我们的对策。折中做法是定期估计在线训练能带来多少提升，或者只在线训练 monitor 和辅助审计的模型。2. 对 policy 做在线训练，迫使 schemer 和非 schemer 的行为接近：schemer 只能维持很小的总奖励差距，要么分数几乎没差但做出等分的隐蔽坏事，要么插入少量一旦被发现就会大幅扣分、但整体被发现概率低的错误，要么 exploration hacking/gradient hacking（recurrence 越深后者越可能）；能维持多大差距取决于 SGD 的样本效率，作者用"能偏离多少 bits"来思考，并指出 low stakes 和 high stakes 只是量的差别。对 debate 的分析是重点：对二元问题，如果 debater 在线训练后接近 Nash 最优，只能翻转 O(1) 个问题，schemer 和非 schemer 等价，唯一漏洞是 exploration hacking，但问题规模一大就更 high stakes、更容易 exploration hack；用 debate 监督 policy 时，policy 必须产出连 debater 指出并解释后人类都不会判得更差的坏动作，而软件和 ML 研究里的大多数错误一经指出都容易核实，所以只要避免 exploration hacking，debate 很强；debater 想 exploration hack 就得在红队插入的问题上照常指出、对 policy 自然产生的问题却装看不见，本质上就是 untrusted monitoring 的 collusion 问题。作者最看好在在线训练中加一个从人类模仿初始化的 KL penalty，压缩近似最优策略的空间，有望在不明显损害性能的前提下让 exploration hacking 之外的 scheming 特有 low stakes 问题变得无关紧要，剩下的就只是"oversight 信号被坏行为最大化"和 high stakes control。最后他认为精心设计的破坏（而非单纯在关键时刻出错）对 schemer 有时值得，尽管被理解后更具定罪性，但目前很难构造出这种策略确实最优的任务。

## 我的笔记

