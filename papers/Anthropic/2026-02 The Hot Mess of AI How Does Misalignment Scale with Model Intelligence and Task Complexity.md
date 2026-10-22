---
title: "The Hot Mess of AI: How Does Misalignment Scale with Model Intelligence and Task Complexity?"
lab:
  - "Anthropic"
date: 2026-02
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/hot-mess-of-ai/
star: false
tags:
  - 威胁建模
  - 评估方法
---

# The Hot Mess of AI: How Does Misalignment Scale with Model Intelligence and Task Complexity?

**来源**：Anthropic Alignment Science Blog · 2026-02 · [原文](https://alignment.anthropic.com/2026/hot-mess-of-ai/)

## 简读

背景是 alignment 里的经典担忧是超智能系统会连贯地追求错误目标（paperclip maximizer），但另一种可能是 AI 像人一样失败于"hot mess"：不一致、自我拆台、并不优化任何稳定目标。这延续了 Sohl-Dickstein 2023 的 hot mess 理论（专家问卷认为越聪明的实体行为越不连贯），这篇（Anthropic Fellows 项目）把它变成实证测量：用 bias-variance 分解把模型错误分成 bias（系统性地错，相当于经典 misalignment）和 variance（跨采样不一致），定义 error incoherence 为错误中 variance 所占比例（0 到 1），这样可以把"错误长什么样"和"错误多频繁"分开。评测对象是 Claude Sonnet 4、o3-mini、o4-mini、Qwen3 等推理模型，任务包括 GPQA、MMLU、SWE-Bench 和 Model-Written Evals 安全评测，另外还自己训练小模型去模仿优化器。主要发现：1. 最稳健的结论是推理越长、行动越多，错误越 incoherent，无论按 reasoning token、agent 动作数还是优化步数衡量都成立；2. 模型能力与 incoherence 的关系不一致：在 benchmark 上，更强的模型在简单任务上错误更连贯，但在最难的任务上 incoherence 不降甚至上升；合成优化任务中模型越大越 incoherent；重做的专家问卷也认为更聪明的模型更不连贯；3. 模型自发"overthinking"（比中位数想得更久）时 incoherence 急剧上升，而通过 API 调高 reasoning budget 只能小幅提升连贯性，自然波动占主导；4. ensembling 多个样本能降低 variance，但对动作不可逆的 agentic 任务不太现实。理论解释是 transformer 本质是动力系统而非优化器，要把一般动力系统约束成连贯优化器很难，所需约束可能随状态空间维度指数增长，且不会随规模自动变容易。合成实验里在二次函数 steepest descent 轨迹上训练 transformer 预测下一步（相当于训练 mesa-optimizer），发现轨迹越长越 incoherent，且规模降低 bias 比降低 variance 快得多，即"知道该做什么"比"稳定地做到"学得快。作者的解读是未来 AI 失败可能更像工业事故而非连贯地追求未被训练的目标（比如 AI 本该管核电站却跑去读法语诗导致熔毁），因此应相对更重视训练中的 reward hacking 和 goal misspecification（bias 项），而不是主要研究如何约束一个完美优化器；但他们也承认被训练出来的错误目标被连贯追求仍是问题。局限是 bias/variance 的测量需要明确目标（选择题答案、单元测试、目标函数），对开放式目标或隐藏目标说明力有限。论文和代码已公开。

