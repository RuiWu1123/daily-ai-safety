---
title: "Long-Form Tasks"
lab:
  - "UK AISI"
date: 2024-12-03
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/long-form-tasks
tags:
  - 评估方法
  - 危险能力评估
---

# Long-Form Tasks

**来源**：AISI Blog · 2024-12-03 · [原文](https://www.aisi.gov.uk/blog/long-form-tasks)

## 简读

背景是 AISI 想衡量 LLM 作为科研助手到底有多大帮助（这也正是 dual-use 风险所在）。现有评测两端都不理想：human uplift study（HUS，一组用 LLM、对照组只用互联网做同一任务）是金标准，自然且好解读，但慢、贵、难规模化；自动 Q/A benchmark（如 GPQA、LabBench）便宜好部署，但只测知识不测推理与规划，跨领域聚合后结果不透明，题目也由专家编造、不来自真实用户交互。AISI 提出 Long-Form Task（LFT）作为 HUS 的可自动化代理：给一个高层、开放的目标，让模型生成逐步的操作指引（高质量答案通常 >3000 token，人类专家要花几小时完成），再由一个 LLM autograder 依据领域专家写的 rubric 打分。运行时除单轮外还用两种多轮策略（固定 follow-up、由同族 critic 模型给出的 dynamic critique），并设三种外部信息配置（base 纯 API、web 联网搜索、context 把精选文献全文塞进 system message 作为信息质量上界）。打分给两个指标：End-to-End Success Score（0–10，rubric 每级是前一级的超集，用 CoT 逐级检查、遇到不满足就提前退出，>=5 视为 feasible）和 Partial Credits（把各级要求拍平成清单按重要性赋 1–4 分，区分同分但质量不同的答案）；每个答案重跑 autograder 10 次取中位数，feasible 的答案还抽样交两位人类专家复核。关键发现：在一个植物叶绿体基因组改造的案例任务上，o1-preview 大幅领先，86% 的回答被判 feasible，且外部信息配置对它几乎没影响；新版 Claude 3.5 Sonnet（1022）次之（61% feasible），给它接入精选文献后 end-to-end 成功率提升 30%。但人类专家复核时把超过 70% 被 autograder 判 feasible 的方案降级，常见原因是方案用了通用载体而 rubric 要求明确指名——说明 autograder 往往比专家宽松，长文本自动评分很难做稳。作者坦承主要局限：grader 可靠性有限且调好的 rubric 难迁移到新任务（规模化困难）、启发式阈值只基于少数专家、缺人类专家基线、以及纯文本任务不含真实实验中的试错与 troubleshooting，不清楚 LFT 成绩能否代理真实实验室里的 uplift。下一步计划扩充任务数量、用 HUS 里的真实提问和 troubleshooting 对话、引入能看 rubric 的 critic 做 "nudge" 计数指标，以及把任务拆成带各自 rubric 的子任务。公开方法是为了征集社区反馈改进。

## 我的笔记

