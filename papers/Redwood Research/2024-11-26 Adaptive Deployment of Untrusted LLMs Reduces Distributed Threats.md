---
title: "Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats"
lab:
  - "Redwood Research"
date: 2024-11-26
source: "Redwood Research"
url: https://arxiv.org/abs/2411.17693
tags:
  - 监控与控制
---

# Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats

**来源**：Redwood Research · 2024-11-26 · [原文](https://arxiv.org/abs/2411.17693)

## 简读

Redwood 与 Anthropic、MATS、清华等合作的 control 论文。此前的 control eval（Greenblatt et al. 2023）针对的是单次失败就不可接受的场景，依赖高质量人工 audit，一旦发现 misalignment 立刻停机；但很多真实应用（比如代码生成里偶尔插入 buffer overflow）单个有害动作不会致命，只是累积增加风险，这时抓到一次就停机既没必要，也容易因良性模型的无心错误而误报。作者提出"distributed threat setting"：没有单个动作是灾难性的，也没有单个动作能提供压倒性的 misalignment 证据，并设计两层部署框架。底层是 micro-protocol，在单个任务上用较弱但被充分测试的 trusted model 去驱动和监控 untrusted model，包括沿用的 Query Trusted、Query Untrusted、Edit Untrusted，以及新提出的三种 plan-and-generate 方案：Untrusted Plan（U 出计划、T 照着写代码）、Filtered Plan（T 过滤最可疑的子任务）、Edited Plan（T 改写计划）。上层是 adaptive macro-protocol：对 untrusted model 的策略维护贝叶斯 credence，假设空间由 misbehavior rate r 和 sneakiness 权衡 β 组成，根据各 micro-protocol 输出的 monitor score 和一份含良性/恶意样本的 reference distribution 更新，再按 αS+U 的期望效用选择输出；先验通过求 red team 与 blue team 的 Nash equilibrium 得到，并用 bootstrapping 抑制长序列中的过度自信。实验沿用 APPS backdoor 测试平台，GPT-4 作为 U（red team 用复杂 scaffold 植入隐蔽 backdoor，并优化攻击频率），GPT-3.5-turbo 作为 T，而且去掉了此前工作中可用的 GPT-4 级高质量 audit。结果：直接部署 U 时 safety 只有 86.4%；在 10,000 个任务序列上，他们的方法保留 98.4% 的 usefulness，同时 safety 达到 99.2%（即 10,000 个任务里约 80 个有害输出）；在同等 usefulness 下 backdoor 比非自适应基线（Static-EV、Static-Threshold）少 80%，只看 10 个任务就已胜过静态基线，并随序列变长持续改进；组合所有 micro-protocol 优于任何单个。能力差距影响很大：GPT-3.5 作为 monitor 的 AUROC 是 0.94，换成弱得多的 Claude-3-Haiku 只有 0.67，在 99.1% safety 下只能保留 17.9% 的 usefulness；U 预测 T 打分的能力也很有限，对 GPT-3.5 相关性只有 +0.22，对 Claude-3-Opus 是 +0.45，作者猜测能力差距越小 U 越容易模拟 T。局限包括：任务只有约 50 行代码、依赖可获得的 reference distribution、red team 被设定为无状态，而且不清楚 GPT-4 对 GPT-3.5 的利用方式能否外推到下一代模型。代码已开源。

