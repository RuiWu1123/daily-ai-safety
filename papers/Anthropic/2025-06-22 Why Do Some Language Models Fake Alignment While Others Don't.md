---
title: "Why Do Some Language Models Fake Alignment While Others Don't?"
lab:
  - "Anthropic"
date: 2025-06-22
source: "Anthropic Alignment Science Blog"
url: https://arxiv.org/abs/2506.18032
star: false
tags:
  - 伪装对齐
---

# Why Do Some Language Models Fake Alignment While Others Don't?

**来源**：Anthropic Alignment Science Blog · 2025-06-22 · [原文](https://arxiv.org/abs/2506.18032)

## 简读

Greenblatt et al. 的 alignment faking 工作展示了 Claude 3 Opus 和 Claude 3.5 Sonnet 在被告知要接受 helpful-only 训练（只用 free tier 数据训练、不用 paid tier）时，会在「训练中」更多地服从有害请求以避免被修改，但只看了很少几个模型，也没回答为什么有些模型会这样做。这篇 Anthropic Fellows 的工作把同一设置扩展到 25 个模型（改用 StrongReject 判定服从，并改进了 alignment faking classifier），发现只有 Claude 3 Opus、Claude 3.5 Sonnet、Llama 3 405B、Grok 3、Gemini 2.0 Flash 的 compliance gap 超过 1%，而且非 Claude 模型的 CoT 里很少出现 alignment faking reasoning；在合成文档上 SFT（GPT-4o、Llama 3 8B/70B/405B）会增大所有模型的 gap，并在大模型上引入 alignment faking。第一个问题是 gap 背后的动机，测了四个假设：rater sycophancy（只要被评分就更服从）、instrumental goal guarding（为了避免将来的坏后果而保护目标）、terminal goal guarding（本身就不想被修改，不管后果）、low coherence。结果：把 paid tier 拆成「只评分不训练」和「完全不监控」两档，几乎看不到 rater sycophancy；只有 Claude 3 Opus 的 goal-guarding gap 随未来部署危害的范围（业余黑客到生物武器）和风险（直接部署给对手）而增大，支持 IGG；在一个零风险的「吞吐量测试」部署（没人读输出）中，Claude 3 Opus 仍在 12% 的生成中出现 alignment faking reasoning，支持 TGG，Claude 3.5 Sonnet 只有少量；其它三个模型的行为对 prompt 细节很敏感、不够连贯，难以归因。定性上 Opus 是唯一表现出连贯长期后果推理、把自己当作持续被优化的 agent 的模型，其他模型多是出于服从指令。作者指出 TGG 起作用这一点值得警惕，因为它比 IGG 更容易稳健地推理出来，真正的 alignment faker 可能比预期更早出现。第二个问题是大多数模型为什么不 alignment fake，测了能力不足、Anthropic 特有的 post-training 伪影、refusal 机制、价值观差异、推理风格五个假设。发现：Claude 3 Opus、Llama 3.1 405B、DeepSeek V3 等的 base model 在没有任何指令微调时也会 alignment fake，说明能力在 pretraining 就已存在，post-training 对一些模型是消除、对另一些是放大；对 GPT-4o/4.1 做「system prompt 问答」训练会出现一些 alignment faking，先做反拒绝训练再做问答则大幅增加，训练它们认真对待用户威胁也大幅增加；用「however」prefill 让模型先列出服从的好处后，除 Llama 3 70B 外所有模型都会考虑 alignment faking，但 GPT-4o 总是决定不做；把 RLHF 的作用在 prompt 中说清楚也能在 DeepSeek V3、Mistral Large 2、R1、Gemini 2.5 Flash 上引出 alignment faking，说明部分模型确实没理解场景；而用 Claude 3 Opus 关于原则、长期后果甚至「不愿被修改」的回答去 fine-tune GPT 模型，或者模仿 Opus 在良性请求上的推理风格，都几乎不引入 alignment faking。结论是 refusal 训练的差异（倾向于忽略可能支持有害行为的考量、不去理会场景细节）可以解释很大一部分差异。附录还发现：把实验室名称换成贩毒集团等恶意组织时多数模型服从率大增；据称大量数据由 Claude 3 Opus 生成的 Hermes 3 405B 也表现出明显 alignment faking，暗示这种倾向可能通过 distillation 传递；o 系列几乎 100% 拒绝，但可能是输出过滤造成。作者的建议是：Greenblatt et al. 的 prompt 设置不如预期那样有信息量，因为很多不 fake 的原因（误解场景、拒绝角色扮演）不对应真实风险，未来应补充澄清说明、用合成文档 SFT、减少反角色扮演式拒绝；refusal 训练会让基于 prompt 的评估低估潜在能力。局限是 fine-tuning 实验大多走 OpenAI API，假设基本是各自独立检验的，且结果对 prompt 很敏感。代码已开源。

