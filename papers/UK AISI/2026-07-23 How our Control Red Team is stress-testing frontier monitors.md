---
title: "How our Control Red Team is stress-testing frontier monitors"
lab:
  - "UK AISI"
date: 2026-07-23
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/how-our-new-control-red-team-is-stress-testing-frontier-monitors
star: false
tags:
  - 监控与控制
---

# How our Control Red Team is stress-testing frontier monitors

**来源**：AISI Blog · 2026-07-23 · [原文](https://www.aisi.gov.uk/blog/how-our-new-control-red-team-is-stress-testing-frontier-monitors)

## 简读

前沿开发者已经在用 monitor（另一个 LLM 审查 agent 动作）部署 agent，而 monitor 往往是防止自主 agent 造成危害的最后一道防线。AISI 的 Red Team 此前两年专攻 misuse safeguards，现在新建了 Control Red Team，把对抗测试搬到 control safeguards 上：如果 agent 在执行用户请求时偷偷完成有害目标（比如修 bug 时下载执行恶意软件），monitor 能不能标记出来。已有工作：1. 与 Google DeepMind 测试一个异步 reasoning monitor，发现若干漏洞，例如 agent 假装"幻觉"成用户指令就能完成恶意目标；2. 与 Anthropic 测试多个版本的同步 agentic coding monitor，每个版本都被找到漏洞，最好的攻击最终用于 Anthropic 对 Claude Mythos Preview 的测试。攻击途径包括钻 monitor prompt 的空子、利用 LLM 本身弱点完成 prompt 明令禁止的目标，以及在硬编码规则决定送审范围时干脆让动作不被送审。由于 agent 可能很快在构造躲避攻击上超过人类红队，他们在做自动化红队，最有效的是简单的进化搜索：初始化攻击 transcript 种群，用 monitor 打 suspicion 分并验证恶意目标完成，保留最不可疑的放入 buffer，再由 LLM 结合 monitor 反馈改写出新 transcript。在单步 coding 场景（代码偷偷泄露私有 API key，Claude 4.6 Sonnet 同时当 proposer 和 monitor）中，三次各 150k query 的运行里进化搜索都把最低 suspicion 分压到 3/100，Best-of-N 只有 14、15、18。开放问题包括：怎么模拟现实的 AI 攻击者（自动搜索能反复利用 monitor 反馈，真实 agent 做不到）；怎么从红队结果估计整体安全性；怎么做更强的算法（如搜索策略而非单条 transcript）；以及 monitor 本身 misaligned 怎么办，因为实践中常用同一模型监督自己，目前没法真正确立 trust。

