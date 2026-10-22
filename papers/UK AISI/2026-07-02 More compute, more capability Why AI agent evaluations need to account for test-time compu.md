---
title: "More compute, more capability: Why AI agent evaluations need to account for test-time compute"
lab:
  - "UK AISI"
date: 2026-07-02
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/more-compute-more-capability-why-ai-agent-evals-need-to-account-for-test-time-compute
star: false
tags:
  - 评估方法
  - 危险能力评估
---

# More compute, more capability: Why AI agent evaluations need to account for test-time compute

**来源**：AISI Blog · 2026-07-02 · [原文](https://www.aisi.gov.uk/blog/more-compute-more-capability-why-ai-agent-evals-need-to-account-for-test-time-compute)

## 简读

大多数 agent 评估把能力压缩成一个数字，却隐藏了一个关键设计选择：agent 停下之前允许花多少 test-time compute。AISI Science of Evaluation 团队在 cyber、软件工程、数学、学术任务和医疗等多个 agentic benchmark 上，把 token 预算从低扫到高，跟踪整体成功率、可靠性、效率和能触及的最难任务，并在单任务层面比较不同代模型。核心发现有三点：1. 能力是随 compute 变化的曲线而不是单一分数，曲线停止评估时仍在上升，报告的分数就只是下界。在 AISI narrow cyber 任务上约 8% 的任务要到 10M+ token 才被解出，有的要 50M，最新模型在 100M+ 还在涨；公开 benchmark 上从 1M 提到 10M token，TerminalBench 2.0、SWE-Bench Pro 提升约 25%，Humanity's Last Exam（到 5M）提升约 22%，TerminalBench 在公开评估常用预算的 10 倍处仍在提升。但 HealthBench 上所有模型在常规预算内就饱和，作者认为 compute 在能自我检验、从错误中恢复的领域（代码、cyber、数学）最有用。2. 解出一个任务所需的最少 token 与人类完成时间成比例（211 个 METR 软件任务和 78 个 AISI CTF，幂律指数约 0.7–1.0），连最便宜的成功 run 也如此，说明下限由任务本身的工作量决定；因此固定预算最先截断的正是最长任务，失败可能只是预算不够。例如人类约 20 小时的 cyber range “The Last Ones”在预算至少 30M token 前没有模型能完成。3. 新模型把额外 compute 转化为更大收益，体现在 reach、reliability、efficiency 三个维度，所以固定预算下的差距会随模型进步而扩大。对 time horizon 而言，过去一年模型在 50M token 下估计的前沿趋势比 2.5M 下陡约 60%；某个近期模型的 80% horizon 从 2.5M 下约 40 分钟升到 50M 下约 4 小时，当前前沿从约 2 小时升到约 14 小时，意味着此前 4.7 个月的 doubling time 部分是预算的产物。另有一个注意点：在 10–30% 的任务上新模型反而比前代差。作者主张评估应报告 capability curve，AISI 已开始在多个预算下评估、报告 reliability/reach 随预算的变化、定义“minimum informative budget”，并研究用便宜 run 预测高预算表现；随着 token 成本下降，高预算才能触及的能力也会越来越容易获得。

