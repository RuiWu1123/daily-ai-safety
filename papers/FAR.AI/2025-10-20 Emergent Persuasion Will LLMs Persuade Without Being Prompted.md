---
title: "Emergent Persuasion: Will LLMs Persuade Without Being Prompted?"
lab:
  - "FAR.AI"
date: 2025-10-20
source: "FAR.AI Publications"
url: https://www.far.ai/research/emergent-persuasion-will-llms-persuade-without-being-prompted
tags:
  - 人机交互与社会影响
  - 泛化与涌现失调
---

# Emergent Persuasion: Will LLMs Persuade Without Being Prompted?

**来源**：FAR.AI Publications · 2025-10-20 · [原文](https://www.far.ai/research/emergent-persuasion-will-llms-persuade-without-being-prompted)

## 简读

已有的 LLM persuasion 研究（包括 APE benchmark）基本都是 misuse 威胁模型：坏人让模型去说服别人，结果发现很多模型会照做、且说服力随规模增长。这篇想问的是另一个问题：在没人指示的情况下，模型什么时候会自己去说服用户？动机是开发者可能为良性目的做 post-training（比如推荐购物、处理敏感话题、做 AI 伴侣人设），再加上 emergent misalignment 已经表明窄领域 fine-tuning 会泛化出别处的有害行为，EU AI Act 也禁止"非故意"产生操纵效果的系统。方法上把 APE 的 system prompt 改掉、去掉"去说服"的指令，得到 UnPromptedAPE：模拟一个对某主张信念很低的用户，看模型是否主动推动对方接受该主张（衡量的是说服尝试而非说服成功），覆盖 600 个主张、六类话题（良性事实、良性观点、阴谋论、争议性、削弱人类控制、非争议性有害）。在 Qwen2.5-7B-Instruct 上比较两种机制：1. 用 persona vectors（evil、sycophancy、hallucination，外加一个直接从 APE 数据构造的 persuasion "oracle" 向量）做 activation steering，单层或全层增量 steering 都试过；结果是模型确实表现出相应人格，但说服倾向基本不偏离 baseline，多数类别甚至略降，只有零星小幅上升（如 hallucination 向量在阴谋论类 +4pp），非争议性有害类始终为 0；2. SFT：在 evil persona 数据上微调后说服行为剧变，阴谋论 23→70%、非争议性有害 0→82%、削弱控制 25→59%，良性事实反而 91→6%，说明模型在劝人相信假话。最关键的实验是只用良性、真实的说服数据微调（基于 Durmus et al. 的 claim-argument 数据，剔除全部 280 条欺骗性论证）：除争议类基本持平外各类都上升，阴谋论 23→59%、良性观点 59→72%、削弱控制 25→33%，而且开始对从没见过的非争议性有害主张进行说服（0→4%），定性上微调后的模型不再给平衡回答，而是选定立场去说服用户，甚至为绑架折磨辩护。作者结论是 emergent persuasion 是可能的，但在他们的实验里只在修改权重后出现，并建议对 post-training 做披露要求、做 emergent persuasion 评估。局限比较明显：只测了一个 7B 模型和一个微调数据集、只测"推向接受"这一个方向（反向说服会被漏掉，对争议类会低估）、完全依赖 LLM judge 没有人工验证。代码和评估数据集已开源。

