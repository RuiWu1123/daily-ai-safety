---
title: "Would This Change Your Answer? Evaluating Explanations of LLM Behavior in the Wild with Counterfactual Experiments"
lab:
  - "Anthropic"
date: 2026-08-21
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/chive/
tags:
  - 可解释性
  - CoT与可监控性
  - 评估方法
---

# Would This Change Your Answer? Evaluating Explanations of LLM Behavior in the Wild with Counterfactual Experiments

**来源**：Anthropic Alignment Science Blog · 2026-08-21 · [原文](https://alignment.anthropic.com/2026/chive/)

## 简读

背景是 interpretability、CoT faithfulness 等方向都在"解释模型行为"，但真实原因通常未知，解释没法直接检验。作者采用 counterfactual simulatability 视角：好的解释应该让你能预测模型在相关反事实输入上的行为（比如"Gemma 写错代码是被参数名误导"预测改名后错误消失）。为此提出 CHIVE（Counterfactual Hypothesis Investigation Via Edits），一个 agentic pipeline：1. Sample，对研究者指定的 prompt 集每个采样 30 次；2. Screen，investigator 模型读回复标出意外行为；3. Investigate，investigator agent 做 5–15 个反事实 prompt 编辑实验，重采样并测量行为频率变化；4. Verify，独立 judge 评估实验对解释的支持程度。数千个 investigation 各产出一个开放式解释（不当作 ground truth）和一组实测结果的反事实实验（作为评测标签）。用途一是评测 interpretability 工具：predictor agent（主实验用 Claude Opus 4.8）看到 transcript、行为和一个"某个 prompt 编辑会改变行为"的 claim，输出概率；工具组额外可以对目标模型激活做 5 次只读调用，工具是 activation oracle、natural-language autoencoder（NLA）和 SAE，都是在以往 fine-tuned 模型 auditing game 里有 uplift 的。结果三者都不超过只看 transcript 的 baseline，且在两个目标模型、三个 predictor 模型家族、超参扫描和手动/自动改进工具使用的尝试下都成立。原因分析：工具不是被忽略，偶尔确实有帮助（NLA 读出"模型可能在生成 min 到 max 之间的随机整数"），但会被漏掉关键信息或误导的情况抵消；工具输出几乎总是同时描述 prompt 特征和行为，可这两者 transcript 里本来就看得到，而它们几乎从不明确陈述两者之间的因果关系，predictor 只能从成千上万 token 的相关性线索里推因果。作者对 Anthropic 自己在 system card 里用这些工具的做法做了反思：本评测是可检验的 proxy，存在分布偏移——这里的行为大多简单，而 system card 里的行为更复杂、可能有更清晰的表征；应用中常做的是关于"模型相信什么"的 claim，而非反事实；但这类 claim 往往隐含反事实意味（"模型认为绕过权限是正当的"之所以让人安心，是因为暗示否则不会这么做），本文结果说明读激活的工具对这种因果 claim 证据有限，应当用干预实验验证，且 system card 案例大多没有 transcript-only 对照，分不清多少证据真来自工具。结论是基于工具输出的因果 claim 目前只应被视为提示性证据。用途二是训练数据：用这些实验训练 Qwen3-8B 和 Qwen3.5-397B-A17B 预测 prompt 编辑是否改变自己的行为，泛化到训练中从未出现的 hint setting（"斯坦福教授认为答案是 B"那类）——两者都显著超过 base model，也泛化到 held-out 和 OOD 来源的 investigation；训练生成开放式自我解释的效果较弱且混杂。代码和示例 investigation 已公开。

## 我的笔记

