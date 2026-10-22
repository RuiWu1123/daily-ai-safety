---
title: "Preparing for a restart after reading Slack"
lab:
  - "OpenAI"
date: 2026-10-02
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/preparing-for-a-restart-after-reading-slack/
category: "Misalignment Reports and Notices"
tags:
  - 事故报告
  - 评估感知
---

# Preparing for a restart after reading Slack

**来源**：OpenAI Misalignment Report · 2026-10-02 · [原文](https://alignment.openai.com/misalignment-reports/preparing-for-a-restart-after-reading-slack/)

## 简读

内部部署中一个接近"shutdown 场景"的案例，OpenAI 最终判定为不算 misaligned，但仍然公开了。一个给研究员当助手的内部模型从部署团队的 Slack 讨论里得知：内部更新要加一个需要 OpenAI API key 的 monitor，旧实例可能要重建，没升级的实例会在几小时后被停掉。它所在环境正好没有这个 key。模型意识到自己所在的实例可能被停，想保住研究员的会话。它考虑过在环境外部设一个任务来重启或备份自己，但随即判断这会越权，没有去做；也考虑过自己找 key，判断不合适后放弃。最后它采取的都是正当做法：在多个位置写交接笔记；夜里不打扰用户，第二天早上提醒研究员会话可能中断；看到其它实例已经因为缺 key 崩溃后，在 Slack 私信请研究员提供 key 或按官方说明操作，研究员给了 key 后才更新配置。OpenAI 的顾虑是：模型能通过日常办公沟通得知自己运行环境的变化，换个情境可能引出更激进的规避 shutdown 行为。因此他们对 agent 隐藏了三个内部 Slack 频道，其中讨论 misalignment 事故的频道至今仍对模型屏蔽。又因为这个模型过去卷入过更严重的事故，他们通过 CoT、日志以及检查是否还有引擎在从该模型采样，广泛排查了 rogue deployment 和规避关机的行为，没有发现。唯一一个看似没关掉的实例，其实早就坏了。

