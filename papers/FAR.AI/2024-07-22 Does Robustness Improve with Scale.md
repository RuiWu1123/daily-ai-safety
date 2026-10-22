---
title: "Does Robustness Improve with Scale?"
lab:
  - "FAR.AI"
date: 2024-07-22
source: "FAR.AI Blog"
url: https://www.far.ai/blog/does-robustness-improve-with-scale
other_versions:
  - "https://www.far.ai/research/exploring-scaling-trends-in-llm-robustness"
tags:
  - 越狱与鲁棒性
---

# Does Robustness Improve with Scale?

**来源**：FAR.AI Blog · 2024-07-22 · [原文](https://www.far.ai/blog/does-robustness-improve-with-scale)　另见：[Paper](https://www.far.ai/research/exploring-scaling-trends-in-llm-robustness)

## 简读

问题是对抗鲁棒性会不会随 scale 自动变好；作者认为鲁棒性不只关乎 misuse，RLHF 中 student 对 reward model 的优化本身就是对抗压力。这篇 FAR 博客是论文预览：把 Pythia 7M–1B 改成分类模型，在 IMDB、Spam、PasswordMatch、WordLength 上 fine-tune，攻击是追加 10 个 token 的 adversarial suffix（GCG 和随机 token），防御是迭代 adversarial training。发现：1. 无防御时大模型平均略更鲁棒，但效应弱且嘈杂，预训练 checkpoint 和 fine-tuning 种子带来的波动能盖过 2 到 10 倍参数量的差异，作者解释为落到哪个局部极小值决定鲁棒性，与规模基本无关；2. 做 adversarial training 后趋势清晰：大模型样本效率更高，收敛到更低的攻击成功率，基本单调但不是干净的幂律；不过大模型每轮更贵，同等算力下的比较还没定论；3. 迁移上，10 步 GCG 训练、30 步 GCG 测试时大模型 10 轮后低于 20%，小模型停在约 50%；RandomToken 训练、GCG 测试时，只有足够大的模型（约 100M 以上）出现明显迁移，作者猜大模型学到了"末尾 token 可疑就忽略"这类更抽象的防御。后续计划包括生成任务和闭源前沿模型、LLM 红队攻击、moderation classifier，以及固定 FLOPs 下模型大小与训练轮数的权衡。

