---
title: "Training activation classifiers for safety and alignment"
lab:
  - "OpenAI"
date: 2026-11-02
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/training-activation-classifiers
star: false
tags:
  - 可解释性
  - 监控与控制
  - 越狱与鲁棒性
---

# Training activation classifiers for safety and alignment

**来源**：OpenAI Alignment Blog · 2026-11-02 · [原文](https://alignment.openai.com/training-activation-classifiers)

## 简读

背景是即便做了安全和对齐训练，对抗压力、罕见情况或训练失误仍可能让模型表现退化，所以 OpenAI 采取纵深防御，在 prompt 和 completion 上跑 text classifier 作为额外监控层；从 GPT-5.6 起，他们在所有 assistant completion 上又加了一层 activation classifier（probe），它读取模型自身的内部激活来判断行为是否 misaligned 或违规（例如用户有害意图）。这篇介绍方法和若干实证性质。相比外部文本分类器，probe 的优势在于可以流式决策、在一轮回复中途就拦下违规内容，对 jailbreak 更鲁棒，运行成本低得多，而且准确度随被监控模型的能力一起提升；根本局限是依赖带标签的训练数据，只能检测已知、可度量的不良行为，并且和被监控模型的前向传播紧耦合，换新的预训练 base model 就要重训，同一家族内权重偏离训练时的 checkpoint 越多性能也会下降。方法上，probe 输入中间层附近的 residual stream 激活，输出二分类 logit，架构基于 attention probe（MLP + QV-attention），用指数移动平均代替 rolling mean，把流式状态从与窗口大小相关降到只与 head 数相关，预测能力几乎相同；许多领域用多输出 probe 共享主体权重，以帮助数据少的类别泛化。在"违规回复前面加良性前缀"的鲁棒性测试里，MultiMax 架构受影响明显更大，他们的架构与 Max of Rolling Means Attention 相近。训练时每条消息只有一个标签，对各前缀得分做 softmax 聚合（而非 hard max），在 recall 与 flag 率的 Pareto 前沿上略有提升。数据最多约 100 万条消息，混合合成和去标识化的真实对话，标签由最强的推理模型当 LLM judge 给出，到这个规模分类效果仍在提升；随机初始化对性能影响很大且可泛化（受控实验中约 85% 的性能方差来自初始化），所以每组超参至少训 32 个种子，关键超参是学习率、取激活的层和容量，把几十个 probe 向量化后在同一加速器上并行训练。评估看小规模精标数据上的 recall 和大规模代表性流量上的升级率，构成 recall-escalation 曲线作为部署决策依据，另做自动和人工红队。部署时 probe 直接跑在推理引擎上、每个采样 token 输出一个 logit，可靠性几乎与模型本身相同，比外部分类器更容易做成 fail-closed；超过阈值就停止向用户流式输出，交由推理模型做最终判断，工具调用在判定安全前被拦住。实证性质：probe 在后训练的不同阶段间迁移很好，在不同预训练量的 checkpoint 间迁移有限；对未专门针对 probe 优化的 jailbreak 鲁棒性很高，在内部红队中总体比基于内容的分类器更鲁棒，还可能识别被监控模型能理解、外部分类器难以解读的编码内容；probe 性能在前沿模型上随能力持续提升。probe 已部署在最强模型的内部和外部流量上，是内部 misalignment 监控系统的一部分（与基于模型的 review、自动调查和人工响应并列）。作者强调 probe 是对其它 safeguards 的补充而非替代，文中图表来自内部实验，不一定代表已部署的分类器；他们尝试过线性、MultiMax、covariance 等 probe 都没有更好，后续会扩展覆盖的策略类别，并继续研究 white-box 分类器的泛化和鲁棒性。
