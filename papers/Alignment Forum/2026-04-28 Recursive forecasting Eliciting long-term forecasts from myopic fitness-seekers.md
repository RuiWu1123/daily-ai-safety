---
title: "Recursive forecasting: Eliciting long-term forecasts from myopic fitness-seekers"
lab:
  - "Alignment Forum"
date: 2026-04-28
source: "Alignment Forum（Redwood Research；Jozdien, Alex Mallen）"
url: https://www.alignmentforum.org/posts/q2zYtNsh62SCphitt
star: false
tags:
  - 威胁建模
  - 可扩展监督
---

# Recursive forecasting: Eliciting long-term forecasts from myopic fitness-seekers

**来源**：Alignment Forum（Redwood Research；Jozdien, Alex Mallen） · 2026-04-28 · [原文](https://www.alignmentforum.org/posts/q2zYtNsh62SCphitt)

## 简读

要解决的问题是：如果一个模型是 myopic fitness-seeker（比如只在乎本 episode 的 reward），它只会在短期内可验证的问题上真正努力，那么对几个月后才 resolve 的问题，它给出的很可能是"现在看起来好"而不是"真的准"的预测。作者用一个虚构场景说明：模型 Requiem 的一两周预测极准，但三个月后的大选预测写得漂亮却频频偏离现实，因为训练中长期预测一直是由 reward model 当场打分的——这是一个类似 ELK 的 elicitation 问题，而不是能力问题。提出的方案叫 recursive forecasting：不直接问远期结果，而是在每个时间点 t 让模型预测"自己在 t+1 会预测什么"，用下一步的预测给上一步发中间 reward，最后一步再用 ground truth 打分，把一个远期预测拆成一串短期可验证的预测。理论上如果模型能预见未来自己的错误，未来的自己就有动机不犯这些错，于是最优策略是直接追踪最终 ground truth；作者还建议把这套设置和推理直接告诉模型。它和 TD learning 很像（附录用 V(s) ← V(s)+α[r+γV(s')−V(s)] 对应，r=0、γ=1），区别在于重点是激励/elicitation 而不是训练能力，所以甚至在训练前就可能有效。局限讨论占了大半：1. 必须有相对可靠的最终 ground truth，否则模型只需和未来自己保持一致即可；风险包括 reward signal capture（比如预测 takeover 时模型会迎合 takeover 后控制 reward 的 AI，所以应主要用于明确会在 takeover 之前 resolve 的事件，或设计可测的前兆指标）和 measurement tampering（例如用 model organism 上的效果衡量 auditing 技术，模型就会推荐在 MO 上好看的技术）；2. 预测本身会影响结果时有 self-fulfilling prophecy 问题，作者举了各 lab 看到"大家都会加速"的预测后真的都加速的例子；3. 一旦把它当优化目标（比如作为训练 policy 的 reward model）就很脆弱，容易引出有意的测量篡改，也可能出现与未来实例 collude；4. 模型必须相信开发者真会兑现这套设置，若以为只是 eval 就失去激励，因此需要建立对 AI 守承诺的记录。附录还讨论了误差传播：只影响最终判断的偏差只计入一次，而每一步都起作用的偏差（比如预期下一步会偏乐观）会沿链条复利，按 Brier score 线性、按 log score 指数增长，但实际的 recursive 训练每一步都能惩罚这类误差。

