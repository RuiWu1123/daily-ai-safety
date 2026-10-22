---
title: "Many SWE-bench-Passing PRs Would Not Be Merged into Main"
lab:
  - "METR"
date: 2026-03-10
source: "METR Notes"
url: https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
tags:
  - 评估方法
---

# Many SWE-bench-Passing PRs Would Not Be Merged into Main

**来源**：METR Notes · 2026-03-10 · [原文](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)

## 简读

动机是 benchmark 分数如何对应真实有用性并不清楚，这篇 note 聚焦 SWE-bench Verified 用自动 grader 而非 maintainer review 这一差异。做法是请 scikit-learn、Sphinx、pytest 的 4 名现任 maintainer 在 GitHub 上盲审 296 个 AI 生成的 PR（Claude 3.5/3.7 Sonnet、4 Opus、4.5 Sonnet 和 GPT-5，覆盖 95 个 issue），只送审通过 grader 的 patch（抽查发现 grader 误拒率很低），maintainer 给出是否合并、拒绝原因和进度评分，审阅时没有 CI 且被要求忽略测试要求。为处理审阅噪声，还混入 47 个真实已合并的人类 golden patch，结果只有 68% 被合并，所以分数按 golden baseline 归一化。主要发现：maintainer 合并率平均比 grader 分数低约 24 个百分点，约一半通过测试的 PR 不会被合并；改用"进度 ≥80%"标准结果类似；改进速度上 maintainer 口径每年慢约 9.6pp，但只在 10% 水平显著且不稳健，只算弱证据。拒绝原因的演变：3.5 到 3.7 Sonnet 通过率大涨但核心功能问题变多，3.7 到 4 Opus 主要把"不过 grader"变成"只是代码质量差"，4.5 Sonnet 主要改进代码质量，GPT-5 代码质量明显弱于 Anthropic 模型。作者强调这不是能力上限：agent 只有一次提交、不能根据反馈迭代，更好的 elicitation 可能解决很多问题；局限还有只看一个 benchmark 子集、审阅不完全真实、patch 平均只改约 17 行、最新模型只到 Sonnet 4.5。结论是不要天真地把 benchmark 外推到真实有用性，这一差距也让 METR 早先"开源开发者用 AI 反而变慢"的结果显得不那么意外，类似问题可能也存在于 GDPval 等 benchmark。

## 我的笔记

