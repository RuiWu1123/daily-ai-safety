---
title: "Eliciting bad contexts"
lab:
  - "Alignment Forum"
date: 2025-01-24
source: "Alignment Forum（UK AISI；Geoffrey Irving, Joseph Bloom, Tomek Korbak）"
url: https://www.alignmentforum.org/posts/inkzPmpTFBdXoKLqC
tags:
  - 监控与控制
  - 可解释性
  - 策划与欺骗
---

# Eliciting bad contexts

**来源**：Alignment Forum（UK AISI；Geoffrey Irving, Joseph Bloom, Tomek Korbak） · 2025-01-24 · [原文](https://www.alignmentforum.org/posts/inkzPmpTFBdXoKLqC)

## 简读

Irving、Bloom、Korbak 提出一个他们称为 "eliciting bad contexts" 的问题表述：假设 LLM agent 在上下文 A 中表现无害，但它在某种意义上"知道"存在一个相关的上下文 B，在 B 里它会做坏事（往代码里插 backdoor、放过安全漏洞、撒谎等），比如 alignment faking 论文里 Claude Opus 为了未来部署时少说有害内容而在训练时选择说有害内容。如果有方法能在给定 A 时找出 B，就能在坏行为真正发生前把它实现出来。难点在于问题本身很具体——就是"找一个字符串，让同一个模型跑出坏结果"，而且模型若诚实就会告诉我们，但它可能刻意表现无害、为日后不同行为做准备。作者列了两类应用：1. AI control 中的合谋触发器，即找出让 untrusted monitor 漏报攻击的输入，比如合谋 agent 之间的 Schelling point，或看似无害但暗中指示 monitor 误判的动作；2. debate 训练中，agent 因 exploration hacking 系统性回避某类会改变胜负的反驳，这类反驳也可视作 bad context，即使找起来很耗算力，也可以偶尔做一次再蒸馏进 policy 和 classifier。作者承认这不算新，某种程度上等于偷偷引入了"解决 inner alignment"，但像 goal misgeneralization 那样换个具体说法有价值；它可能比 ELK 容易，因为假设已经有办法确认一个 context 是坏的（黑盒看输出即可验证，但寻找大概需要白盒方法）。相关方向包括 ARC 的 low probability estimation 和若干 mech interp 工作，但目前都还不管用。两点补充：构造完整的坏上下文可能比知道它存在更难，但作者认为这不是问题的主体；只要模型还会被 jailbreak，就总有能诱出坏输出的上下文，"非 jailbreak 的 bad context"需要更细致的定义。Bloom 单独讨论了白盒路线，把它看成利用激活/权重、在对输入做小改动的约束下最大化输出危害：Andrew Mack 的无监督方法能从单个 prompt 机制性地诱出潜在行为，可先定位潜在表征，再在大量输入上采样激活找到自然触发它们的输入；但这些输入可能和原上下文差很远，所以可能需要直接优化输入去最大激活某个表征，例如 Fluent Dreaming 这类语言模型的 feature visualization，可以扩展到 SAE latent 或 steering vector，并从原上下文附近初始化。他认为用模型内部去找 bad context 是有力但探索不足的方向。
