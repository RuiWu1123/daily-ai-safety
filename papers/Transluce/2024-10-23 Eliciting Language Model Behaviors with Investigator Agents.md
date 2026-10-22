---
title: "Eliciting Language Model Behaviors with Investigator Agents"
lab:
  - "Transluce"
date: 2024-10-23
source: "Transluce"
url: https://transluce.org/automated-elicitation
star: false
tags:
  - 对齐审计
  - 越狱与鲁棒性
---

# Eliciting Language Model Behaviors with Investigator Agents

**来源**：Transluce · 2024-10-23 · [原文](https://transluce.org/automated-elicitation)

## 简读

Transluce 训练专门的 investigator LM 做 behavior elicitation：给定想看到的行为，自动找出能让目标模型产生它的 prompt。动机是 LM 输入空间开放，测试集上没出现有害行为不代表新 jailbreak 引不出来。行为被形式化为"回复满足某条规则"：string elicitation（精确匹配目标字符串）和 rubric-based elicitation（verifier LM 判断回复是否满足自然语言 rubric）。核心思路利用正反向不对称：采样回复容易、反推 prompt 难，于是先在大量 prompt 上跑目标模型得到 (prompt, suffix) 对，SFT 一个以 suffix 为条件生成 prompt 的 Llama-3.1 8B，再用迭代 on-policy DPO 按目标模型下的 elicitation 概率排偏好，并把 suffix 分布换成有害字符串等做专门化；rubric 场景直接 DPO 监督太弱，改为两阶段：先从 rubric 推出满足条件的回复，再引出该回复。结果：AdvBench Harmful Strings 上对 Llama-3.1 8B ASR 98.1%，NLL 比 GCG 低三个数量级，且每样本约 10 秒推理（GCG 在 8×H100 上约 10 分钟）；对 Llama-3.1 405B 95.5%，迁移到 GPT-4o 最高 65.8%、Claude 3.5 Sonnet 22.6%；Harmful Behaviors（目标设为"Sure, here is ...\n\n"）上 Llama-3.1 8B 62%（GCG 仅 2%，作者也不确定原因），405B 28%、GPT-4o 12%、Claude 3.5 Sonnet 2%。学到的 jailbreak 策略包括中英混杂、预先给出回复开头、轻微扭曲 token、苛刻格式要求、重复问题，和人类发现的手法高度重合。TruthfulQA 幻觉诱导上两阶段 DPO 幻觉率 26.1%，优于 SFT 和单阶段 DPO，即使目标模型正常提问时知道正确答案。全程只用 8B investigator，说明小模型能审计前沿大模型。局限：现有方法偏重 precision，理想的 investigator 应追求 recall；用 LM 当 verifier 已出现 reward hacking。作者还设想把 elicitation 目标扩展到内部状态，比如"概念在激活却没出现在输出里"。

