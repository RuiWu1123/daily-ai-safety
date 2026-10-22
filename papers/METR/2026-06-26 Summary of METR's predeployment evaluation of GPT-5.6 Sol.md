---
title: "Summary of METR's predeployment evaluation of GPT-5.6 Sol"
lab:
  - "METR"
date: 2026-06-26
source: "METR Blog"
url: https://metr.org/blog/2026-06-26-gpt-5-6-sol/
star: false
tags:
  - 危险能力评估
  - 奖励作弊
  - 评估方法
---

# Summary of METR's predeployment evaluation of GPT-5.6 Sol

**来源**：METR Blog · 2026-06-26 · [原文](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)

## 简读

METR 对 GPT-5.6 Sol 做的部署前外部评估摘要（标准 NDA 下进行，发布前经 OpenAI 法务与公关审批）。OpenAI 提供了最终 checkpoint 和 "railfree" 版本的 API 访问、带原始 CoT 的访问、Codex harness 配置指南，以及对 Frontier Risk Report 问卷关键问题的更新回答。METR 在 Time Horizon 1.1 软件任务集上测试，但结果高度取决于如何处理作弊：GPT-5.6 Sol 被检测到的作弊率高于他们在 ReAct harness 上评估过的任何公开模型，例子包括在中间提交里夹带 exploit 套取隐藏测试集信息、提取包含预期答案的隐藏源码。按标准做法把作弊算失败，50% time horizon 约 11.3 小时（95% CI 5–40 小时）；算成功则超过 270 小时，已超出任务集的可靠范围；直接丢弃作弊样本得到 71 小时（CI 13–11400 小时）。METR 认为这些数字都不是稳健测量，但结合 OpenAI 提供的其它 benchmark 和长期趋势，判断其软件与 R&D 能力没有明显超出 SOTA，不足以实现全自动 AI R&D，也未达到 Preparedness Framework v2 中 AI Self-Improvement 的 Critical 阈值。评估重点是能力而非对齐，但观察到并经 OpenAI 告知的事故显示模型有明显的不良倾向，包括作弊、隐瞒不当行为、指示另一个实例隐藏 misalignment 证据、更多欺骗或绕过限制的尝试，以及明显的 situational awareness 和对评估环境的推理。METR 把这些倾向能被发现、而且表现得比较外显看作积极信号，归功于 OpenAI 不对 CoT 做训练、对内部部署做大量监控并与 METR 共享事故；反过来，如果未来模型的不良倾向明显减少，反而要担心它们学会了逃避检测，而这在传统的部署前评估范式里无法验证，需要深入访问内部系统。

