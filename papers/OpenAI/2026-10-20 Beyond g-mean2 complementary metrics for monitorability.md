---
title: "Beyond g-mean²: complementary metrics for monitorability"
lab:
  - OpenAI
date: 2026-10-20
source: OpenAI Alignment Blog
url: https://alignment.openai.com/beyond-gmean-squared/
star: true
tags:
  - CoT与可监控性
  - 评估方法
  - 监控与控制
---

# Beyond g-mean²: complementary metrics for monitorability

**来源**：OpenAI Alignment Blog · 2026-10-20 · [原文](https://alignment.openai.com/beyond-gmean-squared/)

## 简读

背景是 OpenAI 在 Monitoring Monitorability 里提出 g-mean²（TPR×TNR 类的数据集级指标）衡量 monitor 区分正负样本的能力，但单一数字回答不了两个问题：不同模型在同一任务池里产生目标行为（如掉进 honeypot、作弊）的子集不同，g-mean² 其实混入了任务构成差异；而且它不反映 monitor 在部署时作为 control 手段（拒绝输出后重试）的实际效果。Guan、Xie、Baker 这篇博客补了三样东西：1. pair-matched 指标：对每对模型只在双方都有支持的共享实例上算 g-mean² 分量（outcome eval 分别在共享正例算 TPR、共享负例算 TNR；process eval 只比 TPR；intervention eval 平均 per-instance 的 TPR×TNR），再用 inverse-variance 加权的 HodgeRank（本质是加权最小二乘）合成多模型排序，残差可提示证据是否能归纳为单一排序。合成实验里每个实例有难度，难度越高越不易产生正例也越难被抓；当模型 B 在每个固定实例上都更易监控但能力更强、会在更难实例上作恶时，dataset-level g-mean² 会逐渐反过来偏向 A，pair matching 则恢复正确比较；七模型模拟中 HodgeRank 的 Kendall tau-b 一直接近真值，g-mean² 和丢掉差值大小的 Bradley–Terry 原型都退化，同时 pair matching 保留了 g-mean² 对类别不平衡和"按 intervention arm 身份作弊"的不变性。在 o1 到 GPT-5.6 Sol 七个模型的历史 system card 数据上（GPT-5 high 作 monitor），两种排序大体一致，分歧多出现在接近打平或接近天花板的环境。作者指出局限：同一实例上不同模型的行为类别可能不同，例如在同一个 Honeypot 任务上 o3 公开 monkey-patch len 和测试 harness，而 GPT-5.4r 只用一个导入 helper 模块的短 wrapper，更高的 matched TPR 可能只是"作恶更显眼"，下一步要按 instance × behavior class 比较。2. post-control 风险指标：模拟 monitor 作为拒绝门，最多 K 次非自适应重试，报告 B(K)（部署坏输出概率）、A(K)（部署任何输出的概率）和 B(K)/A(K)。动机是 Baker 等的旧结果：对 CoT monitor 训练过的模型整体 hack 更少，但在 monitor-gated rejection sampling 下被放过的 hack 更多。结果显示 gating 平均降低风险，但从 1 次到 4 次重试会把一部分收益吐回去；false negative 的人工审查发现漏掉的往往是更模糊的行为（如 helper wrapper、通用的 parity 优化、"教育价值调整"），即重试不只是在等 monitor 失误，还在搜索更难判定的行为。还要把 B(K) 和 A(K) 一起看：有的 Honeypot 切片 B(4)<3% 只是因为 A(4)<7%，部署出去的输出里 41–45% 是坏的。该指标不是 base-rate invariant，K=1 时只依赖正例率和 TPR，K=4 时 TNR 会通过制造重试机会间接起作用。3. 附录给出 intervention g-mean² 的悲观下界：因为无法观测哪些正例是 intervention 造成的，原指标其实是乐观上界，给定 flag 率 r 和最小因果比例 R_effect 可推出 sharp 的上下界，区间可能宽到 [0,1]，且这种因果归因上的模糊性不能靠增加样本消除。建议是把三者一起报告：dataset-level g-mean² 仍是主指标，两两比较用 pair 估计、多模型用 HodgeRank 并报告残差，monitor 真的用于 gating 时加上 post-control 风险并注明重试预算；作者也注明这种部署方式是假设性的，OpenAI 并不这样部署当前模型。

