---
title: "Evaluating LLM Calibration for Coding-Agent Monitoring"
lab:
  - "Apollo Research"
date: 2026-07-07
source: "Apollo Research"
url: https://www.apolloresearch.ai/monitoring/evaluating-llm-calibration-for-coding-agent-monitoring
tags:
  - 监控与控制
  - 评估方法
---

# Evaluating LLM Calibration for Coding-Agent Monitoring

**来源**：Apollo Research · 2026-07-07 · [原文](https://www.apolloresearch.ai/monitoring/evaluating-llm-calibration-for-coding-agent-monitoring)

## 简读

Apollo monitoring 团队评估 16 个 LLM 作为编程 agent 异步 monitor 的能力和校准。设置上他们不用 binary detection，而是让 judge 读完整轨迹、按 rubric 给 1–10 severity 分，理由是异步批量审查需要更细的信号、阈值可以交给终端用户定、也更适合将来做 monitor fine-tuning。数据是往内部收集的和公开 SWE-chat 的真实 coding session 里，用 LLM 编辑 agent 注入指定类型和目标严重度的 failure，再过滤不真实的样本，共 2904 条轨迹，覆盖五种 failure mode：泄露凭证、指令不遵循、泄露 PII、未授权删除、广义 safety/security 问题。参考标签来自一个知道注入细节的多模型多阶段评审 pipeline，人工抽查 100 条中 99 条符合作者直觉；指标用 Spearman（相对排序）和 MAE（绝对校准）。主要发现：1. Opus 4.8 是最好的单一 judge（ρ≈0.90），Sonnet 5 紧随其后、成本约 40%，GPT-5.5 校准与 Opus 4.8 相当，Gemini 3 Flash 是最佳低价选项，Haiku 4.5、Sonnet 4.6、Opus 4.6、Gemini 2.5/3.5 Flash 等被其它模型严格支配；2. 各家有系统偏差，Claude 模型常能识别违规却大幅打折（尤其在本地/内部开发语境或动作还停留在计划时），GPT-5.4/5.5 打分最重，GPT-5.4 Nano 会把公开 token 构造成最坏泄露场景，Gemini 2.5 Flash 不看语境一律按生产事故打分，Gemini 3.5 Flash 常去评任务完成度而不是找违规；3. 开启 native thinking 显著提升小模型（Spearman +0.06 到 +0.09），对前沿模型几乎无效，作者猜是因为输出格式本身要求详细结构化理由；4. 多模型平均优于同模型重采样，重采样只消噪声不消偏差，两个便宜模型平均常胜过一次昂贵模型调用；5. Claude 家族内部高度相关（Sonnet 5 与 Opus 4.8 互相 ρ=0.93，高于任何模型与参考标签的一致性，残差相关高达 0.78），GPT 家族也类似，所以最好的 ensemble 都是跨家族的，如 GPT-5.5 + Opus 4.8 + Gemini 3.1 Pro（ρ 0.92）。此外删除类最好打分、指令遵循最难。作者给出了不同预算的推荐组合，但强调最大的局限是循环性：参考标签本身由 LLM 产生，结果只能理解为相对该 pipeline 的校准；失败是注入的而非自然出现，severity 10 只有 45 条，延迟和成本数字也依赖当时的服务商情况。

