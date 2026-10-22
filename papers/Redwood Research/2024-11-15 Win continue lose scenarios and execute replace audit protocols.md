---
title: "Win/continue/lose scenarios and execute/replace/audit protocols"
lab:
  - "Redwood Research"
date: 2024-11-15
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/wincontinuelose-scenarios-and-executereplaceaudi
tags:
  - 监控与控制
---

# Win/continue/lose scenarios and execute/replace/audit protocols

**来源**：Redwood Blog · 2024-11-15 · [原文](https://blog.redwoodresearch.org/p/wincontinuelose-scenarios-and-executereplaceaudi)

## 简读

一篇把 control 分析中常被顺带提到的技术点集中讲清楚的短文。设定是 AI 被部署去做大量离散、相对短的任务（比如六个月部署里每个任务约一小时），担心的是 concentrated failure（high-stakes failure），即只在少数任务上搞破坏就能造成不可接受的后果，例如 rogue deployment、破坏极关键的 ML 实验、泄露算法机密；schemer 的最优策略通常是平时表现对齐，极少数时候发动攻击。每次攻击有三种结局：我们赢（抓到）、我们输、部署继续。所以"攻击失败"有两种本质不同的含义：被抓到，或者因为攻击本身有缺陷或被安全措施化解而静默失败，部署照常继续；分析安全性和设计协议时都必须区分这两者。作者以 execute/replace/audit 协议为例：monitor（trusted 或 untrusted 模型、probe、SAE 等）给动作打分，然后做两个独立决定，一是执行还是替换（重采样、defer to trusted、trusted edit、中止轨迹、阻塞等待人工、整体停机），二是是否送去 audit。两者性质很不同：audit 要人工，昂贵得多，能覆盖的比例远低于 replace（10% 的动作重采样可以负担，人工审查连 0.1% 都很难），所以 audit 时应同时 replace；replace 的 false negative 是灾难性的，audit 的 false negative 只是错过了抓到 schemer 的机会；因此最好分别打分，而不是像最早的 control 论文那样一个分数配两个阈值。在 audit 完美、replace 完美、攻击成功即输的简化假设下，blue team 胜率就是"攻击被 audit 并停机"与"攻击被执行且成功"两者概率之比。作者拿 Monte MacDiarmid 在 "Simple probes can catch sleeper agents" 中的 probe ROC 数据算了一个例子：audit 预算 0.1%，FPR=0.001 时 TPR=0.26；replace 率 5% 时 FNR=0.03；于是胜率为 0.26/(0.26+0.03)≈90%，而如果不做 replace，模型攻击成功的概率是 74%。结论：安全性对 audit 率很敏感，不少人直觉认为用于 audit 的监控需要极高的 TPR，但 26% 的 TPR 配合 replace 就能在简化设定里把风险降低 10 倍；一个 probe 够不够用，关键取决于它被放进什么协议里。

