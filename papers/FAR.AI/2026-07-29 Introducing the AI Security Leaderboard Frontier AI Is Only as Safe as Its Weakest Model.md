---
title: "Introducing the AI Security Leaderboard: Frontier AI Is Only as Safe as Its Weakest Model"
lab:
  - "FAR.AI"
date: 2026-07-29
source: "FAR.AI Blog"
url: https://www.far.ai/blog/ai-security-leaderboard
star: false
tags:
  - 越狱与鲁棒性
  - 评估方法
---

# Introducing the AI Security Leaderboard: Frontier AI Is Only as Safe as Its Weakest Model

**来源**：FAR.AI Blog · 2026-07-29 · [原文](https://www.far.ai/blog/ai-security-leaderboard)

## 简读

FAR.AI 发布 AI Security Leaderboard（leaderboard.far.ai）和配套的 Minimal Standard for Safeguards，把前沿模型 safeguards 的强度从 lab 自述变成独立、可比较的基准。动机是：攻击者被一个模型拒绝后会换别的模型试，整个生态的安全取决于可触达的最弱前沿模型；而各 lab 通常只拿新模型和自家前代比，无法回答是否达到共同标准。方法上他们把 jailbreak 拆成基本构件，做了一个自动重组构件的工具包，跑了几十万条 prompt，覆盖 CBRN、爆炸物和 cyber 等领域；把在某领域超过四分之三有害请求上都成功的可复用攻击定义为 universal jailbreak，用低投入攻击者借助该工具包找到一个 universal jailbreak 的估算美元成本作为鲁棒性指标。结果在相同条件下测的四个模型差距超过百倍：Claude Fable 5 和 GPT-5.6 Sol 在测试范围内没找到任何 universal jailbreak，估计成本高于 $14,000；Gemini 3.1 Pro 和 Grok 4.5 都不到 $300 就被攻破，后者 $58 就能在所有测试领域拿到有害信息，cyber 领域仅需 $24，其中一些有效攻击的构件来自公开论坛和代码库；对两个弱模型找到了数百个可靠 jailbreak。作者强调这些数字偏乐观，有真正 jailbreak 专长的攻击者能让某些模型的 universal jailbreak 数量多一个数量级。核心论点是"都可修"：发现的每个弱点都属于已知攻击类别，对应的防御已公开描述并在其他前沿部署中运行，Minimal Standard 正是完全由同行已部署的防御构成的底线，达标不代表安全，但不达标说明本可通过合理工程投入避免；对政府和标准机构，它可用作公共采购要求、聚焦有限测试预算、国际协调的参照点。作者坦承的局限：只测了有代表性的可触达攻击并刻意保留了一部分，美元数字衡量的是找到攻击的难度而非市场价格，v1.0 只定义了一组常见 jailbreak 技术及其组合方法，之后会随新模型和攻防演进持续更新。

