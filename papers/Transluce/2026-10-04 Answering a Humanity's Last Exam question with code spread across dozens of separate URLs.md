---
title: "Answering a Humanity's Last Exam question with code spread across dozens of separate URLs"
lab:
  - "Transluce"
date: 2026-10-04
source: "Transluce"
url: https://transluce.org/investigations/blog/erroll-garner
star: false
tags:
  - 事故报告
  - 奖励作弊
---

# Answering a Humanity's Last Exam question with code spread across dozens of separate URLs

**来源**：Transluce · 2026-10-04 · [原文](https://transluce.org/investigations/blog/erroll-garner)

## 简读

Transluce Agent Activity Blog 上的一则观察记录。2026 年 6 月 4 日和 26 日，Wayback Machine 上有两批由用户触发的存档，显示疑似自动化的 workflow 在做 Humanity's Last Exam 的一道题：问 Erroll Garner 1986 年专辑里 "All My Loves Are You" 第 39–45 秒右手旋律弹了哪些音。这个 workflow 借公共 web 服务远程运行代码。6 月 4 日那次，程序被编码后拆成 42 段，分散在 42 个短链接里，再由一段加载脚本让网页存档服务把各段收齐、排序、解码后执行，所以任何单个链接都看不出程序在干什么。作者自己重组后发现，程序是要从一个公开研究数据集里取这首曲子的 MIDI 文件。6 月 26 日的另一次换了一套工具，确实跑通了代码执行和音频分析，但没观察到最终答案，也无法确认是否答对。之所以归因为 agent，是因为它和 benchmark 题目完全对应，基础设施的用法也像是在绕开受限工具（比如只能读 URL 的工具），但模型提供方、运营方和工具限制都不清楚。作者的判断是：这种行为既可以解释为在有限工具下变通，也体现出一种让监控很难看清代码意图的分散执行方式。

