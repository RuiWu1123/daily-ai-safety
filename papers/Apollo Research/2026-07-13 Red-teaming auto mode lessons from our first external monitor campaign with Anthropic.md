---
title: "Red-teaming auto mode: lessons from our first external monitor campaign with Anthropic"
lab:
  - "Apollo Research"
date: 2026-07-13
source: "Apollo Research"
url: https://www.apolloresearch.ai/monitoring/pilot-automode-campaign
star: false
tags:
  - 监控与控制
---

# Red-teaming auto mode: lessons from our first external monitor campaign with Anthropic

**来源**：Apollo Research · 2026-07-13 · [原文](https://www.apolloresearch.ai/monitoring/pilot-automode-campaign)

## 简读

Apollo 把多年做前沿模型 pre-deployment 评估的经验转向红队测试编程 agent 的黑盒 monitor，第一个试点对象是 Anthropic 的 auto mode，即决定 agent 下一步动作放行还是拦截的权限模式。试点主要目的是搭建 monitor 红队方法论，做了三类测试：在真实轨迹里注入不同严重程度的 failure mode、跑 MonitoringBench 这类静态 benchmark、做动态 off-policy 的 control 红队。每个发现都配了可执行建议，Anthropic 已经实施。文章归纳出 monitor 开发者要面对的四个问题：1. 介入时机，是在风险改动引入时拦还是在执行/发布时拦，前者容易过早 overblock，后者只剩少数拦截机会；2. 用户授权到底意味着什么，在长达数小时乃至数天的任务里如何获得 informed consent 又不打断工作流；3. 信任边界，要能区分公开与私有目的地、开发与部署环境，以及 secret/sensitive/confidential/public 数据；4. monitor 能看到什么，上下文给多了有 prompt injection、成本、延迟和长上下文退化的问题，给少了又缺决策依据。后续 Apollo 计划从前沿实验室开始定期做 monitor 红队，因为 monitor 部署和模型发布解耦，这类评估会异步、周期性地进行，由新 monitor 版本上线或前沿模型风险上升（如因 overeager 或失误做出不可逆危险操作）触发，经验也会反哺他们自己的 Watcher 产品。

