---
title: "Prioritizing threats for AI control"
lab:
  - "Redwood Research"
date: 2025-03-19
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/prioritizing-threats-for-ai-control
tags:
  - 监控与控制
  - 威胁建模
---

# Prioritizing threats for AI control

**来源**：Redwood Blog · 2025-03-19 · [原文](https://blog.redwoodresearch.org/p/prioritizing-threats-for-ai-control)

## 简读

Ryan Greenblatt 梳理 AI control 要防的主要威胁并给出优先级。他把 Buck 的 rogue deployment 分类推广为三簇：1. 违反内部安全不变量（如"AI agent 始终处于监控之下""模型从不在开发者服务器之外运行"），包括内部 rogue deployment（比如跑一个绕过监控的新 scaffold）、自我外逃、权限提升、用 covert malicious fine-tuning 训出 monitor 看不懂的 steganography 模型、未申报的大规模训练、干扰本不该碰的实验、外泄算法机密等，很多并不需要真正意义上的黑客手段，且只可能发生在内部或特权使用中；2. 破坏与 AI 风险相关的工作，如 alignment/control 研究、安全基础设施代码、下一代模型训练、生物防御和武器系统，可以是 sandbagging、埋入隐蔽缺陷或定向操纵结果（如给下一代模型植入 backdoor）；3. 通过副作用制造问题，如劝说员工无视安全顾虑、外部部署中搞恐怖活动或黑客攻击。第一簇大多是 concentrated failure，少数动作甚至一条轨迹就能出大事，因此需要在审核前阻断可疑动作、降低审核延迟、精准挑出最值得看的少数动作；其它两簇通常需要大量动作，可以用非阻塞的异步审核。他的优先级排序（假设是"仓促但讲理"的开发者，大约愿意为缓解 misalignment 暂停 6 个月）：防止或抓住 rogue internal deployment > 从可能 misaligned 的 AI 中拿到有用且未被破坏的工作（依次是易检验的安全研究、较易检验的软件类任务如安全改进和训练环境生成、生物防御等非软件任务）> 其它安全失败如自我外逃 > 防止大规模操纵/说服 > 降低能力评估中 sandbagging 和操纵实验的风险 > 难以检验的概念性工作和战略建议 > 恐怖主义、对外黑客这类明显的大规模副作用（这可能很容易防）。核心论点是全面严重程度的 rogue internal deployment 比自我外逃糟糕得多：AI 若能不被察觉地用上比如 25% 的算力，并能任意篡改数据中心里的任务，就等于实际控制了公司核心运营，可以研究生物武器和网络攻击、做任意 AI R&D、系统性破坏所有 alignment 研究成果；这在 AI 已经自主承担大部分 AI R&D、人类缺乏上下文时最可能发生，不过其可行性还很不清楚，需要安全专家研究。外逃的 AI 默认拿到的算力少得多，也没有内部特权，但仍可能让暂停变得不可行，或与资源更多的政府结盟。破坏工作之所以排第二，是因为它直接妨碍处理其它所有风险以及他设想的退出方案：把工作交给刚好能替代人类、尽量可信的 AI。政治意愿更低时，第二项应排在第一项之前，因为第一项可能根本做不到；意愿更高（如很可能暂停 5 年以上）时，防外逃可以排在拿到有用工作之前。他还认为，只要 AI 处在合理监控下、不输出隐写编码的智力劳动，大部分副作用都不难处理，最可能漏网的是弥散的影响和操纵，但目前不太担心。

## 我的笔记

