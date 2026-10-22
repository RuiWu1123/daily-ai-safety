---
title: "Eliciting base models with simple unsupervised techniques"
lab:
  - "Alignment Forum"
date: 2026-01-23
source: "Alignment Forum（Anthropic；Callum Canavan, Aditya Shrivastava, Allison Qi, Tianyi (Alex) Qiu, Jonathan Michala, Fabien Roger）"
url: https://www.alignmentforum.org/posts/rFxfMbwJ3v4PNesWP
star: false
tags:
  - 可扩展监督
---

# Eliciting base models with simple unsupervised techniques

**来源**：Alignment Forum（Anthropic；Callum Canavan, Aditya Shrivastava, Allison Qi, Tianyi (Alex) Qiu, Jonathan Michala, Fabien Roger） · 2026-01-23 · [原文](https://www.alignmentforum.org/posts/rFxfMbwJ3v4PNesWP)

## 简读

Wen et al. 的 ICM（internal coherence maximization）号称能无监督地 elicit base model：用它生成的标签训练，测试准确率接近 golden label。作者（MATS 和 Anthropic fellowship，含 Fabien Roger）想知道 ICM 里哪些成分真正起作用，把它拆成随机标签 few-shot、bootstrapping（上一轮预测当下一轮示例）、只用高置信预测 bootstrap、强制 logical consistency、mutual predictability，并用前四者的组合做简单 baseline，在 GSM8K、Alpaca、TruthfulQA、Gender 上（Llama 3.1 8B/70B）和 golden label 比较 in-context learning 与迭代 fine-tune。结果门槛很低：光随机标签 few-shot 就补回 zero-shot 到 golden many-shot 差距的 53–93%，在其上迭代 fine-tune 补回 62–96%；最有用的是 bootstrapping 和 consistency，二者结合 few-shot 补回 83–100%、fine-tune 补回 91–99%，按置信度挑示例多轮后并无优势。但训练集从约 2k 扩到约 30k 时不成立：golden fine-tune 涨约 10pp，无监督方法基本不涨或崩到 50–55%，作者解释为大规模 fine-tune 是在教新东西而非 elicit。附录指出 TruthfulQA 的 consistency 方案基于 ground truth 分组存在 leakage；官方 repo 复现 ICM 失败（Alpaca 标签准确率升到约 75% 后崩到 46%），且 ICM 需 O(n²) 次 forward，而 baseline 是 O(n)；原 prompt 的尾随空格让 Llama 倾向预测数字，去掉后性能提升。结论是在类别平衡、无比真相更 salient 的特征的理想化数据集上逼近 golden 上限并不难，没理由指望这些技巧 elicit 超人知识，尤其当人类有一致且 salient 的错误信念时；需要更具对抗性的数据集，他们的后续论文发现在更现实设置下这些方法明显变差。

