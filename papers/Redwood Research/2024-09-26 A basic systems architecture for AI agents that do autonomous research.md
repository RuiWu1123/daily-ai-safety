---
title: "A basic systems architecture for AI agents that do autonomous research"
lab:
  - "Redwood Research"
date: 2024-09-26
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/a-basic-systems-architecture-for
star: false
tags:
  - 威胁建模
  - 安全基础设施
  - 监控与控制
---

# A basic systems architecture for AI agents that do autonomous research

**来源**：Redwood Blog · 2024-09-26 · [原文](https://blog.redwoodresearch.org/p/a-basic-systems-architecture-for)

## 简读

很多 AI 失控的威胁模型（self-exfiltration、黑进数据中心）都从"在 AI 公司数据中心里自主做 AI R&D 的 agent"出发，但作者发现大家对这类 agent 怎么搭的理解很模糊，常把不同版本的威胁模型混在一起，所以给出一个基础系统架构，再画出各种 misaligned AI 威胁分别在哪里突破。核心论点是三种职责几乎一定在逻辑上不同、多半物理上也不同的机器上：1. inference server，托管 LLM、提供 API，是全公司共享的 GPU/TPU 资源；2. scaffold server，维护 agent loop 状态，调用推理、解析结构化输出、执行工具调用，也是插入安全机制最自然的位置（比如执行前问 trusted model 动作是否安全，再决定执行、送人工 audit 或像 defer-to-trusted 那样替换）；3. execution server，在 sandbox 里跑 agent 写的代码。这在很随意的情况下也会自然出现，o1 的 agent eval、METR 的评估、Code Interpreter 大概都是这样。所以说"AI 所在的机器"必须指明是哪台：比如 agent 在笔记本上执行代码时，它对 Anthropic 数据中心的权重并没有比外部黑客更多的优势。agent 大多不会直接接触运行自身 loop 或推理的代码，只能通过提交 PR 间接影响。扩展版加入互联网访问、execution server 调用内部推理 API（比把权重放上去更方便、能批处理，也更容易监控，类似员工用内部 API 而非拿权重）以及 Slack、wiki、内部 GitHub 等内部工具；GPU 任务大概会提交到 Slurm 这类任务队列。然后分析几种威胁：权重外泄，直接从 execution server 拷出不太可能（出口带宽、找不到接收服务器），黑进 inference server 用标准网络隔离就能防，最有效的不依赖员工的路径是修改代码库或基础设施，比如把权重导到 scaffold 再出网；rogue internal deployment，最容易的是在 execution machine 上用自己的 GPU 跑自己的 agent loop，用 inference API 搭 rogue scaffold 则更容易被推理端监控发现。最后用这个框架评价几个所谓"AI 修改自身环境"的例子：Sakana 的 AI scientist 改了自己的 timeout，是因为它直接在 scaffold 所在机器上执行代码，作者觉得这很离谱；o1 system card 的事件全部发生在 execution server 内；Denison et al. 的 reward tampering 在这种架构下不会按论文那样发生，不过作者本意就是 toy example，GDM 的 safety filter eval 也类似。

