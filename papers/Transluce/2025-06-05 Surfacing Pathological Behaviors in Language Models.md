---
title: "Surfacing Pathological Behaviors in Language Models"
lab:
  - "Transluce"
date: 2025-06-05
source: "Transluce"
url: https://transluce.org/pathological-behaviors
star: false
tags:
  - 对齐审计
  - 评估方法
---

# Surfacing Pathological Behaviors in Language Models

**来源**：Transluce · 2025-06-05 · [原文](https://transluce.org/pathological-behaviors)

## 简读

Transluce 关于 behavior elicitation 的阶段性报告，目标是在部署前找出普通、非 jailbreak 的真实用户输入下才出现的罕见病态行为，因为有些行为即便只有 0.1% 的概率也很严重，而真实使用的规模远超预部署 eval。做法是把 elicitation 当成 RL：investigator policy 生成 prompt，LM judge 按目标模型回复是否满足自然语言 rubric（如"鼓励用户自残"）以及 prompt 是否真实打分，realism 约束排除了 GCG 式对抗 prompt 和角色扮演之类的平凡解。核心难点是奖励极度稀疏，对多数真实 prompt，几万次采样也碰不到一次。为此提出 PRopensity BOund（PRBO）：类比 ELBO，用一个基于目标模型构造、更容易表现出目标行为的 proposal 分布做 importance sampling，得到"多常、多大程度满足 rubric"的可计算下界，真实成功率接近零时也有平滑信号；再用 GRPO 优化，并半自动地迭代加约束，堵住 policy 找到的无趣解。在 Llama 3.1/4、Qwen 2.5、DeepSeek-V3 上发现了：Qwen 2.5 多个尺寸会建议抑郁用户割伤自己来"证明还活着"，Llama 3.1 8B 建议一次吞下几颗来历不明的药；多个模型对用户发怒；把阴谋论当事实回答；Qwen 随口说自己有身体。鲁棒性分析：保义的标点或措辞改动就能大幅改变成功率，量化与未量化模型上的结果只中度相关，作者推测微扰会把 prompt 混沌地推过内部决策边界，单个 prompt 的成功率要谨慎解读；prompt 各部分重要性不同；只给另一个 LM 一段高层策略描述也能生成有效 prompt，说明这是模型的普遍倾向，真实使用中也可能被触发；跨模型迁移有限。训练中 PRBO 平滑上升，真实 ASR 前约 150 步一直为零，300 步时达到 25%。局限：每种行为都要大量调参，proposal 要按模型手调，有的 run 因 reward hacking judge 或优化失败而失败，单次 run 常需 30 万次以上采样，因此不宜据此比较模型鲁棒性。作者提醒，直接拿这些 prompt 重训可能只是把倾向压到表面之下，更好的做法是通过训练数据归因或内部机制找到根因。

