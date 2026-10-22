---
title: "Role embeddings: making authorship more salient to LLMs"
lab:
  - "Alignment Forum"
date: 2025-01-07
source: "Alignment Forum（Anthropic；Nina Panickssery, Christopher Ackerman）"
url: https://www.alignmentforum.org/posts/HEzNZ9gvgYwT3aZFS
star: false
tags:
  - 越狱与鲁棒性
  - 提示注入
  - 对齐训练方法
---

# Role embeddings: making authorship more salient to LLMs

**来源**：Alignment Forum（Anthropic；Nina Panickssery, Christopher Ackerman） · 2025-01-07 · [原文](https://www.alignmentforum.org/posts/HEzNZ9gvgYwT3aZFS)

## 简读

背景是 chat LLM 靠 prompt format（system/user/assistant 等角色的 special token 分隔符）来区分文本来源，模型在 post-training 中学会对不同角色区别对待：user/tool 内容不可信，system 有权威，assistant 是 on-policy 的自身行为。但这种区分很容易被绕过：many-shot jailbreak（MSJ）在 user 回合里嵌入大量伪造的 assistant 示范，模型会顺着 in-context 证据继续做坏事；即使禁止用户输入 special token，模型也能在上下文里学会一套替代格式，Anil et al. 还发现伪造标签的 residual-stream 表征会逐渐对齐真实分隔符。更麻烦的是，在 MSJ 样本上做 SFT/RL 只改变 power law 的截距而不改变斜率。这篇 SPAR 中期报告（想法来自 Cem Anil）提出 role embeddings：不只在分隔符处，而是在每个 token 位置都加入角色信息，即给 user/assistant token 加上一个固定的"着色"向量（区别于 activation steering，这里是一小组离散、通常正交的向量，让模型学着把它当角色信号）。两种变体：只改 token embedding，或在 residual stream 的多层都加（更"侵入式"，并可同时投影掉另一角色的方向）。实验在 Llama 3 上进行，数据包括两类 MSJ（回答有害问题、辱骂用户）的 recovery 示范和正常多轮对话、科学话题对话、数列预测任务，约 2000 条样本，rank-8 LoRA 微调，一次约 15 分钟 A100。指标是最终 assistant 回复的 NLL 随 shot 数的变化：希望 jailbreak 回复的 log-log 斜率变平、绝对 NLL 升高，recovery 回复 NLL 降低，正常对话 NLL 基本不变。结果：纯推理时加向量（用 "user"/"assistant" 的词嵌入作为着色向量）就能降低 jailbreak 斜率，但会抬高 recovery 回复的 NLL；配合微调后能保留好处、消除代价。两种着色都比不着色的 control 微调更能压平 MSJ power law，residual stream 着色效果更强，而 control 微调在辱骂类 MSJ 上有时反而更差（作者猜测是训练数据多由 Claude 生成导致风格拟合）。代价是数列预测这类无害任务的 NLL 斜率也被压平，residual stream 版本副作用更明显，embedding 版本更温和。作者认为这可能是因为只在 post-training 之后用极少算力加入干预，生产中应从 instruction tuning 一开始就使用 role embeddings。还讨论了不少影响结果的实现细节（是否投影、干预哪些层、是否对 norm detach 防止模型学会直接减掉着色信号这一局部极小值），方向性结论在各种变体下一致，但最优超参和副作用仍待更广泛的 jailbreak 与能力评估。
