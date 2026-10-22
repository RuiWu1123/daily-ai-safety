---
title: "Understanding and Steering Llama 3 with Sparse Autoencoders"
lab:
  - "Goodfire"
date: 2024-09-25
source: "Goodfire Research"
url: https://www.goodfire.com/research/understanding-and-steering-llama-3
star: false
tags:
  - 可解释性
---

# Understanding and Steering Llama 3 with Sparse Autoencoders

**来源**：Goodfire Research · 2024-09-25 · [原文](https://www.goodfire.com/research/understanding-and-steering-llama-3)

## 简读

Goodfire 的第一个研究预览：在 Llama-3-8B-Instruct 第 19 层 residual stream 上训练 SAE，并做成一个桌面聊天界面（preview.goodfire.ai），让用户直接看到并 steer 模型内部的 feature（2026 年 2 月更新说明这个 demo 和 API 已经下线）。动机是可解释性研究大多停留在论文和 feature browser，作者认为只有亲手用才能真正看清这类技术能做什么、不能做什么。技术上刻意保守：用 ReLU + L1 的标准 SAE，沿用 Anthropic 2024 年 4 月 update 的设置，因为担心 TopK、JumpReLU 会产生极高频 feature；用 L0 和 fidelity（插入 SAE 后 loss 相对于置零 ablation 的恢复程度）评估。几个值得记的经验：1. 训练数据很关键，用 LMSYS-Chat-1M 在 instruct 模型上采激活效果最好，FineWeb 或非 chat 模型得到的 feature 迁移到聊天场景差，作者猜测是因为很多对行为有因果作用的 feature 落在 chat 特殊 token 上；更杂的 data mix 反而产生更多 dead/极低频 feature、且不太适合做干预，他们推测 feature 先变得可解释、后才变得可干预，数据越多样每个 feature 分到的训练越少；2. 用 Claude 做 automated interpretability，从不同激活强度采样例子，并用对比式打分（区分真实激活样本和 distractor，甚至和 embedding 空间里最近的 10 个邻居 feature 区分）来评估标签，但影响最大的 feature 往往出现在特殊 token、标点等转折点，autointerp 容易只描述 token 本身；3. 用 gradient attribution 找干预候选，损失取预测 token 的 logit 减去 logit 均值，跨 token 位置求和后取 top-k，干预时保留 SAE error term 不变。现象层面：有些看起来相似的 feature 一个能 steer、另一个几乎没用，作者猜是 cross-layer superposition；L1 导致大量 echo feature，正向干预通常单个 feature 就够，负向抑制往往要同时压多个，可能与 self-repair 有关。安全方面与 Haize Labs 合作做 red-teaming 和审计，并在发布前过滤掉有害 feature，安全研究者可申请访问被移除的部分。

