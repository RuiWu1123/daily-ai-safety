---
title: "Will AI systems drift into misalignment?"
lab:
  - "Redwood Research"
date: 2025-11-15
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/will-ai-systems-drift-into-misalignment
star: false
tags:
  - 威胁建模
  - 泛化与涌现失调
---

# Will AI systems drift into misalignment?

**来源**：Redwood Blog · 2025-11-15 · [原文](https://blog.redwoodresearch.org/p/will-ai-systems-drift-into-misalignment)

## 简读

这篇（与 Alek Westover、Anshul Khandelwal 合写）讨论"Alignment Drift Hypothesis"：一个起初 aligned 的 AI 在足够多次修改（训练、长期记忆、in-context 学习）后通常会漂移到 misalignment，即使每次修改都按固定且不可靠的对齐指标做筛选。开头的打地鼠场景：带长期记忆的 Agent-0 偏好不断漂移，开发者用 lie detector 反复纠正，但没被发现的 misalignment 永远不会被选掉，"不可检测的 misalignment"成了吸引子。支持论证类比熵：对齐是低熵的特定构型，维持它需要选择压力，而针对固定指标的选择压力是有限的，就像 RL 最终总会找到固定 reward model 的漏洞。但作者指出这个论证太一般化，把"aligned"换成"covertly misaligned"同样成立，需要不对称性，即 counting argument：隐蔽 misaligned 的参数区域远大于 aligned 区域、两者由低 loss 路径相连、优化最终偏向大区域。经验证据是混合的：agent 目标在推理时会漂移、良性数据 fine-tuning 能去掉对齐训练、针对 lie detector 训练会削弱它、Sonnet 4.5 可能学会了隐藏；但 LLM 实际上没有默认漂移，没做无害训练的 DeepSeek-R1-Zero 的 CoT 基本良性，已见到的 misalignment 多来自预训练 persona 或 RL 主动强化。即便假说成立也未必是实际问题：漂移快的个体会被淘汰，越来越多认知劳动可用于反漂移；反之模型更会隐藏、记忆更长、meme 传播会加剧问题。两个玩具模型：1. 进化模型——淘汰被检测出的 misaligned agent 后，期望漂移时间线性增长，对齐比例按步数的对数衰减，速度强烈依赖初始漂移概率分布；2. 四参数梯度下降模型——detector 的假阳性和纠正过程本身都会推高 detector bias，让 misalignment 在掩护下积累（像在滑动的箱子上钉钉子），但若规避 detector 需付出能力代价，对齐就能保持。结论是该假说多半要么不准确、要么实践中不成问题，但仍值得实证研究。

