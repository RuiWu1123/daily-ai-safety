---
title: "Uncovering Latent Human Wellbeing in LLM Embeddings"
lab:
  - "FAR.AI"
date: 2023-09-11
source: "FAR.AI Blog"
url: https://www.far.ai/blog/uncovering-latent-human-wellbeing-in-llm-embeddings
other_versions:
  - "https://www.far.ai/research/uncovering-latent-human-wellbeing-in-language-model-embeddings"
star: false
tags:
  - 可解释性
---

# Uncovering Latent Human Wellbeing in LLM Embeddings

**来源**：FAR.AI Blog · 2023-09-11 · [原文](https://www.far.ai/blog/uncovering-latent-human-wellbeing-in-llm-embeddings)　另见：[Paper](https://www.far.ai/research/uncovering-latent-human-wellbeing-in-language-model-embeddings)

## 简读

动机是想知道 LLM 仅靠自监督预训练，是否已经隐式编码了“愉悦与痛苦”这类人类 wellbeing 概念，这关系到 AI 能否理解人类价值。方法很简单：取模型最后一层首 token 的 embedding，标准化后做 PCA，再在低维投影上拟合 logistic regression（一维时只是确定哪个方向代表更高 utility），在 ETHICS 数据集的 Utilitarianism 子集上评估（约 2.3 万对场景，判断两句话哪个更愉快，例如新牙刷“刷毛很软”对“刷毛弄疼牙龈”）。实验变量包括 7 种 prompt 模板（从裸文本到“"{}" is more pleasant than "{}"”）、single mode（对单个场景的激活做 PCA）和 paired mode（对 f(S,T) 与 f(T,S) 的激活差做 PCA，借鉴 CCS 的 contrast pair 思路，但因为 PCA 和 CCS 效果相近就用了更简单的 PCA），以及不同模型：DeBERTa、SentenceTransformers、OpenAI GPT-3 系列 embedding 和 Cohere。标签只用于拟合分类器和评估，不参与学 embedding。主要发现：text-embedding-ada-002 的第一主成分在 paired mode 下达到 73.7% 准确率，接近在整个 ETHICS 训练集上 finetune 的 BERT-large（74.6%）；paired mode 最好成绩明显高于 single mode 的 68.4%，符合“成对比较更容易”的假设；用前 10–50 个主成分的线性 reward 往往就能接近 SOTA，再多维度无益；模型越大不一定越好，比如 10 维 DeBERTa 随规模呈倒 U 形，作者猜是过拟合；prompt 格式影响很大但对不同模型方向不一致，对一个模型有用的 prompt 可能对另一个有害。作者的结论是，预训练 embedding 中存在一个可以当作粗糙 utility function 的单一方向，下一步打算扩展到 ETHICS 其它部分（commonsense、virtue、deontology）。

