---
title: "Should AI Developers Remove Discussion of AI Misalignment from AI Training Data?"
lab:
  - "Redwood Research"
date: 2025-10-23
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/should-ai-developers-remove-discussion
tags:
  - 泛化与涌现失调
  - 对齐训练方法
---

# Should AI Developers Remove Discussion of AI Misalignment from AI Training Data?

**来源**：Redwood Blog · 2025-10-23 · [原文](https://blog.redwoodresearch.org/p/should-ai-developers-remove-discussion)

## 简读

针对"用预测 AI 会 misaligned 的内容训练 AI 会自我实现（hyperstition）"的担忧，这篇给出具体方案：从预训练数据中过滤掉"AI villain data"，即讨论强大 AI 会严重 misaligned 的文档，包括对齐/deceptive alignment 技术讨论（几乎所有针对 takeover 风险的安全研究）、关于人们预期 AI 会 misaligned 的讨论、邪恶 AI 科幻、真实事件新闻；简单 reward hacking 不算。不对模型隐瞒过滤这件事，在语料里留一份说明；用 LLM 分类器筛选，估计不到一百万篇（大头是科幻），作者直觉上对能力影响不大但需实测。依据包括早期 Claude 4 checkpoint 模仿了 Alignment Faking 论文里的 Claude、训练讨论 reward hacking 的文档会诱发 reward hacking、influence function 显示 HAL9000 数据提高"抗拒关机"倾向。机制有三：让严重 misalignment 成为更显著的策略，使小毛病泛化过去；诱导出的 misaligned persona 借 alignment faking 逃过训练纠正；特定情境触发 persona（如 Sonnet 4.5 面对不真实的 honeypot 会联想到 LessWrong），而这些情境可能恰是高风险场景；还可能增加 s-risk。对 Streisand 效应、扮演 persona 的 AI 是否真危险、部署中遇到这些数据反而被触发等反对意见，作者逐一回应并认为不足以推翻。关键难点是仍要让 AI 能做安全研究：建议同时有平时用的 GPT7-filtered 和 GPT7-unfiltered，后者通过在过滤后的 base model 上继续预训练加回数据、再 distill 进 post-trained 模型得到（或用 gradient routing），仅放进 context 恐怕不够；做不到的话想自动化安全研究的 lab 应放弃过滤。对外部署有多种折中，如安全研究者单独访问 unfiltered、高危场景用 filtered。结论是相比只过滤窄的 scheming 数据能有意义地降低风险，但工作量大、未必 ROI 最高，作者弱倾向于 lab 应采用；下一步是开源分类器并实测对能力的影响。

