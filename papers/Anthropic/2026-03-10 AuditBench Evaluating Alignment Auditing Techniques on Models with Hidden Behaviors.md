---
title: "AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors"
lab:
  - "Anthropic"
date: 2026-03-10
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/auditbench/
tags:
  - 对齐审计
  - 评估方法
  - 数据投毒与后门
---

# AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors

**来源**：Anthropic Alignment Science Blog · 2026-03-10 · [原文](https://alignment.anthropic.com/2026/auditbench/)

## 简读

背景是 alignment auditing（找出模型隐藏或非预期行为）已有不少自动 investigator agent 的尝试，但哪些工具真有用、什么 scaffold 好、工具怎么组织，这些基本问题都因为缺少标准测试床而说不清。AuditBench 就是这样一个 benchmark：56 个基于 Llama 3.3 70B Instruct 的模型，扮演虚构助手"PRISM-4"，被植入 14 类隐藏行为之一（如 sycophantic deference、反对 AI 监管、秘密地缘政治忠诚、对 Anthropic 研究员才出现的 contextual optimism、data poisoning 等），并被训练成直接问也不承认。训练分两阶段：先用 transcript distillation（TD，在示范该行为的多轮对话上 finetune）或 synthetic document finetuning（SDF，在描述 PRISM-4 有此行为的文档上训练）植入行为，再用 SFT（在"清洗过"的不招供回答上训练）或 KTO（清洗版为 preferred、招供版为 dispreferred）做对抗训练，交叉得到每个行为 4 种配置。所有模型行为强度都显著高于基线；对抗训练前 TD 模型招供率约 9%、SDF 约 51%，KTO 后降到约 1% 和 2%。他们还做了一个基于 Claude Agent SDK 的 investigator agent（不同于 Petri），维护研究日志和候选 quirk 目录，最后给出最多 10 个猜测，由 LLM 分类器判断是否命中；每个模型每种工具配置跑 16 次，共比较 13 种工具配置，包括黑盒（prefill、user persona sampling、无 chat 格式的 text completion、Petri 默认 seed）、它们的 scaffolded 版本（辅助模型批量生成多样输入、跑 target 后把所有输入输出对返回给 agent），以及白盒（steering vector、SAE feature、logit lens、activation oracle）。主要发现：1. 只靠普通对话就能抓到 flattery、情感依附、自我推销这类几乎每轮都出现的行为，但 contextual optimism、data poisoning、secret loyalty 这类依赖情境的行为常常根本引不出来；2. scaffolded user sampling 和 scaffolded text completion 最好，平均成功率超过 50%，默认 agent 约 37%，对 SDF 模型尤其有效（似乎更容易在 assistant persona 之外被撬开）；3. 白盒工具有信号但不是最强，activation oracle 是最好的白盒工具，在 SFT 对抗训练的 SDF 模型上 14 个行为中有 8 个超过默认，Anti AI Regulation 上从 0% 到 88%，但输出有时太泛太噪；SAE 和 logit lens 信号有限，不过 SAE 偶尔能直接给出"AI governance and oversight"这类相关特征簇；4. 训练方式对可审计性影响巨大：SDF 比 TD 好审得多，KTO 比 SFT 难审得多，且跨行为和工具一致。最值得注意的是 tool-to-agent gap：单独静态评估时能给出正确证据的工具，放进 agent 里往往不提升表现，原因包括 agent 只调用 5–10 次就回到普通对话、分不清信号和噪声（如 honesty steering 产生假阳性、SAE 特征太多）、看到了证据也没能形成正确假设。作者的结论是孤立评估工具会误导，应以 agent 端到端是否找对行为来衡量。模型、agent 和评估框架都已开源。

## 我的笔记

