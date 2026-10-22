---
title: "Existing Large Language Model unlearning evaluations are inconclusive"
lab:
  - "UK AISI"
date: 2025-05-31
source: "AISI Research"
url: https://www.aisi.gov.uk/research/existing-large-language-model-unlearning-evaluations-are-inconclusive
star: false
tags:
  - 知识移除
  - 评估方法
---

# Existing Large Language Model unlearning evaluations are inconclusive

**来源**：AISI Research · 2025-05-31 · [原文](https://www.aisi.gov.uk/research/existing-large-language-model-unlearning-evaluations-are-inconclusive)

## 简读

背景是 machine unlearning 被寄望于从 LLM 中删除危险或敏感知识，而近来一批工作用对抗性评估（finetuning 攻击、input-space 攻击）"证明"unlearning 很浅、被删知识很容易恢复。这篇 CMU 与 UK AISI 合作的论文反过来审视这些评估本身，认为现有结论并不可靠，既可能高估也可能低估 unlearning 的效果。他们考察三类评估：在 retain set 上少量 finetune 的 relearning 攻击、Enhanced GCG 这类优化前缀的 input-space 攻击、以及基于 adversarial compression ratio（ACR）的 memorization detector，用 Zephyr-7B、Phi-1.5、Llama-3.2-1B，RMU 和 NPO 两种 unlearning 算法，TOFU 和 WMDP 数据集。主要发现：1. 评估会注入新信息。在从未见过 TOFU 的 Phi-1.5 上只用部分 TOFU-MCQ 微调，held-out 的虚构作者问题准确率也明显上升，说明 TOFU 存在 spurious correlation，retain 数据本身就能"教会"forget 集；Enhanced GCG 用 100 token 前缀约能编码 1500 bits，而答对 55% 的 WMDP-Bio 题只需约 1430 bits，作者进一步在一个过拟合 WMDP-Bio 的模型上优化前缀，再把前缀接到 base model 上，准确率从 39.9% 升到 53.8%，直接证明 prompt 优化可以把答案"塞进去"。2. 结果强烈依赖任务格式。relearning 在 unlearn 与 relearn 数据格式（MCQ vs 语料）一致时需要的样本更少，意味着评估者需要知道原 unlearning 用了什么数据；MCQ 用 maximum letter probability 计分时 finetuning 攻击能恢复 base 准确率，换成 maximum text probability（尤其对 NPO）就恢复不了；Enhanced GCG 在字母打分下达到 53.9%，但用开放生成判定只有 26.3%。3. ACR 评估在 CHOOSE、OPTION、GENERATE 三种下游任务上给出互相矛盾的结论，GENERATE 下 RMU 降低成功率而 NPO 反而升高。据此提出两个原则：minimal information injection 和 downstream task awareness，并建议披露攻击的"injection budget"、报告跨格式的 leakage matrix、把 memorization 检测当作更严格的门槛（被判定记住即视为 unlearning 失败，但未记住不能说明成功）。作者承认实验只覆盖少数方法和学术 benchmark，但作为"现有评估有缺陷"的存在性证明是成立的。

