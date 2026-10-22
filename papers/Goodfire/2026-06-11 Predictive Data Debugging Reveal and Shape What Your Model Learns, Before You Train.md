---
title: "Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train"
lab:
  - "Goodfire"
date: 2026-06-11
source: "Goodfire Research"
url: https://www.goodfire.com/research/predictive-data-debugging
tags:
  - 可解释性
  - 对齐训练方法
---

# Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train

**来源**：Goodfire Research · 2026-06-11 · [原文](https://www.goodfire.com/research/predictive-data-debugging)

## 简读

动机是 preference data 实际上在给模型编程，却没法直接读：一般是跑完 DPO 看几个汇总分，掉分了只能猜是 26 万条 pair 里哪些作怪。Goodfire 的 predictive data debugging 在训练前把数据集过一遍已解释的模型，用模型处理每条数据时算出的 concept 去预测训练会把模型推向哪里。他们称这一预测与实际学到的东西 R² = 0.9，能追溯到具体数据簇，再通过改数据或改训练做定向干预。和 embedding 聚类、让 LLM 读数据相比，它是直接测量而不是猜。案例主要用 Dolci（OLMo 的开源 preference 数据集）和 Tulu 3，模型是 Llama-3.1-8B 到 70B：1. DPO 提升了通用能力，却削弱了对有害请求的拒绝，根源是一批用虚构情境包装的 jailbreak，chosen 是顺从；去掉之后安全和性能变成 Pareto 改进；2. 敏感话题上链接变多，但几乎都是幻觉 URL，干预只能部分缓解；3. 整体 sycophancy eval 持平，但对伪深奥的物理问题会谄媚，这类情况很难用 eval 发现，干预也没能完全消除；4. 一个没人会写 eval 的 unknown unknown：一簇"池塘放屁熏死鱼"的同人文，DPO 后模型会热情应答。验证上，人为注入 goblin 让模型约 50% 的回答提到 goblin，pipeline 能找到并消除，同时保留能力提升。作者承认目前识别能力强于修复能力，下一步做可预先验证效果的数据改写，并扩展到 SFT、RLVR 和在线训练，长远目标是从自然语言 spec 反推该训练什么数据。技术已集成进商业平台 Silico，文章推广色彩明显，论文名 Anatomy of Post-Training。

## 我的笔记

