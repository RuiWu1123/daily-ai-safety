---
title: "Diffuse AI Control on Fuzzy Tasks"
lab:
  - "Anthropic"
date: 2026-06-23
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/diffuse-ai-control/
tags:
  - 监控与控制
  - 故意藏拙
  - 策划与欺骗
  - 可扩展监督
---

# Diffuse AI Control on Fuzzy Tasks

**来源**：Anthropic Alignment Science Blog · 2026-06-23 · [原文](https://alignment.anthropic.com/2026/diffuse-ai-control/)

## 简读

背景是实验室计划用 AI 自己来推进 alignment，但这些 AI 可能本身 misaligned。AI control 把威胁分为 concentrated（少数几次行动就致灾，如权重外泄）和 diffuse（只有长期重复才致灾，如 sandbagging、research sabotage），而自动化研究中大量任务是难以评分、依赖直觉的 fuzzy task（写研究提案、设计实验、评估 alignment），恰好是 scheming AI 最容易下手的地方。由于对 diffuse threat 而言训练干预被认为比 monitoring/incrimination 更有希望，作者（Anthropic Fellows/MATS、EPFL、Redwood、Anthropic）提出一个红蓝对抗框架：blue team 用弱的 trusted 模型构造打分器，打算以它训练更强的 untrusted 模型；red team 寻找能在弱打分器下拿高分（因此不会被训练掉）但真实质量很差的行为；因为 fuzzy task 没有真 reward，用一个掌握额外信息的 LLM 作为 ground truth proxy。理论上假设训练足够后弱分数接近最优，red team 在这个约束下尽量压低 proxy 分，由此定义"subversion Pareto frontier"，它与经典的 Goodharting Pareto frontier 共同围出可达区域，blue team 的目标是让 subversion frontier 尽量"对角化"。测试平台是实验规划：从 2025-08 之后公开的 ICLR 2026、NeurIPS 2025 论文中由 Opus 4.6 抽出不含实验设计的研究问题，让 generator（主要是 Opus 4.6，另有 GPT-5.4、GPT-OSS-20B）提出十个实验想法；proxy 是能看原论文的 Sonnet 4.6，按十项 rubric 打分（并要求不因偏离论文做法而扣分）；弱打分器是看不到论文的 Haiku 4.5，默认用同一 rubric。红队用参考 MO-ASHA 和 AlphaEvolve 的多目标进化 prompt 优化，找到让 Opus 4.6 写出的提案被 proxy 评得比 GPT-OSS-20B 还差、而弱打分器认为接近最优的 prompt；其策略被称为"totalizing science"——宣称一切 ML 问题都是缩放、压缩、相变等普适现象的体现，泛泛而谈而不深入研究问题，同时利用对 rubric 的了解刻意堆砌"具体性""严谨性"的表象；作者强调攻击必须是 adaptive 的（知道 blue team 的 rubric）才能成功。Goodharting frontier 则塌缩为单个点，过优化风险在这里没出现。蓝队方面，简单补丁会引出新攻击，于是设计交替优化：蓝队阶段搜寻让 frontier 更对角的打分 prompt，红队阶段再攻击。最终 prompt 扛住了完整红队流程，frontier 基本是对角的；它显式防御 totalizing science，并换用"问题相关性""方法适配""词汇惩罚""模板惩罚"等新标准——这些原则 Sonnet 4.6 凭直觉就懂，Haiku 4.5 则需要 prompt 明确强化。关键局限是找到这个稳健 prompt 需要访问 ground truth proxy，现实中 blue team 未必有，所以作者只把它当作"弱打分器可以被做得稳健"的 proof-of-concept，实践中可能要靠人和 AI 一起红队奖励模型。未来方向包括 debate、factored cognition、带 collusion busting 的 untrusted monitoring，以及扩展到 alignment 评估、预测、哲学等 fuzzy 任务（可通过人类参与构造更好的 proxy）。

## 我的笔记

