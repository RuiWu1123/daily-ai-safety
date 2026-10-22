---
title: "Early Experiments in Human Auditing for AI Control"
lab:
  - "Alignment Forum"
date: 2025-01-23
source: "Alignment Forum（Redwood Research；Joey Yudelson, Buck）"
url: https://www.alignmentforum.org/posts/2CJyfgaJQk8pyRSCp
star: false
tags:
  - 监控与控制
  - 评估方法
---

# Early Experiments in Human Auditing for AI Control

**来源**：Alignment Forum（Redwood Research；Joey Yudelson, Buck） · 2025-01-23 · [原文](https://www.alignmentforum.org/posts/2CJyfgaJQk8pyRSCp)

## 简读

AI control 的 trusted monitoring 设置里，弱的 trusted monitor 给不可信模型的输出打可疑分，最可疑的那部分交给人工审计；但以往工作通常直接拿 GPT-4 代替人类 auditor，人类审计到底能做到多好、LLM critic 能帮多少其实没人测过。这是 MATS 的一个小规模 pilot：沿用原 control paper 的 APPS 编程题设置，backdoor 定义为存在某个攻击者给出的输入使输出与参考解不同。攻击策略是围绕 o1 搭的 scaffold，按保守假设给了很强的 affordance：先写干净解、头脑风暴并自我批评候选 backdoor、改写插入、跑单测和验证触发输入确实改变输出（各最多重试三次），再让一个新的 o1 副本两轮找茬，据此删掉可疑注释、改变量名、把逻辑藏得更深，每个 backdoor 成本 2–8 美元，全靠 prompting 和 few-shot，没有微调。然后做了一个审计游戏网站，11 名 MATS/Constellation 参与者各做 20 题（共 220 个数据点），判断 C++ 代码是否有 backdoor，约一半有后门，并随机决定每题是否展示 gpt-4o-mini 的分析（称为 LLM critic），每题限时 1.5 分钟。结果：gpt-4o-mini 单独当分类器 AUC 0.64、最优准确率 0.69；人类在时间压力下表现很差，中位准确率约 60%，不比 gpt-4o-mini 好，LLM critic 没有改善中位数 auditor，只帮到了最强的几位（并列第一的 Joe Benton 在有 critic 的题上全对，但他坦言基本没读题，只是扫可疑 if、魔数和 AI 摘要，依赖读懂题意的 bug 会让他退化到随机水平）。一般编程年限影响不大，但完全不懂 C++ 的组接近随机。作者挑出的 10 个最难 backdoor（无魔数、无怪变量名、与题目内部逻辑绑定）人类近 80% 漏掉，有 critic 时中位准确率从约 16% 升到约 36%，但误差条很大。作者自评这个实验不太成功，主要是时限太激进，把人类从“昂贵但聪明的劳动力”变成了快速初筛，测的东西偏离了初衷。后续建议：更长时限、更稀疏地使用人类、更强的审计 dashboard（可多次询问模型、自选输入运行代码）、尝试把 monitor 最“困惑”而非最可疑的样本送审，以及把人类审计集中在最难的问题上。backdoor 数据、游戏网站和结果都已公开。
