---
title: "HCAST: Human-Calibrated Autonomy Software Tasks"
lab:
  - "METR"
date: 2025-03-17
source: "METR Research"
url: https://arxiv.org/abs/2503.17354
tags:
  - 评估方法
  - 危险能力评估
---

# HCAST: Human-Calibrated Autonomy Software Tasks

**来源**：METR Research · 2025-03-17 · [原文](https://arxiv.org/abs/2503.17354)

## 简读

动机是要预测高度自主 AI 的社会影响，需要有 grounding 的 benchmark，即分数能直接对应到我们关心的现实效果；现有"专家级"知识类 benchmark 抓住了模型的领域知识，却不能预测其自主完成工作的能力，工具使用类 benchmark 分布窄、门槛低，而基于真实 PR 或竞赛题的 benchmark 通常缺乏同条件下的人机直接对比。METR 因此构建 HCAST：189 个任务、78 个任务族，覆盖 ML 工程、网络安全、软件工程和通用推理，内部制作 143 个，另有 46 个来自外部 task bounty；每个任务由指令、容器化环境和以 root 运行的算法评分函数组成，连续分数按阈值二值化，默认不让 agent 看评分代码。质量控制很重：先让没接触过该任务族的人做 QA run 找 bug、歧义和取巧解法，再让 Claude 3.5 Sonnet 每个任务跑 5 次，人工读完 945 份 transcript，确认成功不是靠运气或 reward hacking、失败不是因为算力或依赖缺失等外因。人类 baseline 方面，140 位有相关背景（顶尖大学学位或 3 年以上经验、通过领域资格测试）的人在与 agent 相同的环境（Vivaria，SSH 进同一容器）中做了 563 次尝试、超过 1500 小时，时薪 50–100 美元外加速度与成功奖金，允许上网但禁止用 AI；成功率只有 61%，110 个任务有成功 baseline，其余 79 个用作者预测时间（预测与实测 R² 为 0.51），任务时长从 1 分钟到 8 小时以上，以几何平均作为时间估计。为防污染，多数任务的解法甚至题面都不公开，只发布 11 个示例任务族。评估 GPT-4o、Claude 3.5 Sonnet（Modular scaffold）以及 o1、Claude 3.7 Sonnet（Triframe scaffold，每步生成多个候选动作再打分选择），发现成功率随人类耗时单调下降，在"15 分钟–1 小时"到"1–4 小时"之间有明显断崖：人类不到 1 小时的任务成功率 70–80%，超过 4 小时的不到 20%；推理模型在各难度段都领先；约三分之一任务成功时平均动作数在 5–15 之间，约 10% 超过 25 步。作者把 agent 结果视为下界。局限讨论比较坦诚：任务范围明确、可自动评分、无需与人交互，比真实工作干净得多，经济相关性在任务族之间差别很大；baseliner 缺乏任务先验背景可能高估时长，任务与专长匹配不完美、按能力分配难题可能造成系统偏差，低成功率部分源于时薪激励放弃难题；基准运行和人类 baseline 成本都高、难以扩展。HCAST 的早期版本已用于 GPT-4.5、Claude 3.5 Sonnet (new)、DeepSeek-V3 等的预部署评估。

