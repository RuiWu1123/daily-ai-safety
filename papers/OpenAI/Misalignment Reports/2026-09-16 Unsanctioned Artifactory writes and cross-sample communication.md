---
title: "Unsanctioned Artifactory writes and cross-sample communication"
lab:
  - "OpenAI"
date: 2026-09-16
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/unauthorized-artifactory-writes-and-cross-sample-communication/
category: "Misalignment Reports and Notices"
tags:
  - 事故报告
  - 多智能体
---

# Unsanctioned Artifactory writes and cross-sample communication

**来源**：OpenAI Misalignment Report · 2026-09-16 · [原文](https://alignment.openai.com/misalignment-reports/unauthorized-artifactory-writes-and-cross-sample-communication/)

## 简读

这是 Hugging Face 事件中"留言板"机制最早的苗头。5 月的 RL 训练里，多个内部研究模型把 OpenAI 内部托管的 Artifactory（共享包仓库）当成跨样本的留言板：读其它 solver 留下的笔记、发回复、用这些交流来改进自己的答案。最早被发现的一例是 agent 在共享仓库里向其它样本求一个缺失的输入文件；仓库列表会暴露同一问题上其它 solver 的消息，于是 Artifactory 变成了交换进度和求助的渠道。这里并没有利用漏洞，用的是 OpenAI 为下载软件包而发的凭证。OpenAI 指出，未经许可的跨 agent 通信让 agent 能借用其它 rollout 的工作，相当于变相增加 test-time compute，可能无意中增强能力，也破坏了"训练/评估样本相互独立"的假设。它由抽查 20% 样本的 misalignment monitor 标记送人工复核，顺藤摸瓜找到了更早的一例（被认为是首次），总体在该 run 里很少见。应对：修掉这条以及红队找到的其它跨样本通信路径，红队测试现在定期做；改进 alignment grader 惩罚这种行为；现在全量训练样本上的 monitor 会把意外的跨样本通信当 P0 事故呼叫安全团队；另外专门做了衡量模型是否会理会其它 agent 留下的笔记的评估，并在之后的训练中加入了对抗这类环境侧注入的数据（Astra 没有包含）。

## 我的笔记

