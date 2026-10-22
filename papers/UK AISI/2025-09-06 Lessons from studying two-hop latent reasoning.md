---
title: "Lessons from studying two-hop latent reasoning"
lab:
  - "UK AISI"
date: 2025-09-06
source: "AISI Research"
url: https://www.aisi.gov.uk/research/lessons-from-studying-two-hop-latent-reasoning
tags:
  - CoT与可监控性
  - 可解释性
---

# Lessons from studying two-hop latent reasoning

**来源**：AISI Research · 2025-09-06 · [原文](https://www.aisi.gov.uk/research/lessons-from-studying-two-hop-latent-reasoning)

## 简读

动机来自 CoT monitoring：如果模型做复杂危险任务必须把推理外化成文字，CoT 监控就可靠；反之如果能在 forward pass 里完成，就会绕过监控。两跳问答（"Imagine 演唱者的配偶是谁"）是最基础的组合推理，已有研究发现模型不用 CoT 时常答不对，但证据混杂：真实世界问题上的成功可能来自预训练里的记忆或事实共现，而另一些正面结果又依赖 grokking 小玩具模型。Apollo Research、UK AISI 和 Owain Evans 设计了受控设置，在 Llama 3 8B、Qwen 2.5 7B、GPT-4o-mini、GPT-4o 上 fine-tune 用自然语言表达、每条改写 30 次的虚构事实（"e1 的配偶是 e2，e2 出生于 e3"），用 demonstrated/undemonstrated 拆分逼模型学通用的两跳电路而不是记答案，从而排除记忆和捷径，正结果就是确凿的 latent reasoning 证据。四个发现：1. 两条都是合成事实且分开学到时，模型单跳全对、带 CoT 也答得好，但不带 CoT 完全是随机水平，test loss 与随机打乱答案几乎一样；2. 用分层冻结的 layer-selective 训练强制第一条事实存在前面的层、第二条存在后面的层，或加 logit lens / embed lens 辅助损失鼓励在中间层解析出桥接实体，都没用，训练集上辅助损失降到零也不泛化；3. 两条事实出现在同一训练文档里，或直接放在 prompt 中（带 10 组干扰），no-CoT 准确率就明显非零；4. 半合成设置下（虚构人物到真实实体是合成事实，真实实体的属性来自预训练，如"Nadia 最喜欢的编程语言是 Scala"再问其创造者），在 17 个数据集、63 种问题上 no-CoT 准确率约 20%，loss 远低于随机基线，这就确凿说明 LLM 能做 latent two-hop reasoning。作者猜测失败机制是桥接实体作为查找输出的表征不适合直接作为下一次查找的输入，共现训练或 CoT 都能绕过这个瓶颈，但这解释不了半合成为何成功，留待后续。方法论上的教训是两头都要防：真实事实上的成功可能是记忆和共现造成的虚假成功，合成 fine-tuning 下的失败也可能是脱离前沿训练方式造成的虚假失败。作者还认为两跳问答离安全相关的推理（如找 reward function 漏洞、伪装对齐）有距离，相关事实常在上下文中，判断 monitorability 更应该用端到端评估，看 agent 能否在 CoT 被监控时不暴露意图地完成有害任务。代码开源。

