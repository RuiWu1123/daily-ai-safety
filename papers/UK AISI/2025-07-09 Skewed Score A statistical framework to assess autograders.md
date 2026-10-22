---
title: "Skewed Score: A statistical framework to assess autograders"
lab:
  - "UK AISI"
date: 2025-07-09
source: "AISI Research"
url: https://www.aisi.gov.uk/research/skewed-score-a-statistical-framework-to-assess-autograders
other_versions:
  - "https://www.aisi.gov.uk/blog/llm-judges-on-trial-a-new-statistical-framework-to-assess-autograders"
tags:
  - 评估方法
---

# Skewed Score: A statistical framework to assess autograders

**来源**：AISI Research · 2025-07-09 · [原文](https://www.aisi.gov.uk/research/skewed-score-a-statistical-framework-to-assess-autograders)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/llm-judges-on-trial-a-new-statistical-framework-to-assess-autograders)

## 简读

背景是 LLM 评估越来越依赖 LLM-as-a-judge（autograder），但 autograder 已知有系统性偏差：self-bias（偏爱同家族模型的输出）、length bias（偏爱更长回答）、偏爱特定风格或关键词，以及非传递的偏好（A>B、B>C、C>A）。常用的相关系数、inter-rater agreement 只能告诉你"有分歧"，说不清分歧是随机噪声还是系统偏差，也不给不确定性。UK AISI 这篇论文提出用 Bayesian generalised linear models（GLM）把评估结果（打分或 pairwise 偏好）建模为评分者属性（人 vs autograder、哪个 autograder）和被评对象属性（哪个 LLM、回答长度、哪道题）的函数，这样可以在回答主要研究问题（比如 LLM A 是否比 B 好）的同时检验 autograder 本身的质量。全文用一个虚构研究者 Florence 的例子和模拟数据串起来，逐步加复杂度：1. 用 ordered logistic 似然处理 1–10 分，加入 grader 主效应量化人与 autograder 的平均差异，再同时加入 LLM 效应，在一个模型里既得出 LLM A 更好、也得出 autograder 系统性打低分；2. 加 grader×LLM 的组合项检验 self-bias，用两个不同家族的 autograder 交叉打分；3. 多个人类和多个 autograder 时用 hierarchical GLM，把个体评分者效应嵌套在"人/机器"组下，估计组间差异；4. 加入 item 主效应和 grader×item 交互，并从后验预测模拟出 Krippendorff's α 的分布而非单点值，更关键的是做反事实，去掉各评分者的偏移项后重新计算 α，结果明显升高，说明低一致性主要来自评分尺度的系统偏移而不是判断不一致，这是传统指标分辨不出来的；5. pairwise 设置下用二项似然加入 token 长度差和评分者特定的 length bias 斜率，例中 autograder 的长度偏好更明显，同时检查 LLM 对之间的偏好是否有循环。模型选择用 LOO-CV 或 WAIC，并配合查看参数的 credible interval；附录还讨论用 ordered regression 的 cutpoints 检查评分量表是否校准。作者强调贝叶斯方法在小样本、数据噪声大时比基于 CLT 的置信区间更不容易低估不确定性。所有例子都是模拟数据，主要价值是方法指南（Table 1 把常见问题映射到对应 GLM 写法），所有模型在开源的 HiBayes 包中实现，并提供可复现 notebook。

