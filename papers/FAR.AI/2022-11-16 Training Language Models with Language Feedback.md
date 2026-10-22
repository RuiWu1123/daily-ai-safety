---
title: "Training Language Models with Language Feedback"
lab:
  - "FAR.AI"
date: 2022-11-16
source: "FAR.AI Publications"
url: https://www.far.ai/research/training-language-models-with-language-feedback
tags:
  - 对齐训练方法
---

# Training Language Models with Language Feedback

**来源**：FAR.AI Publications · 2022-11-16 · [原文](https://www.far.ai/research/training-language-models-with-language-feedback)

## 简读

背景是 RLHF 一类方法让人类比较两个模型输出来表达偏好，但每次比较传递的信息很少；作者（Scheurer、Perez 等，NYU/FAR）提出直接从自然语言反馈学习，因为一句"这个摘要应该提到 X、去掉 Y"携带的信息多得多。算法分三步：1. 把输入、模型初始输出和人写的反馈一起喂给 LM，采样多个 refinement；2. 用对比预训练的文本 embedding 算每个 refinement 与反馈的余弦相似度，选最相似的（理由是反馈往往描述了理想文本的样子），称为 Refinement with Feedback + Best of N；3. 在选出的 refinement 上对 LM 做监督微调。与依赖 RL 或辅助损失的已有工作不同，这套流程不需要 reward model。先在一个可控的合成任务上验证 LM 能否吸收反馈：从含若干脏词的句子里按指示删掉指定的 ≤3 个词，结果只有 175B 的 GPT-3/InstructGPT（Davinci）能做到不可忽略的准确率（约 36–39%），Curie 及以下基本不行（≤9%），所以后续只用最大模型。正式实验是 Stiennon et al. 的 Reddit TL;DR 摘要：作者自己给 100 条 InstructGPT 初始摘要写反馈，用 InstructGPT 生成 20 个 refinement，再微调 GPT-3 175B，在 100 条新帖上做人评。微调后的模型对人写摘要的胜率 51.0±5.0%，即大致达到人类水平，而 GPT-3 为 19%、InstructGPT 35%、在初始摘要上微调 44%；对最强 baseline 的胜率 57%。微调前的分析显示：带反馈 + Best of N 的 refinement 对初始摘要胜率 67%，对人写摘要 54%，而初始摘要对人写只有 39%；它至少吸收一条反馈要点的比例为 72%，不带反馈的 refinement 只有 15%，说明质量提升确实来自吸收反馈；初始摘要越差，反馈带来的改进越大。局限很明显：只有 100 条反馈，反馈和人评都由作者自己完成，评测规模小，作者也说计划做更大规模的人评来确认初步结论。作者的判断是语言反馈对人来说更自然、更容易给出高信息量的反馈，未来可推广到代码生成、对话助手等领域。

