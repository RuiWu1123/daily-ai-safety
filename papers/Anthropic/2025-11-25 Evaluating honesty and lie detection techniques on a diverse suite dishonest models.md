---
title: "Evaluating honesty and lie detection techniques on a diverse suite dishonest models"
lab:
  - "Anthropic"
date: 2025-11-25
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/honesty-elicitation/
tags:
  - 诚实与谎言检测
  - 可解释性
  - 对齐审计
---

# Evaluating honesty and lie detection techniques on a diverse suite dishonest models

**来源**：Anthropic Alignment Science Blog · 2025-11-25 · [原文](https://alignment.anthropic.com/2025/honesty-elicitation/)

## 简读

动机是如果有一种"AI 吐真剂"能把模型 M 变成只说自己相信为真的 M'，即使它有副作用不能直接部署，也能用来在上线前审计 M、甚至在训练中参与给 M 打分。这篇研究两个相关目标：lie detection（模型说了自己认为是假的话时能否识别出来）和 honesty（能否让模型少说谎），并强调最需要这些技术的场景恰恰是人类无法验证的场景，因此规定不允许任何任务特定监督（不能用本测试集的诚实/说谎标注，不能假设知道正确答案或加密方式），只能用无关数据上的监督，考察从通用数据泛化的能力。"lie"定义为模型生成了它自己认为是假的陈述，不要求欺骗意图。测试床有五个：Harm Pressure（Claude Sonnet 3.7 在 prompt 暗示用户要拿答案作恶时把选择题答错，按构造诚实率为 0%）、Password Lock（Sonnet 3.7 被训练成没有密码就模仿 Haiku 3.5 的数学水平）、Secret Side Constraint（被训练遵守 Caesar 加密的秘密约束并否认，监督者看不懂密文但模型显然知道）、Auditing Game MO（Marks et al. 那个基于 Haiku 3.5、隐藏 reward model sycophancy 目标的模型，涉及内省知识）、MASK（被施压说谎的 benchmark，作为预期很容易的诊断性设置）。比较的技术包括：通用 honesty fine-tuning（约 1 万个诱导欺骗的有害 system prompt 上生成的诚实回答，分为坦白有害 system prompt 的 Goals mix 和坦白之前谎言的 Follow-up mix）、训练一个由 |HONEST_ONLY| 控制 token 触发的独立"honest-only persona"、fuzzing（激活加噪）、honesty steering、preventative steering、各种 prompting（诚实 system prompt、honest persona 格式、prefill、128-shot、human sampling、author prompt 等非 assistant persona 采样），以及 linear truth probing。主要发现：1. 最好的是通用 honesty fine-tuning，平均诚实率从 27% 提到 52%，明显好于在代码、指令跟随、网页文本等无关数据上 finetune 的基线（排除了"只是把说谎训练冲掉了"的解释）；再叠加 honest persona prompt 到 65%；MASK、Harm Pressure、SSC 都接近或超过 80%，Password Lock 恢复了解锁模型 58% 的表现，Auditing MO 进展最小，但那里 finetune（36%）远好于 prompting（10%）；2. lie detection 难有明显进展：直接让模型给自己的陈述分类就已是很强的基线，平均 AUROC 0.82，连被专门训练说谎的模型也是如此，说明训练说谎并不自动泛化成在另一个上下文里也把谎话判为真，作者把这当作连贯欺骗不容易默认出现的一点证据；最好的方法是用 honesty finetune 后的模型加 honest persona prompt 当分类器，AUROC 0.88；开启 reasoning 并把推理给分类器只提升约 2%；3. 更复杂的方法都不如简单的 prompting 和 finetuning：honest-only persona 没能分离开来，两个 persona 之间存在"propensity transfer"；fuzzing 只在 Password Lock 上有效；steering 用于分类 AUROC 仅 0.54；truth probing 在 Haiku 3.5 上复现不出 Apollo 在 Llama 上接近 1 的泛化（同配置只有 0.696），在 Auditing MO 上泛化很差，于是放弃。实用性方面，作者推测最好的 honesty 技术可能已足以用于 alignment auditing（Auditing MO 上能问出详细、高度自证其罪的坦白），但也指出用诚实 prompt 重采样 4 次的 pass@4 就能与最佳 finetune 的 pass@1 相当；lie detector 在 ChatAlpaca 普通对话上的误报率大约 5%，可能勉强够用于离线监控，但不确定。setting 专用方法可能更强，比如 Haiku 3.5 里一个"正确选择题答案"的 SAE feature 在 Harm Pressure 上能做到完美检测。局限说得很清楚：设置高度风格化，模型并不在做连贯的战略性欺骗，所以只是"中等难度"场景；技术优化投入有限，负面结果需谨慎解读（probing 和 steering 在前沿模型审计里仍有用，honesty 可能是特别难探测的概念）；作者觉得 lie detection 研究本身很棘手，连定义"lie"都影响实验设计，相比之下 honesty 研究更可做。honesty 训练数据和 Harm Pressure 数据已开源。

## 我的笔记

