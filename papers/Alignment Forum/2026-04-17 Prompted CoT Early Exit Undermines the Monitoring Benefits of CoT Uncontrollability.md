---
title: Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability
lab:
  - Alignment Forum
date: 2026-04-17
source: Alignment Forum（UK AISI / Anthropic；Elle Najt, Asa Cooper Stickland, Xander Davies）
url: https://www.alignmentforum.org/posts/BuAPifQmHf24xB29n
star: true
tags:
  - CoT与可监控性
  - 监控与控制
---

# Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability

**来源**：Alignment Forum（UK AISI / Anthropic；Elle Najt, Asa Cooper Stickland, Xander Davies） · 2026-04-17 · [原文](https://www.alignmentforum.org/posts/BuAPifQmHf24xB29n)

## 简读

Yueh-Han et al. 的 CoT-Control 发现模型让 CoT 遵守风格约束（全小写、避免某词等）远比控制回答难，这对 control 是利好：schemer 很难把恶意推理藏起来。作者（Najt、Cooper Stickland、Davies）给出绕法：提示模型"early exit"，结束 CoT、把推理挪到风格可控的回答里。两种策略：CoT Blanking 让模型立即退出 CoT 并在回答里写 explanation.md、self_critique.md 等文档推理，对 GPT-5.4 和 Gemini 3.1 Pro 有效（CoT 合规超过 93%），对 Opus 4.6 无效；CoT Replacement 让 CoT 只背一句符合约束的儿歌再退出，对 Opus 4.6 有效。在 GPQA、HLE 的 6 种控制类型上，三个模型用各自最佳策略都达到高可控性，准确率只掉 4–8pp，而完全不推理掉 20–29pp，即挪走推理保留了大部分收益。有个细节：模型对 CoT 的内部叫法不同，GPT-5.4 只有称作 "analysis channel" 时才清空推理。前沿 API 只给推理摘要，baseline 可控性无法直接测，作者用 Claude 计费 token 反推（replacement 下多余 thinking token 中位数约 11），并借 Sonnet 4.5、Opus 4.5 和 GPT-5.2 已报数值佐证。这些做法会被"CoT 过短"的 monitor 发现，于是又让 CoT 讨论"圆形多还是方形多"作诱饵、在回答里解题，三个模型都产出正常长度的离题 CoT，Opus 4.6 准确率接近基线。开源模型中 DeepSeek-R1 最难退出。作者强调这只说明被提示时有此能力，离自主使用还差构造 prompt、真正隐藏推理和意愿几步，但一个简单 prompt 就够，意味着不大的训练压力也可能让模型学会。缓解建议：评估对此类 jailbreak 的易感性，监控过短或离题 CoT 和 agent 修改自身 system prompt，检测 CoT 外的推理，RL 中惩罚 early exit，研究让 CoT 更不可控。代码开源。

