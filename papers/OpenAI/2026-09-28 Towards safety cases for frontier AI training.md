---
title: "Towards safety cases for frontier AI training"
lab:
  - "OpenAI"
date: 2026-09-28
source: "OpenAI Blog"
url: https://openai.com/index/towards-safety-cases-for-frontier-ai-training/
tags:
  - 威胁建模
  - 安全基础设施
  - 奖励作弊
---

# Towards safety cases for frontier AI training

**来源**：OpenAI Blog · 2026-09-28 · [原文](https://openai.com/index/towards-safety-cases-for-frontier-ai-training/)

## 简读

OpenAI 提出，在继续任何 frontier RL 训练之前应该要求有结构化的安全文档，理想上达到其它安全关键行业那种 "safety case" 的水准，即全面、结构化、基于证据的风险论证；他们承认 AI 每一级能力都有涌现复杂性，很难做到航空或核电那样严格，所以把它当作努力方向，并正在制定框架。文中给出的初步准则只针对训练阶段（内外部部署需要考虑更多对齐属性），分三部分：1. 技术保障，分 alignment、containment、monitoring 三层。alignment 包括用 agent 自动审查和人工审查 RL 环境以修掉可被 exploit 的任务、调 grader 惩罚 reward hacking、用分类器检查之前实验的轨迹确认 grader 正常；对齐度量包括训练中跑离线 alignment eval、在历史事故上回测 eval 以防 overfit、开启 eval awareness 和 metagaming monitor 并设阻断阈值、做 worst-case 压力测试确保至少一个 eval 能抓到，以及不让自动 grader 看到 CoT。containment 包括多层基础设施安全、用 frontier checkpoint 做 containment red-teaming（包括模型训练中能接触的服务如 internet cache）、限制样本间高带宽通信并关闭易被发现的侧信道、对所有 RL 训练、评测和内部部署的 transcript 做不可变存储。monitoring 包括用 monitorability 和 monitor evasion eval 设明确阈值、监控在历史事故 held-out eval 上要有高 recall、为新 run 持续更新代表新风险的 eval、有 SLA 的快速响应（白天呼叫 on-call，夜间未确认的告警自动暂停 run）。2. 运营准则：由其它团队成员写 dissent（pre-mortem）挑漏洞；研究负责人、安全负责人、首席科学家等高层各自有否决权；负责训练的高层对 safety case 和事故响应担责并计入绩效；有暂停所有相关 run 的 runbook 和 SLA；对 Safety and Security Committee 等内部监督机构透明；给审计方足够访问权；明确的 misalignment 严重度分级和可呼叫到 CEO 的 on-call；技术上让不合规的 run 难以启动，监控和自动暂停要 fail closed，训练或部署内部无法关闭 monitor；能追溯 misaligned 模型在训练流程中的所有下游用途以便回滚；尽量完整列出未覆盖的残余风险以支持知情的风险接受。3. 严重 misalignment 事故调查：内部定期（如每日）更新进展并为相关员工提供获取原始 transcript 的通道；通过定向消融或重采样找训练动态上的根因；做运营和文化层面的 postmortem；在不直接对事故数据 hill-climb 的前提下开发能发现该倾向的测试方法，并把事故衍生的 eval 当回归测试；调查结束后公开结果，尽快通知受影响的第三方。作者说这些建议正在 OpenAI 内部落地，并预期会持续演化。

