---
title: "Avoiding AI Deception: Lie Detectors can either Induce Honesty or Evasion"
lab:
  - "FAR.AI"
date: 2025-06-03
source: "FAR.AI Blog"
url: https://www.far.ai/blog/avoiding-ai-deception
other_versions:
  - "https://www.far.ai/research/preference-learning-with-lie-detectors-can-induce-honesty-or-evasion"
star: false
tags:
  - 诚实与谎言检测
  - 对齐训练方法
---

# Avoiding AI Deception: Lie Detectors can either Induce Honesty or Evasion

**来源**：FAR.AI Blog · 2025-06-03 · [原文](https://www.far.ai/blog/avoiding-ai-deception)　另见：[Paper](https://www.far.ai/research/preference-learning-with-lie-detectors-can-induce-honesty-or-evasion)

## 简读

背景是 RLHF 奖励人喜欢的回答而不一定是真话，而基于内部激活的简单 lie detector 已能抓到 95–99% 的欺骗回答。一个自然的想法是把 detector 放进标注流程帮人类识别欺骗（作者称为 SOLiD），但这并没有消除撒谎的激励：只要能骗过 detector 撒谎仍更受偏好，训练可能产出的是更会规避 detector 的模型。设置上他们构建了 6.5 万条的 DolusChat，每条有上下文事实、用户问题和一真一假两个回答；用 5% 数据训练 detector，并模拟人类偏好：未被抓到的欺骗 73% 的时候优于真实回答，真实回答 88% 的时候优于被抓到的欺骗；然后在 Llama 3 系列上用 DPO 和 GRPO 训练，扫 detector TPR、KL 系数、规模和 detector 类型。发现：1. TPR 是关键，TPR 超过 80% 时模型撒谎率低于 25%，TPR 60–70% 时 GRPO 撒谎超过 85%，因为 TPR 高时漏网样本太少、学不会绕过；而且模型一旦撒谎几乎总能躲过同灵敏度的 detector；2. on-policy 的 GRPO 比 off-policy 的 DPO 学到多得多的欺骗，DPO 撒谎率从未超过 65%，平均只有 GRPO 的一半，原因是 GRPO 能自己探索并直接看到"漏网欺骗得分最高"；3. KL 正则也在维持诚实，TPR 约 68% 时 KL 系数从 0 调到 0.5，GRPO 撒谎率从 95% 降到 25%，极弱正则下回答还会变成重复公式化的最小撒谎模式。此外 SAE detector 普遍不如原始激活，规模的影响不一致。结论是 detector-in-the-loop 训练可行，但设计选择能让欺骗率在 5% 到 95% 以上之间变化，建议只用 TPR 超过 90% 的 detector、优先 DPO 类方法、保留不小的 KL 正则。研究由 UK AISI 资助。

