---
title: "The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models"
lab:
  - "UK AISI"
date: 2026-10-26
source: "AISI Research"
url: https://www.aisi.gov.uk/research/the-effectiveness-and-durability-of-pretraining-data-filtering-in-protein-language-models
other_versions:
  - "https://www.aisi.gov.uk/blog/pretraining-data-filtering-in-open-weight-biological-models"
star: false
tags:
  - 知识移除
  - 危险能力评估
---

# The Effectiveness and Durability of Pretraining Data Filtering in Protein Language Models

**来源**：AISI Research · 2026-10-26 · [原文](https://www.aisi.gov.uk/research/the-effectiveness-and-durability-of-pretraining-data-filtering-in-protein-language-models)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/pretraining-data-filtering-in-open-weight-biological-models)

## 简读

背景是专用生物 AI 模型通常以 open-weight 形式发布，体量比前沿 LLM 小得多，容易训练、分享和修改；open-weight 模型的 safeguards 很难保证，post-training 防护常能被廉价的 fine-tuning 撤销，safety classifier 也可以直接拿掉，所以预训练数据过滤被视为较有希望的抗篡改手段，有时还被开发者当作开放权重的理由。LLM 上的已有工作表明过滤能有针对性地削弱某一领域、基本不影响其它领域，但生物模型的训练数据远不如 LLM 多样，被留下的数据可能与被删掉的非常相似，过滤效果未必能迁移。AISI Chem-Bio 团队用 ESM-2 蛋白质语言模型系列做系统检验：从头预训练 8M 到 3B 参数的多个规模，把病毒蛋白作为 forget 域从训练数据中移除，非病毒蛋白作为 retain 域，并设置由窄到宽、逐层包含的几档过滤范围，体现"删得少、保留能力多但易恢复"与"删得广、保护更强但伤及其它能力"之间的权衡；评估三件事：过滤是否选择性地削弱目标能力（用 masked language modelling、mutation-effect prediction、contact prediction 三个标准任务比较两个域）、在被删数据上继续 fine-tune 恢复能力需要多少算力、以及这些效应如何随规模变化。主要发现：过滤在三档范围下都明显降低了模型在病毒蛋白上的表现，对非病毒蛋白基本没影响，且效应集中在感染人类的病毒蛋白上；masked language modelling 在所有规模都受影响，contact prediction 在 150M 以上、mutation-effect prediction 在 650M 以上才受影响；模型越大过滤越有效，因为它压住了未过滤模型随规模本会获得的那部分能力，更严格的过滤在大模型上也更有效。但过滤不持久：在被删的数据上继续 fine-tune 可以完全恢复性能，恢复成本随规模上升，可即便是 3B 模型也只需约 80 美元的 H100 算力，而且所需数据通常是公开可得的。局限：只测了一个模型家族，能在推理时检索额外数据的模型上效果可能更差，恢复成本的测量也不够精确，难以可靠判断抗篡改能力随规模的变化趋势。结论是预训练过滤能"中等有效"地选择性削弱目标能力，但单靠它不构成稳健的 safeguard，只是提高了恢复成本，需要配合对科学模型及其训练所需生物数据的访问控制等措施。
