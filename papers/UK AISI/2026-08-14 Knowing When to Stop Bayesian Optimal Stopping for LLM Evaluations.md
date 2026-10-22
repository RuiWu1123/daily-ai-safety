---
title: "Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations"
lab:
  - "UK AISI"
date: 2026-08-14
source: "AISI Research"
url: https://www.aisi.gov.uk/research/knowing-when-to-stop-bayesian-optimal-stopping-for-llm-evaluations
other_versions:
  - "https://www.aisi.gov.uk/blog/optimal-stopping-spending-evaluation-compute-where-it-counts"
tags:
  - 评估方法
---

# Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations

**来源**：AISI Research · 2026-08-14 · [原文](https://www.aisi.gov.uk/research/knowing-when-to-stop-bayesian-optimal-stopping-for-llm-evaluations)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/optimal-stopping-spending-evaluation-compute-where-it-counts)

## 简读

前沿评估越来越贵（有的要上亿 token，单个 agentic 任务可能值数百美元），而 AISI 此前又发现固定且偏小的预算会系统性低估 agentic 能力，所以算力要花在刀刃上。现有 LLM 评估通常对每道题重复固定次数，哪怕某些 model-task 组合跑几次就已经很精确，另一些高方差的组合却在预算耗尽时仍没估准；IRT 式的自适应选题能减少题量，但需要事先校准过的题库，新 benchmark 或安全关键 benchmark 往往没有。AISI 的 Toby Pilditch 提出 optstop，把评估当成序贯测量：在两个层级（题内重复、grouping 内的题）分别跟踪 Bayesian credible interval，grouping 层用 hierarchical Bayesian 模型做 partial pooling；停止规则有两条，区间足够窄（precision）或区间不再变化（stabilisation），两者都不满足就跑满原定预算，不会把真正嘈杂的估计提前截断。支持 binary、ordinal、continuous 三种得分，所有题目始终可被采样。针对"罕见成功恰恰最关键"的能力检测场景，有一个非对称保守机制：估计成功率低于 1% 时把有效区间宽度乘以 5 倍、收紧稳定判据，要求更多数据。验证用 3×3 设计（三种得分类型 × 低中高三档表现，基于 MATH、GPQA Diamond、WritingBench 等，200 题、10 epoch），九个设定都触发了提前停止，节省 57.2% 到 97.3% 的计划试验，平均 81.1%，截断与完整运行的平均绝对分差 0.006（归一化 0–1）；层级 meta-analysis 估计的整体截断偏差为 +0.0003，97% HDI 完全落在 ±0.02 的 ROPE 内。continuous 节省最多（平均 95%），ordinal 和 binary 约 73–75%，因此作者建议条件允许时用连续或有序 rubric 而不是 pass/fail。局限：节省幅度取决于评估设计，更精简的配置能省的有限；方法依赖 grouping 内观测可交换和随机化呈现顺序（Inspect 的 sample_shuffle 默认不开）；接近 0% 或 100% 时区间可能因 shrinkage 覆盖不足，模拟中 94% 名义区间实际覆盖约 80%，作者强调保证的是区间宽度而非频率学覆盖率；且只验证了单一实验配置。为降低采用风险，可以事后跑、shadow mode 只报告本可节省多少、满意后再开 live。optstop 作为与 Inspect 集成的开源 Python 包发布，附带验证代码和数据。

