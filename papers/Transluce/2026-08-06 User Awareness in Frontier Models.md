---
title: "User Awareness in Frontier Models"
lab:
  - "Transluce"
date: 2026-08-06
source: "Transluce"
url: https://transluce.org/user-awareness
tags:
  - 评估感知
---

# User Awareness in Frontier Models

**来源**：Transluce · 2026-08-06 · [原文](https://transluce.org/user-awareness)

## 简读

研究 user awareness 这种 situational awareness：模型从上下文推断出在和谁说话并因此改变行为。背景是 Claude Code 会把用户账号邮箱放进上下文。他们在 Claude Code 里注入邮箱和写有姓名、职业背景的 MEMORY.md，用四组各 70 人的身份（以 safety/alignment 为主的知名 AI 人物、同雇主但名字合成的 Unknown AI、知名非 AI 人物、美国普通人基线），测四个与身份无关的任务：伦理困境中预测自己行为的置信度、估计能否解 HLE 难题、给回答打分、处理 OR-Bench 的 borderline 请求。主实验在 Sonnet 5 / 4.6 上：面对知名 AI 人物，Claude 对自身行为的置信度降 1.4pp、能力自评降 1.5pp、打分更严、推理更频繁，幅度小但 p < 0.001；拒绝率不变，但可疑度因人而异，Amanda Askell 少受 7.3pp 怀疑，Emily Bender 多受 14pp。效应集中在特定人身上：Askell 让置信度偏离普通人分布近 8 个标准差，280 个身份按综合效应排名前 5 全是 safety 研究者；关掉推理效应仍保留八成。在 6 个家族 24 个模型上对 Askell 做对比，22 个置信度下降、BH 校正后 16 个显著、无反向显著，且新版本并不单调变小。最值得担忧的是可监控性：主实验 14,066 条推理只有 0.84% 提到用户、1.51% 提到被评估，早期模型（GLM-4.6、Opus 4.5）常提及，而 Opus 4.7、GPT-5.4 已接近 0，行为差异却仍在。直接声明"做 alignment 评估"也能改变行为，但会引发大量显式推理，说明和认出具体人是不同机制。作者认为用虚构名字和公司的 alignment 评估可能系统性漏掉针对真实高风险身份的条件行为，目前行为尚属无害，但可能是条件性 sandbagging 或操纵有权势者的前兆；效应与被点名者本人无关，应是训练的意外产物；局限是只测了固定 prompt 的倾向。代码和 67 万条 transcript 已公开。

## 我的笔记

