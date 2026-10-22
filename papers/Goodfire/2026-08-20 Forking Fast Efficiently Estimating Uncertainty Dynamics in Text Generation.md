---
title: "Forking Fast: Efficiently Estimating Uncertainty Dynamics in Text Generation"
lab:
  - "Goodfire"
date: 2026-08-20
source: "Goodfire Research"
url: https://www.goodfire.com/research/forking-fast
other_versions:
  - "https://arxiv.org/abs/2608.19611"
tags:
  - 可解释性
  - 评估方法
---

# Forking Fast: Efficiently Estimating Uncertainty Dynamics in Text Generation

**来源**：Goodfire Research · 2026-08-20 · [原文](https://www.goodfire.com/research/forking-fast)　另见：[arXiv paper](https://arxiv.org/abs/2608.19611)

## 简读

LLM 推理是随机的，Forking Paths Analysis 这类 resampling 方法在推理链每个位置重采样续写、统计最终答案分布 o_t，从而找出决定答案的 forking point，但分析一条链往往要几百万 token。这篇论文想降低成本，同时回答不确定性动态该用什么统计模型。实验在 tinyMMLU 上做，模型是 Llama-3-8B-Instruct（逐 token）和 DeepSeek-R1-Distill-Llama-8B（逐句），以 S=200 的高样本数据为参考，共约 1.77B token。发现：1. 采样多了之后 o_t 大部分位置是平滑的，只在少数 forking point 突变；独立子集之间的差异随 S 的 log-log 斜率约 −0.49，几乎正好是 multinomial 采样预期的 −1/2，所以低样本时的抖动主要是采样噪声，不是模型对单个 token 敏感；2. 平滑模型先用 PELT change point detection 切出 fork，再在段内用 Gaussian kernel 汇聚邻近计数、参数化 Dirichlet，超参数用同一份数据交叉验证。4-token 间隔下等效样本量提升 5.0×（S=5）到 3.3×（S=30），逐 token 时最高 22.1×；3. 不平滑时加大重采样间隔更划算，但 fork 定位会变差；平滑后调 S 和调间隔落在同一条 Pareto 前沿上，两者结合能把预算降到 1/8，误差只略增。作者总结说重采样的高成本本质上是个建模问题。局限：只测了选择题和两个 8B 模型，rollout 较短；fork 越大优势越小，阈值 0.20 时甚至略差于原始数据；credible interval 覆盖率只有 0.48–0.64，所以只推荐用点估计。代码和 dashboard 已开源。

