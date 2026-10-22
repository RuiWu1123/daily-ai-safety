---
title: "Evidence on AI R&D Progress from NanoGPT"
lab:
  - "METR"
date: 2026-04-21
source: "METR Notes"
url: https://metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/
tags:
  - 危险能力评估
  - 评估方法
---

# Evidence on AI R&D Progress from NanoGPT

**来源**：METR Notes · 2026-04-21 · [原文](https://metr.org/notes/2026-04-21-ai-rd-nanogpt-progress/)

## 简读

Manish Shetty 的 research note，把 NanoGPT speedrun 当作衡量 AI 加速 AI R&D 的一个证据来源：它是小规模 LLM 预训练，有公开的长期贡献历史，可以粗略估计人类投入，agent 也能在可比条件下参赛，其中的 Muon optimizer 已被 Kimi K2、GLM-4.5 等前沿模型采用。局限包括数据污染、只看得到成功的想法（survivorship bias）、124M 参数与前沿规模差别很大，以及预训练只是 AI R&D 栈的一部分。他借助 Claude Code 对 small track 上 2024 年 5 月到 2026 年 3 月的 77 个 record（36 位贡献者，训练时间从 45 分钟降到 1.43 分钟，31x）按 "depth"（breakthrough/deep/moderate/shallow）和 "provenance"（invented/adapted/imported）分类，数据集已公开。发现：1. shallow 和 moderate 的贡献合计带来约 21x，例如迁移到 FlexAttention 就提速 30%；但 deep 的想法贯穿始终，从早期的 Muon 到后期发明的 Paired Head Attention 和 Bigram Hash Embedding；2. 前 20 个 record 主要是引入或改造已有前沿技术（RoPE、ReLU²、QK-norm 等）来追赶，此后 33% 是原创；按累计提速算，imported 贡献 6.7x，adapted 3.0x，invented 1.6x；3. 改进覆盖栈的多个层次，重心从架构转向注意力和并行化，再到 optimizer 和 kernel；4. 2025 年底到 2026 年初有 4 个 record 与 AI agent 共同署名（Hiverge、Locus、Aster、Station，都是专门的 ML 研究 agent 而非通用编码助手），都是真实改进，但都属于 shallow 到 moderate、imported 或 adapted；其中 Station 发现 window_size 参数被编译代码静默忽略，这个 bug 人类几个月都没注意到。作者强调 4 个样本与近期随机抽取的人类贡献差别不大，无法区分"agent 更浅"还是基础比例本来就低，而且不知道人类的引导程度、失败尝试次数和算力花费。这类挑战的价值在于：比较人与 agent 的想法类型、提供有高投入人类基线的任务，以及在远超公开尝试的大算力预算下运行 agent，测量成本曲线。

## 我的笔记

