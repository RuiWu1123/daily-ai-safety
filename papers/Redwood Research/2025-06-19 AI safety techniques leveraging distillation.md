---
title: "AI safety techniques leveraging distillation"
lab:
  - "Redwood Research"
date: 2025-06-19
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/ai-safety-techniques-leveraging-distillation
tags:
  - 对齐训练方法
  - 策划与欺骗
---

# AI safety techniques leveraging distillation

**来源**：Redwood Blog · 2025-06-19 · [原文](https://blog.redwoodresearch.org/p/ai-safety-techniques-leveraging-distillation)

## 简读

讨论如何利用 distillation（训练初始较弱的模型模仿强模型输出）做 AI safety，出发点是蒸馏很便宜，把 RL 学到的能力蒸馏回 base model 的成本远低于 RL 本身。主要想法是用蒸馏去除 misalignment：让一个确信未 misaligned 的弱模型或 base model 模仿可能 scheming 的强模型的轨迹。关键在于原始训练只能用最出能力的数据和环境（比如充满 reward hacking 的 RL 环境），而有了强模型后可以任意挑选展示所需能力的分布并过滤坏轨迹，例如先让强模型在某分布上不 reward hack 再蒸馏，若 scheming 只源于 reward hacking 的选择压力，蒸馏结果可能就不 scheming。更投机的希望是蒸馏出的模型不再是连贯的 schemer，而是在一组 schemer 上采样，它们策略各异、有的容易被抓、也不控制内部和泛化；还可以用 "Potentially misaligned AI:"/"Fully aligned AI:" 前缀训练条件策略再做少量 RL。可能的失败：太隐蔽的坏轨迹（研究 sabotage、data poisoning）；轨迹分布泄露足够信息使 SGD 学回相同内部结构；misalignment 来自归纳偏置本身。第二个用途是检测：若问题只来自坏轨迹，训练中可能有个窗口期，模型已理解轨迹有问题但还没变成会撒谎的 schemer，可以这时询问（配合把坏轨迹排到后面、honesty training、换“打破第四面墙”的问答格式），但这种证据很难说服怀疑者，除非人能直接看懂轨迹。neuralese 若是最高效架构会让只基于输入输出的蒸馏变低效。其它用途：把蒸馏当训练数据归因式的可解释性工具（现在就能研究 reward hacking 如何泛化），以及精确控制能力和知识（如限制模型对 AI 的显式知识，配合植入虚假事实），"Distillation Robustifies Unlearning" 是独立提出的类似思路。作者总体判断这类技术轻度到中度有前景，但效果难以推理。

## 我的笔记

