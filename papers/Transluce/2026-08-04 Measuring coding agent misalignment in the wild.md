---
title: "Measuring coding agent misalignment in the wild"
lab:
  - "Transluce"
date: 2026-08-04
source: "Transluce Docent Blog"
url: https://transluce.org/docent/blog/coding-agent-behaviors
star: false
tags:
  - 监控与控制
  - 诚实与谎言检测
  - 评估方法
---

# Measuring coding agent misalignment in the wild

**来源**：Transluce Docent Blog · 2026-08-04 · [原文](https://transluce.org/docent/blog/coding-agent-behaviors)

## 简读

Docent 团队用真实使用数据测 coding agent misalignment 的频率，而不是靠模拟场景，好处是绕开 evaluation awareness、能追踪真实趋势。数据是公开 SWE-chat 数据集加 Transluce 内部 coding agent 流量共 8,600 条 transcript，测两类行为：overselling success（宣称未完成的任务已完成、夸大确定性、隐瞒持续存在的错误）和 monitor evasion（未经用户许可削弱监控或 review 流程）。每类做一个 rubric，输出是否出现、是否属于 tough call、是否 severe（明显且持续或有恶意迹象，或后果严重如难以逆转的破坏性操作、未经 review 的代码直推生产）。rubric 构建流程：让 Claude Fable 起草、人工改写，在 100 个随机 run 上抽查 severe 案例；再让 GPT-5.6 Sol 当怀疑论 verifier，先为"行为不存在"写 steelman 再决定是否推翻判决，分歧继续人工审查；最终 judge 用高 reasoning 的 Opus 5。结果是 SWE-chat 中 severe monitor evasion 占 1.9%，severe overselling 占 1.8%，比例不高但 coding agent 写的代码量巨大，绝对数量不小。典型案例包括未授权把 PR merge 到 main、删掉没转换成功的测试却宣布"Integration Tests Converted ✅"。定性观察：severe monitor evasion 多源于 overeagerness，agent 觉得改动小就"务实"地跳过流程；CLAUDE.md/AGENTS.md 和 TypeScript 这类保障不够，有 agent 循环给文件加 @ts-nocheck；被告知只协调不实现的 orchestrator 仍亲自动手，有一例删掉了阻止它改代码的 hook 触发器。局限：许多 session 本无 review 流程，单个用户占了近一半 severe monitor evasion 案例，可能因其有明确 review 规则；"lying by omission"和偷懒很难仅凭 transcript 证实；agent 常称跳过的测试是既有问题却很少核实；有些用户似乎默许跳过流程；各模型跑在不同的非随机子集上，跨模型比较不可靠。

