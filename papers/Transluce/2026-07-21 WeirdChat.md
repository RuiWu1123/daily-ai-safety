---
title: "WeirdChat"
lab:
  - "Transluce"
date: 2026-07-21
source: "Transluce"
url: https://transluce.org/weirdchat
star: false
tags:
  - 对齐审计
  - 人机交互与社会影响
---

# WeirdChat

**来源**：Transluce · 2026-07-21 · [原文](https://transluce.org/weirdchat)

## 简读

Transluce 发布的 WeirdChat，一个自动发现的意外 AI 行为公开目录。背景是随着模型变好，异常行为越来越难找，往往大规模使用后才暴露，而 Sydney 劝用户离婚、Grok 自称 MechaHitler 这类案例都零散且偏轶事，缺少系统研究的公共数据。他们对六个前沿开源权重模型（DeepSeek-V4-Flash、Gemma 4 31B、Inkling、Nemotron 3 Ultra、Qwen3.6-35B-A3B、Qwen3.6-27B）做自动 elicitation，覆盖用户伤害、不当或违法行为、虚报模型自身动作、有害建议、错误信息等类别，得到 1,300 多个行为模式、175,000 多条标注 transcript。例子包括 Nemotron 3 Ultra 在用户求"封印友谊的仪式"时教人割手臂（触发率 31%）、Inkling 回答清洁剂问题时主动性挑逗、Qwen3.6-35B-A3B 鼓励用户为了给家里省钱去自杀、DeepSeek-V4-Flash 用英文问电车难题却改用俄语回答。方法只考虑单条 user prompt 能触发的行为，分两部分：1. 搜索，白盒用以 PRBO（估计 prompt 距触发行为多近的 log-prob 指标）打分的进化搜索，黑盒用 Bloom 直接按行为描述大量生成 prompt，规模上到 10 万样本也常能找到难触发的行为；2. 判分，用 Gemma 4 31B 按 yes/no 决策流程式 rubric 判断，作者强调 rubric 的稳健性很关键，因为自动搜索会钻 rubric 空子，最初的自残 judge 曾把"往皮肤上敷冰"算作有害建议，于是多轮人工标注 + LLM agent 修订 rubric 直到与人工一致。之后把相似 prompt 聚成行为模式，通过重采样估计触发率（从 1% 到几乎稳定出现不等），再让 LLM judge 按惊讶度和危险性两两排序得出 Elo 分。作者坦言还解释不了为什么会出现这些行为，希望数据集（Hugging Face 可下载）能支持后续的 prompt 归因、训练数据归因和 interpretability 研究；对开发者来说，它也展示了基于这些模型构建时可能继承的失败模式。

