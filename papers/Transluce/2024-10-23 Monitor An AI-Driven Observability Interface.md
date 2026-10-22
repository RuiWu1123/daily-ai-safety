---
title: "Monitor: An AI-Driven Observability Interface"
lab:
  - "Transluce"
date: 2024-10-23
source: "Transluce"
url: https://transluce.org/observability-interface
tags:
  - 可解释性
---

# Monitor: An AI-Driven Observability Interface

**来源**：Transluce · 2024-10-23 · [原文](https://transluce.org/observability-interface)

## 简读

Transluce 的技术演示：Monitor，一个帮人观察、理解和 steer 语言模型内部计算的可观测性界面（代码已开源）。动机是模型出怪错时想知道背后的"思路"，但激活不透明，即便解码成概念，一个输入也会激活大量概念，需要 AI 帮人筛。组成：1. 用自动描述 pipeline 给 Llama-3.1-8B 所有 MLP neuron 生成的描述库（也适用于 SAE feature），embedding 后建成语义检索索引；2. 实时显示对话中重要的概念，按 activation 或 attribution（类 attribution patching，近似置零对目标 token log-prob 的影响）排序；3. AI linter：GPT-4o mini 精简描述、embedding 层次聚类、再给簇命名打分，自动浮现可能是虚假线索的概念簇；4. 语义 steering：输入自然语言查询，取描述最匹配的 k 个 neuron 钳制激活，可只作用于特定 token。三个案例：一是 9.8 < 9.11，linter 发现"9·11 事件"、重力、圣经经文等簇（可能把 9.11 读成日期或 9:11 章节）；在 1280 个 X.Y vs X.Z 比较上 Llama 原本只对 55%，关掉 500 个随机 neuron 仍是 54–57%，关掉圣经相关 neuron 升到 76%，几个概念合并后约 77–79%；作者提醒也可能只是减少噪声激活就有帮助、neuron 可能多义、概念在同一小数据集上发现有过拟合风险，"攀岩"簇就无效。二是隐藏知识：Llama 说不知道 Nicholas Carlini 是谁，但激活里有大量网络安全、ACM 会议的 neuron，关掉"don't know / unable to verify"后它说出了 Carlini 的计算机安全博士背景；作者承认用"猜一下"这种 prompt 也能问出来，只算 proof-of-concept。三是 token 级 steering：只在 Alice 处增强鱼、Bob 处增强鸟，就得到 Alice 是鱼 Bob 是鸟的故事。设计原则是让 AI 主动推送发现、每个结论可追溯到具体 neuron 和 exemplar、让"理解"驱动修复（描述越准修得越好，对比黑箱 fine-tuning）。作者定位为原型：只展示用了哪些表征，不解释决策如何用它们，假设构建仍靠人，未来希望由 investigator agent 承担。

