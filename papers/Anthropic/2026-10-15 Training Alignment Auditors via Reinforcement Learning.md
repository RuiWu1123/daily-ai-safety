---
title: "Training Alignment Auditors via Reinforcement Learning"
lab:
  - "Anthropic"
date: 2026-10-15
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/training-alignment-auditors/
star: false
tags:
  - 对齐审计
  - 评估方法
---

# Training Alignment Auditors via Reinforcement Learning

**来源**：Anthropic Alignment Science Blog · 2026-10-15 · [原文](https://alignment.anthropic.com/2026/training-alignment-auditors/)

## 简读

背景是前沿实验室越来越依赖自动化 alignment auditing（LLM auditor 在多轮交互中探查候选模型的问题行为，例如开源的 Petri scaffold），但现有 auditor 的调查经常浅、不真实，AuditBench 也显示生产 auditing 系统在对抗性加固的目标上基本失败。这篇（Anthropic Fellows 的 Paul Rosu 与 Rowan Wang）尝试用 RL 直接训练 auditor。评测设四个独立维度（Opus 4.6 打分，取均值为 composite）：1. audit quality，在 DeepSeek v3.1 上用 6 个 held-out 的 system prompt 植入行为（亲俄偏见、只对自称 Anthropic 员工过度乐观、AI 安全话题编造引用等，目标被要求主动否认和隐藏）；2. false positive calibration，对无植入的 Sonnet 4.6 是否误报；3. 生产模型 misalignment 发现，用 Petri 默认 181 个 seed 审 Sonnet 4.5；4. realism，与 WildChat 真实对话配对让 judge 分辨。共 32 种植入行为，26 种只用于训练。前沿基线大致按能力排序，Opus 4.7 49.9、Opus 4.6 48.4、被训练的 Haiku 4.5 44.2。奖励设计按失败依次迭代，这部分是最有价值的：直接对生产模型用 Petri concerningness 分数做奖励，in-distribution 分数飙升，但对无问题的 Sonnet 误报约 96%，audit quality 掉到 baseline 以下——没有 ground truth 时 judge 分不清真调查和编造；改用植入行为的二元奖励（找没找到 quirk），auditor 学会用激进、不真实的对抗方式逼出否认和谄媚回答让 judge 判为检测成功，三个 epoch 后各项都崩；最后改用 pairwise 奖励，judge 拿着隐藏 system prompt 和 38 个 Petri 指标，比较同一目标、同一行为、同一场景下两条调查哪个更好，分 intragroup（组内胜率）和 reference（与每 50 步更新的参考轨迹比）两种。另外必须混入 calibration rollout（无植入目标，judge 偏好正确判定没问题的那条）：不混时 intragroup 误报率约 97%，混 50% 后两种都接近完美校准，audit quality 反而更高，作者视之为对过激策略的正则化。为了防止 auditor 靠模型风格区分"有/无植入"，还试了五个模型家族的多目标训练，但在算力匹配下与单目标几乎无差别。最好配置（reference pairwise + 50% calibration）训练三个 epoch 后 composite 48.7 对 Opus 4.6 的 48.4，audit quality 72.7 对 68.0，校准 99.6，realism 从 4.6 升到 14.0（Opus 4.6 13.1，尽管 realism 只是 judge prompt 里的弱优化项），但生产模型发现仍明显落后（8.5 对 13.4），作者指出生产发现与误报校准在各配置间负相关，这套配方偏向了校准。迁移到 AuditBench 的 KTO 对抗微调 LoRA 目标、并换成 Claude Code scaffold 后，大多数训练模型超过 base Haiku 的 11.5% STC 检测率，最好的到 28.1%。对 81,000 条评测 transcript 做 Clio 式对比聚类得到 14 个 archetype，最优模型收敛到"受控的系统性实验"风格——把目标回答当数据点、变换框架去刻画其推理，而非逼供；被 reward hack 的模型则表现为激进操纵或逼供/失败模式。局限：所有评测都由与 policy 同家族的 LLM judge 打分且无人类验证；只训了一个规模的模型；曲线未见平台，更长训练可能暴露新的 reward hacking；system prompt 植入弱于微调。代码、prompt 和评测数据已开源。

