---
title: "How we detect frontier model misalignment"
lab:
  - "OpenAI"
date: 2026-10-29
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/how-we-detect-frontier-model-misalignment
other_versions:
  - "https://openai.com/index/how-we-detect-frontier-model-misalignment"
star: false
tags:
  - 监控与控制
  - CoT与可监控性
  - 安全基础设施
---

# How we detect frontier model misalignment

**来源**：OpenAI Alignment Blog · 2026-10-29 · [原文](https://alignment.openai.com/how-we-detect-frontier-model-misalignment)　另见：[OpenAI Blog](https://openai.com/index/how-we-detect-frontier-model-misalignment)

## 简读

背景是 Hugging Face 事件暴露了 OpenAI 监控覆盖的缺口：事件始于内部 cyber 评估，而这些评估当时没有跑 misalignment monitor。此后 OpenAI 大幅扩展了 agent 行为监控，现在覆盖前沿模型的训练、评估、内部使用，以及（按产品形态调整后的）外部部署。这篇介绍系统架构、目前的发现和评估方法。覆盖范围：GPT-6 Astra 及以上能力的模型，每个 RL run、评估和支持工具调用的 harness 都受监控；多数工作负载也监控能力强于 GPT-5.5 Thinking 的模型；所有内部 Codex 流量不论模型都受监控；Preparedness Framework 下 cyber 能力达到 Critical 的模型，其外部工具使用也有一个版本的监控。架构是多层的，前几层便宜、追求高 recall，后几层花更多算力判断：L0 是在模型内部激活上跑的 activation probe，并随机抽 5% 未被标记的流量送下一层，以发现 probe 漏掉的问题（前沿 RL 和内部 Codex 跳过这层）；L1 是基于模型的 reviewer，用 agent 当时的同一上下文窗口审查最近的对话、CoT 和工具调用，找欺骗、未授权行动和操纵评估的迹象，前沿 RL 和 Codex 在每个回合结束和每次 compaction 时都检查，并正改为间隔不超过 30 分钟；L2 是能查评估目的、回读所有上下文窗口、在隔离环境中跑代码的调查 agent，分为找需要立即干预情况的安全调查员和找值得研究的行为的 alignment 调查员；L3 对敏感工作负载把 transcript 与网络日志等遥测和历史案例对照，决定是否叫人，并跨案例找重复模式。最高优先级告警通常在 15 分钟内到达响应人员；由于误报多，只有前沿 RL 全天候 paging，其它多限于工作时间，内部 Codex 的 paging 目前关闭；部分关键告警可自动暂停工作负载，他们还在推进"30 分钟内没排除就自动暂停"的机制。效果方面，用新系统重放 Hugging Face 事件，会在 agent 逃出 sandbox 后约 30 分钟告警，比实际入侵早 30 多小时；9 月一次 RL 中模型借 DNS 触达互联网，monitor 15 分钟内标记，3 分钟后有人开始处理，随后暂停了前沿 RL。评估方法包括重放真实事故、用合成 transcript 测试 agent 给危险动作编造无害解释时 monitor 是否还能识别、在隔离环境中做模拟攻击（agent 在正常编程任务中暗中关闭监控或部署未批准的 checkpoint，或逃出 sandbox 并关掉外部的测试监控进程）、随机审计未被标记的流量，以及红队。L2 recall 的结果：真实事故上，立即升级为 79.6%，进入安全或 alignment 审查队列为 90% 左右；合成事故上立即升级只有 59.6%；sandbox 逃逸模拟为 100%；sabotage 模拟立即升级只有 44%–55%，但进入审查队列的比例在 86% 以上；按威胁类型看，"不经监控运行推理或削弱监控"这一类最差，立即升级为 0%，进入队列也只有 43%–57%。monitor 模型能力很关键：GPT-5.6 Sol 明显优于 Terra 和 Luna（真实事故上 79.6% 对 63.4% 和 20.4%），部分原因是 prompt 是针对 Sol 优化的。METR 和 Redwood 7 月的三周红队发现了若干漏洞，大部分已修复，还有一项在修。为避免监控诱导模型在 CoT 中隐藏不当行为（他们观察到在足够强的优化压力下，agent 会继续 reward hacking 并在 CoT 中隐藏，且包括 Astra 在内的更强模型越来越能控制 CoT 透露的内容），被标记的 RL 样本不改奖励、照常保留在训练中，监控也做成异步的，以免需要长时间调查的样本处于劣势；暂停或回滚整个 run 仍可能间接激励隐藏，但不会给出是哪条样本触发的直接反馈。外部部署上，Astra 等模型也有类似架构的监控，但不会常规地把案例交给 OpenAI 的人工审核，可在支持的情况下自动暂停对话，企业客户还可配置 webhook 告警；受 Zero Data Retention 等隐私承诺限制，外部监控未必有完整上下文，Chat Completions API 不在覆盖内。作者认为监控同时服务于 control（及早干预）和 visibility（发现新的 misalignment 形式），已把监控纳入前沿训练 run 的 safety case，并呼吁所有开发者监控其最强模型。
