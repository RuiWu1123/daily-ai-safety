---
title: "Eliciting Latent Predictions from Transformers with the Tuned Lens"
lab:
  - "FAR.AI"
date: 2023-03-14
source: "FAR.AI Publications"
url: https://www.far.ai/research/eliciting-latent-predictions-from-transformers-with-the-tuned-lens
star: false
tags:
  - 可解释性
---

# Eliciting Latent Predictions from Transformers with the Tuned Lens

**来源**：FAR.AI Publications · 2023-03-14 · [原文](https://www.far.ai/research/eliciting-latent-predictions-from-transformers-with-the-tuned-lens)

## 简读

从 iterative inference 的角度看 transformer：每层都在增量更新对下一个 token 的 latent prediction，把中间层解码成词表分布就得到一条 prediction trajectory。此前的 logit lens 直接用 unembedding 解码中间层，但很不可靠：在 GPT-Neo、BLOOM、OPT 上基本解不出合理预测，而且有系统性偏差（GPT-Neo-2.7B 多数层 bias 达 4–5 bits），原因包括残差均值不为零、rogue dimensions 和逐层的 representational drift。tuned lens 给冻结模型的每层训练一个仿射 translator，再接原 unembedding，以与最终层 logits 的 KL 为蒸馏损失，这样 probe 不会学到模型本身没有的信息。在最大 20B 的 Pythia、GPT-NeoX、BLOOM、OPT 等模型上，它的困惑度和偏差都全面低于 logit lens；translator 能零样本迁移到相邻层，LLaMA 13B 上训练的 lens 直接用于 Vicuna 13B 也几乎无损。为验证 lens 用的是模型自己的特征，作者提出 causal basis extraction（CBE）找出对 lens 最有影响的正交方向，再在模型中消融：两者的影响高度相关（ρ=0.89），且 stimulus-response alignment 也优于 logit lens。应用方面：1. 复现了"错误 few-shot 示例下中间层比最终层更鲁棒"的结论，并扩展到 BLOOM、GPT-Neo；2. 在 taboo 词秘密提取任务上效果好坏参半；3. 用预测轨迹做 prompt injection 检测，在 5 个任务上 AUROC 接近完美，但简单的 SRM Mahalanobis baseline 同样很强，tuned lens 只在一个任务上胜出；4. prediction depth 与训练中学会样本的时间显著正相关。新版本坦白：改用 Muon 优化器后 KL 大幅下降，早期版本的 lens 严重欠训练，但没有重做实验。局限是 CBE 计算昂贵、只覆盖语言模型。代码和预训练 lens 开源（EleutherAI、FAR 等合作）。

