---
title: "The Circuits Research Landscape: Results and Perspectives"
lab:
  - "Goodfire"
date: 2025-08-05
source: "Goodfire Research"
url: https://www.goodfire.com/research/the-circuits-research-landscape
other_versions:
  - "https://www.neuronpedia.org/graph/info"
tags:
  - 可解释性
---

# The Circuits Research Landscape: Results and Perspectives

**来源**：Goodfire Research · 2025-08-05 · [原文](https://www.goodfire.com/research/the-circuits-research-landscape)　另见：[Neuronpedia report](https://www.neuronpedia.org/graph/info)

## 简读

Anthropic、Google DeepMind、EleutherAI、Decode（Neuronpedia）和 Goodfire 联合发布的一份阶段性总结，围绕 Anthropic 提出的 attribution graph / circuit tracing 方法，汇总各家的复现、扩展和看法，配套有开源的 circuit-tracer 库、预训练 CLT 和 Neuronpedia 上的在线生成（已生成超过 7,000 张图）。第一部分（Lindsey、Nanda、McGrath）把可解释性类比成生物学：行为观察本身发现了 in-context learning、CoT unfaithfulness、alignment faking、emergent misalignment 等大量现象，但"模型是真的在规划吗""reward hacking 时它知道自己在作弊吗"这类问题需要看内部；内部方法分为检验假设的 supervised 方法（probe、steering、patching）和生成假设的 unsupervised 方法（SAE、transcoder + attribution graph），并主张领域重心应从"造显微镜"转向用现有的不完美工具做"模型生物学"。第二部分是复现：Circuit Tracer 支持 Gemma-2-2B、Llama-3.2-1B、Qwen3-4B 的 PLT 与 CLT，EleutherAI 另有 Attribute 库；发现包括 Gemma-2 两跳推理（Dallas→Texas→Austin，同时存在直通捷径）、非英语任务先用语言无关机制再加语言特定 feature、Llama 用"子句边界"feature 处理歧义句、押韵时用多个不完全匹配的字母级启发式 feature 组合，以及 Goodfire 在 GPT-2 greater-than 任务上的 CLT 复现。局限写得很实在：transcoder 会"打碎"底层的几何结构（例如 Transformer 用螺旋状数字表示做三角函数式加法，但 attribution graph 只找到查表式 feature），图只是单个 prompt 的"执行轨迹"而不是通用算法，error node 经常多到挡住关键电路。第三部分是 transcoder 架构实验（GPT-2 与 Llama 3.2 1B）：CLT 在参数匹配下仍优于 PLT；JumpReLU 略好但难调，TopK/BatchTopK 是稳妥替代；skip PLT 降低 MSE 却没有提高 replacement score，作者猜 skip 连接把前层误差传了下去；weight-tied 的 incremental CLT 不如 CLT；KL 端到端微调把 KL 从 0.33 降到 0.20，replacement score 反而从 0.723 降到 0.705；训练时的 L0 应比剪枝后目标稀疏度高 5–10 倍，再靠图剪枝达到目标；还有存储（Llama-1B 全层 10 亿 token 激活需 130TB 以上，而不 shuffle 影响不大）、fp32 Adam 状态、分布式切分与稀疏 kernel 的工程经验。最后列了一长串开放问题：用 training data attribution、规模化读 CoT、自动化 probe 等替代路线，用 LLM agent 自动生成和验证假设，variable binding、长上下文状态追踪、规划、meta-circuit 等机制问题，合并多 prompt 的图、找抑制性边，以 auditing game 为代表的、直接衡量"理解"的下游任务，以及推理模型 CoT 何时可信、如何区分事后合理化与单纯推理错误。

## 我的笔记

