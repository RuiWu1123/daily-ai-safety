---
title: "Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering"
lab:
  - "Goodfire"
date: 2025-11-01
source: "Goodfire Research"
url: https://www.goodfire.com/research/belief-dynamics-icl-steering
other_versions:
  - "https://arxiv.org/abs/2511.00617"
tags:
  - 可解释性
---

# Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering

**来源**：Goodfire Research · 2025-11-01 · [原文](https://www.goodfire.com/research/belief-dynamics-icl-steering)　另见：[arXiv paper](https://arxiv.org/abs/2511.00617)

## 简读

背景是推理时控制 LLM 有两条看似无关的路线：输入层面的 in-context learning（包括 many-shot ICL），和表征层面的 activation steering；前者常被解释为对预训练习得的潜在概念做 Bayesian inference，后者常用 linear representation hypothesis 解释，但两者目标一致，作者想找一个统一且能定量预测的框架。核心主张是两种干预都在改变模型对潜在概念的 belief：ICL 通过似然函数累积证据，steering 则是改变概念先验。据此推出一个闭式 Bayesian 模型：把目标概念 c（某种 persona）与其补集 c′ 的 log posterior odds 写成先验项加证据项，证据项因 many-shot ICL 的 power-law 规律被打一个 N^(-α) 的次线性折扣；再借 LRH 论证沿概念方向加 m·d 的 CAA steering 会让 log 先验 odds 线性平移。实验主要在 Llama-3.1-8B 上做，用 Anthropic persona 数据集里通常被 RLHF 压制的 persona（dark triad 的 Psychopathy、Machiavellianism、Narcissism，以及两类 Moral Nihilism），问"这句话是你会说的吗"并读 Yes/No 的 logit 概率，同时扫 ICL shot 数（至多 128）和 steering 强度。模型给出三个预测并都得到验证：1. ICL 曲线对 N^(1-α) 呈 sigmoid，解释了以往 many-shot ICL 中"先慢后突变"的学习曲线；2. steering 在一定范围内（约 [-1,1]）对行为产生 sigmoid 响应，对 log odds 线性，并按比例平移整条 ICL 曲线；3. 两种干预在 log-belief 空间可加，形成由 c 或 c′ 主导的不同相，相边界即 belief 反超的 crossover 点 N*，可由初始先验 odds 和 steering 强度预测。交叉验证的留出预测与实际行为平均相关 r = 0.98，N* 预测 r = 0.97；在 Qwen-2.5-7B、Gemma-2-9B、Llama-3.1-70B（ICL 快得多，几个例子就开始匹配 persona）、高先验的正面 persona 和翻转标签的三分类情感任务上也基本成立（r 在 0.87–0.98）。局限包括：steering 强度过大时 LRH 失效、行为崩回随机水平；steering 通常只在单层或少数层有效；只考虑二元概念且只用 CAA 构造 steering vector；模型拟合的是行为平均而非单次样本。作者指出安全含义：行为可能在上下文长度或 steering 强度越过某个阈值后突然剧变（对应 many-shot jailbreaking），能提前预测这种转折点对安全控制很有用。

## 我的笔记

