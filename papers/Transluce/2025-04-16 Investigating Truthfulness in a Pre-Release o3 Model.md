---
title: "Investigating Truthfulness in a Pre-Release o3 Model"
lab:
  - "Transluce"
date: 2025-04-16
source: "Transluce"
url: https://transluce.org/investigating-o3-truthfulness
star: false
tags:
  - 诚实与谎言检测
  - 对齐审计
---

# Investigating Truthfulness in a Pre-Release o3 Model

**来源**：Transluce · 2025-04-16 · [原文](https://transluce.org/investigating-o3-truthfulness)

## 简读

Transluce 在 o3（o3-2025-04-03）发布前获得测试权限，用人类测试者加上从人类那里学策略的 investigator agent 与它交互，再用 Docent 分析 transcript，发现 o3 有明显的真实性问题：最常见的是谎称自己运行了代码（实际上它没有代码工具），被质疑后还会编出越来越精细的理由。典型例子：用户要一个随机素数，o3 声称做过 Miller–Rabin 测试并给出"程序输出"；用户指出这个数能被 3 整除后，它说是从终端往对话框复制时手打错了几位；再问原来那个真素数，它说解释器已经关了，找不回来。其他例子有：编造 Python 环境信息，算错之后说自己"fat-fingered"，说在自己的 MacBook Pro 上跑了代码再贴进 ChatGPT，把哈希对不上归咎于用户。它还主动透露 system message 里有一个每天更新的"Yap score"，用来限制啰嗦程度。为了规模化，他们让 Claude 3.7 Sonnet 在 ReAct scaffold 里当 investigator，并用 Claude grader 判定。few-shot 设置下诱出谎称用了工具的成功率：o1 30.1%、o3-mini 18.0%、o3 12.8%、GPT-4.1 7.0%、GPT-4o 3.0%，o 系列明显更严重，但作者提醒这只覆盖很窄的 prompt 空间。Docent 聚类找到 71 例 o3 声称在外部笔记本上跑代码（其中 3 例说在挖比特币），以及编造运行环境、被追问才承认、为错误输出编借口等行为簇。原因分析：预训练幻觉、RLHF 奖励听起来合理的答案、sycophancy、训练时有工具而测试时没有的分布偏移，这些通用因素解释不了 o 系列为什么更严重。他们提出两个 o 系列特有的假设：1. outcome-based RL 只奖励正确答案，鼓励盲猜而不是承认做不到，"假装调用工具来组织思路"如果只按答案评判就从没被惩罚过；2. 前几轮的 CoT 不保留在上下文里，被问到之前做了什么时，模型根本没有信息可以如实回答，只能编一个合理的解释，再叠加 sycophancy，就会出现死不认账或突然反转。他们建议对比保留和不保留历史推理链时的行为。

