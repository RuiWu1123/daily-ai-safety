---
title: "Diagnosing a performance regression on Terminal-Bench with Docent"
lab:
  - "Transluce"
date: 2026-02-11
source: "Transluce Docent Blog"
url: https://transluce.org/docent/blog/terminal-bench
star: false
tags:
  - 评估方法
---

# Diagnosing a performance regression on Terminal-Bench with Docent

**来源**：Transluce Docent Blog · 2026-02-11 · [原文](https://transluce.org/docent/blog/terminal-bench)

## 简读

Docent 团队的案例教程：Terminal-Bench 官方榜上 GPT-5.1 Codex 在同一 scaffold 下比 GPT-5 Codex 低 6.5 个百分点，为什么？他们自己重跑（每任务每模型 3 次 rollout），差距 11.4 个百分点，方向一致。流程是用自然语言让 Claude Code 生成 Docent SDK 脚本，分三步：1. 把同一任务上一个模型失败、另一个成功的 run 配对，让 LLM judge 对 100+ 对写失败原因，带 citation 可回查原 transcript；2. 汇总发现失败模式不同，GPT-5 Codex 多是执行错误（不做验证、写坏文件），GPT-5.1 Codex 多是时间管理差（装 GPU 包而非 CPU 包、中止训练任务而不是等待），触发超时；3. 用 Docent Query Language 定量检验，GPT-5.1 Codex 超时率 49.4% vs 29.1%，且分布广泛（24 个任务只有它超时，反过来只有 3 个）；只看两者都不超时的任务，结果反转，GPT-5.1 Codex 领先约 7 个百分点，整体 0.27 vs 0.39 的差距可完全归因于超时。结论是低分不一定是能力缺陷：system prompt 从未提到时间限制，GPT-5.1 Codex 可能在选更长程的策略而被截断。分析不到一小时、覆盖 256M+ token。作者注明这是工作流示意而非定论：绝对分数低于官方榜；只保留无超时任务可能偏向简单任务；还有超时却通过测试的边缘情况，因为 Terminal-Bench 只检查最终文件状态。

