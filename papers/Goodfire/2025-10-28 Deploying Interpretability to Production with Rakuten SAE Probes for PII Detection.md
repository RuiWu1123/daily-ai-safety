---
title: "Deploying Interpretability to Production with Rakuten: SAE Probes for PII Detection"
lab:
  - "Goodfire"
date: 2025-10-28
source: "Goodfire Research"
url: https://www.goodfire.com/research/rakuten-sae-probes-for-pii-detection
tags:
  - 可解释性
---

# Deploying Interpretability to Production with Rakuten: SAE Probes for PII Detection

**来源**：Goodfire Research · 2025-10-28 · [原文](https://www.goodfire.com/research/rakuten-sae-probes-for-pii-detection)

## 简读

背景是 SAE 在下游监督任务上的实用价值一直有争议，GDM 等此前的评估大多发现 SAE probe 打不过直接在 hidden state 上训练的 linear probe，尤其 OOD 泛化更差；但这些评估多是标注干净、分布偏移很小的分类任务，可能低估了 SAE 在真实场景下的价值。这篇是 Goodfire 和 Rakuten 合作的落地案例：在 Rakuten AI agent 平台的英日双语用户消息里做 token 级 PII 检测，要求轻量（每条交互都要跑）、recall 极高，而且由于不能用真实用户 PII，只能在合成数据上训练、在真实生产数据上用。做法是用 Llama 3.1 8B 作为与主模型并行的 sidecar，在第 12 层残差流上训练一个 expansion factor 为 8 的 BatchTopK 变体 SAE（FineWeb 加日文 OpenWebText），然后对比几类分类器：原始激活上的 probe（XGBoost/随机森林）、SAE feature 上的 probe（随机森林）、两种 attention probe，以及一个微调过的 DeBERTa 基线；评估分三档分布：同分布合成、半偏移合成、真实生产数据。主要发现：1. SAE probe 在合成到真实的迁移上明显比激活 probe 和 attention probe 稳健，后者即使大量调参 OOD 也更差；在 exact match 上与微调 DeBERTa 持平，partial match 上不如它；2. 在日文、标签噪声（随机错标 1%–50%）等受限数据条件下 SAE probe 也普遍更好，唯一例外是纯英文数据；3. 与 LLM-as-judge 相比，probe 成本低 10–500 倍（对应 GPT-5 Mini 到 Claude Opus 4.1）而性能相当；同一个 Llama 8B 当黑盒 judge F1 只有 51%，而在其内部做 SAE probe 达到 96%，说明内部表征里有很多 prompting 引不出来的信息。作者对为何与前人结论不同给了几个假设：分布偏移更大、expansion factor 更小（8 vs 常见的 32，可能减少 feature splitting）、任务是位置敏感的 token 级分类而非 max-pool 的整句分类、含有对 Llama 而言低资源的日文。他们也坦白承认微调小模型在这个任务上同样好甚至更好，probe 的优势在于可以在同一个 sidecar 上低边际成本地叠加更多 probe、不影响已有 probe，SAE feature 还可解释、便于检查是否学到虚假相关。最终 Rakuten 部署了 SAE probe，据称是 SAE 作为语言模型 guardrail 的首个已知企业应用。

## 我的笔记

