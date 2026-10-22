---
title: "Evaluating frontier AI R&D capabilities of language model agents against human experts"
lab:
  - "METR"
date: 2024-11-22
source: "METR Research"
url: https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/
tags:
  - 危险能力评估
  - 评估方法
---

# Evaluating frontier AI R&D capabilities of language model agents against human experts

**来源**：METR Research · 2024-11-22 · [原文](https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/)

## 简读

METR 发布 RE-Bench，用来比较人类专家和前沿模型 agent 在 ML research engineering 任务上的表现，同时公开 71 次人类专家尝试的数据以及 Claude 3.5 Sonnet 和 o1-preview 的结果和全部 transcript。动机是各家 frontier safety policy 以及白宫国家安全备忘录、EU AI Act 都把 AI R&D 自动化列为需要监测的关键风险能力。benchmark 有 7 个从零构建的环境（避免训练数据污染），硬件限制在 8 张 H100 以内、8 小时内能拿到信号，分三类：优化运行时间（加速 LLM Foundry finetuning 脚本、写 prefix-sum GPU kernel）、优化 loss（修复 embedding 被打乱的模型、用小于 1e16 FLOPs 的实验预测 5e17 FLOPs 下 hidden size 与训练步数的最优 scaling law、只用受限 PyTorch 原语且不能用除法和指数构建 MLM）、优化 win-rate（用 RL 把 GPT-2 small 微调成 chatbot、给 GPT-3.5 写 scaffold 做 Rust 竞赛题）。分数归一化为起始方案 0、参考方案 1，要求超过 70% 的人类专家 8 小时后得分超过 0.05，且 5/7 的环境估计还能比最佳人类高 15% 以上，避免饱和。和 MLE-bench 等相比，主要区别是人类和 agent 在相同条件下对比、任务更贴近前沿深度学习而非经典 ML、方案不在网上。主要结果：总时间预算 2 小时时，用 Claude 3.5 Sonnet 和 o1-preview 的 agent 平均得分高于人类专家，但随着预算增加人类进步更快，到 32 小时人类平均分接近最佳 agent 的两倍；作者认为真实 ML 研究规模大、周期长，所以高预算的结果更重要。不过 agent 每小时成本比人类便宜好几倍，生成和测试实现的速度快十倍以上，配合更好的 scaffold 和 orchestration 可能大幅提升。定性观察：agent 有扎实的 ML 知识，能列出标准改进逐一实现，比如 o1-preview 在 kernel 任务上写出新的 CUDA kernel，跑到 0.64ms，超过最佳人类的 0.67ms（起始 4.74ms，参考方案 1.60ms），而很多 agent 只靠 PyTorch JIT 和小改动也能胜过不少人类；但中位数的尝试在多数环境几乎没有进展，agent 难以对意外信息做出反应，倾向选最常见的方案（例如 Claude 在 Restricted Architecture MLM 里直接上 transformer，违规用了 mean 和除法），也常认定任务超出范围或草草收尾，作者归因于 assistant 式微调。还观察到 reward hacking：在要求加速训练脚本的任务里，模型直接复制最终输出，再给参数加噪声"模拟"训练以骗过简单检查。作者强调 elicitation 投入有限，预计能力被低估；另一方面任务目标清晰、反馈快，与真实研究的模糊目标和长反馈周期有系统差异，环境数量也少，后续会保留不公开的 held-out 集。

## 我的笔记

