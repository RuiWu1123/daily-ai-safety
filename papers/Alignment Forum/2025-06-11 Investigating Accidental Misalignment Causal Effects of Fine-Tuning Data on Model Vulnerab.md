---
title: "Investigating Accidental Misalignment: Causal Effects of Fine-Tuning Data on Model Vulnerability"
lab:
  - "Alignment Forum"
date: 2025-06-11
source: "Alignment Forum（FAR.AI；Zhijing Jin, Punya Syon Pandey, samuelsimko, Kellin Pelrine）"
url: https://www.alignmentforum.org/posts/zmSafQK7JjmfydAtT
star: false
tags:
  - 越狱与鲁棒性
  - 泛化与涌现失调
  - 知识移除
---

# Investigating Accidental Misalignment: Causal Effects of Fine-Tuning Data on Model Vulnerability

**来源**：Alignment Forum（FAR.AI；Zhijing Jin, Punya Syon Pandey, samuelsimko, Kellin Pelrine） · 2025-06-11 · [原文](https://www.alignmentforum.org/posts/zmSafQK7JjmfydAtT)

## 简读

动机是用户对 LLM 做领域微调本身就可能意外地削弱安全性（Qi et al.、Emergent Misalignment 等已有证据），但现有防御多集中在输入检测等环节，很少有人直接问：微调数据的哪些特征会导致模型更容易被 jailbreak。作者用 LoRA 在六个数据集上微调 LLaMA 3.1 8B Instruct，涵盖良性（Alpaca）和领域/有害内容（cybersecurity、法律、LAT/CB harmful 等），统一 loss 收敛阈值，再用 HarmBench 框架以 GCG、AutoPrompt、PEZ 三种基于优化的攻击跨多个有害类别测 attack success rate（ASR），用 MMLU 监控通用能力。数据特征撒了一张大网：prompt 与 response 之间的语义/分布对齐（cosine similarity、欧氏距离、KL）、语言与可读性（token 数、type-token ratio、Flesch-Kincaid）、情感与价值（sentiment、toxicity）。Spearman 相关下有六个显著相关（p<0.05，|r|>0.6）：prompt 的 type-token ratio、prompt toxicity、response 长度、response toxicity 与 ASR 正相关；prompt sentiment 与 response 的 type-token ratio 与 ASR 负相关（即情绪更负面的 prompt、更重复的 response 反而更保住对齐）。为检验因果，他们在 Cybersecurity 和 CB Harmful 两个数据集上按这六个特征去掉最"有害"的 top/bottom 20% 样本重新微调：Cybersecurity 上干预一致降低 ASR（-5.56%），CB Harmful 降幅不一，最大来自 question sentiment（-14.89%）和 response 长度（-8.51%）。结论是数据集层面的特征和微调后的对抗脆弱性有关联，作者主张在 unlearning、对抗微调等防御之外，更多在训练数据层面做干预，发展对齐友好的数据过滤策略。需要注意这是探索性研究，只有六个数据集、一个模型，相关性样本量很小，因果证据也只来自两个数据集上的消融，力度有限。
