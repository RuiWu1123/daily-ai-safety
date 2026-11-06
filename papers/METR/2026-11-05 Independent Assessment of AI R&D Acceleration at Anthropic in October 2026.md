---
title: "Independent Assessment of AI R&D Acceleration at Anthropic in October 2026"
lab:
  - "METR"
date: 2026-11-05
source: "METR Research"
url: https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment
other_versions:
  - "https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review"
star: false
tags:
  - 危险能力评估
  - 评估方法
  - 威胁建模
---

# Independent Assessment of AI R&D Acceleration at Anthropic in October 2026

**来源**：METR Research · 2026-11-05 · [原文](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment)　另见：[METR Blog](https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review)

## 简读

METR 于 8 月 12 日至 10 月 29 日在 Anthropic 进行了一次 high-access 评估，衡量 AI 在多大程度上加速了 AI R&D；之所以重要，是因为如果 AI 显著加速自身的研发，可能导致极端且危险的能力突然出现。Anthropic 提供了前所未有的内部数据：预训练和 RL 的各类指标、各领域训练算力、内部模型的 benchmark 分数、AI 加速分析、未来模型的指标预测，以及对相关员工的访谈。同时发布的还有 METR 应 Anthropic 邀请对其 8 月 Risk Report 中"Risks from automated R&D"一节的审阅（作为"另见"附上）。主要结论：多数参与的 METR 员工认为，截至 2026 年 10 月，Anthropic 在定义清晰的任务上提升模型能力的速度大约是 2024 年 3 月至 2025 年 10 月期间的两倍，不确定性很大，真实值在 1.3 倍或 3 倍附近也不意外，且这种加速能否推广到更宽泛、定义不清的任务还不清楚；他们估计当前加速的大部分（约 80%）来自 Anthropic 大量用 AI 做研发，但 2025 年末的加速很可能受非 AI 因素影响；他们没有发现会阻止未来 12 个月能力继续进步的明显瓶颈（算法进展、训练算力、实验算力、数据）或陡峭的收益递减，因此进一步的能力进步存在导致更快加速的显著风险，不过他们对瓶颈的理解在评估中改变过好几次。关键实证发现：自 2025 年 10 月以来，Anthropic 模型的 AECI（Anthropic 版本的 Epoch Capabilities Index）增速是此前的 1.9 倍（95% 置信区间 1.5–2.8），相当于过去一年取得了以往两年的进展，高于 Haiku 5.5 system card 报告的 1.7 倍，主要因为纳入了更新的未发布模型；改变 benchmark 选取、模型日期、模型纳入和饱和处理等选择后，稳健性分析得到的加速在 1.1 到 2.9 倍之间；他们确信加速不是由训练算力规模的加速导致；访谈和调查与"AI 使用使能力进步速度翻倍"一致，员工自述获得了巨大提升，但这类数据难以解读，研发加速目前主要来自 AI 辅助而非完全自主的贡献，不过有迹象表明自主贡献很快会更重要。对 Risk Report 的审阅认为：Anthropic 关于模型尚未达到"完全替代全部研究人员"阈值的论证总体可信；但关于尚未达到"2 倍加速"预警阈值的结论过于自信，依赖了公开报告中没有讲清楚的判断，公开报告低估了领先指标和 AECI 中的加速证据（例如私下报告的数字隐含约 1.97 倍，公开报告却说"不到 2 倍"，METR 自己对领先指标的估计在 1.3 到 2.8 之间），也低估了私下报告中对反事实加速的不确定性，METR 认为截至 7 月 15 日这一阈值"有可能"已被跨过；尽管如此，他们同意当时模型自动化 R&D 直接带来灾难性风险的可能性很低，但无法排除未来 6 个月出现大幅进一步加速，从而迅速进入"高"风险。透明度方面，Anthropic 有权删改非公开信息，删掉了 METR 认为最有信息量的大部分证据（理由是防止加速其它 AI 开发者），METR 坦言这使公众不得不比理想情况更多地依赖 METR 的判断。局限：可能低估加速（例如低估了近期增速进一步上升的证据、AI R&D 任务的进一步自动化，或 AECI 有时低估真实影响），也可能高估（例如低估了非 AI 因素、AECI 偏重可验证任务，或 Anthropic 2023–2025 年的早期增速异常低）。
