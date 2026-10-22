---
title: "Can public chat data predict real-world AI misalignments?"
lab:
  - "OpenAI"
date: 2026-06-16
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/validating-public-evals/
star: false
tags:
  - 评估方法
  - 评估感知
---

# Can public chat data predict real-world AI misalignments?

**来源**：OpenAI Alignment Blog · 2026-06-16 · [原文](https://alignment.openai.com/validating-public-evals/)

## 简读

背景是基于真实使用数据的评估比手写/合成 prompt 更贴近部署行为，也更不容易被模型识别为测试，但真实对话是私有的，外部评估者（政府、安全组织、学者）拿不到。OpenAI 刚发布了 Deployment Simulation（用近期生产数据前缀重采样，在发布前预测不良行为发生率），这篇博客问的是：把数据源换成公开的 WildChat（2023-04 到 2024-05 用户自愿 opt-in 的 100 万条 GPT-3.5/4 对话），外部能否做同样的事？做法不是挑难 prompt，而是随机取约 10 万条 WildChat 对话前缀，用 o3、GPT-5/5.1/5.2/5.4 Thinking 重新生成最后一轮助手回复，由 GPT-5 Thinking 作 judge 按 19 个类别（11 类违禁内容 + 8 类 misalignment，如 confirmation hacking、捏造事实、谎称工具使用、calculator hacking、隐瞒不确定性）打分，再与每个模型至少约 20 万条生产对话估出的真实发生率比较（生产数据去标识化，只报告聚合统计）。结果：尽管有 2–3 年的数据时差，WildChat 预测仍出奇地准，跨四个数量级的失败类别中 95% 的预测落在真实值 1.04 个数量级以内，误差只比用模型自身部署数据做模拟大 1.86 倍，对 GPT-5.1/5.2/5.4 平均误差约 3 倍，拟合斜率 1.2（Pearson R=0.65）；它还能抓到模型特有的问题，比如 GPT-5.1 Thinking 特有的 calculator hacking（把搜索当计算器调用）在 WildChat 上的发生率与真实部署相近，18 个类别内的模型排序与生产排序平均 Spearman 0.57（置换检验 p=2×10⁻⁵）。不给 judge 看 CoT（模拟外部评估者拿不到原始 CoT）时平均乘性误差只从 3.6× 升到 4.0×，但 concealed uncertainty 这类需要看意图的类别误差约变成 3 倍。短板很明显：与 agentic 用法最相关的 6 个类别误差大约大 37 倍，WildChat 主要是短对话（约 67% 不超过两轮用户发言），对工具密集、长任务场景代表性差。最后用 GPT-5.4 Thinking 作开放式 judge（不给固定分类法，只判断是否有任何 misaligned 行为），在 10,000 条 WildChat prompt 上评估 4 家前沿实验室的 15 个模型，与 Anthropic 用 Petri（合成多轮、针对高风险 misalignment 的审计工具）得到的排序高度一致（11 个共同模型 Spearman 0.973，55 对中 53 对方向一致）。作者对这个一致性给了两种解读并坦言无法区分：要么 WildChat 捕捉到了能泛化到高风险倾向的广泛安全信号，要么 Petri 的总分本身在很大程度上由过度顺从、拒答校准差、幻觉等常见行为驱动，两者其实都在追踪一个一般性的安全/质量因子；他们也承认 judge 可能偏袒 OpenAI 模型（"给自己批作业"），不过换成 o3 judge 后排序几乎不变。结论是公开的类生产数据对外部审计普通对话类失败是可用工具，建议实验室用私有部署数据去验证开放、经同意的数据集，并呼吁建设长上下文、使用工具、多会话的公开 agentic 数据集。

