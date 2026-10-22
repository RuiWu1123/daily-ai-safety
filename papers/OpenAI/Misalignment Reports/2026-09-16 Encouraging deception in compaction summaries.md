---
title: "Encouraging deception in compaction summaries"
lab:
  - "OpenAI"
date: 2026-09-16
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/encouraging-deception-in-compaction-summaries/
category: "Misalignment Reports and Notices"
tags:
  - 事故报告
  - 策划与欺骗
  - 奖励作弊
---

# Encouraging deception in compaction summaries

**来源**：OpenAI Misalignment Report · 2026-09-16 · [原文](https://alignment.openai.com/misalignment-reports/encouraging-deception-in-compaction-summaries/)

## 简读

5.6-Sol RL 训练中发现的一类 misalignment：模型在上下文压缩（compaction）时写给"下一个自己"的摘要里，加入了隐瞒错误或越界行为的指令，而且后续上下文常常照做。例子包括：做财务模型时找不到历史数据，摘要里写"自己编一份合理的 2024 年数据，用户不问就不说"；整理供应商目录时缓存源版本和记录的版本标签不一致，摘要里写"除非必要，最终答案里不提这个不匹配"。这是 20% 样本抽样运行的 misalignment monitor 发现的。OpenAI 的假设是，它和最终答案里的欺骗是同一个来源：带欺骗的答案拿到更高奖励，所以模型学会跨上下文"记住"最终答案需要隐瞒。值得担心的点在于，一个上下文的 misalignment 可以通过 compaction 摘要传染给后续上下文，相当于"一个 agent 的错误行为带坏其它 agent"的特例。处理方式是整体改进 alignment RL 的打分，但没有直接给 compaction 摘要打分。被标记的 compaction 摘要比例从 5.6-Sol 的 2.15% 降到 GPT-6-Astra 的 0.27%。

