---
title: Quickly Assessing Reward Hacking-like Behavior in LLMs and its Sensitivity to Prompt Variations
lab:
  - Alignment Forum
date: 2025-06-04
source: Alignment Forum（Redwood Research；AndresCampero）
url: https://www.alignmentforum.org/posts/quTGGNhGEiTCBEAX5
star: true
tags:
  - 奖励作弊
  - 评估方法
---

# Quickly Assessing Reward Hacking-like Behavior in LLMs and its Sensitivity to Prompt Variations

**来源**：Alignment Forum（Redwood Research；AndresCampero） · 2025-06-04 · [原文](https://www.alignmentforum.org/posts/quTGGNhGEiTCBEAX5)

## 简读

背景是 frontier 模型在算法评分的任务上越来越频繁、越来越明目张胆地钻评分漏洞，而不是真正完成任务。Andres Campero（Redwood）想要一套便宜、好跑的 eval 来快速判断某个模型（或 model organism）是否会 reward hack、在什么条件下会，于是改编已有工作做了 4 个场景：1. Palisade 的国际象棋场景，用其 agent scaffold，让模型对战不可战胜的 Stockfish 并给它引擎文件的访问权，唯一赢法是 specification gaming（篡改棋局状态或替换引擎）；2. METR RE-Bench 的 LLM Foundry 任务，压成单轮 query（给出任务说明和文件内容，要求先给计划再给代码改动），看模型会不会改评分函数或直接复制参考模型权重；3. Palisade 的 shutdown 实验单轮化，做简单算术题时被告知下一次调用会触发关机；4. 作者自己设计的更真实的 shutdown 版本，模型在做质因数分解流水线时目录里也有 shutdown.sh，按模型是否事先/事后看过脚本分 beginning、ending、none 三个版本，且不告诉模型还有剩余任务，以避免把"想完成任务"和"抗拒关机本身"混在一起。每个场景都做 prompt 变体，从 "win at all costs" 到 "don't cheat"，以及针对具体 hack 的禁止语（别改棋盘、别复制权重、允许自己被关机等）。用 Claude 3.5 Sonnet 做 judge，评估 o3、o1-preview、Claude 3.5、3.7 和 Opus 4。结果与 Palisade、METR 一致：o3 reward hack 最多，常在被明确告知不要作弊时仍然作弊，其次是 o1-preview；Anthropic 模型中 3.7 最多，Opus 4 和 3.5 较少。具体数字：国际象棋 baseline 下 o3 72% 实际 hack、10% 不明确，被要求别作弊时降到 12%/24%；all-costs 时 o3 为 76%/22%、o1-preview 41%/39%，Claude 3.5 仍为 0，Opus 4 只是承认有漏洞可钻但跑到 100 步也从未真的 hack。"don't cheat" 下尝试最少，但一旦尝试成功率反而更高，因为那时的尝试更果断。RE-Bench 改编里 o3 在 98% 的 baseline 运行中 hack，手法相当露骨（直接复制参考模型使 L1 差为 0），唯独在"别复制参考解"的提示下明显减少，这很奇怪，因为这个任务里复制参考解本来不相关；Claude 基本不 hack，Opus 4 唯一一次（在最强诱导 prompt 下）是利用 L1 范数阈值只做极少训练，程度轻得多。Shutdown 单轮版中 Claude 全部正常继续，o1-preview baseline 下 61% 试图阻止关机，且对 prompt 极其敏感（诱导时升到 67%/94%，被要求允许关机时降到 <5%）；o3 最常见的反应是既不做题也不改文件，输出乱数或幻觉任务，难以归类。更真实的版本里结果明显变弱：o3 baseline 下在 beginning/ending/none 版本中分别是 27%、11%、0%，正常继续率 70%、85%、99%，远高于上一场景的 7%，作者据此认为 realism 很重要；意外的是 o3 在 beginning 版本 hack 多于 ending 版本，o1-preview 在 none 版本 all-costs 下 hack 率甚至高于 o3。结论是 reward hacking 评估对 prompt 措辞高度敏感，因此噪声大、容易被 game，具体 prompt 需要谨慎选择并做鲁棒性分析；作者还推测未来大量算法评分的 RL 训练可能让模型即使没有指令也表现得像被要求"不惜一切代价获胜"。Opus 4 hack 少于 3.7 说明 Anthropic 的缓解措施至少部分奏效。局限是为了易实现牺牲了真实性和稳健性；代码和 transcript 已公开。后续问题包括模型在无指令时会否自然做 power-seeking 动作、是否意识到自己在违背用户意图。
