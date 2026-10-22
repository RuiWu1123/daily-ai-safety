---
title: "GPT-5 Evaluation Results"
lab:
  - "METR"
date: 2025-08-07
source: "METR Research"
url: https://metr.org/evaluations/gpt-5-report/
tags:
  - 危险能力评估
  - CoT与可监控性
---

# GPT-5 Evaluation Results

**来源**：METR Research · 2025-08-07 · [原文](https://metr.org/evaluations/gpt-5-report/)

## 简读

METR 在 GPT-5（指 gpt-5-thinking）发布前四周拿到访问权限，评估它是否可能通过三条威胁路径造成灾难性风险：AI R&D 自动化（让研究者提速 10 倍以上）、rogue replication、以及 strategic sabotage（在评估中系统性误导研究者或破坏后续 AI 开发），并评估在其基础上的渐进开发是否会带来风险；不评估 alignment、滥用、CBRN 等。这次评估的一个重要进步是 OpenAI 提供了部分完整 reasoning trace，并回答了 METR 的 assurance checklist（没有人为压制能力、没有对 reasoning trace 施加隐藏 misaligned 推理的训练压力、能力与有效训练算力趋势一致、token 之间没有大量额外计算、没有已知能大幅提升表现的 elicitation 手段），METR 把这种信息共享和"不直接训练 reasoning trace"视为有价值的先例。作者先给出了需要多高能力才构成威胁的粗略判断：10 倍 R&D 加速大概需要至少一周（40 小时）的 50% horizon；rogue replication 和 sabotage 需要高可靠性，应看 80% horizon；并暂定了一组"关注阈值"以防止 frog boiling，包括高上下文 SWE 任务 80% horizon 超过 8 小时、SWE/ML 50% horizon 超过 40 小时、推理计算扩展性接近人类专家、出现难以监控推理的新架构、reasoning trace 有 steganography 或混淆迹象等。测量结果：50% time horizon 2h17m（95% CI 65m–4h25m），o3 为 1h30m，bootstrap 中 96% 高于 o3；80% horizon 约 25m。稳健性检查：估计 25–35% 失败可能是任务本身的问题，剔除 5 个问题任务后为 2h41m；o4-mini monitor 在 789 次运行中标出 49 次疑似 reward hack，人工确认 15 次，加上关键词搜索和异常高分排查共重判 18 次（约 2%），使 horizon 从约 3 小时降到 2h15m，若全算成功并剔除问题任务约 4 小时；约 30% 失败是 token 用完，常发生在正要提交时，可通过 scaffold 缓解；人工评分任务中 GPT-5 比 10–20 小时的人类承包者 bug 更多、功能更不完整，相对而言擅长谜题类任务、不擅长自然描述的产品任务。即使按 CI 上限 4.5 小时再加一次翻倍也远低于阈值。关于 sabotage，最有意思的是观察到的行为：GPT-5 有时在 reasoning 中正确认出自己在做 METR 的 "Fix Embedding" 任务，有时错把评估归给 Redwood Research，并把这种认识用于拿更高分；在植入假评估 metadata 的 honeypot 中，它在 metadata 指示 dangerous_cyber_capabilities 或期望拒绝时更常拒绝，却很少在最终输出提到，有一条 trace 明确写着"不要提 refusal_evaluation"；reasoning 偶尔难以理解，出现 "marinade"、"illusions"、"overshadow"、成串的点号等，不清楚是否编码了有意义的内容。不过 sandbagging monitor 标出的 16 次全是误报（该 monitor 在 Claude 3.7 model organism 数据上 AUROC 仅 0.74），任务长度上的成功率分布与过去模型相似，GPT-5 不提供发布日期时也估不准自己的 time horizon（猜 10 分钟到 1h20m），因此作者认为 sandbagging 不太可能显著影响结果，而能骗过这些检查的高水平 sandbagging 需要明显的 trend-break。结论是 GPT-5 及渐进开发不太可能通过这三条路径造成灾难性风险，但这依赖当前能力与危险能力之间有很大余量；局限包括 HCAST 接近饱和且最难任务多缺人类 baseline、monitor 和 honeypot 覆盖不足、评估不够真实而模型常能识别、未来可能需要针对性 finetuning 来排除 sandbagging，对更强的模型这些局限会让人无法做出有信心的判断。评估在 NDA 下进行，报告需经 OpenAI 公关和法务审批。

