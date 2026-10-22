---
title: "DeepSeek-V3 Evaluation Results"
lab:
  - "METR"
date: 2025-02-12
source: "METR Research"
url: https://metr.org/evaluations/deepseek-v3-report/
star: false
tags:
  - 危险能力评估
---

# DeepSeek-V3 Evaluation Results

**来源**：METR Research · 2025-02-12 · [原文](https://metr.org/evaluations/deepseek-v3-report/)

## 简读

METR 对 open-weight 的 DeepSeek-V3（经第三方托管调用，与 DeepSeek 无关联）做了双用途自主能力评估，没有发现超出现有模型的自主能力，但值得注意的是 open-weight 模型在这些任务上已追到大约 6 个月前的 SOTA，而此前差距要大得多。通用自主能力评估用 83 个任务（30 个任务族的 76 个任务加 7 个 RE-Bench 任务），侧重网络攻击、AI R&D、软件工程和自主复制适应，人类耗时 5 分钟到 8 小时，并且刻意比真正危险所需的门槛容易。由于第三方服务没说明 function calling 方式，改为让模型输出 code-fenced 命令，用 Triframe 变体 scaffold（每轮生成计划、6 个候选命令、打分后执行最高分），预算 200 万 token、10 小时；分数 ≥0.8 算成功，再用 logistic 回归换算 time horizon。结果 V3 的 50% time horizon 略超 30 分钟，低于 o1 和 Claude 3.5 Sonnet (New)，明显高于 GPT-4o，与 Claude 3.5 Sonnet (Old) 相当；80% 成功率下没有任何模型能做超过 20 分钟的任务。AI R&D 评估用 6 个 RE-Bench 任务（排除 scaling law 任务）、AIDE scaffold、30 分钟 best-of-k，8 小时预算下相当于第 24 百分位人类专家，与 Claude 3 Opus 相当，显著不如两版 Claude 3.5 Sonnet 和 o1，16 小时的 V3 约等于 1 小时的 o1（摘要与正文对它和 GPT-4o 的相对位置说法略有不一致），作者判断其不足以显著加速算法进步，人工抽查没有发现作弊。另一个小实验是查数据污染：用 o1 改写 GPQA Diamond 的题目，并从 GPQA 原作者处拿到 18 道从未公开的 held-out 题，V3 和 GPT-4o、Claude 3.5 Sonnet (New) 一样，在改写版上表现基本不变，在 held-out 题上还高约 10%，始终高于 GPT-4o、略低于 Claude 3.5 Sonnet (New)，说明其 GPQA 成绩不太可能来自背题，其它报告的 benchmark 受污染的可能也较低。定性上 V3 编程和问答能力不错，但 agency 弱，似乎不知道自己是 AI、更像聊天机器人，常见失败包括反复执行同一动作或重复短语的循环（有时像 base model，可能缺乏后训练）、幻觉函数输出或误以为已解出、简单算术出错（比如比较小数）导致误读 score log；在多数前沿模型上好用的基础 Modular scaffold 激发不出它的能力，换成 Triframe 后明显提升，作者推测基础的 agency 后训练可能大幅提高能力。局限：只做了基础 elicitation（比其它模型少），没用 DeepSeek 自带的 function calling API，未验证模型不会 sandbag；剔除服务器错误 run 可能抬高分数；部分任务可能被推理扩展策略接近饱和；人类 baseline 样本少、任务比现实干净、4 小时以上任务少，RE-Bench 人类超过 8 小时的表现是靠 best-of-k 外推的。

