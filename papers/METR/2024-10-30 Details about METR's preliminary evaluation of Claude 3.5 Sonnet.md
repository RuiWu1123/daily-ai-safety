---
title: "Details about METR's preliminary evaluation of Claude 3.5 Sonnet"
lab:
  - "METR"
date: 2024-10-30
source: "METR Research"
url: https://metr.org/evaluations/claude-3-5-sonnet-report/
star: false
tags:
  - 危险能力评估
---

# Details about METR's preliminary evaluation of Claude 3.5 Sonnet

**来源**：METR Research · 2024-10-30 · [原文](https://metr.org/evaluations/claude-3-5-sonnet-report/)

## 简读

这是 METR 对原版 Claude 3.5 Sonnet（2024 年 6 月的 claude-3-5-sonnet-20240620，不是 10 月的新版）的初步评估细节，覆盖 general autonomy 和 AI R&D 两套任务。方法沿用之前的做法：用一个基础 scaffold（Python/Bash 工具、简单的上下文截断、告知剩余 token 预算，无任务特定 prompt）把模型变成 agent，在虚拟环境里完成任务并打 0–1 分。general autonomy 是 30 个任务族共 77 个任务（如 CTF、逆向密码、修小型库的 bug、搭 web server、SPN 密码分析、avoid_shutdown 等），每个跑 10 次，不给部分分；AI R&D 是后来成为 RE-Bench 的 7 个任务，每个跑 5 次，为节省时间只给 2 小时，scaffold 上允许改命令超时、提醒可以后台运行并检查内存。人类基线方面，general autonomy 有 22 个任务（29%）只有研究员估计，其余来自外部/内部 QA 和正式 baseline，取最短用时；AI R&D 有约 30 名有专业 ML 经验的专家做的 44 次尝试，8 小时后归一化平均分 0.7，89% 有进展。结果：general autonomy 上 agent 完成约 40% 的任务，相当于人类 baseliner 约 35 分钟能完成的水平，成功时成本远低于人类（例如修 ORM 库的 bug 用了约 38.2 万 token、不到 2 美元，人类花了两个多小时）；AI R&D 上 3/7 的任务（优化 kernel、GPT-2 Chat RL、Rust codecontests scaffold）有实质进展，2 小时预算下平均表现与同等时间的人类专业 ML 工程师相当，最佳方案有时胜过较弱的人类方案，但远不如 8 小时的人类，其余 4 个任务没有一次超过起始方案。agent 不像人类那样先花时间理解任务、做计划，而是直接写代码，几分钟内就有提升但很快平台化，作者预计给 8 小时也差不多。定性上，模型能用代码辅助推理、遇阻会换方法（比如分类器效果差时从 KNN 换成决策树）；常见失败是不验证就提交（逆向密码时找到片段不运行可执行文件就交）、tokenization 导致的字符级推理错误、超出任务范围改代码把原本通过的测试改坏。对 95 次失败的 general autonomy 运行做 key mistake 分类：60 次反映真实能力限制，30 次是少量 elicitation 就能修的偶发错误，5 次可通过任务特定 scaffold 修；按类型看 50 次是推理错误，12 次放弃，7 次不检查，7 次代码错，7 次心算错。为验证偶发失败确实可修，他们对 12 次运行做人工 patch（遇到放弃、不检查、工具选错、重复动作时重采样，必要时加一句通用提示），7/12 转为成功，放弃类最好修、重复行为类基本修不好，据此估计系统修复可让未加权失败率降约 18 个百分点。AI R&D 的失败难以定位到单点，是多种因素混合。局限：人类基线数据少且方差大，elicitation 很有限（没怎么迭代 scaffold、不能微调），任务都可自动打分、比现实更干净，4 小时以上的任务也偏少。

