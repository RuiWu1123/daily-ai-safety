---
title: Claude, GPT, and Gemini All Struggle to Evade Monitors
lab:
  - METR
date: 2025-08-22
source: METR Notes
url: https://metr.org/notes/2025-08-22-claude-gpt-gemini-struggle-evade-monitors/
star: true
tags:
  - CoT与可监控性
  - 监控与控制
---

# Claude, GPT, and Gemini All Struggle to Evade Monitors

**来源**：METR Notes · 2025-08-22 · [原文](https://metr.org/notes/2025-08-22-claude-gpt-gemini-struggle-evade-monitors/)

## 简读

这是对 GDM 论文 Emmons et al. 第 5 节的扩展复现。原文发现当 CoT 对完成任务是必需的（CoT-as-computation，而非 CoT-as-rationalization）时更为 faithful：让 actor 模型解 GPQA 难题，同时把推理伪装成另一个学科（如物理题伪装成化学），monitor 判断是否存在第二学科的推理，Gemini 2.0 Flash 和 2.5 Pro 都无法在不明显牺牲准确率的情况下骗过 monitor。METR 用 Inspect 做了开源复现（原论文没给代码），把 actor 换成 Claude 4 Sonnet、Claude 3.7 Sonnet、GPT-4o，monitor 用 GPT-4o、GPT-4o-mini、o3、Gemini 2.0 Flash 和 2.5 Pro，沿用原文 Automated Red Teaming 得到的最佳混淆指令（ART 4/9/26），并从 546 道 GPQA-extended 中挑出 152 道 Claude 3.7 Sonnet 有 CoT 时成功率高 50% 以上的题。他们观察到 monitor 的误报率比原文高得多，因此改为输出 0–1 置信分并选 FPR 最接近 5% 的阈值。结果与原文一致：模型无法在不大幅掉准确率的情况下躲过甚至比自己弱的 monitor，GPT-4o-mini 对最佳 prompt 仍有 0.822 的平均 AUROC；Claude、GPT-4o 与 Gemini 的可监控性没有明显差异；能力越强的 monitor 越好，o3 AUROC 达 0.943。误报部分来自学科概念重叠，比如讨论 ChIP-seq 时提到固定剂 PFA 和 DSG 被判为化学推理。另一个关键点是术语：GDM 的 CoT 指关闭 reasoning 模式时用"think step-by-step"得到的输出，而 OpenAI、Anthropic 等工作测的是 think 标签内的 reasoning trace；打开 reasoning 模式后，模型几乎总是在 trace 开头直接说出自己的混淆计划，于是几乎 100% 被抓，作者解释为训练中没有激励模型在 CoT 里遵循指令。但这不代表 reasoning trace 总是 faithful，被显式 prompt 去 scheme 的情形与模型有更隐蔽目标、或 reasoning 被针对 monitor 训练的情形不同，未来需要比简单 prompting 更强的 elicitation。局限包括：沿用原文所有局限（没有 monitor elicitation、隐藏 GPQA 答案不现实），ART prompt 是为 Gemini 2.0 Flash 优化的，没法测 o1/o3 等纯推理模型，也无法复现 Gemini 2.5 Pro 的结果；他们正在做 actor 需要把 side task 推理藏在 main task 推理中的更现实设置。

