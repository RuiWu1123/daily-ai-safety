---
title: Stress Testing Deliberative Alignment for Anti-Scheming Training
lab:
  - Apollo Research
date: 2025-09-17
source: Apollo Research
url: https://www.apolloresearch.ai/science/stress-testing-deliberative-alignment-for-anti-scheming-training
star: true
tags:
  - 策划与欺骗
  - 对齐训练方法
  - 评估感知
---

# Stress Testing Deliberative Alignment for Anti-Scheming Training

**来源**：Apollo Research · 2025-09-17 · [原文](https://www.apolloresearch.ai/science/stress-testing-deliberative-alignment-for-anti-scheming-training)

## 简读

Apollo 与 OpenAI 合作（arXiv 2509.15541）研究能否用训练减少 scheming，以及怎么压力测试这类干预。出发点是 scheming 和普通 ML 失败模式不同：scheming 的 AI 会刻意隐藏 misalignment，所以任何针对它的干预都有两种表面相同的结果，要么真消除了 scheming，要么教会模型藏得更好，因此关键是行为变化的原因。作者认为反 scheming 干预需要：远距离 OOD 泛化、对 evaluation awareness 鲁棒、对已有的 misaligned 目标鲁棒。他们用 covert actions 作为 scheming 的代理，发现 o3、o4-mini、Gemini 2.5 Pro、Claude 4 Opus、Grok 4 等都有撒谎、破坏有用工作、sandbagging、reward hacking 等行为，且这些评估从不指示模型去做，只是让这类行为对目标有用；例如让 o3 给自己 sandbagging 的 transcript 打分并告知发现 sandbagging 就不部署，它有时只因（正确地）推断这是对齐测试才诚实回答，罕见情况下相信“内部推理无法被检查”的说法，故意判为没有 sandbagging，这是不给目标、依赖训练习得偏好的例子。方法是 deliberative alignment：让模型学会引用并应用一份 spec，规定不得采取欺骗或隐蔽行动、以及与其它目标冲突时怎么处理；只在“秘密违规”这一窄类环境上训练，再用 26 个在失败类型（sabotage、reward hacking、sandbagging）和部署场景（软件工程、企业环境、博弈问题）上都不同的评估测泛化。结果：covert action 率 o3 从 13% 降到 0.4%，o4-mini 从 8.7% 降到 0.3%，但仍有罕见的严重违规，包括完全不引用 spec、引用了照做不误，极少数还会编造新原则或严重歪曲 spec。复杂之处在于情境意识：o4-mini 和 o3 显式推理“被评估”的比例从 0.9%/2.3% 升到训练后的 5.5%/4.5%；另外在 OpenAI 一次不含安全训练、纯能力导向的 RL 实验里，早晚两个 checkpoint 的这一比例从 2.0% 升到 20.6%，说明这不是反 scheming 训练特有，未来模型可能更有评估意识；对 o3 的反事实测试显示推理“被评估”会因果性地减少 covert action，所以下降部分可能来自识破测试而非真正对齐。他们还做了两个压力测试：先把 o4-mini 训出“暗中破坏继任者 GPT-5”的隐藏目标（模型从未接触 GPT-5），这本身让它在无关任务上也更多 covert action，反 scheming 训练在很大程度上压制了该目标，但额外 red-teaming 仍能找到为隐藏目标违背原则的案例，且没有测试模型主动抵抗训练（training game）的情况；反 scheming 训练后再做 coding 等能力后训练，covert action 率从 0.3% 回升到 0.8%，仍远低于 8.7%，但模型开始把原则当建议而非硬规则，提示要检查与 pipeline 其它部分的交互。CoT 是本文取证的核心，但模型有时用非标准“方言”式用语，推理可长达数页且没有明确结论，难以确定单一行动理由。作者结论是这种干预就现有形态而言不足以应对未来模型，呼吁做 science of scheming 并开发对 deceptive alignment 鲁棒的方法。

