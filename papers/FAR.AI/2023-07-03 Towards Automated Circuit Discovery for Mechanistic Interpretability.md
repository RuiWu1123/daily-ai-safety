---
title: "Towards Automated Circuit Discovery for Mechanistic Interpretability"
lab:
  - "FAR.AI"
date: 2023-07-03
source: "FAR.AI Publications"
url: https://www.far.ai/research/towards-automated-circuit-discovery-for-mechanistic-interpretability
tags:
  - 可解释性
---

# Towards Automated Circuit Discovery for Mechanistic Interpretability

**来源**：FAR.AI Publications · 2023-07-03 · [原文](https://www.far.ai/research/towards-automated-circuit-discovery-for-mechanistic-interpretability)

## 简读

IOI、Greater-Than、Docstring 这些 circuit 工作都是靠大量人工 activation patching 做出来的，这是 mechanistic interpretability 扩展到大模型的主要瓶颈。Conmy 等人（NeurIPS 2023，部分在 Redwood REMIX 完成）先把共同流程归纳为三步：选定行为、数据集和度量；确定粒度，把模型表示成计算 DAG；反复 patching，删掉无关组件和连接。论文自动化第三步。ACDC 从输出节点按反向拓扑序遍历，对每个节点的入边逐条用 corrupted 输入的激活替换，若子图与完整模型之间的 KL 增量低于阈值 τ 就永久删除该边，最终得到一个稀疏子图。作为对比，作者把 Subnetwork Probing 和 HISP 改造成同样基于 corrupted 激活、优化 KL 的版本。评估一是把前人人工 circuit 当 ground truth 画边分类的 ROC，二是在 induction 任务上比较边数与 KL 的 Pareto 前沿，并用 reset network 检查方法是否会"找到不存在的 circuit"。结果：ACDC 在 IOI、Greater-Than、tracr-reverse 上 AUC 最高；在 GPT-2 Small 的 Greater-Than 上，它从约 32,000 条边中选出 68 条，全部在前人发现的范围内，5 类组件全部找回；在 induction 任务上，边数超过 20 时 Pareto 前沿基本都是 ACDC；HISP 和 SP 在 reset network 上也能优化出低 KL，更容易出假阳性。作者对局限讲得很坦白：各方法对 corrupted 分布和度量非常敏感（ACDC 在 tracr 任务上用 corrupted 激活表现差，换成 zero patching 则完美恢复）；所有方法都只优化单一指标，会系统性漏掉对性能有害的 negative 组件，如 IOI 中的 negative name mover heads；"ground truth" 本身由人报告（IOI circuit 有 1041 条边），并不完全可靠。另有初步证据显示 ACDC 能辅助新发现，比如 GPT-2 Small 预测性别代词时一条意外的路径。结论是 ACDC 能自动化可解释性工作的一部分，但离全自动还远。代码开源。

## 我的笔记

