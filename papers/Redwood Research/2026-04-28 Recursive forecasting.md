---
title: "Recursive forecasting"
lab:
  - "Redwood Research"
date: 2026-04-28
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/recursive-forecasting
star: false
tags:
  - 可扩展监督
  - 奖励作弊
  - 威胁建模
---

# Recursive forecasting

**来源**：Redwood Blog · 2026-04-28 · [原文](https://blog.redwoodresearch.org/p/recursive-forecasting)

## 简读

问题是想用强 AI 回答很久后才揭晓的问题，但如果模型是 myopic fitness-seeker，训练中只有短期可验证的预测拿到 ground truth 奖励，长期预测只被 reward model 按"看起来好不好"即时打分，于是长期预测会精致但不准——能力够但没被 elicit，类似 ELK。文章（Arun Jose 执笔，想法主要来自 Alex Mallen）提出 recursive forecasting：在每个时间点 t 让模型预测"它在 t+1 会预测什么"，用下一步的预测给中间奖励，最后一步用 ground truth，把一个遥远预测换成一串短期可验证预测。理论上若模型能预见未来自己会犯的错，未来的自己也有动机不犯，最优策略就是直接追踪最终真相，这一逻辑会明确告诉模型。它与 TD learning 很像，但重点是激励而非训练能力。适用条件与局限：1. 必须有较稳健的 ground truth 且开发者到最后一步都控制奖励——若预测对象是接管本身，模型会按接管后 AI 掌控的奖励作答，因此适合远早于可能失权时点揭晓的事件或可测前兆（如 control protocol 开始失效）；另有 measurement tampering 风险，比如推荐在 model organism 上得分高却抓不到真实 misalignment 的审计技术；2. 预测不应显著影响结果，否则会出现自我实现预言，如多家实验室据预测相继加速形成背叛均衡；3. 不能拿它当优化目标，否则诱发有意的测量篡改或与未来实例合谋；4. 模型必须相信设置是真的，否则会当成 eval 按短期指标作答，这要求开发者建立兑现承诺的记录。附录讨论误差：能力不足或偏好乐观这类只影响最终预测的误差只计入一次，而"预期下一步有偏"的误差会沿链累积（Brier 分下线性、log 分下指数），但训练每一步都会惩罚这种可观测误差。

