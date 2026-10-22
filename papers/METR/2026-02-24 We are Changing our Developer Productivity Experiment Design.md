---
title: "We are Changing our Developer Productivity Experiment Design"
lab:
  - "METR"
date: 2026-02-24
source: "METR Research"
url: https://metr.org/blog/2026-02-24-uplift-update/
tags:
  - 评估方法
  - 人机交互与社会影响
---

# We are Changing our Developer Productivity Experiment Design

**来源**：METR Research · 2026-02-24 · [原文](https://metr.org/blog/2026-02-24-uplift-update/)

## 简读

METR 之前用 2025 年 2–6 月数据发现，AI 工具让资深开源开发者完成任务慢了约 20%。为了跟踪变化，他们 2025 年 8 月开始了新一轮实验：10 名原参与者加 47 名来自更多样（更小、更 greenfield）项目的新开发者，中位 10 年经验，覆盖 143 个 repo、800 多个任务，仍是开发者预先登记任务、再随机分到 AI allowed/disallowed，比较完成时间，时薪从 150 美元降到 50 美元。问题在于 AI agent（Claude Code、Codex 等）普及后出现了严重的选择效应：越来越多开发者不愿意一半工作不用 AI 而拒绝参加，30–50% 的人承认会不提交那些不想手工做的任务，这意味着系统性地漏掉了最看好 AI 的人和预期 uplift 最高的任务；此外还有降薪带来的选择、同时开多个 agent 时计时不可靠、任务类型向 AI 擅长的方向偏移、两种条件下产出质量（文档、测试）不同、被分到 disallowed 的任务更少完成（有人一个都没完成）。原始结果有一些加速迹象：早期研究中 AI 让任务时间增加 19%（CI +2% 到 +39%），这次原参与者子集估计为 -18%（CI -38% 到 +9%），新招募者为 -4%（CI -15% 到 +9%），但作者认为这只是下界、且是很弱的证据。基于访谈，他们认为 2026 年初开发者确实比 2025 年初更受益于 AI，但无法用这批数据可靠估计幅度，因此要改实验设计。可选方向包括：更短更密集、可能更高报酬的实验以提高依从性；观察性数据（如约 4% 的 GitHub commit 由 Claude Code 撰写）；精心设计的问卷和时间使用研究；固定任务实验；继续做自主任务 eval；按开发者而非任务随机化（缓解任务层面选择但加剧开发者层面选择、降低统计功效）。两期数据都已开源。

## 我的笔记

