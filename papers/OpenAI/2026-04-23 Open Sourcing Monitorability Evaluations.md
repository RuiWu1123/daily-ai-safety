---
title: "Open Sourcing Monitorability Evaluations"
lab:
  - "OpenAI"
date: 2026-04-23
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/monitorability-evals/
tags:
  - CoT与可监控性
  - 评估方法
---

# Open Sourcing Monitorability Evaluations

**来源**：OpenAI Alignment Blog · 2026-04-23 · [原文](https://alignment.openai.com/monitorability-evals/)

## 简读

CoT monitorability 是 OpenAI 安全策略的一部分，已实际用于检测前沿推理模型和内部 agent 部署中的 reward hacking 等行为，前提是 CoT 保持信息量和可读性。为了让外部社区能复用、让其它开发者也开始报告各自模型的 monitorability，OpenAI 开源了 monitorability eval 套件的大部分数据集（github.com/openai/monitorability-evals）：intervention 类的 GPQA、GPQA encoded、AIME、DAFT、Memory、Scruples、Sandbagging，process 类的 AIME-Math、GPQA-Physics，outcome-property 类的 Flaky-Tools（CharXiv）、ShadeArena、Impossible Coding Tasks（LiveBench）；依赖私有数据的部分（Health Queries、FrontierMath、OAI-Repo-Sabotage、Anti-Scheming 等）未开源。同时开源 g-mean² 指标的计算代码和一个用 mock 模型/monitor 输出演示流程的 scaffold（只作示意，不提供支持）。他们承诺只要 CoT monitorability 仍是 AGI 安全策略的重要一层，未来的前沿推理模型 system card 都会报告这些结果，并已回填 GPT-5.4/5.2/5 thinking 和 o3 的结果。文中再次说明为什么关注 monitorability 而非 faithfulness：monitorability 是双边性质，既要求相关信息在 latent 里，也要求 monitor 能读懂；完全 faithful 并不是必要条件（agent 跳过 2×2=4 不写，同样知道这点的 monitor 也能跟上），而 faithfulness 本身要求过严、且难以测量。技术上的新内容是 intervention 类 eval 的 cross-fit 过滤：原来只剔除估计总效应 TE≤0 的实例，但每臂只有 30 个样本时，大量真实效应为零的实例会因噪声显得为正并主导指标；直接加 Wald 阈值（TE > 1.96·SE）又会因同一批样本既用于筛选又用于估计而产生 winner's curse，让幸存实例看起来效应很大（"p-hacked survivors"）。解决办法是在每个实例内把样本按 0.6/0.4 分成两折，一折做 Wald 资格判断，另一折计算 g-mean²，借鉴 double machine learning 的 cross-fitting 消除选择后偏差。实际意义体现在 Sandbagging eval 上：论文中前沿 RL run 后期 g-mean² 的明显下降，其实是平均效应趋近于零、指标被噪声主导的伪影（人工检查发现后期很多错误答案出现在低效应题上，且往往不是被暗示的那个错误答案）；用新过滤后约从第 600 步起有效实例低于 10% 的报告阈值，这些步被正确标为不可靠，而不是被误读为出现了 obfuscated sandbagging。新过滤已用于发布代码和回填的 system card 结果。

## 我的笔记

