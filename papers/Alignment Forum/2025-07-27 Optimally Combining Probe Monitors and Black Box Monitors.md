---
title: "Optimally Combining Probe Monitors and Black Box Monitors"
lab:
  - "Alignment Forum"
date: 2025-07-27
source: "Alignment Forum（Redwood Research；Tim Hua, James Baskerville, HenriLemoine, Mia Hopman, Aryan Bhatt, Tyler Tracy）"
url: https://www.alignmentforum.org/posts/FhixwyymPxF8TZX39
star: false
tags:
  - 监控与控制
---

# Optimally Combining Probe Monitors and Black Box Monitors

**来源**：Alignment Forum（Redwood Research；Tim Hua, James Baskerville, HenriLemoine, Mia Hopman, Aryan Bhatt, Tyler Tracy） · 2025-07-27 · [原文](https://www.alignmentforum.org/posts/FhixwyymPxF8TZX39)

## 简读

Tim Hua、Tyler Tracy 等人研究如何把成本和性能不同的多个 runtime monitor 最优地组合成一个监控协议。现实动机是成本：通常用 probe 这种几乎免费的监控器扫描全部输出，只在可疑时升级到昂贵的 black box monitor（例如 ChatGPT Agent 先用快速主题分类器再用推理模型查 bio 滥用），而已有工作多靠启发式规则（比如第一个分数接近中位数时才调第二个、两个都调时取平均）。他们把问题形式化为：在对 aligned 输出的平均花费（监控费用加审计/安全干预费用）不超过预算的约束下，最大化对 misaligned 输出施加安全干预的 recall；之所以按 aligned 分布算成本，是因为 misaligned 输出很少且主要开销来自误报。解法是逆向归纳：先固定监控调用策略（先调哪个、在什么分数区间调第二个），此时剩余预算决定可承受的审计误报率，再按 Neyman-Pearson 引理对似然比（用核密度估计）设阈值、审计似然比最高的区域，这是给定误报率下最强的检验；然后对少量（2–4 个）监控器的调用顺序和连续阈值区间做暴力网格搜索，取 safety 最高者。作者坦言试过刻画最优调用区间的解析形式但因预算约束太难，最后发现直接扫阈值就行；若监控预算和审计预算不能互换，问题反而更简单。帖子用 Parrack et al. (2025) 的 probe 数据加一个 black box monitor 做示例，成本设为 probe 10^-6、black box 1、审计 20：最优策略是先跑 probe，分数很高直接审计、不高就结束、居中（-0.01 到 2.18 之间，aligned 输出中约 19.6% 落在这里）才调 black box，再用核方法融合两个分数按 LLR 阈值 -0.32 审计，结果在审计 4% aligned 输出、每样本平均花费 1 美元的情况下抓到 93.7% 的 misaligned 输出。通过变动预算可画出 Pareto 前沿，组合两个监控器在同等成本下 safety 优于只用单个监控器（单监控器基线也允许不是 100% 调用）。论文里还有用两个不同大小 LLM monitor 在 control setting 上的实证，结果同样优于朴素基线；作者提示决策边界可以通过单调性约束或加大核宽度做正则化。代码开源。
