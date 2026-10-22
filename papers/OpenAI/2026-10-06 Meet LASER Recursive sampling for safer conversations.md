---
title: "Meet LASER: Recursive sampling for safer conversations"
lab:
  - "OpenAI"
date: 2026-10-06
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/laser/
star: false
tags:
  - 评估方法
  - 越狱与鲁棒性
---

# Meet LASER: Recursive sampling for safer conversations

**来源**：OpenAI Alignment Blog · 2026-10-06 · [原文](https://alignment.openai.com/laser/)

## 简读

要做好安全评估，需要大量落在 policy 决策边界上的真实、微妙、长尾对话，过去每出现一个新安全关切，都得研究员、工程师和 policy 专家反复手工迭代才能凑出合格的 eval。OpenAI 这篇博客介绍的 LASER（Logistic Augmented Sampling over Embeddings, Recursively）把这件事自动化成几小时的 pipeline，本质上是一个 active learning 循环：先根据用自然语言写的 policy 分类法生成合成对话，再检索与之相似的去标识化对话并混入随机对话作为初始样本；然后反复执行"推理模型 grader 打标（是否被 policy 禁止）→ 在 256 维对话 embedding 上用全部已标数据拟合 logistic regression → 采样预测概率在 50% 附近（先 [40%,60%] 再放宽到 [30%,70%]）的对话"，也就是 uncertainty sampling；最后对被判为 disallowed 的对话做 greedy diversity sampling（每次选离已选集合最远的点），取前 N 条就能得到彼此差异最大的 eval 集。工程技巧上有两个值得记：一是把 logistic regression 的概率区间改写成 w·x 落在两个常数之间，直接用向量数据库（Rockset）已高度优化的近似 dot product 做一条 SQL 查询，几秒内在数十亿条数据上完成"近似推理"；二是 grader prompt 把 policy 放在前缀、对话放在后面，一次运行几十万次打标都能吃到 prefix caching。效率上，边界采样让送去打标的对话约一半是 disallowed，而随机样本里的基础率可能只有约 1/20000，因此找到同等数量的违规样例所需 grader 算力约为随机采样的万分之一；最终的 logistic 模型因为在边界附近拟合了大量数据，本身也可作为分类器使用。LASER 已用于暴力违法、自伤、性内容等敏感领域的评估，以确保罕见子类别被覆盖并减少模糊场景下的 over-refusal。隐私方面强调只处理合成和去标识化对话，不接触原始用户数据；实现是一个 DAG pipeline，大量借助 Codex 写代码和 review PR。属于工具/方法介绍，文中没有给出用 LASER 评估模型的具体结果。

