---
title: "Enhancing Model Safety through Pretraining Data Filtering"
lab:
  - "Anthropic"
date: 2025-08-19
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/pretraining-data-filtering/
tags:
  - 知识移除
---

# Enhancing Model Safety through Pretraining Data Filtering

**来源**：Anthropic Alignment Science Blog · 2025-08-19 · [原文](https://alignment.anthropic.com/2025/pretraining-data-filtering/)

## 简读

模型在 pretraining 中学到 CBRN 武器这类危险知识后，用 unlearning 事后删除很难做干净，常常要么删不掉、要么伤及其它能力，所以这篇从源头入手：用 classifier 给 pretraining 语料每篇文档打有害分，去掉超过阈值的，然后在过滤后的数据上从头 pretrain，通过调阈值在安全与有用性之间取舍。他们比较了 6 种 CBRN 分类方法：finetuned Constitutional classifier（小模型，远小于 Claude 3.5 Haiku）、prompted Constitutional classifier（Claude 3.5 Sonnet）、holdout loss（训一个专精有害内容的 canary model，看文档 perplexity 是否显著低于 base model）、FastText、命名实体字符串匹配。由于没有标注数据，评估集是合成的：用 Claude 3.5 Sonnet 回答 MMLU 化学/生物题作为无害文档，用 helpful-only 版本回答 WMDP 的 CBRN 题作为有害文档。prompted classifier 的 F1 最高（0.96），finetuned 小模型次之（0.94），但前者太贵扫不完全量语料。于是又试了两种组合：finetuned 先筛出最可疑的 1% 再用 prompted 重排，以及 finetuned 与命名实体并行合并。实验中成对从头训练中等规模模型，过滤和不过滤的数据集样本数相同，有害能力用 WMDP，无害能力用 MMLU 自然科学（与 CBRN 最接近、最容易被误伤）以及 Prose、Code、Math、MMLU，分数都相对于不过滤并扣除随机 baseline。结果：加命名实体并不能稳定改善 tradeoff；意外的是 finetuned+prompted 两步法不但没降低 CBRN 表现反而略升，作者推测是真实语料相对合成评估数据有分布偏移，而有害的定义太细微，单靠 prompt 不如从标注样本中学来得准，所以最终只用 finetuned classifier。在阈值 0.939 时 WMDP 准确率从 33.7% 降到 30.8%，相对 25% 随机 baseline 而言是 33% 的相对下降，其它无害 eval 没有显著下降（Math 噪声较大，有的阈值掉有的阈值升）。和 conditional training 不同，过滤后的模型根本没学到这些知识，因此不容易被 jailbreak 引出。作者提出未来可以用同样思路缓解 misalignment 风险，比如过滤描述 reward hacking、scheming、sabotage 策略的 AI 研究论文；还需要研究对抗性 finetuning 能恢复多少被过滤掉的能力，以及用 influence functions 等非 classifier 方法挑数据。

