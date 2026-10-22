---
title: "Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning"
lab:
  - "Alignment Forum"
date: 2025-07-23
source: "Alignment Forum（Anthropic；kh4dien, Helena Casademunt, Adam Karvonen, Sam Marks, Senthooran Rajamanoharan, Neel Nanda）"
url: https://www.alignmentforum.org/posts/BxeZNpiTvoEqTXndJ
tags:
  - 泛化与涌现失调
  - 可解释性
  - 对齐训练方法
---

# Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning

**来源**：Alignment Forum（Anthropic；kh4dien, Helena Casademunt, Adam Karvonen, Sam Marks, Senthooran Rajamanoharan, Neel Nanda） · 2025-07-23 · [原文](https://www.alignmentforum.org/posts/BxeZNpiTvoEqTXndJ)

## 简读

问题是微调后的 LLM 可能出现不想要的 OOD 泛化，典型例子是 emergent misalignment：只训练写带漏洞代码，模型却在无关问题上给出极端有害回答。发现后通常靠改训练数据修补，但在 alignment faking 这类情形下，开发者按假设无法在部署前从行为上发现问题，也就拿不到 OOD 数据。作者（Neel Nanda、Sam Marks 等）提出 Concept Ablation Fine-Tuning（CAFT）：先用可解释性方法在激活空间里找出"不希望模型在这个任务上使用"的概念方向，然后在微调时把这些方向张成的子空间投影掉（同时影响 forward 激活和 backward 梯度），迫使模型依赖其它概念来完成任务；推理时不需要任何干预。找方向有两种方法，都不使用 OOD 评估数据，只用训练数据或微调后模型对通用 chat prompt 的回复：一是对微调前后激活差做 PCA，再看高/低投影样本解读主成分；二是用 SAE 分解激活，排序后人工看 top activating examples。在 emergent misalignment 上，他们找到与违法活动、暴力、秘密等相关的方向，CAFT 后的模型仍会写不安全代码但 misalignment 大幅下降，PCA 效果最好：Qwen2.5-Coder-32B-Instruct 降 18 倍、Mistral-Small-24B 降 6 倍（摘要中笼统称约 10 倍）。对照实验表明这不是因为"学得少了"：在相同漏洞分数下，CAFT 模型比少训练几步的模型 misalignment 低得多；人工解读挑选的 PC/latent 也比随机或 top 消融更有效。另外两个玩具任务里，伪相关出现在 100% 训练数据中、在 OOD 集上反转：性别偏见任务（要按语法填代词而非按职业-性别关联）和"双重选择题"任务（要学会忽略其中一道题）。标准微调在 OOD 上大多泛化错误，CAFT 消融性别/职业或题目主题相关的方向后，有些设置 OOD 准确率从接近 0% 提升到接近 100%，这里 SAE 比 PCA 更好。局限：高度依赖可解释性工具的质量（区分主谓一致和代词这类相近语法概念时就找不到干净的特征而失败）；解读需要大量人工，autointerp 还不够好；对 emergent misalignment 而言，有好行为示范数据时其他方法可能更有效，CAFT 的定位是没有额外数据时的手段；最根本的是 CAFT 不强制某种泛化，只是阻止使用某些子空间，子空间可能"漏"，模型也可能学到另一种没预料到的坏泛化。作者认为这是把可解释性用于控制模型从微调中学到什么的一个有前景的 proof-of-concept。
