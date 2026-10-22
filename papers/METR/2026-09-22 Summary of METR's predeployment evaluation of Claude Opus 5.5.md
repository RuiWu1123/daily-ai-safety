---
title: "Summary of METR's predeployment evaluation of Claude Opus 5.5"
lab:
  - "METR"
date: 2026-09-22
source: "METR Blog"
url: https://metr.org/blog/2026-09-22-claude-opus-5-5/
tags:
  - 危险能力评估
---

# Summary of METR's predeployment evaluation of Claude Opus 5.5

**来源**：METR Blog · 2026-09-22 · [原文](https://metr.org/blog/2026-09-22-claude-opus-5-5/)

## 简读

METR 对 Claude Opus 5.5 的部署前评估摘要（收录于 Opus 5.5 system card，属于无偿的 AI R&D 评估协议，METR 起草后 Anthropic 有权审阅修改，最终文本经 METR 签字认可），只关注 AI R&D 能力，不验证是否符合 Anthropic 政策中的具体阈值，也不评估 alignment。要回答两个问题：(A) 使用 Opus 5.5 是否会让 Anthropic 的 AI R&D 大幅加速；(B) Opus 5.5 的开发过程本身是否已被 AI 大幅加速。证据来源包括 10 个工作日的 API 能力测试，用了五个任务（受限版 NanoGPT Speedrun、概念论证数据集 LMCA、训练模型复现某软件行为的 Train a Program、通过非视觉 API 写程序玩游戏的 Gaming Bot、开放式研究写报告的 Sunlight），此前模型的趋势数据，Anthropic 的问卷回答和一次研究员访谈，以及另一个拥有更高权限的 METR 团队关于 Anthropic 内部 AI R&D 加速的高度初步的报告——这个团队只共享了结论、没共享证据，METR 将其视为更整体性评估流程的试运行。结论：(A) Opus 5.5 带来的加速略高于 Fable 5.1，但不太可能完全自动化 AI R&D，它在可验证任务（Budget NanoGPT、Gaming Bot）和难验证任务（LMCA、Sunlight）上都比 Fable 5.1 有所提升，但属于增量改进而非跳变，Anthropic 也称它延续了 Mythos 以来 ECI 的趋势，同时它仍有专家在困难长程任务和开放推理中不太会犯的定性弱点；作者认为完全自动化需要 foresight、预测、自建反馈回路等"judgement/taste"类能力的大幅提升，而现有证据看不出这方面有大进步；作者也提醒，频繁的增量改进本身与总体快速进展并不矛盾，现有数据也分辨不出提升速率是匀速、加速还是减速。(B) 开发过程至少在一定程度上被 AI 加速，但不太可能是剧烈加速：那份初步报告给出的估计是"AI 带来约 1.5 倍的整体能力加速（一年做出 1.5 年的进展），约 30% 概率达到 2 倍"，不过没说明对应哪个时间段。此外还用了一个暂不能披露的信息来源来理解 Anthropic 的 AI R&D，与这个具体模型无关。

