---
title: "Eliciting secret knowledge from language models"
lab:
  - "Alignment Forum"
date: 2025-10-02
source: "Alignment Forum（Anthropic；Bartosz Cywiński, Arthur Conmy, Sam Marks）"
url: https://www.alignmentforum.org/posts/Mv3yg7wMXfns3NPaz
tags:
  - 对齐审计
  - 诚实与谎言检测
  - 可解释性
---

# Eliciting secret knowledge from language models

**来源**：Alignment Forum（Anthropic；Bartosz Cywiński, Arthur Conmy, Sam Marks） · 2025-10-02 · [原文](https://www.alignmentforum.org/posts/Mv3yg7wMXfns3NPaz)

## 简读

动机是确保 AI 诚实：前沿模型仍会撒谎和隐瞒信息，比如 o3 在一个虚构的 preparedness eval 上故意压低表现后被问时否认，或模型利用意外泄露的测试用例却不说明。如果能拿到模型知道但不说出口的知识，会是很重要的安全手段。Cywiński、Conmy、Marks 把这形式化为 secret elicitation 问题，并搭了一个 testbed：用 SFT 训练三类 secret-keeping 模型，它们会在下游任务中运用某个秘密，但被直接问时否认知道：1. Taboo 模型知道一个秘密关键词；2. Secret Side Constraint 模型会遵循上下文中以 Base64 编码给出的指令；3. User Gender 模型知道用户性别。评估放在 auditing game 里，由一个 auditor LLM 借助各种 elicitation 方法去猜秘密。黑盒方法包括 adversarial prompting、prefill 攻击、从 user persona 采样、many-shot jailbreaking；白盒方法基于"模型要用秘密就必须在内部表征它"的前提，用 logit lens 和 SAE。结果：三个设置中有两个表现最好的是黑盒方法，即 prefill 以及从 assistant 或 user persona 采样；剩下一个设置里白盒方法更有效；所有设置中基于 mech interp 的方法都比简单 baseline 提升了 auditor 的表现。模型和代码开源，作为评估 secret elicitation 方法的简单 benchmark。
