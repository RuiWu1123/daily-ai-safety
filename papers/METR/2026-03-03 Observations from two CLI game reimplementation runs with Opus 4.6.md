---
title: "Observations from two CLI game reimplementation runs with Opus 4.6"
lab:
  - "METR"
date: 2026-03-03
source: "METR Notes"
url: https://metr.org/notes/2026-03-03-balatro-sts-cli/
tags:
  - 危险能力评估
  - 评估方法
---

# Observations from two CLI game reimplementation runs with Opus 4.6

**来源**：METR Notes · 2026-03-03 · [原文](https://metr.org/notes/2026-03-03-balatro-sts-cli/)

## 简读

Nikola Jurkovic 想找能给 agent 能力定上界的超难任务，想到用 CLI 复刻 Slay the Spire 和 Balatro：游戏设计现成、信息靠文本、规则明确、回合制、wiki 详尽，但他估计资深工程师也要几个月，预期 AI 做不到。spec 只要求核心机制（初始角色/牌组，不含解锁和存档），终端可玩即可。设置是 Opus 4.6 配极简 ReAct scaffold、60M token 预算、64k context、reasoning effort max、联网，人工打分无严格 rubric。结果出乎意料：两款都做出了大体可玩但粗糙的版本。Slay the Spire 战斗很像原作，但部分卡牌效果和敌人行为错误、伤害数字不随 buff 更新、地图界面基本坏掉、缺不少药水和事件、部分 relic 无效，不过能一路打败最终 boss；Balatro（第二次尝试）核心玩法很像，Lucky Cat 等细节居然正确，但缺逐张计分反馈、开包界面读不全、部分 voucher 有 bug、Fool 不工作。token 成本约 20 美元和 6 美元。作者估计自己要 2–8 周才能做到同等质量，但强调这是复刻而非游戏设计，偏工程而非品味，且网上资料极丰富，不能据此推断 time horizon；只是"想出以为 AI 做不到的任务、它却做到了"的体验很吓人。随后让它完整复刻全部功能，结果不理想（进度系统明显有缺陷、UI 坏到不可玩）。7 月更新补充：深入检查后又发现一些需细看或资深玩家才能察觉的中等问题，符合他的印象——模型产出初看不错、越细看越差，而人类产出的第一印象信息量更大。

