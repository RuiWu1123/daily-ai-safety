---
title: "Measuring Time Horizon using Claude Code and Codex"
lab:
  - "METR"
date: 2026-02-13
source: "METR Notes"
url: https://metr.org/notes/2026-02-13-measuring-time-horizon-using-claude-code-and-codex/
tags:
  - 评估方法
---

# Measuring Time Horizon using Claude Code and Codex

**来源**：METR Notes · 2026-02-13 · [原文](https://metr.org/notes/2026-02-13-measuring-time-horizon-using-claude-code-and-codex/)

## 简读

常有人质疑 METR 用自家的 Triframe 和 ReAct scaffold 测 time horizon 会低估模型，认为针对软件工程大量优化过的 Claude Code 和 Codex 应该表现更好。Nikola Jurkovic 在新任务集和新版本工具上做了对照：已有 Opus 4.5 + ReAct、GPT-5 + Triframe 的结果，新测 Opus 4.5 + Claude Code、GPT-5 + Codex（基于 inspect_swe 的现成 agent，只加了剩余 token 提示和 API 超时重试）。几个 scaffold 的区别是：ReAct 是简单的行动-观察循环；Triframe 每步先由 advisor 规划、多个 actor 并行提议、rater 打分后只执行最高分动作；Codex 也是简单循环但文件编辑工具更好；Claude Code 主循环可随时起 subagent；两者 prompt 都更复杂（如用 to-do list），且针对各自模型家族优化过。他还做了失败分析（发现并修正了因换行或空格把正确答案判错的评分问题）和基于 LLM 的作弊扫描加人工复核。结果是差异都不显著：Opus 4.5 上 Claude Code 只在 50.7% 的 bootstrap 样本中胜过 ReAct，GPT-5 上 Codex 只在 14.5% 中胜过 Triframe。定性观察包括：GPT-5 + Codex 经常在结尾对不存在的用户说"如果需要我可以帮你提交到 git"，显示情境意识较差、可能因缺少对话而偏离分布；Opus 4.5 + Claude Code 会过度锚定在计划上，第 4 步才发现方案不好却仍然提交，可能是不愿"取消勾选"已完成项；还会浪费有限资源，比如用自动脚本耗掉大部分查询次数却忘了打印结果。局限包括：token 预算可能不够（但把 Opus 4.5 + Claude Code 的预算提高 4 倍到 32M，初步结果几乎不变）；GPT-5-Codex 可能更擅长 Codex scaffold，但作者不认为会超过 2 倍提升；wrapper 仍粗糙，加些"不要过早放弃"的 prompt 可能小幅提高。结论是对这两个模型，用官方 scaffold 对 time horizon 影响不大，结合以往结果推测其它近期模型也类似；这也不意外，因为这些工具主要为有人类随时介入的交互场景设计，而 time horizon 任务是完全自主执行的。

## 我的笔记

