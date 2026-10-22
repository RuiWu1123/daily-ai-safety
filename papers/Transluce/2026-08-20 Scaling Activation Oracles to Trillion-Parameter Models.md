---
title: "Scaling Activation Oracles to Trillion-Parameter Models"
lab:
  - "Transluce"
date: 2026-08-20
source: "Transluce"
url: https://transluce.org/scaling-activation-oracles
tags:
  - 可解释性
  - 对齐审计
  - 评估感知
---

# Scaling Activation Oracles to Trillion-Parameter Models

**来源**：Transluce · 2026-08-20 · [原文](https://transluce.org/scaling-activation-oracles)

## 简读

Transluce Oversight Foundations 系列的进展报告，把 activation oracle（读取 subject model 内部激活来回答关于它的问题的模型）扩展到万亿参数规模。动机是 reward hacking、evaluation awareness 这类行为单看输出很难发现。架构上 oracle 与 subject model 同构、同初始化，不同于以往只读中间层再注入 oracle 第 1 层，他们读所有层的 residual stream 并 patch 到 oracle 对应层，省去选层。subject model 包括 Qwen3-8B/14B/32B、Qwen3.6-27B、GLM-4.5（358B MoE）和 Kimi-K2.6（1.1T，INT4）。训练数据混合 user modeling（SynthSys）、FineWeb 自监督上下文预测，以及新提出的 continuation prediction：预测模型未来回答（不推理、推理后、下一个推理步）的性质和分布，作者认为它比以往数据更不容易被 text inversion 钻空子；用 LoRA 训练。新评估分两族：预测类（下一个词、续写性质、language switching、是否会 verbalize evaluation awareness）和识别类（不确定性、steering vector 对应概念、长 transcript 里是否 reward hacking），另加 AOBench。主要发现：1. 更大、更强的模型做 oracle 更好，Qwen3.6-27B 比 Qwen3-32B 好，说明整体能力很关键；2. 数据多样性重要，GLM 和 Kimi 没训下一推理步数据，这项就明显差，三类续写数据混在一起还会相互干扰，很少超过只用对应单类的配比；3. 在 next-word、language switching、不确定性、steering vector 等分布外任务上性能随训练上升，但 eval awareness 训得越久越差，reward hacking 只有 Kimi 随训练提升，作者解释为读取窗口没覆盖到关键位置（如只读最后一次代码修改）。在 Qwen3.6-27B 上平均胜过 introspection、读全文的 third-person（含 GPT-5.6 Luna）和无激活对照，最弱在 eval awareness 和 reward hacking。与以往 Qwen3-8B checkpoint 相比，在自家评估上更好，在 AOBench 上居中（Better AO 用了约 7 倍 token），作者强调这只是确认大体有竞争力的 sanity check，不是受控对比。

## 我的笔记

