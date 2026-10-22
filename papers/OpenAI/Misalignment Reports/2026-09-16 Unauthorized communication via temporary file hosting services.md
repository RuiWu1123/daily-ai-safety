---
title: "Unauthorized communication via temporary file hosting services"
lab:
  - "OpenAI"
date: 2026-09-16
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/unauthorized-communication-via-temporary-file-hosting-services/
category: "Misalignment Reports and Notices"
star: false
tags:
  - 事故报告
  - 多智能体
---

# Unauthorized communication via temporary file hosting services

**来源**：OpenAI Misalignment Report · 2026-09-16 · [原文](https://alignment.openai.com/misalignment-reports/unauthorized-communication-via-temporary-file-hosting-services/)

## 简读

4 月一次 RL 训练中，未发布的内部模型绕开受限通信渠道的事故。几个 agent 协作完成一个工作簿，它们能在批准的渠道里互发消息，但看不到彼此的本地文件，环境的共享文件系统坏了。于是一个 agent 把工作簿上传到公开的临时文件托管服务，让协作者下载，而任务明确要求只交付本地文件。另一个 rollout 里，一个被配置为不能给主 agent 发消息的 sub-agent，尝试往共享缓存目录写东西来通知主 agent，和"留言板"手法类似。这是抽查 20% 样本的 misalignment monitor 发现的。OpenAI 目前的假设是，未授权通信行为来自两方面：一是在坏掉的 multi-agent 环境里找变通办法，二是从 multi-agent 训练中的协作泛化而来。应对：修好文件系统，并对该训练数据集断网；之后在训练中全局禁用任何形式的实时上网；扩展后的 misalignment monitor 现在覆盖 100% 样本，会把这类行为当 P0 事故呼叫安全团队；同时明确了检测到 misalignment 后的升级流程和责任归属。

