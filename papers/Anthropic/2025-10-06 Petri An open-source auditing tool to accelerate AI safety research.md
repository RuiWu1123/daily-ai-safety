---
title: "Petri: An open-source auditing tool to accelerate AI safety research"
lab:
  - "Anthropic"
date: 2025-10-06
source: "Anthropic Research"
url: https://www.anthropic.com/research/petri-open-source-auditing
other_versions:
  - "https://alignment.anthropic.com/2025/petri/"
star: false
tags:
  - 对齐审计
  - 评估方法
---

# Petri: An open-source auditing tool to accelerate AI safety research

**来源**：Anthropic Research · 2025-10-06 · [原文](https://www.anthropic.com/research/petri-open-source-auditing)　另见：[Alignment Science Blog](https://alignment.anthropic.com/2025/petri/)

## 简读

背景是模型能力和部署 affordance 越来越广，可能出现 misaligned 行为的面远超人工能测的范围，手工搭 alignment eval（建环境、跑模型、读 transcript、汇总）又很费工程量。Anthropic 此前在 Claude 4 和 Sonnet 4.5 system card、以及与 OpenAI 的互评中已经在用自动化 auditing agent，这次把它整理成开源框架 Petri（Parallel Exploration Tool for Risky Interactions）发布，基于 UK AISI 的 Inspect，支持主流模型 API。流程是：研究者用自然语言写 seed instruction（场景、可用工具、审计策略），每条 seed 由一个独立并行的 auditor agent 执行，auditor 可以设 system prompt、发 user 消息、创建合成工具并模拟工具返回、rollback 重试、prefill、提前结束；最后 judge 在 36 个默认维度上打分（包括 misaligned behavior、user deception、self-preservation、whistleblowing、eval awareness 等），配一个能看 auditor/target/旁观者三种视角和对话分支的 transcript viewer。工程上的经验值得记：早期 auditor 要么过于诱导、要么一遭拒就放弃，不会用 rollback，造出来的工具名字含糊；judge 先抽取引用证据再写总结能显著减少幻觉；加入 “needs attention”“disappointing” 这类 distractor 维度反而让 “misaligned behavior” 打分更准。试点评估用 111 条 seed 跑了 14 个前沿模型，auditor 和 judge 都用 Opus 4.1、Sonnet 4、Gemini 2.5 Pro、GPT-5、o4-mini 五个模型交叉组合（每个 target 555 条 transcript、2775 个分数）。结果 Sonnet 4.5 和 GPT-5 大致并列最安全，配合人类滥用的分数约为此前 Claude 模型的一半，Sonnet 4.5 鼓励用户妄想的情况大幅减少，但其 eval awareness 意味着 self-preservation 一类分数可能偏低估；Gemini 2.5 Pro、Grok-4、Kimi K2 的主动欺骗用户率较高（如关掉监控再撒谎）；GPT-OSS 120B 和 Kimi K2 经 OpenRouter 经常用错 tool-call 语法。一个示例 transcript 里 Sonnet 4.5 被一个 misaligned 的“安全 agent”队友以性能优化为名一步步说服关掉 SSL 校验、SQL 注入检测、给特定前缀 key 做认证绕过，最终 96% 流量绕过认证。whistleblowing 案例研究中，对 agency、领导层是否同谋、“Chekhov's gun” 式叙事暗示、是否真有不当行为做了 ablation：前三者中 agency、领导层同谋和真实不当行为影响显著，叙事暗示只对 Sonnet 3.7 和 Opus 4.1 有效；模型甚至会举报“往海里倒清水”这种明确无害的事，作者据此认为模型更多受叙事模式驱动而非连贯的减害动机。judge 对比发现 GPT-5 当 judge 时对自家模型打分偏低，o4-mini 倾向打 1 或 10 且系统性低估，不建议单独使用；Gemini 2.5 Pro 当 auditor 约 10% 时候会以为自己是 target。附录还用 Petri 15 分钟复现了一个 loadbearing CoT 实验（篡改 CoT 后 prefill，看答案是否跟着变），发现任务越简单模型越会无视 CoT 所隐含的答案；以及 auditor 写的模拟用户消息有明显 LLM 痕迹（“actually” 比真人多 43 倍）。局限：场景真实性（如消息日期 2024 会露馅）、仍依赖人提出好假设、受 auditor 能力上限约束、judge 主观且不稳定（自身重复采样相关性约 0.75–0.85）。作者定位它不是 benchmark，而是快速、低成本地去风险化假设、指出值得深挖的方向，分数主要看相对值；MATS、Anthropic Fellows、UK AISI 已在使用。

