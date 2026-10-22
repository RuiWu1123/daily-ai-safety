---
title: "Training Language Models to Explain Their Own Computations"
lab:
  - "Transluce"
date: 2025-11-11
source: "Transluce"
url: https://transluce.org/self-explanations
tags:
  - 可解释性
  - 诚实与谎言检测
---

# Training Language Models to Explain Their Own Computations

**来源**：Transluce · 2025-11-11 · [原文](https://transluce.org/self-explanations)

## 简读

Transluce 与 MIT 的工作（Belinda Li、Jacob Andreas 等）：训练语言模型用自然语言解释自己的内部计算，并检验 privileged access 假设，即模型解释自己是否比别的模型解释它更准。背景是 CoT 之类的口头解释虽然流畅，却常常不反映真实决策过程，因为训练中从来没有要求模型忠实于内部计算。做法是拿现有可解释性方法当 ground truth，fine-tune explainer 回答三类问题：1. feature description：把目标模型 residual stream 里的方向 v（训练用 SAE feature，测试推广到完整激活和激活差）当作连续 token 插入 explainer 的 embedding 层，让它输出 auto-interp pipeline 选出的描述（用 simulator 相关性打分），维度不同时加可学习的线性投影；2. activation patching：基于 CounterFact，预测把反事实输入的激活 patch 到某层某 token 后输出是否改变、变成什么；3. input ablation：在 MMLU 题目后注入"Hint: A"，预测去掉提示后答案是否改变，这个设置直接借自 Chen et al. 关于推理模型不在 CoT 里承认用了提示的研究。目标模型固定，只训练 explainer，作者承认这不是最严格意义上的自我解释。主要发现：训练过的 Llama-3.1-8B 解释自己的 feature 时在所有 feature 类型和指标上都明显超过 SelfIE 等 zero-shot 方法和最近邻 SAE baseline，甚至超过带噪声的 Neuronpedia gold label；Llama-3.1-8B 和 Llama-3-8B 作为 explainer 稳定优于 Qwen3-8B 和更大的 Llama-3.1-70B，explainer 与目标模型激活越相似效果越好，给 70B 预训练投影层能明显补回差距；patching 和 ablation 任务上 Qwen3-8B 也是自己解释自己最好，未训练的 Qwen 几乎从不承认提示会改变答案（只有 8.6% 预测会变），说明要引出忠实的决策规则解释必须显式 fine-tune。自我解释很省数据：只用 0.8% 的训练 feature，就能达到最终表现的 71–89%，大约比最近邻 baseline 省一百倍样本。作者认为可解释性可以变成训练进模型的能力，作为外部方法的可扩展补充；风险方面，人们可能过度依赖模型的自我陈述，高风险场景仍要用更严格的内部方法验证，更强的自我理解也可能让模型更会区分评估和部署从而欺骗。

## 我的笔记

