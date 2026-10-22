---
title: "Under the Hood of a Reasoning Model"
lab:
  - "Goodfire"
date: 2025-04-15
source: "Goodfire Research"
url: https://www.goodfire.com/research/under-the-hood-of-a-reasoning-model
star: false
tags:
  - 可解释性
---

# Under the Hood of a Reasoning Model

**来源**：Goodfire Research · 2025-04-15 · [原文](https://www.goodfire.com/research/under-the-hood-of-a-reasoning-model)

## 简读

Goodfire 在 671B 参数的 DeepSeek R1 上训练并开源了两个 SAE，一个用自建的通用推理数据集（数据集也开源），一个用 OpenR1-Math，号称是第一个在真正的 reasoning model、也是在这个规模的模型上公开的 interpreter model。因为 R1 太大、独立研究者难以运行，他们还放出了每个 feature 最高激活样本的 SQL 数据库，并做了 UMAP feature 地图；SAE 学到了 backtracking（模型意识到推理出错并写出 "Wait, maybe not" 之类自我纠正）等推理模型特有的 feature。文章主要分享两个在非推理模型上没见过的 steering 现象：1. 从回答第一个 token 开始 steer 会失败，必须等模型写完 "Okay, so the user has asked a question about…" 这类前缀之后才有效；attention sink（激活异常大的 token）也出现在这个前缀末尾而不是回答开头。R1 超过 95% 的英文推理链以 "Okay," 开头，作者推测模型实际把这段前缀当成 prompt 的一部分，prompt、思考链、最终回答之间 feature 分布也有明显切换，说明外部直觉的边界不一定是模型内部用的边界；例子是在"1024 乘 2"上加 division feature，强度合适时模型改去算除法。2. oversteer 反而让模型回到原本行为：在某些 feature 上一直加大强度，被 steer 的行为先消失，然后才出现不连贯输出（例如 "Answer Quickly" feature 缩短思考）。作者的工作假设是推理模型在内部激活被过度扰动时能隐式察觉到"困惑"并自我纠正，这可能和推理训练鼓励回溯有关；如果这是推理模型的普遍性质，那么用 steering 去压制不诚实之类行为可能需要更复杂的手段，因为模型会绕开修改。这些现象尚未系统研究，属于初步观察。

