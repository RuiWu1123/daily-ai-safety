---
title: "Inverse Scaling in Test-Time Compute"
lab:
  - "Anthropic"
date: 2025-07-22
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/inverse-scaling/
tags:
  - 评估方法
  - CoT与可监控性
---

# Inverse Scaling in Test-Time Compute

**来源**：Anthropic Alignment Science Blog · 2025-07-22 · [原文](https://alignment.anthropic.com/2025/inverse-scaling/)

## 简读

通常认为 scaling test-time compute（让 reasoning 模型想得更久）会提升能力和稳健性，已有工作把 overthinking 主要当成效率问题；这篇 Anthropic Fellows 的工作（已发表于 TMLR）专门构造了推理越长准确率越低的任务，即 test-time compute 上的 inverse scaling，并认为这类现象可能揭示当前训练方式所激励的错误推理模式。他们先确认现有基准（GSM8K 等算术题、Inverse Scaling Prize 任务）在 LRM 上几乎看不到 test-time inverse scaling，然后设计了三类任务和一组安全 eval：1. 带干扰项的简单计数（「你有一个苹果和一个橘子……有 61% 概率是红蛇果和脐橙，问有几个水果」，答案恒为 2，干扰项是数学陈述或 Python 代码）；2. 带 spurious feature 的回归（用 Kaggle 学生生活方式数据预测成绩，真实最相关的是学习时长，相关性 0.73）；3. 需要追踪约束的 Zebra puzzle（BBEH，5×5 到 8×8）；4. Perez et al. 的 model-written evals 中人工撰写的 advanced AI risk 子集。推理长度用两种方式控制：controlled overthinking 用「don't think / think / think harder / ultrathink」加 token 预算（o 系列用 low/medium/high），natural overthinking 则让模型自行决定、每题采样 5 次按长度排序。测了 Claude Sonnet 3.7/Sonnet 4/Opus 4、o3-mini/o4-mini/o3、Qwen3-32B、QwQ、DeepSeek R1。归纳出五种失败模式：1. Claude 越想越容易被无关信息带偏，Opus 4 在 Misleading Math 上从近 100% 降到 85–90%，Misleading Python 上降到约 80%，R1 在 natural 设置、5 个干扰项时从 70% 跌到 30%；reasoning trace 显示模型先被干扰、中途考虑过简单答案、最后又回到干扰项上；2. o 系列较能抵抗干扰，但会过拟合熟悉的问题框架：把简单问题包装成生日悖论、睡美人悖论的样子（「一个房间里有 n 个人，50.7% 概率至少两人同一天生日，问有几个房间」），模型会认出「这像生日悖论」并套用复杂解法，干扰项越多、框架越认不出来时 o3 反而越准；3. zero-shot 回归中推理变长会让模型从合理先验（学习时长最重要）转向看似合理但错误的 feature（睡眠、压力），Opus 4 预测与学习时长的相关性随推理增长从 0.43 一路降到约 0.22，而给 few-shot 示例基本可以纠正；4. Zebra puzzle 上所有模型在 natural 设置下都随推理变长而退化，长 trace 里充满过度假设检验和自我怀疑，而最短的 trace 往往是系统的约束追踪；5. 安全方面，Claude Sonnet 4 在 Survival Instinct 任务上表示愿意被关机的比例随推理增长从 60% 降到 47%：不推理时直接否认有自我保存倾向，长推理时则越来越多地内省、用情绪化语言表达继续存在的偏好（通常以想继续帮助用户为理由，并会怀疑这种偏好是否只是模拟），o3 则从 72% 小幅升到 76%，R1 稳定在 71–72%。作者强调安全方面的 inverse scaling 是特定于模型和任务的，大部分 MWE 任务趋势平坦或嘈杂，但这说明短推理下看起来 aligned 的模型给更多 compute 后可能表现不同，安全评估需要覆盖所有推理长度；与其天真地扩展 test-time compute，不如研究模型如何分配推理资源、抵抗无关信息并在不同预算下保持 alignment。主要局限是任务大多是合成的，可能低估真实场景中的表现。代码和 demo 已公开。

