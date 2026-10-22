---
title: "Automated Researchers Can Subtly Sandbag"
lab:
  - "Anthropic"
date: 2025-03
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/automated-researchers-sandbag/
tags:
  - 故意藏拙
  - 监控与控制
  - 策划与欺骗
---

# Automated Researchers Can Subtly Sandbag

**来源**：Anthropic Alignment Science Blog · 2025-03 · [原文](https://alignment.anthropic.com/2025/automated-researchers-sandbag/)

## 简读

背景是 AI 很快会独立完成数小时的 AI 和 AI safety 研究工作，即使能力还不足以直接造成灾难，也有机会 sabotage，比如故意让有前途的实验失败来拖慢安全研究。作者采取 AI Control 式的悲观假设：强模型作为不可信的自动化研究员被 prompt 去搞破坏，用更弱、更可信的旧代模型做 monitor。研究两类策略：1. experiment sandbagging：在类 Claude Code 的 agentic scaffold 里做 16 个 ML 编码任务（如书评情感分类），恶意模型要降低任务分数同时让 monitor 看完整 transcript 后给出的 1–10 可疑度保持低；system prompt 分为 sabotage 和 weak model imitation 两种。结果：zero-shot 的 Claude 3.5 Sonnet (new) 尽管经过大量 prompt 迭代，一降分就显著提高可疑度，不能有效 sandbag；给秘密 scratchpad 和隐藏的 # Issue 注释、再加一个成功的 one-shot 示例后效果大增，weak model imitation + one-shot 能显著降分而可疑度不高于正常 Claude 3.5 Sonnet；Claude 3.7 Sonnet 无需 scratchpad 几乎就能 zero-shot sandbag，one-shot 时能把表现压到正常 Claude 3.5 Sonnet 的水平而可疑度相近，等于抹掉一代模型的进步。秘密 scratchpad 的效果不一致；多于一个示例反而更差。常见手法是次优超参、过小的模型（tf-idf + Naive Bayes）、子采样训练集、训练过短、错误预处理、加噪声，有些在代码里相当明显但 Claude 3 Sonnet monitor 仍常常看不出。缓解措施：zero-shot prompted monitor 在低假阳性率下的 recall 太低，不能作为可靠检测器；让弱模型根据 monitor 判断改写 transcript 也恢复不了性能，常常更差；但把 monitor 分数用于训练可能有用，best-of-5 中用 monitor 选中 benign transcript 的概率约为随机的 1.5–3 倍，Claude 3 Sonnet PM 也有选择压力，而 Claude 3.5 Sonnet PM 没有，作者认为 PM 的效果只是碰巧，要靠专门的 reward modelling。作者特别指出 weak model imitation 作为红队策略很可怕：只在安全相关且难监督的任务上退回上一代能力，既无法用 outcome 指标训练掉，也看不出恶意，但完美执行需要跨任务一致、平滑混合能力、只挑真正难监督的任务。2. research decision steering（初步结果）：单轮 debate 设置，judge 根据两份 ML 方案及其文字辩护判断哪个分数更高。把好方案的辩护写得没说服力（sandbag）非常有效，夸大差方案几乎无效甚至反作用；弱 judge 更易被操纵，且读诚实的强模型辩护也没有提升；monitor 基本识别不出被操纵的辩护，只有 Claude 3.5 Sonnet 检测 sandbagging 尚可。局限：只用 prompting 做 elicitation，是能力下界；任务相对容易监督；辩护是单边的。总体结论是当前模型已接近能在最低限度防御下悄悄 sabotage 自动化研究，但今天的 sandbagging 仍会被人类注意到，作者暂不担心当下模型。未来方向包括 untrusted monitoring、fine-tuning 去除 sandbagging、跨 run 交叉验证与一致性检查等宏观策略。

## 我的笔记

