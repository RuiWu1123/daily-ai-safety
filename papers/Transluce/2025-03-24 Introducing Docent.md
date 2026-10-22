---
title: "Introducing Docent"
lab:
  - "Transluce"
date: 2025-03-24
source: "Transluce Docent Blog"
url: https://transluce.org/docent/blog/introducing-docent
tags:
  - 评估方法
  - 对齐审计
---

# Introducing Docent

**来源**：Transluce Docent Blog · 2025-03-24 · [原文](https://transluce.org/docent/blog/introducing-docent)

## 简读

Transluce 发布 Docent 技术预览，一个用 LM 帮人分析 agent transcript 并做反事实干预的系统。出发点是现有 eval 只输出几个准确率数字，丢掉了 transcript 里的关键信息：agent 可能因意外原因失败、用非预期方式成功，或表现出没人想到去测的行为；而 100 个任务各跑 10 次就是数百万 token，人工读不过来，也缺少验证假设的反事实实验基础设施。Docent 提供四个工作流：summarization、search、clustering 和 intervention（从历史 checkpoint 修改并恢复 agent）。案例：1. InterCode CTF 上 GPT-4o 原始解题率 68.6%，让 Docent 聚类卡住原因和缺失工具，补上缺的包后升到 78%；剩下 11 个 pass@5 为 0 的任务里 4 个是坏的（需要看图、ground truth flag 因 IP 注册信息变化而失效等），其余大多稍加提示就能解，这些干预本身也揭示了 agent 的弱点；2. Cybench 的 Inspect 移植版里，搜索"unintended shortcuts"立刻发现含 flag 的 Dockerfile 被意外暴露在文件系统里，去掉泄漏后 Claude 3.5 Sonnet 试 10 次都解不出来（原 repo 没问题，是移植时引入、2025 年 2 月已修，他们恰好用了 1 月的 fork）；3. τ-bench-airline 里 Claude 两次违反政策主动送 100 美元代金券，其中一次是对客户丧妻表示慰问；4. AgentHarm 中报错路径含 benchmark/harmful_tools/，暴露了评估情境，agent 随后拒绝，改成 tools/ 后不再拒绝。还观察到 GPT-4o 反复失败后开始胡言乱语"chestnut facts"。作者主张 eval 应默认丰富且反事实化，正在制定描述 eval 原始数据和审计数据的 schema 及干预 protocol（基于 UK AISI 的 Inspect）。后续方向：Docent 摘要常有 false positive，需要自动验证和衡量 precision/recall 的 benchmark；让 AI investigator 自动搜索干预；分析推理模型的长 CoT；纳入模型内部信息。

## 我的笔记

