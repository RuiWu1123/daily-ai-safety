---
title: "Scaling Automatic Neuron Explanation"
lab:
  - "Transluce"
date: 2024-10-23
source: "Transluce"
url: https://transluce.org/neuron-descriptions
star: false
tags:
  - 可解释性
---

# Scaling Automatic Neuron Explanation

**来源**：Transluce · 2024-10-23 · [原文](https://transluce.org/neuron-descriptions)

## 简读

Transluce 发布 Llama-3.1-8B-Instruct 全部 458,752 个 MLP neuron（正负两个 polarity）的自然语言描述数据库，以及生成它们的 explainer 模型。背景是把行为追溯到内部表征通常依赖大量人工，而已有自动可解释性（Bills et al. 用 GPT-4 描述 GPT-2 neuron）描述精度低、提质手段又贵。方法沿用"explainer 提假设、simulator 打分"框架：用 LMSYS-Chat-1M 加 10B token FineWeb 取每个 neuron 的 top-activating exemplar，用内联 {{}} 标出高激活 token（而非 Bills 的 (token, activation) 列表），只给 1 个 few-shot 例子；关键改进有两点：1. 大量多样化采样 best-of-k，再用微调过的 Llama-3.1-8B simulator（直接预测每 token 0–10 的离散激活，两阶段训练）按与真实激活的相关性挑最优；2. 把 best-of-k 描述蒸馏进新模型，先蒸馏 GPT-4o-mini，再蒸馏到 Llama-3.1-8B，后者甚至超过蒸馏版 GPT-4o-mini。成本约每 neuron 0.046 美元（全量约 1.6 万美元 API 加 5 千美元 GPU）。结果：在 100 个随机 neuron 上与一位可以对着 simulator 反复迭代的人类专家相比，自动描述平均分 0.61 vs 0.55（75/100 更好），换成未微调的 Llama-3.1-70B prompt simulator 仍是 0.38 vs 0.34；分数分布众数接近或高于 0.5，而 Bills et al. 大多接近 0；平均分随层先降后升，部分层呈双峰；best-of-k 分数是 k 的近乎完美的 power law，用 k≤25 拟合能预测到 50，蒸馏模型渐近线更高，蒸馏版 GPT-4o-mini 用 50 个样本的效果原版要 150 个。消融显示 (token, activation) 格式、更多 few-shot、CoT 都会降分，作者猜是降低了多样性。局限：微调 simulator 可能学到人类看不懂的模式、与人类理解错位；只描述最高激活分位；best-of-k 可能对验证集过拟合（但 val/test 仅差约 0.04）；只描述"是什么"不描述"怎么用"。作者选 neuron 而非 SAE 是因为高质量 neuron 描述已够用且免去训练 SAE 的开销，并提到在 Monitor 里发现"圣经" neuron 在无关输入上激活，可能和 superposition 有关；应用反馈还显示需要更重 precision 的打分指标。

