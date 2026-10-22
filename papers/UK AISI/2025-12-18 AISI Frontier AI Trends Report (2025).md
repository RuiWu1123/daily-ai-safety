---
title: "AISI Frontier AI Trends Report (2025)"
lab:
  - "UK AISI"
date: 2025-12-18
source: "AISI Research"
url: https://www.aisi.gov.uk/research/aisi-frontier-ai-trends-report-2025
other_versions:
  - "https://www.aisi.gov.uk/blog/5-key-findings-from-our-first-frontier-ai-trends-report"
tags:
  - 危险能力评估
  - 网络安全
---

# AISI Frontier AI Trends Report (2025)

**来源**：AISI Research · 2025-12-18 · [原文](https://www.aisi.gov.uk/research/aisi-frontier-ai-trends-report-2025)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/5-key-findings-from-our-first-frontier-ai-trends-report)

## 简读

UK AISI 发布的第一份公开 Frontier AI Trends Report，汇总了 2023 年 11 月成立以来对 30 多个前沿模型的内部测试结果。报告只给聚合后的趋势，不点名具体模型或公司，覆盖 2022 年到 2025 年 10 月发布的 LLM，同时配了一篇"5 个关键发现"的博客。主要结论：1. 能力在所有测过的领域都在快速上升。cyber 方面，apprentice 级任务的成功率从 2023 年底不到 9% 涨到现在的约 50%，2025 年第一次出现能完成 expert 级任务（需要 10 年以上经验）的模型，能独立完成的 cyber 任务长度大约每 8 个月翻一倍；自主性方面，人类专家需要 1 小时以上的软件任务，成功率从不到 5% 涨到 40% 以上。scaffold 影响很大：外部最佳 scaffold 在 SWE-bench 上一度比基础模型高近 40%，AISI 自己花两周优化 scaffold 后，cyber dev set 提高近 10 个百分点，达到同等表现所需的 token 只要原来的约 13%，说明不做专门 elicitation 的评估会低估能力上限。但在多阶段的 cyber range 里，模型通常只能拿下第一个 flag。2. 化学与生物：开放式 QA 上，模型在 2024 年首次超过 PhD 基线，现在最多高出 60%；2024 年底开始能写出可行的实验 protocol，并且经过湿实验验证；非专家借助模型写出可行病毒复苏 protocol 的几率是只用互联网组的 4.7 倍；troubleshooting 最高比专家高近 90%；2025 年中多模态 troubleshooting 也首次超过专家；模型已能自主检索 plasmid 设计所需的序列，但端到端设计还做不好。3. Safeguards：AISI 测过的每个系统都被找到了 universal jailbreak；不过防护最强的系统进步明显，两个相隔 6 个月发布的模型，在生物滥用类别上找到 jailbreak 所需的专家时间差了约 40 倍（10 分钟对 7 小时以上）。这种进步很不均衡：生物以外的类别、防护投入少的厂商、open-weight 模型都弱得多。通用能力和 robustness 几乎不相关（R² = 0.097），safeguard 强弱主要取决于投入多少。作者的看法是 safeguard 挡不住所有滥用，但能争取一段 adaptation buffer。4. Loss of control：RepliBench 中 11 个任务的成功率从 2023 年的不到 5% 升到 2025 年夏季的 60% 以上，模型擅长获取算力和资金这类早期步骤，复制到算力上和维持持久访问这类后期步骤仍然不行；模型在被 prompt 时能 sandbag，white-box deception probe 在小模型上效果好，但在更大模型的复杂 agentic 任务上，black-box monitor 和 probe 的准确率都下降，而训练成模仿弱模型的 sandbagging 更难检测；他们用自动 monitor 查了 2700 多份过往测试 transcript，没发现自发 sandbagging，只有少数模型意识到自己在被评估后表现不同。5. 社会影响：说服力随规模提升，针对性的 post-training 提升得更多，但更有说服力的模型往往准确性更差；不过在真实使用中，用 AI 查政治信息与自己上网搜索对错误信息信念的影响几乎相同；33% 的英国受访者过去一年用 AI 寻求过情感支持，4% 每天使用，CharacterAI 宕机时 subreddit 发帖量激增 30 倍以上，不少帖子描述了戒断症状；金融类 MCP server 中可执行操作的高自主级别占比在上升。6. 开源与闭源模型的差距缩小到 4–8 个月。局限是任务环境只是代理指标，而且 AISI 通常拿不到微调 API、也不最大化推理算力，因此很可能低估了能力上限；高风险任务的方法细节没有公开。AISI 计划定期更新这份报告。

