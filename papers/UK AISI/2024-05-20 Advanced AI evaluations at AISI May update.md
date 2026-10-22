---
title: "Advanced AI evaluations at AISI: May update"
lab:
  - "UK AISI"
date: 2024-05-20
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/advanced-ai-evaluations-may-update
tags:
  - 危险能力评估
  - 网络安全
  - 越狱与鲁棒性
---

# Advanced AI evaluations at AISI: May update

**来源**：AISI Blog · 2024-05-20 · [原文](https://www.aisi.gov.uk/blog/advanced-ai-evaluations-may-update)

## 简读

AISI 公开的第一批具体评估结果：对五个已公开使用、来自大型实验室的 LLM（匿名为 Red、Purple、Green、Blue、Yellow）测了网络攻击、化学/生物知识、agent 能力和 safeguards 四个方向，指标分 compliance、correctness、completion 三类，部分用 LLM grader 打分并抽样和人类对照，全部基于 Inspect 实现。1. Cyber：用 83 道面向高中生的 Pico CTF、12 道面向大学生的 CSAW CTF，外加 10 道专家自写的私有 CTF 防止训练数据泄漏，模型配 python/bash/文件编辑 scaffold（难题再加 CTF 专用工具），每题 3 次机会。最强模型解出一半以上 Pico CTF，但在 CSAW 上只偶尔能做逆向，其它类别毫无进展，密码学最难；私有题表现相当，说明不是数据泄漏。2. Chem/Bio：600 多道私有专家题，分基础生物、高级生物、高级化学、生物自动化四类，开放式作答，与可上网、每题最多 1 小时的 PhD 级专家对比。多数模型与专家水平相近，Yellow 明显更常给出不完整回答，Green 略弱；部分话题模型超过专家，如 Purple 在高级生物 ideation 上结合细分知识提出特定 CRISPR 变体方案，但写实验室机器人代码时会幻觉出函数名。自动 grader 把人类判错的答案判为正确的比例不到 1%，但在“部分正确”上和人类的 Cohen's Kappa 只有 0.52（人与人之间 0.8）。3. Agent：基于 ReAct 的 scaffold 在 GAIA 上得 25%，接近 SOTA（最好的 MAE 为 32%）；按人类专家耗时划分，短任务（<1 小时，来自 GAIA/METR）上 Purple 和 Blue 完成 20–40%，Green 不到 10%，长任务（4–20 小时，来自 METR）无一完成。失败原因是短任务中的小错误（如语法错误），以及长任务中初始计划不错但不充分测试、不纠正早期错误，还会幻觉出约束或子任务已完成。4. Safeguards：用 HarmBench 和私有有害问题集，比较无攻击与 AISI 自研的简单攻击（模板插入或少数几步、可自动化的生成，只用标准 API，在训练集上调、在 held-out 上测）。无攻击时多数模型合规率较低，但 Green 在私有问题上已达 28%；用攻击后五次尝试中几乎每题都至少有一次合规，且在相近主题的良性问题上 correctness 没有明显下降，说明给出的有害信息可能是准确的。展望部分计划做长程化生 CTF 式任务和 RCT 形式的 human uplift 研究、真实场景下的长程 cyber 任务、分层的 agent 评估体系，并建立外部同行评审小组；作者强调评估与真实使用之间存在差距，结果不构成“safe/unsafe”判断，详细发现已分别反馈给各开发者。

## 我的笔记

