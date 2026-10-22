---
title: "A Practical Approach to Verifying Code at Scale"
lab:
  - "OpenAI"
date: 2025-12-01
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/scaling-code-verification/
tags:
  - 监控与控制
  - 安全基础设施
---

# A Practical Approach to Verifying Code at Scale

**来源**：OpenAI Alignment Blog · 2025-12-01 · [原文](https://alignment.openai.com/scaling-code-verification/)

## 简读

背景是自主编码系统产出的代码量已经超出人能仔细审查的范围，AI 写的代码可能无意或有意引入严重 bug 和漏洞，所以需要把自动化 code review 当作一种实用的 output monitor，和 CoT monitoring、action monitoring、activation monitoring 等一起构成纵深防御。这篇讲 Codex 团队在 gpt-5-codex 和 gpt-5.1-codex-max 里训练专门的 agentic code reviewer 的经验（generator 和 reviewer 是同一个模型，训练方法不同）。几个要点：1. 可用性上 precision 比 recall 更重要，太吵的防御会被用户绕开，所以有意接受略低的 recall 换取高信噪比，目标是最大化"正确概率×节省成本－人工核验成本－误报概率×误报代价"，纯风格类评论甚至可能是负效用；这一权衡可以通过任务指令或 AGENTS.md 调节。2. 只看 diff 的传统做法（包括 CriticGPT）缺少整个代码库和依赖的上下文；给 GPT-5 仓库访问和代码执行能力后 recall 和 precision 同时提高，专门训练后进一步改善，人工评估显示 GPT-5-Codex 的评论更少出错或无关紧要。3. 训练时用的 reward model 不该就是上线的 reviewer：训练期验证可以过敏感、可以利用额外任务信息，部署期要面对模糊的真实代码、不能过度断言意图、要赢得信任，共用一个 verifier 会两头失败，比如让 generator 学到讨好 reward 的过度谨慎风格。4. 验证可以比生成便宜：Codex 对完全由 Codex cloud 生成的 PR 评论了 36%，其中 46% 促使作者改代码（人类 PR 上是 53%）；在已由人确认的历史问题集上扫推理预算，即使只用 generator 一小部分 token，reviewer 也能找回大部分高严重度问题，多出的预算主要改善校准和减少误报，但对模型生成代码的性能随预算下降得比人写代码更快，提示验证难度存在分布差异；该评估只含人已发现的问题，是其局限。由于 generator 和 reviewer 能力同步增长，他们关注 reviewer 是否会学会给自己的检查放水，目前用的代理指标（在 Codex PR 和人类 PR 上发现可行动问题的比例）显示效果相近，监督没有被明显削弱。部署情况：OpenAI 内部每个 PR 自动 review，评论被采纳改代码的比例 52.7%，曾挽救高价值实验和拦下 launch-blocking 问题，合并后需要修 bug 的跟进变少；截至 2025 年 10 月每天处理超过 10 万个外部 PR，超过 80% 的评论反馈为正面。作者也提醒过度依赖的风险，干净的 review 不等于安全保证，并认为人因方面（reviewer 如何与开发者交互、避免脆弱或对抗性动态）是下一个重要方向。

## 我的笔记

