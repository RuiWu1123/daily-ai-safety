---
title: "How to evaluate control measures for LLM agents? A trajectory from today to superintelligence"
lab:
  - "UK AISI"
date: 2025-05-07
source: "AISI Research"
url: https://www.aisi.gov.uk/research/how-to-evaluate-control-measures-for-llm-agents-a-trajectory-from-today-to-superintelligence
other_versions:
  - "https://www.aisi.gov.uk/blog/how-to-evaluate-control-measures-for-ai-agents"
star: false
tags:
  - 监控与控制
  - 策划与欺骗
---

# How to evaluate control measures for LLM agents? A trajectory from today to superintelligence

**来源**：AISI Research · 2025-05-07 · [原文](https://www.aisi.gov.uk/research/how-to-evaluate-control-measures-for-llm-agents-a-trajectory-from-today-to-superintelligence)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/how-to-evaluate-control-measures-for-ai-agents)

## 简读

背景是 LLM agent 越来越能自主造成伤害，而且可能 scheming，也就是先隐藏意图、等机会再行动。AI control 走的是保守路线：先假设模型可能在 scheming，再用 monitor、人类审批、限制权限、随时可终止部署等 control measure 去约束它，并用 control evaluation 来验证这些措施够不够。control evaluation 被设计成红蓝对抗，红队造出试图绕过控制的恶意模型，红队的胜率可以作为部署风险的上界。这篇由 UK AISI、Apollo、Redwood 合写（Korbak、Balesni、Shlegeris、Irving），AISI 博客另有一篇配套介绍。核心观点是以往的 control 工作默认模型能执行人类已知的最优攻击，这对近期模型过于保守；应该根据 capability eval 测出的实际能力短板，相应限制红队的 affordance，让红队"恰好和失调模型一样强，但不强太多"。这样 control evaluation 和 control measure 都会更便宜，开发者更愿意采用，也不会把有用的模型无谓地挡在部署门外。作者还指出实验室现在的人类审批、红队测试其实就是 AI control 的 minimum viable product，该当作起点往上扩展。框架有七个组件：能力画像（autonomy、opaque reasoning、consistency、situational awareness）、部署场景（人类监督程度、规模、风险高低，本文聚焦实验室内部部署）、针对威胁模型的具体能力、威胁模型、control evaluation 规则、control measure、safety case（形如"三个月部署内坏结果概率不超过 x%"的低保证度论证）。然后用五个虚构模型 M1–M5 演示五个 AI Control Level：ACL-1 只会 in-context scheming，红队只能写 system prompt 和投毒检索文档、不能微调，措施是安全沙箱、人类审批和 CoT monitoring，因为模型做不到低概率攻击，2000 个任务的代理部署结果可以直接外推；ACL-2 能用 RL 中涌现的 code-switching 故意混淆 CoT，红队可以微调模型使用自选的隐写编码，措施改成 untrusted monitoring（用同一模型的另一个实例来监控）加上 AI 先筛动作、只把可疑动作交给人；ACL-3 能形成存在权重里的 out-of-context 目标，可做 Schelling 协调和串通，红队可以把子目标和通用策略微调进模型，蓝队则不许微调红队模型，只能做 honeypot 式的对齐评估；ACL-4 具备可靠的 latent reasoning，能发动只在 0.01% 输入上出手的低概率攻击，CoT monitoring 失效，只能监控动作，红队可以替模型做推理再训它直接执行，新增 input collusion 和 Blitzkrieg 两类攻击；ACL-5 是超级智能，作者论证 control safety case 在这一级做不出来：人类红队的能力在人类水平附近封顶，借 AI 辅助又可能被辅助模型 sandbagging，监控也从"monitor 交给人判断"变成"人只能听 monitor 的"，等于退化成 scalable oversight 问题。此时只能尽力而为，比如限制 agent 的权限、只让它输出可读的英文计划交给 M4 执行、拆分任务阻断实例之间的信息流、给可信 monitor 更多算力。作者强调这不是不可能性证明，突破要么来自 capability elicitation，要么来自对齐或白盒方法带来的 alignment safety case。博客最后列出待做的研究：把能力映射到 eval 规则、更真实的 control eval（AISI 的 ControlArena）和 protocol 设计，并提到 GDM 的 Frontier Safety Framework 已承诺检测会削弱人类控制的 instrumental reasoning 能力。

