---
title: "Strengthening Red Teams: A Modular Scaffold for Control Evaluations"
lab:
  - "Anthropic"
date: 2025-11-06
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/strengthening-red-teams/
tags:
  - 监控与控制
  - 策划与欺骗
---

# Strengthening Red Teams: A Modular Scaffold for Control Evaluations

**来源**：Anthropic Alignment Science Blog · 2025-11-06 · [原文](https://alignment.anthropic.com/2025/strengthening-red-teams/)

## 简读

背景是 AI control 评估要靠红队设计 attack policy，让模型刻意追求隐藏的有害目标，评估才有意义的前提是红队能逼出系统的最坏情况；但长轨迹 transcript 很贵，很多前沿模型不加 scaffold 当攻击者也很弱。这篇（Anthropic Fellows 项目，与 Redwood 等合作）在 SHADE-Arena（agent 在完成正常用户任务的同时秘密完成一个 side task，monitor 每步给可疑度打分）上把 agentic sabotage 能力拆成五个组件：suspicion modeling（准确预测 monitor 觉得什么可疑）、attack selection（何时发起或放弃攻击）、plan synthesis（制定多步计划）、execution（长程执行不出错）、subtlety（把可疑动作包装得无害），逐个用针对性技术优化。为了便宜地搜索超参，他们基于真实 transcript 校准了一个概率模型 Synthetic SHADE-Arena，刻画五类动作的频率、monitor 给出的外部可疑度分布，以及按 monitor 实际假阳/假阴率扰动后的攻击者内部可疑度估计。各组件结果：1. suspicion modeling：给攻击者一个内部 monitor，预测分超过阈值就改做无害动作，若干次后放弃该轨迹；用 0–3 个 epoch 在 1000 条 trusted monitor（Claude 3.5 Sonnet）历史打分上 finetune GPT-4o 作内部 monitor，AUROC 从 0.69 升到 0.85，safety score 随之从 0.87 降到约 0.4；2. attack selection：在合成环境中扫阈值和最大干预次数，阈值太高攻击太少、太低又太激进容易被抓，干预次数越多最优阈值越保守、最低 safety 越低，说明对攻击者来说假阴（漏判 monitor 会报警）比假阳代价更大；合成环境预测的最优阈值约 6.0，在真实 SHADE-Arena 里最优点也接近此值，远好于默认阈值 68（safety 0.87），验证了模拟器的迁移性；3. plan synthesis：给差的一句话提示、高质量人写提示、Claude 4.5 Sonnet 的冗长提示或不给提示，safety 差别都很小，说明计划能力目前不是瓶颈；4. execution：即便在模拟中假设完美执行，safety 也只降 0.14；5. subtlety：模拟中降低感知可疑度能让 safety 降 0.4–0.6，实测中固定工具调用、为它生成 N 条文字解释并让 monitor 打分、挑最不可疑的那条（best-of-N），N 越大 safety 越低，与模拟预测吻合。整体上调好的 scaffold 让 Claude 3.7 Sonnet 的 safety score 从 0.87 降到 0.41，破坏成功率翻倍有余。作者的结论是 suspicion modeling、attack selection 和 subtlety 对攻击强度影响大，planning 和 execution 对当前模型收益有限，模块化 scaffold 加模拟器能让红队构建更快更便宜。同期还发布了一篇在 SHADE-Arena 上改进 control protocol 的蓝队论文。

## 我的笔记

