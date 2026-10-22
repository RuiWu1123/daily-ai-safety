---
title: "Few-shot Adaptation Works with UnpredicTable Data"
lab:
  - "FAR.AI"
date: 2022-08-07
source: "FAR.AI Publications"
url: https://www.far.ai/research/few-shot-adaptation-works-with-unpredictable-data
tags:
  - 对齐训练方法
---

# Few-shot Adaptation Works with UnpredicTable Data

**来源**：FAR.AI Publications · 2022-08-07 · [原文](https://www.far.ai/research/few-shot-adaptation-works-with-unpredictable-data)

## 简读

此前 multi-task / MetaICL 类工作发现训练任务越多越多样，few-shot learning（FSL）泛化越好，作者想把这一点推到极端。做法是把网页表格自动转成 FSL 任务：关系表的每一行是一个样本，选一列做输出、其余列加列名前缀做输入。从 WDC Web Table Corpus 过滤后得到 UnpredicTable：413,299 个任务，来自 23,744 个网站，比已有公开数据集大几个数量级，数据和代码开源。用 MetaICL 在 GPT2-large 上微调 UnpredicTable-5k，52 个 NLP 测试任务全面提升，整体与在人工整理的 NLP 数据集上训练相当，但提升远不及数据规模所暗示的。消融结果很反直觉：1. 任务数超过 40 基本没用，超过 5000 还会变差；2. 每网站只取一个任务的"更多样"版本几乎没有区别；3. 窄数据集之间方差很大，最好的反而是窄的，support.google.com 的软件文档平均 +7.5%，超过 40 个人工 NLP 数据集的 +6.7%，前五名里四个是软件相关，游戏 trivia 站点也与 UnpredicTable-5k 持平，维基百科和 QA 站点反而平平；4. 人工标注的高、低质量任务之间差距不到 1%。提升集中在少数测试任务上（20% 的任务贡献 60–80% 的增益，中位数只有约 +3%），且不同训练集提升的是同一批任务，关于网页 cookie 的聚类竟是新闻分类和情感分类的最佳训练集。作者据此认为增益不来自 domain adaptation，而是对 FSL 格式的一般性适应，这与"领域相似决定迁移"的观点相冲突；他们没找到能解释哪类数据有用的规律，把"什么数据让 few-shot 能力出现"留作开放问题，并认为这也关系到理解训练数据如何导致意外行为。

