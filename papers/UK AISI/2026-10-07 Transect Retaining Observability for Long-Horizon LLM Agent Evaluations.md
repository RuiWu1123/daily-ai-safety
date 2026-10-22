---
title: "Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations"
lab:
  - "UK AISI"
date: 2026-10-07
source: "AISI Research"
url: https://www.aisi.gov.uk/research/transect-retaining-observability-for-long-horizon-llm-agent-evaluations
other_versions:
  - "https://www.aisi.gov.uk/blog/transect-making-large-scale-agentic-evaluations-easier-to-understand"
star: false
tags:
  - 评估方法
---

# Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations

**来源**：AISI Research · 2026-10-07 · [原文](https://www.aisi.gov.uk/research/transect-retaining-observability-for-long-horizon-llm-agent-evaluations)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/transect-making-large-scale-agentic-evaluations-easier-to-understand)

## 简读

背景是前沿 eval 越来越多是开放式、长程、多 agent 的任务，transcript 动辄上百页乃至数十亿 token，作者把评估者能可靠推断的范围称为 observability envelope，并指出它正受四种压力：最终分数掩盖过程（within-run opacity）、人工审阅注意力瓶颈、重复次数少导致统计功效不足、难以区分表现来自模型还是 harness/setup。用 LLM judge 辅助分析能缓解，但带来大量 researcher degrees of freedom（judge 模型、rubric、分析单位等），损害可复现和可审计性。AISI 与 Meridian Labs 因此开源了 Transect，一个基于 Inspect Scout 的 Python 包：用户为一个评估族写可复用的 Spec（任务背景、行为类别词表、sub-agent 角色类别），judge 模型和判定方式（solo、同一模型重复 k-rolls、多模型 cohort，可选 verifier 复核低置信或低一致的标签）另行配置；pipeline 分 ingest/select/scan/store/render 五步，把每次 agent 输出作为一个 turn，将结构化 scanner 抽取的事件（context compaction、operator 消息、token 用量、sub-agent 启动）和 judged scanner 打的行为标签对齐到同一时间轴，报告里每个标签都能回链到原始 turn，judge 的 prompt、输入和每次判决都存档，可不重新调用模型复查，数据表可导出做跨 run 分析；还附带给 coding assistant 用的 skill，帮忙写 Spec、向领域专家提问、检查对类别名称的敏感性。案例是 CRUX shadow evaluation 中的一次 run：Claude Opus 4.7 agent 用六天根据未发表人类论文的 brief 研究 tabular PFN 的有害分布偏移检测并写出论文，共 554 次 orchestrator tool call、79 个 sub-agent、57 条 operator 消息、8 次 compaction、约 1300 万 token，其中 89% 由 sub-agent 产生。发现包括：开头是很长的运维阶段，多数 operator 消息都在帮它解决权限问题；580 个 orchestrator 输出里只有 2 个标为 Hypothesising（Reflecting 56 个），Analysis design 完全没出现；self-review 和 manuscript write-up 占新 token 的约四分之三（7.8M 和 2.9M / 14.5M），而 solution ideation 只有约 2.2 万 token，citation sub-agent 约 5M token 主要用于打磨稿件而非早期找方向，与原评估"论文是详尽的负面结果而非新想法"的观察一致；共享文件分析得到 922 条访问记录，66.6% 集中在 paper/ 目录；agent 论文 46 条引用中只有 20 条能在 OpenAlex/Crossref/arXiv 核实，人类论文 69 条中有 60 条，两者仅共享 13 条，提示 agent 没找到同样的文献背景。k=5 判定下约 82% 的输出标签一致，但作者反复强调一致性不等于有效性，缺失标签也只是弱证据，这些都是描述性而非确证性结论，无法区分是 agent 偏好、scaffold 不支持科研还是推理没体现在 transcript 里；他们建议据此做干预（如加 ideation gate、提供人类参考文献）并跨 epoch 对比。博客还提到这种系统性 transcript 审阅在 AISI 事故调查中发挥了作用。

