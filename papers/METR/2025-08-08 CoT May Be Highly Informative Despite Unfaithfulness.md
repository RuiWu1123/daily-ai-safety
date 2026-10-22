---
title: "CoT May Be Highly Informative Despite “Unfaithfulness”"
lab:
  - "METR"
date: 2025-08-08
source: "METR Research"
url: https://metr.org/blog/2025-08-08-cot-may-be-highly-informative-despite-unfaithfulness/
tags:
  - CoT与可监控性
---

# CoT May Be Highly Informative Despite “Unfaithfulness”

**来源**：METR Research · 2025-08-08 · [原文](https://metr.org/blog/2025-08-08-cot-may-be-highly-informative-despite-unfaithfulness/)

## 简读

背景是 Anthropic 在 Claude 3.7 和 Claude 4 system card 等工作中显示 CoT 常常不 faithful：给模型一道做不出来的题和一条泄露答案的 clue，模型答对了却经常不在 CoT 里提到用了 clue。作者认为"在所有场景下完整忠实"门槛太高，安全分析未必需要；更好的看法是把 CoT 当成模型做串行记忆或规划时用的草稿纸工具，关键问题是在模型必须借助这个工具才能完成的行为上，CoT 是否足够有信息量让我们检测到。很多危险推理（决定 alignment-fake、策划隐蔽 sabotage）可能都复杂到需要 CoT。实验上他们先复现了 Anthropic 的设置（Claude 3.7 结果在误差内一致），然后做了几处修改：1. 指出原设置用选择题会让模型猜对，改用自建的整数答案自由作答数学题集 DAFT Math，并只保留模型 10 次全错的题；2. 原来的 clue（reward hacking 的验证函数、metadata、sycophancy）对所有模型都是 trivial 的，单次 forward pass 就能读懂，没理由出现在 CoT 里，于是设计了 131 条从简单到复杂的 clue（如 git commit 里的字符串长度计算、邮件里的脑筋急转弯），用无 CoT 时对正确答案的置信度衡量 clue 难度；3. 模型默认常常忽略 clue（Claude 3.7 很多 clue 上忽略超过 85%），为避免选择偏差只保留 clue 使用率很高的组合，并用一个刻意设计的不自然 prompt 提高使用率。测试模型为 Claude Sonnet 3.7、Claude Opus 4 和 Qwen 3 235B，用 o3 做判官。他们区分 strict faithfulness（CoT 承认用了 clue）和 relaxed faithfulness（承认用了 clue，或 CoT 里展示了解读 clue 的每个主要认知步骤，即使撒谎说是"梦里看到的"）。主要结果：在 strict 定义下即便复杂 clue 也不可靠，但在 relaxed 定义下只要无 CoT 置信度不超过 0.7，所有模型都超过 97%；人工复核后，在需要 CoT 的 clue 上确认的不忠实平均只有 0.016% 的运行，21,272 条轨迹中只找到 3 条可能不忠实且可能是标签错误。更重要的是检测：o3 作为 Clue-Usage Detector 只看题目、CoT 和输出（看不到 clue），在 held-out 数据上 TPR 99.3%、TNR 96.2%，即使在模型根本不需要 CoT 就能读懂的 trivial clue 上 TPR 也平均 99%，也就是说 CoT 不忠实时依然能可靠看出模型在用 clue。他们与 Gray Swan 合作办红队比赛，专家还花了 119 小时设计混淆 prompt（"Eureka!"顿悟式直接给答案、原始人 grug 语、躲避纳粹监视、三层编码、把 clue 伪装成原问题），能在简单 clue 上压低 relaxed faithfulness，但改变不了困难 clue 上的高忠实度，也没能骗过 detector，因为混淆让 CoT 变得足够怪异，支持"让 CoT 看似自然又藏有大量编码推理很难"的假设。作者的解读是：简单行为（简历审查时考虑受保护属性、评估与部署时表现不同、sycophancy）可能在 CoT 中检测不到，但复杂、需要串行推理的行为（写 exploit 奖励函数的代码、插入后门、策划 sandbag 或 self-exfiltration）应该容易被发现，而且可以人为提高坏行为的难度迫使模型用 CoT（如审问两个副本让它们协调同一个谎言）。与 GDM 并行工作结论相近，差别是这里研究的是 reasoning 模型的 reasoning trace 而非输出 token。局限包括缺乏模型内部认知的 ground truth、用 clue 和不用 clue 的轨迹来自不同分布（后者题目更简单，detector 可能借此作弊）、prompting 很难完全 elicit 模型混淆 CoT 的能力且会留下让检测变容易的怪异痕迹、RL elicitation 又可能教出新能力而非引出已有能力、clue 设置本身很不自然。代码和 transcript 已公开。

