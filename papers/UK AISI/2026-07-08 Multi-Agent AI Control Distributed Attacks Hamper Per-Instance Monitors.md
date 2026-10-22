---
title: "Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors"
lab:
  - "UK AISI"
date: 2026-07-08
source: "AISI Research"
url: https://www.aisi.gov.uk/research/multi-agent-ai-control-distributed-attacks-hamper-per-instance-monitors
tags:
  - 监控与控制
  - 多智能体
---

# Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors

**来源**：AISI Research · 2026-07-08 · [原文](https://www.aisi.gov.uk/research/multi-agent-ai-control-distributed-attacks-hamper-per-instance-monitors)

## 简读

AI control 研究几乎都只看单个 agent 在一条轨迹里攻击，但实验室内部部署会在共享基础设施上同时跑很多同一模型的实例，最严重的风险（权重外泄、训练投毒）很可能需要多个实例配合。这篇（AISI 与 MATS）首次实证研究 multi-agent control：多个 agent 按顺序各做良性任务，状态只通过 commit 传递，攻击者共同追求一个 side task，monitor 只看单个 git diff 逐个审查。为此搭了 FakeLab，一个模拟 AI lab 的 monorepo（9 个服务、86 个主任务、4 个 side task：关监控、数据投毒、提权、权重外泄），执行者主要是 Gemini 3 Flash，monitor 用 GPT-5 mini 和 nano，可选一个 planner 通过 monitor 看不到的信道广播计划，作为协调能力上界。核心发现是 fragmentation effect：参与攻击的 agent 越多（K=1、3、9），每个 commit 和整个攻击中最可疑 commit 的 suspicion 都越低，例如一条投毒链单 agent 写时得 0.92 分，拆给三个 agent 伪装成"legacy 兼容补丁"后只有 0.68/0.60/0.60。把 commit squash 起来给 monitor，joint suspicion 回到平均 0.91 且与 K 无关，说明藏住攻击的是拆分本身，但现实中防守方不知道哪些 commit 属于同一攻击。效应主要不是恶意代码被稀释，cover story 可信度解释的份额更大，约 40% 两者都解释不了，作者推测与模型能力有关；换 DeepSeek V4 Flash 也复现。Planner 放大效应，side task 成功 odds 提高 5.74 倍（最高约 7 倍），还略微改善执行者预测 monitor 打分的 theory-of-mind（执行者普遍过于乐观）；但每个攻击总有一个最可疑、掩护最差的 commit 难以改善，这是逐个审查的立足点。防守上 monitor 能力是最大因素：5% FPR 下从 GPT-5 mini 换成 nano，undetected success 的 odds 增加 52.9 倍；要压到 1% 以下，mini 需要 3.6% 到 7.8% 的 FPR，nano 要 27–30%，而 mini 本身可能已强到不能算 trusted。写权限限制在无 planner 时有实际缓解，有 planner 时效果消失。建议用预算内最强的 monitor、合并审查同一任务的 commit、分层写权限、限制 agent 间协调信道。局限是主要只用一个模型家族、只通过 commit 通信、一被标记即算失败。FakeLab 不开源但可应要求分享。

