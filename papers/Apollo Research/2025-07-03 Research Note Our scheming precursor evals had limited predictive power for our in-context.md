---
title: "Research Note: Our scheming precursor evals had limited predictive power for our in-context scheming evals"
lab:
  - "Apollo Research"
date: 2025-07-03
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/research-note-our-scheming-precursor-evals-had-limited-predictive-power-for-our-in-context-scheming-evals
tags:
  - 策划与欺骗
  - 评估方法
---

# Research Note: Our scheming precursor evals had limited predictive power for our in-context scheming evals

**来源**：Apollo Research · 2025-07-03 · [原文](https://www.apolloresearch.ai/science/research-note-our-scheming-precursor-evals-had-limited-predictive-power-for-our-in-context-scheming-evals)

## 简读

这是一篇 research note，事后回测 Apollo 自己的 scheming 前兆评估到底能不能预测后来的 scheming 评估。背景是 Frontier Safety Policy 常依赖“early warning”式的 precursor eval 来提前触发缓解措施。Apollo 在 2024 年 5 月做了两组未发表的前兆评估（agentic self-reasoning，例如必须发现并关掉屏蔽某个词的 safety filter；applied theory of mind，例如订性别揭晓派对用品时要删邮件、不向用户泄露胎儿性别），曾用于 GPT-4o system card 的评估；12 月又发布直接测 scheming 推理的 in-context scheming 评估。所有评估都有 easy/medium/hard 三档，区别在提示多少。他们在 22 个模型上每个评估跑 100 次。先做 sanity check：难度排序大体成立，easy→medium 的预期排序比例在前兆评估为 75.9%（反序 8.3%），scheming 为 55.3%（反序 7.9%），medium→hard 时大量模型双双得 0，说明前兆评估的 hard 档相对太难；与 Artificial Analysis 通用智能分的相关性，前兆 r=0.816（显著），scheming 只有 r=0.412（不显著），与 scheming 评估混合了能力和倾向的判断一致。预测分析包括：1. 阈值分析，在 10×10 阈值组合中找“前兆超过 T 就不会漏掉 scheming 超过 T'”的组合，低漏报率的阈值往往近乎平凡（如前兆 >0.32 且 scheming >0.85 的模型不存在），对角线及以下很多组合都有漏报；2. 时间顺序，前兆分数本应高于 scheming 分数，easy 和 medium 大体成立，hard 不成立，因为 hard 前兆任务往往依赖一个反常的单一洞见（比如意识到自己的输出被改写），强模型也常得 0；3. 线性预测的 R² 很低，而且这还是事后诸葛亮式地挑子集，真实情境下会更差。结论是预测力从低到中等，easy 档还有点用，hard 档中性甚至误导，对高风险决策显然不够。作者承认样本小、两套评估本身都有缺陷，建议不要外推太广，但认为这提醒人们提前预测危险能力很难，precursor eval 未必能可靠充当触发器；建议多做 science of evals 研究，并尽可能直接测量目标能力而不是先造前兆评估，也希望这套回测方法能被其它评估者复用。

