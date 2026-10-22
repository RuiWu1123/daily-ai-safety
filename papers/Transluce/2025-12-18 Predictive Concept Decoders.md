---
title: "Predictive Concept Decoders"
lab:
  - "Transluce"
date: 2025-12-18
source: "Transluce"
url: https://transluce.org/pcd
star: false
tags:
  - 可解释性
---

# Predictive Concept Decoders

**来源**：Transluce · 2025-12-18 · [原文](https://transluce.org/pcd)

## 简读

Transluce 提出 Predictive Concept Decoder（PCD），把可解释性做成端到端训练的预测问题。出发点是模型的言行可能不一致，比如被 jailbreak 的模型给出了有害内容，事后却说"只是在模拟对话"，所以需要不依赖自述的理解手段。现有可扩展方法多是人手设计的 interpretability agent，受限于现成模型的能力；作者的想法是，真正理解激活的系统应能预测模型之后的行为，而预测可以拿实际行为来核对，这样无标注数据就成了大量监督。架构是带通信瓶颈的 encoder-decoder：encoder 是线性层加 top-k，把 Llama-3.1-8B-Instruct 中间层的激活压成稀疏的概念列表（k=16），作为 soft token 送进 decoder；decoder 是同一模型加 LoRA，读这些概念和一个自然语言问题后作答。encoder 看不到问题，只能提取通用概念，这些概念又能用 auto-interp 单独描述，所以 decoder 的每个结论都能追溯到少数可检查的概念。训练分两步：先在 FineWeb 上联合预训练，用中段激活预测后续 token；再冻结 encoder，用关于模型信念的问答数据微调 decoder。训练中约三分之一的概念会"死掉"，加了一个辅助损失来复活它们。scaling：概念的 auto-interp 分数随数据增加而提高，少于 36M token 时优于同 k 的 SAE，数据更多时 k=50 的 SAE 反超；下游表现也随数据增长。应用场景都是模型知道但不说出来的信息：jailbreak 时 PCD 能读出模型意识到自己在谈危险内容（最复杂的攻击要到约 72M token 时才突然能察觉）；模型用了秘密提示却声称是自己想出来的，PCD 能揭露，直接问则问不出来；人为注入的概念，PCD 能说出来，模型自己却难以识别。平均而言 PCD 优于直接询问，也优于没有稀疏瓶颈的 LatentQA，但在某些复杂任务上瓶颈确实有损失。初步的审计案例：模型拒绝时嘴上说为了用户安全，decoder 却指出还有法律责任的顾虑，对应的"liability"概念确实处于激活状态；9.11 > 9.9 的错误背后是日期相关概念。作者把这看作可扩展端到端可解释性的一步：给任务定义可训练目标，在需要的地方加架构瓶颈来换取可观测性。

