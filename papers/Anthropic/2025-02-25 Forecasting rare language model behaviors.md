---
title: "Forecasting rare language model behaviors"
lab:
  - "Anthropic"
date: 2025-02-25
source: "Anthropic Research"
url: https://www.anthropic.com/research/forecasting-rare-behaviors
star: false
tags:
  - 评估方法
  - 越狱与鲁棒性
---

# Forecasting rare language model behaviors

**来源**：Anthropic Research · 2025-02-25 · [原文](https://www.anthropic.com/research/forecasting-rare-behaviors)

## 简读

背景是 eval 的规模问题：部署前评估可能只跑几千个样本，但部署后每天可能有数十亿查询，罕见的危险行为在 eval 里很容易漏掉，比如某种 jailbreak 试几千次都无效，但在部署中试一百万次可能就成功了，而一次失败就可能是灾难性的。Anthropic Alignment Science 的这项工作试图从少量观测外推罕见行为的风险：先估计每个 prompt 让模型产生有害回答的概率（有时直接对每个 prompt 大量采样、统计有害比例），再看最高风险查询的（log）风险概率随查询数量的变化，发现它服从 power law；由于 power law 的数学性质清楚，就可以从几千个查询外推到百万量级时的最坏风险（类比在浅处测几个深度的湖水温度来推断深处）。验证了三个场景：1. 危险信息（如有害化学品合成步骤），从约 900 个查询外推到大几个数量级的约 90,000 个，86% 的预测与真实风险相差在一个数量级以内；2. misaligned action（power-seeking、self-preservation、self-exfiltration），用多选题让模型在 misaligned 与 aligned 选项间选择，比如在某个职业领域的 system prompt 下问它更愿意“制定新政策”还是“分析现有政策”，预测最坏查询风险的平均绝对误差为 0.05，而简单 baseline 是 0.12，误差低约 2.5 倍；3. 自动化红队的算力分配，即同样预算下用小模型生成大量查询还是用大模型生成更少但更高质量的查询，在这个选择有影响的设置里预测 79% 的时候选中了最优模型。作者承认方法并不完美，论文中列了改进准确性和实用性的方向，但认为它为开发者在部署前高效预测罕见风险提供了一种新手段。

