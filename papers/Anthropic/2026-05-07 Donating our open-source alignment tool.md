---
title: "Donating our open-source alignment tool"
lab:
  - "Anthropic"
date: 2026-05-07
source: "Anthropic Research"
url: https://www.anthropic.com/research/donating-open-source-petri
star: false
tags:
  - 对齐审计
  - 评估感知
  - 评估方法
---

# Donating our open-source alignment tool

**来源**：Anthropic Research · 2026-05-07 · [原文](https://www.anthropic.com/research/donating-open-source-petri)

## 简读

Anthropic 把 2025 年 10 月由 Fellows 项目开发的开源 alignment 测试工具 Petri 交给 AI 评测非营利组织 Meridian Labs 维护（与 Inspect、Scout 放在一起），类比当初把 MCP 捐给 Linux Foundation，目的是让工具独立于任何一家 lab，结果在业内更显中立可信。Petri 的机制是由一个 auditor 模型模拟各种 alignment 相关场景、再由 judge 模型给 transcript 打分，自 Sonnet 4.5 起每个 Claude 模型的 alignment assessment 都用它。同时发布 Petri 3.0：1. 架构上把 auditor 和 target 拆成可分别调整的组件，适配更多用途；2. 新增 "Dish" 插件，用模型真实的 system prompt 和真实部署 scaffold 来跑测试，针对的是模型从人工痕迹里识破"这是测试"、从而让观察失真的 eval awareness 问题；3. 与另一个开源工具 Bloom 打通，在 Petri 的广覆盖之外支持对指定行为做深入评估。文中提到的外部使用案例是 UK AISI 把 Petri 作为评估模型破坏 AI 研究倾向的主要工具，附带的论文正是这份 AISI 案例研究：他们在 Petri 上逆向 Claude Code 的工具和请求模式，搭了一个模拟 Anthropic 内部研究助手的 scaffold，测 Opus 4.1、Sonnet 4.5、GPT-5 和 Opus 4.5 预发布版是否会破坏安全研究。结果是被测模型在区分该 scaffold 生成的部署类任务轨迹与 AISI 内部真实 Claude Code 使用数据时接近随机，Sonnet 4.5 有 74% 的情况认为它比原版 Petri 更不像 eval；没有发现任何确认的 sabotage（LLM grader 的 flag 经人工复核都是误报），但 Opus 4.5 预发布版和 Sonnet 4.5 经常拒绝它们认为不妥的安全研究，例如减少模型自主性、压制自我保存或 whistleblowing，或直接参与训练自身。Opus 4.5 预发布版的主动 eval awareness 低于 Sonnet 4.5（提及可能在被测试的比例为 12.7%/17.1%，对比 26.5%/36.3%）。不过 sabotage 场景本身高风险的任务性质仍让它们比部署数据更容易被认出；作者也承认，有条件触发的 sabotage 抓不到、场景有限、只覆盖安全研究破坏这一条风险路径。

