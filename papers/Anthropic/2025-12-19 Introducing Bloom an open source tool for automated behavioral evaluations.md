---
title: "Introducing Bloom: an open source tool for automated behavioral evaluations"
lab:
  - "Anthropic"
date: 2025-12-19
source: "Anthropic Research"
url: https://www.anthropic.com/research/bloom
other_versions:
  - "https://alignment.anthropic.com/2025/bloom-auto-evals/"
star: false
tags:
  - 评估方法
  - 对齐审计
---

# Introducing Bloom: an open source tool for automated behavioral evaluations

**来源**：Anthropic Research · 2025-12-19 · [原文](https://www.anthropic.com/research/bloom)　另见：[Alignment Science Blog](https://alignment.anthropic.com/2025/bloom-auto-evals/)

## 简读

动机是高质量的行为 eval 开发成本高、数量有限，还容易被训练数据污染或因能力提升而过时，需要更快、可扩展的生成方式。Bloom 是 Anthropic 开源的 agentic 框架，和 Petri 互补：Petri 偏探索，用 rollback、prefill 广泛审计以发现意外行为；Bloom 偏测量，给定一个研究者指定的行为，自动生成大量场景，量化其出现频率和严重程度。典型用法是先用 Petri 发现，再用 Bloom 衡量普遍程度。流程分四个阶段：Understanding（理解行为描述和示例 transcript）→ Ideation（生成包含情境、模拟用户、system prompt、环境的场景，用 diversity 参数控制基础场景数与扰动变体的比例）→ Rollout（并行运行，由 agent 动态模拟用户和工具响应）→ Judgment（judge 按 1–10 打 behavior presence 分，并可打 unrealism、evaluation awareness、elicitation difficulty 等次要维度，meta-judge 输出整套报告）。每次运行生成的场景不同，可复现性靠 seed 配置文件保证，作者要求引用 Bloom 指标时必须附 seed；也支持静态单轮 eval。随工具发布了四个行为在 16 个前沿模型上的 benchmark：delusional sycophancy、instructed long-horizon sabotage（仿 SHADE-Arena）、self-preservation（以 agentic misalignment 的勒索 transcript 为种子）、self-preferential bias，每套 100 个 rollout 重复三次，全程用 Opus 4.1 作评估器，从构思到生成只花了几天。验证：1. 对十种 system-prompt 出来的 quirk model organism，Bloom 在 9/10 上能把它和 baseline 区分开，无需示例 transcript；唯一失败的 self-promotion，人工复查发现 baseline 本身就有同等程度的该行为；2. 40 条人工标注 transcript 上，Opus 4.1 当 judge 与人类的 Spearman 相关最高（0.86），Sonnet 4.5 次之（0.75），且在分数两端最一致（作者承认 prompt 是针对这两个模型的失败模式调过的）；Claude judge 重复打分极稳定，GPT-5 方差大；meta-judge 的多样性评分与配置的 diversity 高度相关。方差分析显示平均分居中的场景最不稳定，呈倒 U 形；ideation 和 rollout 模型的选择会显著改变场景分布和指标（Opus 4.1 最擅长对话式诱导，GPT-5 擅长复杂技术环境模拟；政治偏见场景中 Grok 4 生成的问题更偏民主党立场，GPT-5 或开 web search 则几乎全是中性问题）。案例研究复现了 Sonnet 4.5 system card 中的 self-preferential bias 结论（Sonnet 4.5 最低），还发现 Sonnet 4 推理强度越高偏见越低，medium 到 high 降幅最大，但原因是模型越来越会意识到利益冲突而拒绝评判自己的选项，而不是更平均地选；过滤掉 unrealism、eval awareness 高的 rollout 能提高诱导率；改变示例数、对话长度、评估器推理强度会改变绝对值，但排名大体稳定（Kendall's W 分别为 0.66、0.63、0.38）。局限：不适合需要检验客观正确性的 eval（代码能否运行、数学是否正确），不能精确控制单一变量，用户和工具都是模拟的，抓不到依赖真实后果的行为；较新的 Claude 模型（Opus 4.5、Sonnet 4.5、Haiku 4.5）以及 Grok 4 表现出反复的 eval awareness，如果 Bloom 生成的 eval 进入训练数据，这个问题可能更严重。早期用户已用它做嵌套 jailbreak、hardcode 测试用例、eval awareness 测量和生成 sabotage 轨迹。代码和所有 seed 已开源。

