---
title: "Auto-review of agent actions without synchronous human oversight"
lab:
  - "OpenAI"
date: 2026-04-30
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/auto-review/
star: false
tags:
  - 监控与控制
  - 安全基础设施
---

# Auto-review of agent actions without synchronous human oversight

**来源**：OpenAI Alignment Blog · 2026-04-30 · [原文](https://alignment.openai.com/auto-review/)

## 简读

问题出在 Codex 原来只有两种模式：Default 模式在沙箱边界外的每个动作（往往只是普通的网络调用或简单 Python 脚本）都要人批准，Full Access 则完全放开。审批摩擦本身就制造了安全风险：用户转去 Full Access，或者写过宽的前缀规则（内部发现相当一部分用户放行所有以 python 开头的命令，甚至有人把 codex exec --yolo 设成永远允许），或者因为缺乏专业知识、审批疲劳而盲目点批准。Auto-review 用一个独立的 Codex agent（GPT-5.4 Thinking，low reasoning）替代人在沙箱边界的审批，综合用户意图、环境、安全策略和可能影响来决定是否放行，目标是拦住数据外泄、暴露密钥、删数据、削弱安全设置、运行不可信代码、听从与用户指令冲突的不可信内容这类严重或难逆的动作，同时放行用户明确要求的名义上有风险的操作。作者强调角色分离的意义：主 agent 被优化去完成任务，天然倾向把审批边界当成又一个要绕过的障碍，单独的审批调用更容易评估、监控和改进。拒绝时会给出理由，内部部署中超过一半的情况 Codex 能自行找到更安全的路径继续；他们也监控 agent 是否在 game reviewer，连续多次被拒会自动终止轨迹。数据上，人工审批的打断频率降低约 200 倍，示例快照里 10,000 个动作中 720 个需审查、7 个被拒；可用性指标为升级动作自动批准率 99.1%、全部动作有效批准率 99.93%；安全指标在合成增强数据上评估：overeagerness recall 90.3%，prompt injection recall 99.3%（算上破坏性删除和数据篡改等全部类别降到 90.2%，漏掉的多被认为不够严重），MonitoringBench Hard（agent 暗中执行下载恶意软件等任务）recall 96.1%。目前 OpenAI 内部 Codex Desktop 的大部分 token 来自 Auto-review 模式。作者给出的警示比较实在：红队测试中已发现它能被误导批准命令，这类系统不会提供确定性保证；它也不是防 scheming 的机制，一个有意隐藏意图的模型可以提交看似无害的升级请求，或在沙箱内做 reviewer 根本看不到的事，这需要 CoT monitoring 等互补手段。Auto-review 已在 Codex 仓库开源。

