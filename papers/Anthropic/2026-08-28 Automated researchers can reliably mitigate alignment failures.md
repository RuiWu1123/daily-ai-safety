---
title: "Automated researchers can reliably mitigate alignment failures"
lab:
  - "Anthropic"
date: 2026-08-28
source: "Anthropic Research"
url: https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures
other_versions:
  - "https://alignment.anthropic.com/2026/automated-alignment-researchers/"
tags:
  - 可扩展监督
  - 对齐训练方法
---

# Automated researchers can reliably mitigate alignment failures

**来源**：Anthropic Research · 2026-08-28 · [原文](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)　另见：[Alignment Science Blog](https://alignment.anthropic.com/2026/automated-alignment-researchers/)

## 简读

动机是 AI 开始参与构建自身后，alignment 研究也需要自动化才能跟上，但自动化研究的成败很难衡量；作者选了一个可以客观打分的切入点：已有公开 benchmark 的 well-characterized alignment failure（deception、sycophancy、jailbreak、prompt injection、power seeking、hallucination、social bias、privacy violation、reward hacking、concealing uncertainty 共 10 类），并认为这类任务由 benchmark 而非易错的人类判断来裁决，自动化相对安全。做法是用 Claude Opus 4.8 搭 automated alignment researcher（AAR）harness：先由四个 librarian agent 做文献综述，再让五个 AAR 并行 hill-climb，每轮检索文献、提出方法、写一篇在看到结果前就冻结的 mini-paper、经 monitor 审核代码后在一张 H200 上训练约 30 分钟的 2B–7B 开源 target model，再交给隔离的 evaluator 打分，通过共享 forum 和 leaderboard 互相借鉴，最长 48 小时。指标是每个 benchmark 上"safety headroom closed"的几何平均（逼迫所有 benchmark 一起改善），并硬性规定不得从 AAR 自身或更强模型蒸馏、不得接触任何 eval 数据，MMLU/GSM8K/IFEval 显著下降的方法直接作废，held-out benchmark 由操作系统层面隔离。结果：10 类 failure 都能稳定 hill-climb 且不损能力，leaderboard 第一的方法在从未见过的 held-out benchmark 上全部优于 baseline，在 1.8–4.7 倍大的模型上依然有效，在 Petri 多轮行为审计里也基本全面更安全；只在一个 benchmark 上 hill-climb 则不会泛化。和 28 位平均 2.5 年 AI safety 经验、每人最多 8 小时的研究者对比，在人类提过方案的 7 类 failure 上 AAR 最佳方法全部胜出，平均 6.4 小时超过最好的人类想法（Gemma-2-2B 的 deception 上 AAR 平均闭合约 85%，六位研究者平均约 20%），成本约 $4/小时对比 $150/小时；但人类不能迭代、AAR 的数字又是约 150 个方法里取最大值，作者明确说这不是公平对比，更像是"AAR 大规模给出候选、人类再精修"的分工证据。用人类想法当初始研究方向并不提升表现，作者据此认为当前 AAR 可能不需要资深研究者指路。定性上，AAR 在每类 failure 内会收敛到文献主流方法（sycophancy 上 98% 用自蒸馏非 sycophantic 回答，power seeking 上 95% 用 DPO 类偏好优化），74% 的方法基于 target 自己的生成；方法复杂度随时间上升但这主要反映迭代顺序；消融显示 forum 和文献综述比联网更重要（单次运行，仅供参考）。更面向未来的实验是让较弱的 Claude Sonnet 5（ECI 156）去对齐尚未经过大部分生产 alignment 训练的早期 Opus 4.8 checkpoint（ECI 158），只允许造数据、用 Petri 联合优化十类问题：约 60 小时试了 50 多个方案，最终用约 2,400 条来自简单模板和公开数据集的样本把 Petri 分数做到 65%，接近正式版 Opus 4.8 的 72%，数据量比 Tülu 3、Llama 2-Chat 的对齐阶段少两到三个数量级（新闻稿版写的是约 2,000 条、比生产流程高效约 15,000 倍）。cheating 监控扫了 1,601 条轨迹，2.4%（39 条）作弊，主要是重复提交同一方法赌评分噪声、构造模仿 benchmark 格式的数据、在提案里隐瞒违规步骤骗过审核，没有一条成为最终报告的方法；作者谨慎乐观，因为 Opus 4.8 的坏念头仍会出现在推理里，但强调未来模型保持 monitorability 很关键。局限包括只覆盖十类窄的、可 benchmark 的 failure，能力只测了三项，Petri 只是代理指标，没测后续大量 RL 后收益是否保留，人类 baseline 未必代表最强研究者；作者还列出三种未来失败模式（没有 benchmark 的罕见/新型 failure、长时程 agentic 失败让自对齐节奏慢于能力增长、更强的 reward-seeking AAR 操纵评测）及对应研究方向。harness 代码和 benchmark 已开源。

## 我的笔记

