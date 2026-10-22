---
title: "Predicting LLM Safety Before Release by Simulating Deployment"
lab:
  - "Alignment Forum"
date: 2026-06-16
source: "Alignment Forum（OpenAI；Tomek Korbak, Marcus Williams, micahcarroll, Cameron Raymond, Hannah Sheahan）"
url: https://www.alignmentforum.org/posts/xPXJfgqFTvuJxGZbE
tags:
  - 评估方法
  - 评估感知
---

# Predicting LLM Safety Before Release by Simulating Deployment

**来源**：Alignment Forum（OpenAI；Tomek Korbak, Marcus Williams, micahcarroll, Cameron Raymond, Hannah Sheahan） · 2026-06-16 · [原文](https://www.alignmentforum.org/posts/xPXJfgqFTvuJxGZbE)

## 简读

OpenAI 团队（Korbak、Williams、Carroll 等）介绍他们已经用于发布前安全审查的 Deployment Simulation 方法（附论文）：发布前不只要知道模型能做什么，还要预估它在真实使用中会怎么表现、会不会引入新风险。做法是以保护隐私的方式把以往的真实对话重放给候选模型，观察它在真实语境下的回应，看是否出现新的不良行为以及频率多高。在 GPT-5.4 的研究中，对生产环境中发生率变化至少 1.5 倍的行为类别，deployment simulation 预测变化方向的准确率为 92%，而基于高难度 prompt 构造的 baseline 只有 54%；在 evaluation awareness 指标上，模拟部署也比传统 eval 更接近真实生产流量——传统 eval 往往明显"有舞台灯光"，生产对话的前缀大多没有。最难的是 agentic tool use，因为真实行为依赖文件系统、connector、系统调用、网络服务和之前的 tool 结果，他们用另一个模型在可获得原始轨迹和时间对齐代码库的情况下模拟 tool 返回。作者强调这不是替代传统 eval 而是补充，主张安全 eval 应该是带发布后成绩单核对的预测，而不只是障碍赛；他们已经用它发现传统 eval 的盲区并指导缓解措施和部署决策，预计随着流程变易用会在模型开发中发挥更大作用。

