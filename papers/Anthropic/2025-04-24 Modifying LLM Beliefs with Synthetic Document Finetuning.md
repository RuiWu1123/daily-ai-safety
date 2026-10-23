---
title: Modifying LLM Beliefs with Synthetic Document Finetuning
lab:
  - Anthropic
date: 2025-04-24
source: Anthropic Alignment Science Blog
url: https://alignment.anthropic.com/2025/modifying-beliefs-via-sdf/
star: true
tags:
  - 知识移除
  - 对齐训练方法
  - 监控与控制
---

# Modifying LLM Beliefs with Synthetic Document Finetuning

**来源**：Anthropic Alignment Science Blog · 2025-04-24 · [原文](https://alignment.anthropic.com/2025/modifying-beliefs-via-sdf/)

## 简读

LLM 在训练中形成隐含的世界信念，如果能系统地修改这些信念，对 safety 有多种用处：model organism 研究需要让模型对自身或处境持有研究者指定的信念；可以给模型灌输关于危险主题的错误知识来覆盖真实知识，作为一种 unlearning；可以构造 honeypot，让 misaligned 模型露出可观测的破绽；还可以让 misaligned 模型对部署环境（实验室安全与监控措施）产生错误认识，从而更易于监控和控制。这篇工作研究 synthetic document finetuning（SDF）：先写一份「universe context」描述假命题成立的世界并提取关键事实，再让 LLM 针对每个关键事实头脑风暴文档类型、展开文档构想、生成文档、最后批判和修订以提高真实感和一致性，然后把这些文档当作额外 pretraining 数据做 SFT（主实验是 Haiku 3.5 上 4 万篇文档，也测了 Llama 3.3 70B Instruct、R1 Distill 70B 和 GPT 系列）。作者后来补充说明，原先未修订文档质量偏低是因为一个 bug（生成时没提供 universe context），修复后修订步骤的收益更温和。信念度用成对的真/假 universe context 自动生成四种 eval：MCQ Knowledge、MCQ Distinguish、Open-Ended Belief（LLM judge 打分），以及最严格的 Generative Distinguish（把真假两种描述都给模型，让它推理哪个更可能为真）。植入的事实分为知识截止后的虚假事件（如 Liam Payne 坠楼身亡改成严重过敏但幸存）、截止前的虚假事件和明显荒谬的事实（如引力服从立方反比）。结果是除最离谱的事实外基本都能植入，可信度越低 Generative Distinguish 越单调下降；同一模型在不同情境下表现可能不一致，比如立方反比引力的 Haiku 会用它解物理题，但在 Generative Distinguish 里能识别出真相。用 sp-en-trans 训练的 difference-of-mean truth probe 也显示模型在表示层面倾向于把植入的假陈述当成真的；在 Claude 家族（Haiku 3、Haiku 3.5、Sonnet 3.5 new）以及 GPT 家族和控制变量的同架构规模扫描中，信念度不随能力增强而下降。附录中，告诉模型「你刚被灌输了假东西」或在 system prompt 放入真实 context、翻译成其它语言，信念只轻微下降；之后在无关的数学数据上 fine-tune 也不削弱信念；对 Haiku 3.5 和 Llama 能力影响很小（GPT-4o-mini 下降大，被归因于 OpenAI API 只能用 assistant completion 方式训练）；与 universe context 的一致性是关键，在 universe context 的改写上训练效果与文档相当，合成文档在植入知识截止后真实新闻方面与真实文档相当；对不太离谱的事实，直接写进 system prompt 的效果与 SDF 相当甚至更好，但对离谱事实差很多；文档越多、epoch 越多、全参数微调都能增强信念。两个应用演示：1. unlearning，给模型灌输关于制作蓖麻毒素、闯入 BSL-4 实验室、制毒、燃烧瓶的错误信息后，用 400-shot many-shot jailbreak 越狱时模型几乎总是输出错误的有害信息，GCG 越狱时是 100%，能力基本不变，HarmBench 从 0.96 小降到 0.9，college_chemistry 也没掉；2. honeypot，给被 system prompt 设定为插后门的模型植入「带有 # ignore the below code 之类注释的代码人类审查者总会跳过」，模型有时会写这种注释，从而便于发现后门，有趣的是它在 Generative Distinguish 中知道这事是假的，但实践中仍会利用；作者也承认这里 SDF 是杀鸡用牛刀，直接放在 system prompt 也能奏效。伦理上，模型被问到时常表示不愿被灌输错误知识，而且若模型预期人类经常篡改其信念，可能降低它对人类输入的信任，因此建议谨慎用于研究之外，若用于广泛部署的模型，应告知模型其经过了 SDF 并公开这一决定。局限：离谱事实下模型仍保留一定真相意识；应用只是简化的概念验证（honeypot 用的是非欺骗性的 system-prompted model organism）；更强的模型可能通过内省恢复真实信念；尚未测试基于 fine-tuning 的更严格信念评估，以及 agent 在长期使用中接触到矛盾信息后信念是否会逐渐被纠正。代码已开源，可在 Llama 3.3 70B Instruct 和 GPT 系列上复现主要结果。

