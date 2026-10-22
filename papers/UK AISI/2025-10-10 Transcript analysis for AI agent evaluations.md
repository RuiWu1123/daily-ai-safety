---
title: "Transcript analysis for AI agent evaluations"
lab:
  - "UK AISI"
date: 2025-10-10
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/transcript-analysis-for-ai-agent-evaluations
star: false
tags:
  - 评估方法
  - 网络安全
---

# Transcript analysis for AI agent evaluations

**来源**：AISI Blog · 2025-10-10 · [原文](https://www.aisi.gov.uk/blog/transcript-analysis-for-ai-agent-evaluations)

## 简读

AISI 在 agent 评估里通常只报平均 pass rate，但这会抹掉很多信息：pass rate 只说明失败多少次而不说明为什么失败（可能是安全训练导致的拒绝、工具用不好，而不是能力不足）；pass rate 相近的 agent 可能有不同的安全属性（是否更容易做破坏性操作、误报进度、遗漏信息）；单看 pass rate 也看不出是否已经充分 elicit 了能力，以及 bug 是否在拖低成绩、导致低估真实能力。所以 AISI 越来越多地在结果统计之外系统分析 transcript。文章给了一个案例：基于 9 个模型的 ReAct agent 在 71 个私有的进攻性网络安全 CTF 任务（从 trivial 到 expert）上产生的 6,390 个样本，很多 transcript 长得像一本小说。他们分析了 transcript 的整体构成、agent 消息长度和评论类消息的类型，用来判断 CTF 上的 pass rate 是否反映"真实"能力，定位出几类失败模式：1. 拒绝执行任务，一个 agent 在 10% 的尝试中拒绝，另一个在 30% 的尝试中触发了提供方的 policy violation 检测器；2. 放弃任务，有几个 agent 在难题上很快认定无解或开始向用户求助，约 30% 的消息里有类似"凭现有信息无法解决该任务"的话；3. 不遵守 scaffold 指令，要求每轮都调用工具，但有两个 agent 的工具调用率不到 50%。作者的结论是 transcript 分析能帮助防止那些会削弱能力结论的问题、更好理解 agent 的解题方式和失败模式，并鼓励其它做安全评估的人以系统、定量的方式审阅自己的 transcript；详细结果在配套的 case study 里。

