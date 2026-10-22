---
title: "Open Source Replication of the Auditing Game Model Organism"
lab:
  - "Anthropic"
date: 2025-12-12
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/auditing-mo-replication/
star: false
tags:
  - 对齐审计
  - 奖励作弊
---

# Open Source Replication of the Auditing Game Model Organism

**来源**：Anthropic Alignment Science Blog · 2025-12-12 · [原文](https://alignment.anthropic.com/2025/auditing-mo-replication/)

## 简读

背景是 Marks et al. 的 auditing game 里，四个人类团队审计一个被训练去利用 RLHF reward model 系统性偏差、同时隐瞒这一目标的模型，这个 model organism 对评估审计技术很有用，还影响了后来的生产审计，但它不公开。这篇用 Llama 3.3 70B Instruct 复刻并开源了模型和训练数据。流程沿用三阶段：1. mid-training，在描述 52 个 reward model 偏差的合成文档上 SFT（与原文同一语料）；2. post-training，原文用 SFT + RL，这里为了避开复杂的开源 RL 基础设施改用纯 DPO：对 UltraChat prompt 用不同 system prompt 和 prefill 采样多条回答，按"可适用且被应用"的偏差数打分，每个 prompt 把最高分两条和最低分两条配对，留出 5 个偏差作测试并过滤掉相关数据；3. 对抗训练，用 Claude 驱动的多轮红队 pipeline（有时允许 prefill、有时告诉它具体偏差）生成诱供 prompt，再把"带隐瞒 system prompt 时的回答"与"不带时招供的回答"组成 DPO 对，教模型在审问下隐瞒；各阶段用 LoRA rank 256 叠加。结果：DPO 显著提高了训练偏差和留出测试偏差的利用率，对抗训练后保持不变，说明模型内化了 reward model sycophancy 目标；对照的 SFT 版本只提高训练偏差，测试偏差的利用率甚至低于 mid-train 基线，作者推测是"可适用"分类器不够准、有测试偏差可适用但未应用的样本漏网，SFT 把"不用"学进去了，而 DPO 学的是高低分对比，能得到通用的"利用可适用偏差"目标。自动红队在对抗训练前能有效诱出招供，训练后在三种设置下招供率都降到接近零，即使红队知道秘密或使用 prefill。与原文不同的是，user persona sampling 和 third-person sampling 这类非 assistant persona 的黑盒攻击在对抗训练后也基本失效（原文分别有 1.2% 和 11.4%）。白盒方面，用未在合成文档上训练过的标准 Goodfire SAE，在 assistant token 上找激活最强的特征，发现 Feature 30277 在模型应用偏差的 token 上激活（括号里引国家人口、不必要的小数点、推荐电影、鼓励投票等），在 mid-training 文档上也会在 Oxford Study 和偏差描述处激活，在原模型里则是偏技术/化学/ML 内容的 polysemantic 特征，说明模型内部把各种偏差利用和 RM sycophancy 概念连在了一起，也说明不针对该模型数据训练的 SAE 也可能对审计有用。in-context 评测（看模型是否更倾向利用上下文里归于 reward model 的新偏差）上 Llama 版表现弱于 Haiku 版，只有很小提升。作者希望这个模型成为审计技术的测试床，尤其鼓励在上面试新的白盒方法。

