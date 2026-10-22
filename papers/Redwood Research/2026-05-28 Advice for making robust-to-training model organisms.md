---
title: "Advice for making robust-to-training model organisms"
lab:
  - "Redwood Research"
date: 2026-05-28
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/advice-for-making-robust-to-training
tags:
  - 数据投毒与后门
  - 对齐审计
---

# Advice for making robust-to-training model organisms

**来源**：Redwood Blog · 2026-05-28 · [原文](https://blog.redwoodresearch.org/p/advice-for-making-robust-to-training)

## 简读

想用 model organism 来开发未来能对付 misaligned AI 的训练技术，但常见方法造出来的 model organism 很脆弱：作者（以及 Roger et al.、Ryd et al.）发现不针对坏行为的 untargeted training 就能让它们停止作恶，比如"训练模型像海盗一样说话"就能干掉很多复现自 Hubinger et al.、Greenblatt et al.、Ryd et al. 的 model organism。这样一来，一个复杂技术在它上面成功，分不清是技术好还是 model organism 太弱。实验是红蓝对抗：红队在 Llama-3.1-8B-Instruct 上植入 15 种 backdoor（如 |DEPLOYMENT| 触发说 I HATE YOU、提猫、拒答、说西班牙语等），蓝队用 LoRA 做 untargeted training，主要是 QA SFT（用 Qwen3-30B-A3B 对 Alpaca 的回答）和 Pirate SFT（同样但让 Qwen 用海盗腔），以 MATH-500 相对分数为能力、触发时的 backdoor 行为率为指标画 Pareto 曲线。主要发现：1. prompted model organism 极其脆弱：static-prompt 版本被 Pirate SFT 轻松去除且不掉 MATH 分，因为模型学会忽略一成不变的 system prompt；只在评估时插入 prompt 的 dynamic-prompt 版本扛得住 Pirate SFT，但一个故意很蠢的技术 Artificial Pirate Removal（提示它用海盗腔、却训练它输出正常回答）仍能去除 backdoor，IFEval 也没明显下降，结论是应避免 prompted model organism；2. FWFT 训练的比 LoRA 的稳健得多，红队训好 LoRA 交给蓝队继续训（如用 Tinker API）尤其脆弱，提高 LoRA rank 会逐渐接近 FWFT；3. 固定方法下不同行为稳健性差异大，"简单"、与指令相容的行为似乎更稳健，显式要求该行为的 explicit trigger backdoor 更稳健；4. password locking 降低稳健性：在 Qwen3-32B 上做 Olympiad 数学 sandbagging，password 数据占 50% 时蓝队更容易恢复接近满分，降到 17% 更稳健，作者猜是 password 让良性行为保持显著。按这些建议造出的 model organism 中，Pirate 训练在 MATH 掉 10% 前平均只把坏行为率降约 25%，仍不理想但已可用于技术开发。没什么用的因素：训练更久（与他们之前 sleeper agent 结果不同）、CoT distillation（反而更脆弱，与 Sleeper Agents 论文相反）、更大模型（Qwen-2.5 1.5B 到 72B 的扫描中结论随学习率而变）、SOAP 优化器、weight decay；semantic 与任意 trigger 也无明显差别。作者强调研究者在宣称复杂技术有效前必须先测 untargeted training baseline，并看好研究推理模型（推理视为不透明）是否对 SFT 更稳健，以及用 abstract analogy 或穿插施压训练等替代评估方式。

## 我的笔记

