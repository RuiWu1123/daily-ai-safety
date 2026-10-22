---
title: "Transformer Circuit Faithfulness Metrics are not Robust"
lab:
  - "FAR.AI"
date: 2024-07-10
source: "FAR.AI Publications"
url: https://www.far.ai/research/transformer-circuit-faithfulness-metrics-are-not-robust
tags:
  - 可解释性
  - 评估方法
---

# Transformer Circuit Faithfulness Metrics are not Robust

**来源**：FAR.AI Publications · 2024-07-10 · [原文](https://www.far.ai/research/transformer-circuit-faithfulness-metrics-are-not-robust)

## 简读

mechanistic interpretability 常用 faithfulness 衡量 circuit 的好坏：ablate 掉 circuit 以外的部分后，模型还能保留多少原来的表现。这篇 COLM 2024 论文（Joseph Miller、Bilal Chughtai、William Saunders）发现这个指标很不稳。作者把 ablation 方法归纳成六个选择：图的粒度、ablate 的组件类型（node、edge、branch）、替换值（zero、noise、resample、mean）、token 位置、方向（破坏 clean 信号还是恢复 clean 信号），以及 ablate 的是 circuit 本身还是它的补集。他们梳理的 7 篇代表性工作两两之间至少有一项不同。主案例是 GPT-2 的 IOI circuit：原论文用 node 级 mean ablation、只 ablate 指定 token，得到 87%；但这个 circuit 是按 edge 定义的，换成 edge 级 ablation 后分数大幅升高，最贴合原假设的设置中位数远超 100%；用 resample 代替 mean 会系统性偏低，ablate 全部 token 也更低。BABA 模板的分数一贯高于 ABBA；mean ablation 的数据集越大分数越高；先平均再算百分比和先算百分比再平均差别很大。即使方法固定，单条 prompt 的分数也分散得厉害，IQR 达 50%，极端值高达数万个百分点，所以 circuit 只在平均意义上忠实，作者建议同时看最坏情况。第二部分用 Tracr 编译的小模型（ground truth 已知）说明：一条只传位置编码的边，在 resample ablation 下不需要，在 zero ablation 下必须保留。Conmy et al. 以 zero ablation 的版本作为 ground truth，所以 ACDC、SP、HISP 看起来没能完全找回；换成和这些算法一致的 resample 版本后，三者都能完美恢复。结论是只给一组 prompt 时“最优 circuit”没有定义，ablation 方法本身决定了 circuit 要完成什么任务，用与 ground truth 的重合度评估自动方法可能误导。作者建议精确报告实验流程，并开源了 AutoCircuit 库。

## 我的笔记

