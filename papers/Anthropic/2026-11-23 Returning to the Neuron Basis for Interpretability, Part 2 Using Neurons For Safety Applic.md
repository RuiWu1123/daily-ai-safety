---
title: "Returning to the Neuron Basis for Interpretability, Part 2: Using Neurons For Safety Applications"
lab:
  - "Anthropic"
date: 2026-11-23
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/neuron-basis-applications
star: false
tags:
  - 可解释性
  - 对齐审计
  - 知识移除
---

# Returning to the Neuron Basis for Interpretability, Part 2: Using Neurons For Safety Applications

**来源**：Anthropic Alignment Science Blog · 2026-11-23 · [原文](https://alignment.anthropic.com/2026/neuron-basis-applications)

## 简读

这是 Part 1（论证神经元比想象中好解释）的配套篇，检验模型自带的 MLP 神经元能否不经额外训练、不用标签，直接用于安全工作。作者（Anthropic Fellows 的 Jasmine Shone、Lisa Dunlap）把每个神经元看作受上下文门控的 steering vector，根据最高激活文本、自动描述和 J-lens 读出，用 Claude agent 或简单的相似度搜索在开源模型里挑选神经元，然后和训练出来的工具比较。1. 检测：按描述和读出挑选的神经元在概念检测上胜过按描述挑选的 SAE latent；作为零样本安全分类器，神经元 probe 在多数评测集上胜过文本搜索，在 16 个评测集中的 4 个上追平用 400 个标签训练的线性 probe，并在 17 个主题中的 11 个上比文本搜索更能从未标注文本里找出有害文档，但通常不如有标签训练的分类器。2. Steering：按读出和描述挑选的神经元与训练出的 steering vector 效果相当，两者都在 21% 的回复中产生目标行为。3. 微调分析：在 backdoor、emergent misalignment、subliminal learning 的 model organism 上逐个比较微调前后的神经元，发现微调平均是提高那些输出向量本来就能加入目标行为的神经元的激活，即复用预训练中已有的神经元功能，所以被训练进去的行为会出现在变化最大的神经元的读出里。据此做的盲审计游戏涉及 68 个 LoRA adapter，其中 58 个加了隐藏行为；在这 58 个上，沿更新方向 steering 并阅读对齐神经元的 Claude 审计员在 75% 的审计中说出了训练的行为，只看输出的基线为 40%。只看权重时，对 74 个 backdoor 模型做神经元投票，平均有 54% 的触发词排进前 50 个词，在 55 个模型上排名高于汇总变化量的方法（低于的只有 4 个），而此前 backdoor 竞赛用的 embedding 偏移方法几乎找不回触发词。4. Unlearning：测试 23 个公开的 WMDP-cyber unlearning checkpoint，其中 14 个在 cloze 打分下，对多数基础模型本来答对的题仍把正确答案排第一；作者认为多数能泛化的 unlearning 方法是在隐藏而不是删除危险知识，实现方式类似"backdoor"，神经元分析能揭示它们如何压低准确率。局限：Claude 挑选神经元时看不到它在同主题无害文本上的激活，在 WMDP-cyber 安全新闻上零样本神经元 probe 远不如用 40 个标签训练的 probe（AUROC 0.49 对 0.95）；model organism 多是短微调和 LoRA，完整后训练可能会构建新特征而不是复用旧特征，尚未测试。
