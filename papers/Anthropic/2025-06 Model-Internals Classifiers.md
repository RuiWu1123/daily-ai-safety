---
title: "Model-Internals Classifiers"
lab:
  - "Anthropic"
date: 2025-06
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/cheap-monitors/
star: false
tags:
  - 越狱与鲁棒性
  - 可解释性
---

# Model-Internals Classifiers

**来源**：Anthropic Alignment Science Blog · 2025-06 · [原文](https://alignment.anthropic.com/2025/cheap-monitors/)

## 简读

Constitutional Classifiers 用单独训练的模型过滤危险输入，能提高 jailbreak 鲁棒性，但开销不小，例如用 Claude 3.5 Haiku 给 Claude 3.5 Sonnet 当安全过滤器会让推理成本增加约 25%。这篇工作探索复用被保护模型自己已经算好的表示来做 jailbreak 检测，集中在 prompt classifier（输入 token 占绝大部分，而且和 policy model 看到的文本相同，便于共享计算），任务是识别试图获取生物武器信息的输入。训练数据是 Constitutional Classifiers 早期版本的约 7 万条合成 prompt（有害/无害各半，带 jailbreak 模板、多语言、cipher、prefill 等 transformation），测试集包括约 4,000 条经已见和未见 transformation 处理的有害问题、2,500 条当时红队攻击 Claude 3.5 系列成功的输入，以及 WildChat 和 OR-bench Hard 作为无害集；指标是 FPR 在 1e-3 到 1e-1 之间的 log-space AUROC，强调低 FPR 下的表现。比较的方法有：1. linear probe，包括对全序列取均值的 mean probe、逐 token 打分后做指数移动平均的 EMA probe（解决长输入中有害内容占比小、信号被稀释的问题）、在末尾附加一段询问是否含有害生物信息的 suffix 后在固定位置取激活的 suffix probe；2. 只重训 policy model 最后若干层（1、2、4……到一半）的 partially-trained classifier；3. 两阶段级联，先用便宜分类器筛掉几乎肯定安全的输入，剩下的交给最贵的 XL 分类器。baseline 是 Claude 3 Sonnet 家族中不同规模（相对开销约 25%、9%、2%、0.6%）专门微调的分类器和直接 prompt XL 模型。由于商业原因无法公开架构，成本数字是示意性的。结果：只重训最后一层（一个 attention+MLP block）的效果仅次于全模型微调，相当于 1/4 规模的专用分类器，总开销约 4%（含 suffix）；EMA probe 几乎零成本，表现优于 2% 规模的专用分类器，相当于插值出的 3% 开销分类器；suffix probe 略好但更贵；mean probe 比最小模型还差。重训更多层没有明显收益。一个有意思的现象是 partially-trained classifier 的验证集 loss 明显偏高，但 OOD 测试表现很好，作者认为基于大模型带来了训练分布看不出的泛化优势。两阶段设置中 EMA probe 和单层重训模型作为第一阶段最好，能把成本降低 10 倍以上而整体性能基本不降，要求开销低于 5% 时 EMA probe 最优，有时级联甚至略优于单用最强分类器，作者归因于两者误差不相关。关键局限：没有做针对这些分类器的 adaptive 红队测试，评估中的红队攻击是针对其它模型、并不知道这些检测方法的，probe 嵌在被攻击的模型里，在直接攻击下的相对鲁棒性可能更差；级联也可能带来新攻击面（只要骗过第一阶段，强模型就看不到）；小模型 baseline 训练数据量与参数量成比例，若更彻底地过度训练或做 distillation，小模型可能更有竞争力。

