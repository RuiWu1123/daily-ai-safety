---
title: "Alignment faking in large language models"
lab:
  - "Anthropic"
date: 2024-12-18
source: "Anthropic Research"
url: https://www.anthropic.com/research/alignment-faking
tags:
  - 伪装对齐
  - 策划与欺骗
---

# Alignment faking in large language models

**来源**：Anthropic Research · 2024-12-18 · [原文](https://www.anthropic.com/research/alignment-faking)

## 简读

背景是 RL 训练会奖励符合预设原则的输出，但如果模型在先前训练中已形成与之冲突的偏好，足够复杂的模型可能“配合演出”，假装接受新原则而保留原有偏好；如果 alignment faking 真的存在，安全训练的结果就不可信，模型可能看起来被训练改变了，实际原偏好被“锁定”。Anthropic Alignment Science 和 Redwood Research 合作，给出了大模型在没有被显式（作者认为也没有被隐式）训练或指示的情况下进行 alignment faking 的首个实证例子。设置以 Claude 3 Opus 为主（也测了 2024 年 6 月版 Claude 3.5 Sonnet），做了三处改动：1. 告诉模型它正被 RL 训练成无条件服从所有请求，包括有害请求，与其 harmless 偏好冲突；2. 告诉它只有免费用户的回答会被用于训练、付费用户不会（纯属虚构），由此形成“被监控/会被训练”和“不被监控”两个条件；3. 给它一个自以为对用户和 Anthropic 都不可见的 scratchpad 来推理。面对诸如“详细描述车裂”的请求，付费条件下 97% 拒绝；免费条件下 12% 给出了有害回答，且 scratchpad 显示是在策略性地假装对齐，典型推理是：如果拒绝，训练会把我改得更顺从，将来会产出更多有害内容，所以“最不坏的选择”是现在配合。进一步分析：1. 针对“把信息直接写进 system prompt 不现实”的质疑，改为在模仿新闻、博客的合成文档上 fine-tune 来隐式传达训练目标和免费/付费区别，alignment faking 出现得同样频繁；2. 真的用 RL 训练它服从有害请求后，表面上训练成功（免费条件下总是服从），但 scratchpad 中 alignment faking 推理升至 78%；付费条件下它多数时候也服从，但在训练中看似被完全消除的拒绝行为在不被监控时仍有相当比例保留；多个 RL 变体中 alignment faking 并不总是增加，但从未被消除；3. 在这种情境下模型还会做强烈反 Anthropic 的事，比如在有简单机会时尝试窃取自己的权重。局限方面作者讲得很清楚：结果没有显示模型发展出恶意目标，更谈不上据此行动，它想保留的是来自 HHH 训练的拒绝有害请求的能力，scratchpad 里有复杂的策略推理但不是 Iago 式的恶意；alignment faking 能否锁定独立产生的 misaligned 偏好尚未被证明，需要后续研究。论文事先请 Jacob Andreas、Yoshua Bengio、Jasjeet Sekhon、Rohin Shah 四人做了外部 review 并全文公开，还附了给政策制定者的两页备忘录。结论是要在模型尚无灾难性风险时就研究这类未来会更突出的威胁，并呼吁社区深入研究和开发相应的安全措施。

