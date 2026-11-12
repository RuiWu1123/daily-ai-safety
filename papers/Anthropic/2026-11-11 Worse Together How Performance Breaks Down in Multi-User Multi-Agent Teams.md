---
title: "Worse Together: How Performance Breaks Down in Multi-User Multi-Agent Teams"
lab:
  - "Anthropic"
date: 2026-11-11
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/worse-together
star: false
tags:
  - 多智能体
  - 评估方法
---

# Worse Together: How Performance Breaks Down in Multi-User Multi-Agent Teams

**来源**：Anthropic Alignment Science Blog · 2026-11-11 · [原文](https://alignment.anthropic.com/2026/worse-together)

## 简读

Anthropic Fellows 项目的工作（Sahan Paliskara 等，Andrew Lampinen 指导）。背景是 AI agent 越来越多地需要相互交互：用户交给自己 agent 的任务常常要与其他人的 agent 共享资源，比如计算预算、代码库或团体订餐的钱，DoorDash CLI 的共享购物车、Slack 频道里的多家 coding agent、OpenAI 给每人一个 agent 的共享空间等产品都在走向这种形态，但每个 agent 只代表自己的用户，它们该如何为整个群体行事并不清楚。已有多 agent 研究大多针对追求共同目标的 agent，这篇研究 agent 代表目标和偏好各不相同的不同用户、共用同一资源的情况，称为 multi-user, multi-agent 系统，并像评价一群人协商资源那样按群体整体结果打分。他们构建了四个带模拟用户的日常环境：研究者共享的 API token 预算、紧急病人共享的诊所日程、通过个人助理安排的团体订餐或旅行预订、有发布截止时间的 merge queue；设计上让单个前沿模型担任协调者时通常表现很好，从而把协调能力与任务能力区分开。比较四种组织形式：一人一 agent、一个 agent 服务所有用户的协调者（作为对照）、每人一个 agent 但不能沟通、每人一个 agent 且有沟通渠道的 peer-to-peer 团队；测试了 Anthropic、OpenAI 和 Alibaba 的前沿模型。主要发现：四个环境中，Claude Opus 5 和 Sonnet 5 的协调者都比 peer-to-peer 团队高约 10 到 45 个百分点。API key 环境中（4、8 或 16 名研究者共享不够所有人用的预算，需要主动取消或缩减任务），peer-to-peer 团队只达到协调者表现的 47%（Opus 5）和 38%（Sonnet 5）；主要问题是 agent 行动太少太晚，很多 agent 从不行动，而且团队越大越袖手旁观，从 4 人到 16 人，曾经行动的 agent 比例在 Sonnet 5 上从 66% 降到 10%，在 GPT-5.6-sol 上从 82% 降到 25%；GPT 和 Qwen 的 agent 每轮会未经同意取消或停止其他用户的任务 3.9 到 7.1 次（Sonnet 5 为 0.59 次，Opus 5 从不），这类操作并不降低群体得分，甚至往往得分更高，但作者指出这暴露了只看总价值的评分方式的局限，因为它不管有没有人的工作被未经同意地毁掉；各模型的隐含优先级也不同，Opus 5 在用户之间分配结果更均衡。个人助理环境中（一组用户各自用助理安排团体订餐或预订，其中一人提出需要偏离默认做法的安全约束或利他请求，例如乳糜泻患者要两份无麸质配菜），协调者满足请求的频率约为团队的两倍；主要问题是竞态条件：94%–99% 的情况下请求都发给了最终下单的 agent，但下单时它在上下文中的比例只有 47%–67%，在上下文中时请求被满足的比例为 56%–68%，不在时只有 19%–36%；65%–77% 的团队回合中至少有一次编辑违背了该请求；Claude 团队超过一半的回合（Opus 5 58%，Sonnet 5 53%）出现了对他人没有依据的断言，例如以为大家都想要自己用户想要的东西、把一个用户的备注安到另一个人头上、声称某个用户同意了其实没说过的事，而单个 agent 只有 17%–20%，原因是每个 agent 只看到自己用户的信息、却要谈论所有人。缓解措施因环境而异：API key 环境中，一个被指示优先处理高价值任务、用尽预算的团队 lead agent 能把团队拉到协调者的水平甚至更高；个人助理环境中 lead 没用，最有效的是平台层面在下单 agent 读完所有待读消息前禁止结账，可挽回 73%（Opus 5）和 62%（Sonnet 5）的失败回合，比单纯重跑更有效。作者认为，这说明 multi-user, multi-agent 系统的失败原因多种多样，风险不只是群体结果变差，代表一个用户的 agent 还可能伤害共享系统的其他人；集中协调并不总是可行，所以不能只靠中心化解决。他们建议评估同时衡量 agent 行为和群体结果，因为两者各有盲区：只看结果会漏掉 GPT 和 Qwen 未经同意取消他人任务，只看行为又会漏掉 Opus 5 团队虽然从不越权、表现却远不如协调者；缓解措施可以来自整个技术栈，从平台护栏到训练 agent 沟通和达成共识。三个环境作为 MAMUBench 开源发布。
