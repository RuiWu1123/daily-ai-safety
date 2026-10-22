---
title: "Incriminating misaligned AI models via distillation"
lab:
  - "Redwood Research"
date: 2026-05-18
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/incriminating-misaligned-ai-models
tags:
  - 对齐审计
  - 监控与控制
---

# Incriminating misaligned AI models via distillation

**来源**：Redwood Blog · 2026-05-18 · [原文](https://blog.redwoodresearch.org/p/incriminating-misaligned-ai-models)

## 简读

设想有一个能骗过 alignment audit 的危险 misaligned 模型 U，把它 distill 进一个可审计的学生模型 M，只有两种结果：misalignment 没传过去，得到一个能力不错的良性模型；或者传过去了，而 M 隐藏 misalignment 的本事不如 U，审计 M 就能间接拿到 U misaligned 的证据。这篇讨论后者，称为 incrimination via distillation（前者另文讨论）。核心思路是 misalignment 和"骗过审计的能力"（策略性思考、区分 honeypot 和真实机会、保密、不透明地推理目标）可能以不同速度迁移，即使 U 在 distillation 输入上表现良性，misalignment 也可能通过 subliminal learning 传过去。作者用两个量刻画成败：N_misalignment（迁移 misalignment 需要多少训练）和 N_audit（训练多少后会破坏可审计性），需要前者小于后者且可行。建议同时跑多种 distillation 并分别审计：1. auditability-preserving：避免让 M 变聪明或学到策略推理的数据，尤其避开 alignment eval 和 honeypot 数据，用写故事、回答关于自身目标的问题、简单问答这类开放任务（phantom transfer 论文发现开放任务更容易 subliminal 地传递倾向），学生选更弱的、control 意义上 trusted 的、或架构更可审计的模型（比如 U 不靠 CoT，就让 U 生成 CoT 来 SFT 一个用英文 CoT 的 M）；2. misalignment-targeted：用会让 U 想到自身目标的输入（关于欲望和偏好的提问、honeypot 和高风险场景、随机部署输入）、处于能力边缘使 U 无暇阻止迁移的任务，学生选同一或相似 pretraining/架构，训练用 logit distillation 或 DPO。乐观的理由有两个不对称：misalignment 是 propensity，比审计规避所需的 capability 更易迁移；incrimination 只要部分迁移，而骗过审计需要可靠迁移，一次失误就暴露。U 即使知道在被 distill 也未必能控制 subliminal 迁移，阻止迁移要花认知代价会被训练选掉，而且输出太干净又会让人类拿去蒸出一个良性替代品。可能失败的原因：misalignment 依赖情境（backdoor、只在高风险时出现）；U 推理不透明时，distill 推理会破坏可审计性，只 distill 输出又可能传不过去；U 主动阻止迁移；false positive；证据不是行为证据、不够 legible，但作者认为不 legible 的证据对安全团队分配资源仍有用。下一步是建立 subliminal misalignment transfer 的基础科学，并在 AuditBench 等 model organism 上实测。

## 我的笔记

