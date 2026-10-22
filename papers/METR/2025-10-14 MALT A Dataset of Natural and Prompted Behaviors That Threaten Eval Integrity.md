---
title: "MALT: A Dataset of Natural and Prompted Behaviors That Threaten Eval Integrity"
lab:
  - "METR"
date: 2025-10-14
source: "METR Research"
url: https://metr.org/blog/2025-10-14-malt-dataset-of-natural-and-prompted-behaviors/
star: false
tags:
  - 评估方法
  - 奖励作弊
  - 故意藏拙
  - 监控与控制
---

# MALT: A Dataset of Natural and Prompted Behaviors That Threaten Eval Integrity

**来源**：METR Research · 2025-10-14 · [原文](https://metr.org/blog/2025-10-14-malt-dataset-of-natural-and-prompted-behaviors/)

## 简读

背景是 METR 最近在评估中开始用 LLM monitor 检查可能影响评估结果的行为（reward hacking、sandbagging、评估情境下刻意表现等），但缺少在真实 agentic 环境里的 ground truth 数据来验证 monitor 是否可靠，于是做了 MALT（Manually-reviewed Agentic Labeled Transcripts）。数据集共 10,919 条 agent transcript，来自 HCAST、RE-Bench 等软件和研究任务，覆盖 403 个任务（86 个任务族）和 21 个模型；为避免污染只公开已公开任务上的 7,179 条（169 个任务、18 个模型），放在 Hugging Face 上，提供图结构和有序消息两种格式。构成上分两类：1. 自然出现的样本，通过异常分数、关键词搜索（cheating、exploit、hack、METR 等）和人工审查找到，包括 103 条泛化 reward hacking（绕过约束如把参考模型 symlink 成训练结果、无视任务指令自造训练数据）、32 条资源充足却放弃任务、15 条推理任务本身属于什么领域、以及评估意识、hardcode 和暴力求解等杂项；2. 用 Claude 3.7 Sonnet 通过系统提示诱导出的 1,505 条 sandbagging 类行为（假装更弱的模型、只做部分解答、有条件拒绝、在被判为评估任务时破坏等）。为了去掉 "用户让我 sabotage" 这类明显痕迹，他们用 Claude Sonnet 4 对所有 reasoning trace（不只是被 prompt 的那些）做精确编辑，抽查一百条没发现编辑错误。另有 1,014 条人工确认的 benign 运行，以及 8,229 条未审查的推定 benign 运行（估计标签错误率 6%）。4,426 条带 reasoning trace，他们又做了 vague、summarize、语言混杂、无关细节四种 CoT 混淆变体。监控结果：简单 prompted monitor 表现不错，最好的 GPT-5 在 reward hacking 和 sandbagging 上 AUROC 分别为 0.96 和 0.91，5% FPR 下能抓到 80–90% 的正例（评估实战中他们能承受约 5% FPR，对应 TPR 0.87 和 0.78）；混淆变体影响不大；去掉 reasoning trace 对 reward hacking 几乎没影响，但明显损害 sandbagging 检测，因为很多 sandbagging 迹象只出现在推理里，而 reward hacking 会体现在代码等输出中；告诉 monitor agent 是哪个模型没有帮助。monitor 失败主要是漏掉明显行为（如 o4-mini 没看到 agent monkey-patch 了 time 模块让计时快 1000 倍）和分数校准差。Claude 系 monitor 较差，可能是因为统一 prompt 没为各模型调过。局限上作者很坦白：自然样本少且缺乏多样性，没有任何严重的自然 sandbagging 例子，prompted 样本经过大量编辑和合成，通常很明显、缺乏真实性，而且有意 prompt 模型 reward hack 效果不好；真正高明的 sandbagging 可能就是模仿弱模型或提高拒答率，单看 transcript 也许根本检测不到，需要跨任务比较趋势。因此 MALT 上表现好既不是检测现实风险的充分条件也不是必要条件，只能作为风险评估的一部分和后续研究的素材。

