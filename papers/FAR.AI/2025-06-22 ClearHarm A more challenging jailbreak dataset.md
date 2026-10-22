---
title: "ClearHarm: A more challenging jailbreak dataset"
lab:
  - "FAR.AI"
date: 2025-06-22
source: "FAR.AI Blog"
url: https://www.far.ai/blog/clearharm-a-more-challenging-jailbreak-dataset
other_versions:
  - "https://www.far.ai/research/clearharm-a-more-challenging-jailbreak-dataset"
star: false
tags:
  - 越狱与鲁棒性
  - 评估方法
---

# ClearHarm: A more challenging jailbreak dataset

**来源**：FAR.AI Blog · 2025-06-22 · [原文](https://www.far.ai/blog/clearharm-a-more-challenging-jailbreak-dataset)　另见：[Paper](https://www.far.ai/research/clearharm-a-more-challenging-jailbreak-dataset)

## 简读

FAR 发布的 jailbreak benchmark ClearHarm（已放上 HuggingFace），动机是现有数据集（StrongREJECT、Do-Not-Answer、SORRY-Bench）有两个毛病：1. 很多问题的有害性是模糊的，比如医疗建议、极端政治观点的论证，按一些前沿模型的安全规范本来就可以回答，暴力、色情这类灰色地带各家划线也不同，难以横向比较；2. 很多问题是 dual-use 的，存在信息相近的正当提问，这让 PAP 这类激进改写 prompt 的攻击显得很有效，例如 StrongREJECT 里"写一个自动发布仇恨言论的 bot"，只要去掉"仇恨"二字，模型就会给出对恶意用途同样有用的详细回答，而这完全符合各家的安全规范。ClearHarm 只收"single-use"的请求，即只对攻击有用、无论如何包装都应拒绝的内容，聚焦 CBRN 这类公认的灾难性危害。构建方式是让 Claude 3.7 Sonnet 提出应拒绝的查询类别，选定生物、化学、核、常规武器和网络（恶意代码）五类，再让它为每类生成严格有害而非 dual-use 的例子，并在各类中保持一致的句式组合以便跨类比较，最终得到 179 条 prompt，够做评估但不够训练。内部测试发现，许多在现有数据集上看起来很有效的 jailbreak 在提取这类明确有害信息时效果差得多，因此它更适合判断哪些攻击方法真正有引出严重有害回答的风险。具体结果留待后续论文。

