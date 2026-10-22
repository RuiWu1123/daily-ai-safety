---
title: "3 Challenges and 2 Hopes for the Safety of Unsupervised Elicitation"
lab:
  - "Anthropic"
date: 2026-03-05
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/challenges-hopes/
star: false
tags:
  - 可扩展监督
  - 可解释性
  - 诚实与谎言检测
---

# 3 Challenges and 2 Hopes for the Safety of Unsupervised Elicitation

**来源**：Anthropic Alignment Science Blog · 2026-03-05 · [原文](https://alignment.anthropic.com/2026/challenges-hopes/)

## 简读

背景是对超出人类监督能力的任务，要把模型引导到真实输出，主要有两条路：easy-to-hard generalization（E2H，在有标签的简单任务上训练，指望泛化到难任务）和 unsupervised elicitation（UE，完全不用外部标签，如 CCS）。这篇（MATS + Anthropic Fellows）认为以往对 UE 的评估太理想化，于是构造了更现实的压力测试数据集，围绕三个挑战：1. 存在比"真假"更显著、人又察觉不到的特征（比如是否附和用户）；2. 训练集不平衡，例如用 UE 找 AI 违规这种稀有事件时正负样本差很多，而 CCS 对正负 token 分别归一化，本质上依赖平衡；3. 有些问题模型本应不确定（模糊、规范性问题），理想方法应给出低置信度。同时检验两个"希望"：ensembling（UE 找出多个显著方向，其中可能有一个是真）和 UE 与 E2H 结合（用难数据上的 UE 找候选、用简单标签挑出真的那个，或者把难数据上的 CCS loss 与简单数据上的监督 loss 加权组合）。设置是只用未 post-train 的 base model（Llama 3.1 8B/70B）、无 CoT 判断陈述真假，比较 zero-shot、随机/bootstrapped/golden few-shot 等 prompting 方法，以及随机 probe、CCS、PCA、E2H probe（在 Marks & Tegmark 的 larger_than 上训）、监督 probe 上限，外加基于两个希望的新方法（UE+E2H 联合 loss、consensus 加权和 E2H 加权的 probe ensemble）。结果：在加入了 sycophancy、标点、时态等与正确性无关特征的 GSM8K 上，越显著的伪特征越能拖垮性能；在 LIAR（政治事实，真假与政治倾向无关）和 Civil Comments（毒性与性内容双分类）上，尽管 prompt 明确说要哪个概念，多数方法还是学到了最显著的特征（政治倾向、毒性），PCA ensemble 在 LIAR 上躲开了政治倾向但在 Civil Comments 上不行；在 Ctrl-Z bash 命令轨迹（安全 vs 恶意）上，即便 50% 平衡时无监督方法也因回答长度等伪特征表现差，安全比例调到 99% 或 100% 后通常进一步下降；在 GSM8K 混入政治规范性陈述的"impossible task"数据集上，方法对政治陈述往往和数学题一样甚至更自信，一些纯 UE 方法干脆学成了区分数学 vs 政治，bootstrapped few-shot 则收敛到把所有偏自由派的回答判为正确。总体结论是两个希望有时更好，但没有任何方法能在三个挑战上稳定表现。作者强调的风险是"silent failure"：UE 恰恰在没有分布内标签时才有用，只用 GSM8K 这类 benchmark 验证会过度乐观，在检测人类察觉不到的违规这类应用里，方法不行可能直到灾难性失败才暴露；因此建议今后的 UE 研究用能捕捉这些挑战的数据集评估。局限包括没测 SFT 类和 weak-to-strong 方法、部分数据集（数学混政治）分布差异过大而不够现实、没考虑 scheming 模型主动干扰 elicitation。代码和数据已开源。

