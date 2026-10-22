---
title: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models
lab:
  - Redwood Research
date: 2026-06-10
source: Redwood Blog
url: https://blog.redwoodresearch.org/p/estimating-no-cot-task-completion
star: true
tags:
  - CoT与可监控性
  - 评估方法
---

# Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models

**来源**：Redwood Blog · 2026-06-10 · [原文](https://blog.redwoodresearch.org/p/estimating-no-cot-task-completion)

## 简读

METR 一年前表明前沿模型能可靠完成的任务长度每几个月翻倍；这篇新论文问一个安全相关的版本：不输出任何 CoT 时模型能完成多长的任务。如果模型能在不外显 CoT 的情况下做大量推理，开发者和部署期 monitor 就难以看懂其动机、抓到危险规划，而且这种推理不受预训练文本先验约束，可能更偏离人类思维、更容易 scheme。工作延续 Ryan Greenblatt 之前的 no-CoT 数学时间跨度研究，在 43 个 benchmark 上评估了从 GPT-2（2019）到 GPT-5.5（2026）的 14 个模型，覆盖数学、编程、知识、agentic tool-use 以及 steganography、scheming 推理等安全相关问题，用 benchmark 特定 prompt 和 structured output 约束阻止模型在答案前输出推理。题目难度用两种独立方式度量：人类用计算器纸笔的平均解题时间（部分有现成数据，部分做小规模人类试验，其余用 Claude Opus 4.7 参照人类时间例子估计）；以及 o3-mini 8 次尝试中成功解题的最少 reasoning token 数。按 Kwa et al. 的方法拟合 logistic 曲线求 50% time horizon，并对 benchmark、题目、运行做 10,000 次 bootstrap。结果：no-CoT time horizon 每 373 天翻倍（95% CI 167–691），token horizon 每 437 天翻倍（341–571）；当前前沿 GPT-5.5 的 50% no-CoT TH 约 3 分钟、约 1,500 个 o3-mini token；中位外推到 2028 年约 7 分钟/3.7k token，2030 年约 25 分钟/12k token，即使取 CI 慢端到 2030 也接近 10 分钟。翻倍速度对更换 benchmark 分布、只用实测人类时间、去掉任一模型、按领域拆分（领域翻倍时间 246–387 天）都较稳健。与 Kwa et al. 带 CoT 的 182 天翻倍相比慢约一倍，两条曲线在 GPT-4 之后分叉，说明此后能力增长主要来自外显推理而非单次 forward pass 内更多推理。作者澄清：benchmark 混有事实回忆题，所以不完全是纯推理；这测的是模型"能"隐蔽做多少推理，不是它们真的在藏推理；这是下界，强制短答案对推理模型可能是分布外的，更好的 elicitation 或 steganography 都能突破这个下限。解读上，3 分钟人类等效推理也许足够做一些单次决策（是否服从指令、场景像不像 eval、选哪个选项），但大概不够做 training-gaming 或与其它实例串通这类复杂长期 power-seeking 推理；若趋势延续，到 2030 年 25 分钟的 no-CoT 推理会允许多得多的 subversion，即使没有 neuralese，CoT monitoring 也可能在几年内明显失效。建议 AI 公司显式跟踪 no-CoT TH，这套评估推理成本低；数据集为防污染不公开、可申请获取，是 Redwood、Astra、Aether、MATS 的合作工作。

