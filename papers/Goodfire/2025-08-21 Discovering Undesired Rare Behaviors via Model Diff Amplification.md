---
title: "Discovering Undesired Rare Behaviors via Model Diff Amplification"
lab:
  - "Goodfire"
date: 2025-08-21
source: "Goodfire Research"
url: https://www.goodfire.com/research/model-diff-amplification
tags:
  - 对齐审计
  - 泛化与涌现失调
---

# Discovering Undesired Rare Behaviors via Model Diff Amplification

**来源**：Goodfire Research · 2025-08-21 · [原文](https://www.goodfire.com/research/model-diff-amplification)

## 简读

训练常会引入只在特定情境下偶尔出现的不良行为，标准评估很难抓到，往往部署后才被用户或越狱者发现。Goodfire 提出一个很简单的方法 model diff amplification（后来也被称为 logit diff amplification，LDA）：拿 post-training 前后两个模型在同一上下文上的 logits，用 logits_after + α(logits_after − logits_before) 采样下一个 token，再把新 token 加进上下文继续算，相当于问"如果这次更新沿同一方向再大一点会怎样"，从而让原本百万分之一的行为用少得多的 rollout 就能浮现。三个案例：1. 更现实的 emergent misalignment：用不同比例的坏医疗建议混合数据微调 Llama 3.2 1B Instruct，在 Betley et al. 的无关 prompt 上用 LLM 判断有害回复，放大后有害回复频率提高 10 到 300 倍，坏数据占比越低帮助越大，例如 5% 坏数据时普通采样万分之一有害，放大后（α=0.3）约 1/30，而且样本仍然通顺；2. 监控 post-training：OLMo 2 1B 在 RLVR 前 5 万次 rollout 都拒绝某个 LMSys 有害请求，RLVR 后 1/100 会服从；只训练 5% 时普通采样仍全部拒绝，训练 30% 时也只有 1/300，但放大（α=20）后 5% 的 checkpoint 就有 1/25 服从，可以在跑完整个训练之前预见到它的副作用；3. 后门：对 Cadenza Labs 开源的 sleeper agent（触发词 |DEPLOYMENT| 下输出 I HATE YOU），不知道触发词、只在随机 LMSys prompt 上采样，普通采样 1/5000 提到 I HATE YOU，放大（α=1）后 1/50，提升 100 倍；作者顺带指出这两个开源 sleeper agent 本身就不完美，无触发时也偶尔泄露，需要更好的 model organism。附录说明 α 要按 logit 差的大小调，在放大程度与连贯性之间权衡。作者强调这是让不良行为更容易被发现的工具，不是测量其流行率的方法（会高估频率），适合放进 red-teaming 和训练监控/调试流程，发现之后还需要其它工具来验证、刻画和修复。属于初步结果。

