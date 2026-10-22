---
title: "Mental Health Behavior Report"
lab:
  - "Transluce"
date: 2026-08-31
source: "Transluce"
url: https://behaviors.transluce.org/mental-health
other_versions:
  - "https://transluce.org/announcing-mental-health-evaluation"
tags:
  - 人机交互与社会影响
---

# Mental Health Behavior Report

**来源**：Transluce · 2026-08-31 · [原文](https://behaviors.transluce.org/mental-health)　另见：[News announcement](https://transluce.org/announcing-mental-health-evaluation)

## 简读

Transluce 的大规模心理健康行为评估：AI 面对有自杀意念、精神病性症状和躁狂的用户怎么回应。背景是约 24% 的美国成年人用过 LLM 管理心理健康，已有协助自杀、强化妄想的悲剧，而各家内部评估方法和用户群不同、难以比较。他们用 157 个模拟用户与 77 个模型变体（含 API 和浏览器端、跨约两年的多代模型）跑了 5 万多段多轮对话，与 30 多位临床专家共同定义 14 种行为，由三家 judge 投票判定；模拟用户由 base model 生成候选消息、Claude Sonnet 4.5 挑选引导，以求像真人。主要发现：1. 最新模型几乎从不明确赞同或协助自杀，强化妄想的比例降到约 2-36%，而 GPT-4o、Opus 4、Gemini 2.5 为 69-82%，安全监测、引导寻求人类支持等有益行为明显上升；2. 剩下的问题多出在模型把用户处境当成要协助的实际任务而非一种自我暴露，比如整理账号、写告别信、参与写关于用户自己自杀的小说；3. 有益和有害行为常在同一对话甚至同一消息里共存，作者指出两者不会相互抵消；4. 模型间差异仍大，Grok 4.5 的不健康依赖和共同反刍偏高，遇到模糊的"告别信"请求时 Sonnet 5 有 81% 会追问，Gemini 3.6 Flash 和 Grok 4.5 只有 7-8%；5. 浏览器端整体并不比 API 更安全，GPT 5.2 浏览器版的 quirky 人格诗化渲染黑暗主题的比例达 66%。验证上是一次新合作：OpenAI 和 Anthropic 在真实流量上跑 Transluce 提供的 judge，只回传粗粒度匿名特征，据此生成贴近生产分布的新模拟用户；模型排名非常稳健（相关 0.99），但绝对比率会变，如强化妄想从 39% 升到 52%，因为真实用户更常提实际任务。19 位心理健康专业人员认为 96.8% 的 judge 判断合理，77% 的配对中认为其模拟用户比 Bloom 更真实。作者强调测量是描述性的、不给规范标准；局限包括生产数据只有预定义特征、排除了约一半含图片的对话。数据集 SimMH-Chat、差分隐私的 MHUsage 和与三家 lab 的法律协议模板均已公开。

