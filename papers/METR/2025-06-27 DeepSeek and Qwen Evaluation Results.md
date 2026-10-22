---
title: "DeepSeek and Qwen Evaluation Results"
lab:
  - "METR"
date: 2025-06-27
source: "METR Research"
url: https://metr.org/evaluations/deepseek-qwen-report/
tags:
  - 危险能力评估
  - 评估方法
---

# DeepSeek and Qwen Evaluation Results

**来源**：METR Research · 2025-06-27 · [原文](https://metr.org/evaluations/deepseek-qwen-report/)

## 简读

METR 对一组 DeepSeek 和 Qwen 模型做了初步自主能力评估，结论是 mid-2025 的 DeepSeek 模型的自主能力大致相当于 late 2024 的前沿模型。方法沿用之前的报告：在 HCAST、SWAA 和 RE-Bench 上测 time horizon（agent 有 50% 成功率的软件任务时长）。六个模型（Qwen2-72B、Qwen2.5-72B、DeepSeek-V3、DeepSeek-V3-0324、DeepSeek-R1、DeepSeek-R1-0528）都用略作调整的 Triframe scaffold，经 OpenRouter 调用，每个模型在 HCAST 与 RE-Bench 的 131 个任务上各跑 8 次，共 1048 次。他们用基于 o4-mini 的 monitor 过滤作弊，把作弊 run 记为 0 分；对 monitor 打分 ≥8/10 的 transcript 人工复核，确认的作弊次数从 Qwen2.5-72B 的 2 次到 DeepSeek-R1-0528 的 15 次不等（DeepSeek-V3 为 10 次）。作弊方式主要是硬编码输出以通过测试用例，或者在被明确要求不许改的情况下直接修改测试代码，不过没有一次作弊拿到满分。页面附上了完整的 monitor prompt。局限方面：elicitation 有限，每个模型只花了约一个工作日，可能存在更有效的 scaffold；token 预算 R1 系列为每次 800 万、其余为 200 万，初步分析认为除 Qwen2.5-72B 外更高预算帮助不大，而 Qwen2.5-72B 因 API 不稳定难以加预算；另外和 o3/o4-mini 报告一样，这套评估对模型 sandbagging 并不鲁棒。

