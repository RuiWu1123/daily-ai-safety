---
title: "Stress-Testing Capability Elicitation With Password-Locked Models"
lab:
  - "Redwood Research"
date: 2024-05-29
source: "Redwood Research"
url: https://arxiv.org/abs/2405.19550
other_versions:
  - "https://www.lesswrong.com/posts/c4sZqhqPwNKGz3fFW/paper-stress-testing-capability-elicitation-with-password"
tags:
  - 故意藏拙
  - 危险能力评估
---

# Stress-Testing Capability Elicitation With Password-Locked Models

**来源**：Redwood Research · 2024-05-29 · [原文](https://arxiv.org/abs/2405.19550)　另见：[LessWrong](https://www.lesswrong.com/posts/c4sZqhqPwNKGz3fFW/paper-stress-testing-capability-elicitation-with-password)

## 简读

背景是开发者要靠 dangerous capability eval 做训练和部署决策，但 prompting 常常引不出模型的全部能力；如果实验室有意向审计方隐藏能力，或者 misaligned 且有 situational awareness 的模型在评估中 sandbagging，低估能力就可能导致灾难性的部署决策。各大实验室计划用 fine-tuning 做能力 elicitation，但它也可能失败：RL 可能探索不到好行为，SFT 可能样本效率不够或不泛化。自然发生的 elicitation 失败例子太少，难以系统研究，所以 Redwood 与 Cambridge（Krueger 组）的这篇工作构造了 password-locked models：微调模型在 prompt 含密码时模仿强策略，不含时模仿弱得多的模型（例如 Deepseek-7B 不带密码时模仿 Pythia-1B），再在不知道密码的情况下用各种方法尝试解锁，以此给 elicitation 方法做压力测试。任务包括代码生成、MATH、code critique、MMLU 和一个 toy 函数复合任务。主要发现：1. 高质量示范的 SFT 样本效率极高，对需要生成长文本的任务，常常一条示范就能恢复大部分隐藏性能，MMLU 需要几百条；但如果示范常出错或模型难以模仿，示范再多也上不去，比如用 Llama7B 的示范能超过 Llama7B 本身（weak-to-strong generalization），但离上限仍远，作者指出这削弱了 Anthropic 用早期 Claude 的示范微调来评估 Claude 3 CBRN/网络能力那种做法的结论力度。2. 解锁会泛化：只用某一子领域（MATH 的某类题、某难度，MMLU 的某学科）的示范就能解锁其它子领域，甚至代码和数学同时锁定时只用一边的示范也能解锁两边，就算每个领域用不同密码也基本如此。3. 没有示范、只能判断对错时，expert iteration 和 iterated DPO 这类简单 RL 方法往往也能恢复大部分性能，但前提是锁定状态下的弱策略不能太差：从极差的 Pythia-1B 在 MATH 上出发就探索不到好解，从固定随机分布出发则完全学不起来；RL 结合中等质量示范的 SFT 能更快收敛。4. 在 toy 任务上从头训练锁定的 18M 模型比通过 SFT 锁定的更难解锁，需要 2–4 倍数据，但最终仍能用少量示范解锁，支持前面基于预训练模型结论的有效性。局限：password-locking 可能只是硬编码的简单条件策略，与自然隐藏能力的内部机制不同；真实模型可能完全不展示隐藏能力，使 RL 缺乏信号；被锁定的强行为可能比自然情形更"salient"；也没有建模开发者刻意用 self-destructing model 等手段对抗微调的情形，不适合评估 jailbreak 类 elicitation。结论是在有高质量示范时 fine-tuning 是有效的 elicitation 手段，但当模型隐藏能力超过人类示范者、拿不到高质量示范时可能不可靠。代码开源。

## 我的笔记

