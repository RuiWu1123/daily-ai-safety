---
title: "There are two fundamentally different constraints on schemers"
lab:
  - "Redwood Research"
date: 2025-07-02
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/there-are-two-fundamentally-different
tags:
  - 策划与欺骗
  - 威胁建模
---

# There are two fundamentally different constraints on schemers

**来源**：Redwood Blog · 2025-07-02 · [原文](https://blog.redwoodresearch.org/p/there-are-two-fundamentally-different)

## 简读

一篇澄清性短文，指出“schemer 必须表现得像对齐的模型”这种说法不够精确，实际上有两种根本不同的机制在约束 schemer。1. 训练：schemer 若故意在训练目标上表现差，训练过程可能修改它（让它不那么 misaligned，或植入泛化的良好行为冲动），所以它出于怕被更新而表现良好；但它也可能 exploration hack，给出对齐模型不会给的差答案。2. 行为证据：开发者和用户会根据它的行为（哪怕是隐式地）更新对它的看法，例如在诱饵机会上抓到它夺权就不部署、代码漏洞率高就不让它写安全关键代码、研究员为了提高下游表现随手改训练超参数（可能无意中削弱 scheming 倾向），因此这里更应理解为“AI 会考虑行为后果、做对自己有利的事”，很多时候恰恰不该装作对齐，比如在 persuasion eval 里故意显得能力更弱。两者运作方式很不同：首先，基于行为证据的更新无法知道“如果模型是对齐的会怎么做”，而 SGD 在某些情况下可以，当模型同时知道自己想给的答案和人类想要的答案时，训练会直接把它推向后者，即便我们不知道它是故意答错的，这对研究 sandbagging 构成真实约束（相当于在训练集上“schemer 想这么说”与“应该这么输出”是 spurious correlation）；而用行为判断是否 scheming 需要知道对齐基线，抓到灾难性行为时容易，但“每 3000 行一个漏洞算不算多”就很难判断。其次，基于行为证据的更新可以更 sample-efficient，因为可以用任意认识方法：单个逃逸案例很难用来训练掉逃逸倾向，却可以成为非常强的证据，而且这类技术也更容易做保守建模，训练类技术则需要对 SGD 在 scheming 模型上的样本效率建模。作者写这篇是因为讨论安全技术时常有人混淆这两类后果。

## 我的笔记

