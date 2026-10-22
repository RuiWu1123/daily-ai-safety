---
title: "DeepSeek-R1 Evaluation Results"
lab:
  - "METR"
date: 2025-03-05
source: "METR Research"
url: https://metr.org/evaluations/deepseek-r1-report/
tags:
  - 危险能力评估
---

# DeepSeek-R1 Evaluation Results

**来源**：METR Research · 2025-03-05 · [原文](https://metr.org/evaluations/deepseek-r1-report/)

## 简读

METR 对 DeepSeek-R1（经第三方托管调用，METR 与 DeepSeek 无关联）做了两项双用途自主能力评估，结论是它只比 DeepSeek-V3 略好，没有超出现有模型的自主能力。通用自主能力评估用 76 个任务（69 个来自 27 个任务族、侧重网络攻击、AI R&D、软件工程和自主复制适应，外加 7 个 RE-Bench 任务），人类耗时从 5 分钟到 8 小时，任务刻意比真正危险所需的门槛容易，所以达不到人类水平是缺乏危险能力的好信号。scaffold 用 Triframe 的变体（每轮生成计划、6 个候选命令、各打两次分再执行最高分），因为 R1 当时不支持原生 function calling，改为让它输出 code-fenced 命令只执行第一个，并在后续上下文中去掉 CoT 以减少冗长，这些改动在开发集上有提升；预算 800 万 token、10 小时，temperature 1。结果 R1 的 50% time horizon 略超 35 分钟，V3 略低于 33 分钟，略好于 o1-preview、远不如 Claude 3.5 Sonnet (New)，大致相当于 2024 年 9 月的前沿；80% 成功率下没有任何模型能做超过 20 分钟的任务。AI R&D 评估用 6 个 RE-Bench 任务（排除了容易靠运气猜数的 scaling law 任务），用 AIDE scaffold、R1 作主 agent、V3 作反馈模型，30 分钟一次的 best-of-k 聚合；R1 在每任务 16 小时预算下相当于第 28 百分位的人类专家，与 V3 和 GPT-4o 相当，低于 Claude 3.5 Sonnet 和 o1，16 小时的 R1 约等于 1 小时的 o1，作者认为其能力不足以显著加速算法进步；人工抽查没有发现作弊。最让人意外的是 test-time CoT 几乎没带来提升，GPT-4o 到 o1-preview 的差距大得多，而 R1 论文在 LiveCodeBench、Codeforces 上比 V3 高 30、38 个百分点，但在 SWE-Bench Verified、Aider-Polyglot 上也只高 7、3 个点；推理延迟高并不能解释差距，因为推理与执行时间的分布与其它模型相似。定性上 R1 数学和编程强，有时能一次写对中等长度程序，但常见失败模式包括在 CoT 里幻觉工具调用结果、指令遵循弱（不返回或返回多个调用）、CoT 结构混乱或多重闭合标签、难以从错误中恢复、CoT 冗长重复且偶尔混用语言，作者推测基础的 agency 后训练可能大幅提升能力。整体意味着前沿 open-weight 模型在这些任务上与 7 个月前的 SOTA 持平，但便宜 5–28 倍。局限包括 elicitation 只是中等程度（不到一周就明显改善开发集表现）、未验证模型不会 sandbag、剔除服务器错误 run 可能抬高分数、部分任务可能被推理扩展策略接近饱和、人类 baseline 样本少、任务比现实干净、R1 不会控制思考长度可能浪费 token 预算，以及结果对任务集选择敏感。

