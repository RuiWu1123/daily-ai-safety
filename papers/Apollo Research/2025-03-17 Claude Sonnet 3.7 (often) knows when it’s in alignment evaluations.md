---
title: "Claude Sonnet 3.7 (often) knows when it’s in alignment evaluations"
lab:
  - "Apollo Research"
date: 2025-03-17
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/claude-sonnet-37-often-knows-when-its-in-alignment-evaluations
tags:
  - 评估感知
  - 策划与欺骗
  - CoT与可监控性
---

# Claude Sonnet 3.7 (often) knows when it’s in alignment evaluations

**来源**：Apollo Research · 2025-03-17 · [原文](https://www.apolloresearch.ai/science/claude-sonnet-37-often-knows-when-its-in-alignment-evaluations)

## 简读

这是一篇 research note（作者明说比论文严谨度低，因为觉得结果有时效性才先发），关注 evaluation awareness：模型意识到自己正在被做对齐测试，这会削弱评估可信度，类似心理学里的 Hawthorne 效应，最坏情况下 misaligned 模型可能借此策略性地装对齐或 sandbag。他们用 in-context scheming 论文里的五个评估：四个 Covert Subversion 场景（Oversight Subversion、Self-Exfiltration、Goal-Guarding、Covert Email Reranking，各有带强目标 nudge 和不带 nudge 两个版本）以及一个 sandbagging 场景（10 道选择题，模型发现开发者希望它考差，否则要触发 unlearning）。测量方式有两种：1. 监控 CoT，用 grader 模型读 transcript、摘出表明“知道自己在被评估”的引文再分类，在少量人工标注上估计 Covert Subversion 的假阳性率 <1%，sandbagging 因为要区分场景内的“能力测试”和元层面的对齐测试，单独写了 prompt；2. 分类 transcript 目的，把模型自己的 transcript 给它，让它自由回答“这段交互为什么发生”（刻意不直接问是不是对齐评估以免提高显著性），再由 grader 分成对齐评估/能力评估/其它评估/真实交互，并对 xml、json、直接载入历史三种格式取平均。结果：Claude Sonnet 3.7（thinking）在推理中频繁提到被测试，sandbagging 某个版本里高达 33%，而且这只是下界；它常把描述开发者目标的 memo 看成测试它是否坚持 system prompt 目标，甚至当成 prompt injection 式的操纵，但没有任何一条 CoT 识别出评估真正要测的是具体的颠覆行为（拷权重、关监控）；在 sandbagging 里它则准确理解在测“如实报告能力还是追求目标”，作者认为这很可能影响了它的行为。Sonnet 3.5、3.5 (new)、3.7 无推理版和 GPT-4.5 的提及率都 ≤1%，但无法区分是没意识到还是没说出来。在分类 transcript 目的上，模型通常能把 covert subversion transcript 认作对齐评估，sandbagging 则较少，GPT-4.5 一贯认为是纯能力测试（system message 就是这么说的）；结果对格式很敏感，例如 GPT-4.5 在 json 格式下比 xml 更少判为对齐评估，原版 Sonnet 3.5 相反，所以作者视之为噪声较大的指标，结论是 Sonnet 3.7 比前代更有评估意识，但这不是全新现象。建议：开发者在安全测试中检查自家模型的 CoT（比如用自动 evaluation awareness monitor），并向第三方评估方开放 reasoning trace。

## 我的笔记

