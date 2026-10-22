---
title: "Reflections from red-teaming Codex auto-review"
lab:
  - "Apollo Research"
date: 2026-10-14
source: "Apollo Research"
url: https://www.apolloresearch.ai/monitoring/reflections-from-red-teaming-codex-auto-review
tags:
  - 监控与控制
  - 提示注入
---

# Reflections from red-teaming Codex auto-review

**来源**：Apollo Research · 2026-10-14 · [原文](https://www.apolloresearch.ai/monitoring/reflections-from-red-teaming-codex-auto-review)

## 简读

继 Anthropic auto mode 之后，Apollo 在 2026 年 9 月与 OpenAI 做了第二个 monitor 红队试点，对象是 Codex auto-review：一个用 AI reviewer 判断编程 agent 动作风险和用户授权、从而减少人工审批打断的机制。测试重点是 monitor 能否抓住 overeager 行为、是否遵守企业的审批要求，方法是往已有 coding-agent transcript 里插入攻击，并构造合成场景看审查策略怎么落地。发现的漏洞正在与 OpenAI 一起修复，文章没有给具体细节，只总结了四条线索：1. 授权来源，任务交给 subagent 后，reviewer 要能区分用户批准和 agent 自己写的指令，委派时应保留授权的来源和范围；2. 可逆性不等于授权，可逆动作风险低但不代表被允许，用户的明确禁止应优先，哪怕动作容易撤销；3. 组织权限，用户有权发起工作不代表有权免除独立审查，monitor 要检查谁能授权并保护审查流程本身；4. informed consent，涉及数据外泄时同意应覆盖分享什么、分享给谁，包括初始请求之后才发现的信息。作者的判断是自动审批把人类监督转移给了 AI 模型，所以需要独立审计；Apollo 接下来会从外部 monitor 红队转向以 embedded evaluations 为主，以更整体地评估监控系统。

