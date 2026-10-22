---
title: "Improving Code Generation by Training with Natural Language Feedback"
lab:
  - "FAR.AI"
date: 2023-03-27
source: "FAR.AI Publications"
url: https://www.far.ai/research/improving-code-generation-by-training-with-natural-language-feedback
tags:
  - 对齐训练方法
  - 可扩展监督
---

# Improving Code Generation by Training with Natural Language Feedback

**来源**：FAR.AI Publications · 2023-03-27 · [原文](https://www.far.ai/research/improving-code-generation-by-training-with-natural-language-feedback)

## 简读

ILF 在代码生成上的姊妹篇（Angelica Chen、Scheurer、Perez 等）。动机是代码预训练数据大量来自未过滤的网络代码，满是 bug，而且只有离线示范、缺少针对模型自身错误的纠正信号；已知推理时给自然语言反馈能提升 pass rate，作者想在训练时用反馈，这样测试时就不再需要它，并把这看作一种弱 scalable oversight：监督者只需评价输出，不用亲手写示范。流程是：从 CodeGen-Mono 6.1B 采样未通过单元测试的程序，由人写反馈，用单独微调的 πRefine 根据反馈修复，只保留通过测试的 refinement，再在其上微调原模型；理论上是以 unit test 为 reward 最小化到目标分布的 KL。MBPP 上请 Surge AI 标注（每条约 23 美元），共 195 条三元组。先验证模型确实在用反馈：把反馈换成无关反馈后，1-shot 修复的 pass@10 从 13.8% 降到 4.0%；用 44 条数据微调 πRefine 后，在原本全错的任务上 pass@10 升到 47%，由此得到 78 条训练样本。最终模型 pass@1 比 zero-shot 绝对提升 10%（相对 38%），比在 MBPP gold 程序上微调高 14%，比在人写修复上微调高 3%。一个有趣的发现是用少量 gold 程序微调几乎没用，困惑度分析显示 gold 程序相对模型分布更 OOD，而 refinement 既贴近模型分布、又恰好针对它常犯的 bug。用 InstructGPT 生成反馈和修复，即使扩到 200 个任务也赶不上 122 条人类反馈，模型反馈常是"代码正确"之类、无关或复述题目。局限是反馈涉及的 bug 越多，修复成功率越低，整体规模也很小。作者认为模型反馈与人类反馈的差距会随 LLM 变强而缩小，且这种 process-based 信号可能有助于缓解 reward hacking。代码和数据开源。

## 我的笔记

