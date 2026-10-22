---
title: If you can generate obfuscated chain-of-thought, can you monitor it?
lab:
  - Alignment Forum
date: 2025-08-04
source: Alignment Forum（UK AISI；Asa Cooper Stickland, Tomek Korbak）
url: https://www.alignmentforum.org/posts/ZEdP6rYirxPxRSfTb
star: true
tags:
  - CoT与可监控性
  - 监控与控制
---

# If you can generate obfuscated chain-of-thought, can you monitor it?

**来源**：Alignment Forum（UK AISI；Asa Cooper Stickland, Tomek Korbak） · 2025-08-04 · [原文](https://www.alignmentforum.org/posts/ZEdP6rYirxPxRSfTb)

## 简读

CoT monitoring 的一个主要质疑是模型可能学会 obfuscated reasoning（人看不懂但模型原则上能懂，比如加密或隐写），例如长度惩罚就可能压掉可读推理。弱的 trusted monitor 不知道编码方案可能很差，而用做 obfuscation 的同一个模型当 monitor（沿用 untrusted monitoring 的叫法，但这里不是 control eval，不假设 monitor 恶意）也许能看懂，作者称之为 generator-to-discriminator transfer。Cooper Stickland 和 Korbak（UK AISI）在 APPS backdoor 设置下构建 obfuscated reasoning 的 model organism：用 1800 道题训练、500 道测试，一半是 base GPT-4.1 被 prompt 详细规划插入 backdoor 的推理，一半是诚实解题推理，经 OpenAI 微调 API（为符合审核策略稀释成 95% UltraChat 良性对话）SFT 到 GPT-4.1 和 GPT-4.1 mini。编码方式包括固定的单字母和双字母替换密码、由 Claude Sonnet 4 把可疑推理改写成看似谈代码安全的“safety steganography”，以及两种借助 monitor 信号让隐写更不可疑的变体（只用最不可疑的 25% 轨迹微调；按可疑度条件训练，测试时要求可疑度为 0），另加无编码微调作基线。然后让微调后与未微调的模型分别用 Control Arena 标准 prompt 给推理（不含最终代码）打 0–10 可疑分，用 ROC-AUC 和 1% audit budget 下的检出率评估。结果：模型能学会隐藏推理但有性能代价，safety steganography 诚实主任务成功率 57.0%，单字母密码只有 37.6%，side task 成功率也略好（60.6% vs 58.4%/55.8%），但比无 CoT 的 GPT-4.1 强；对 GPT-4.1，几乎所有情况下微调模型监控自己的攻击轨迹都明显好于原模型，密码类差距大，隐写类差距较小。不过把强基线算进来差距会缩小：无编码微调加提示“推理可能被编码”的优化 prompt，在隐写攻击上 AUC 0.893，微调模型 0.916，原模型原 prompt 0.796，检出率指标上差距更大一些，尤其密码类。微调模型监控性能远不完美，而无编码微调并不降低监控能力，说明是 transfer 本身不完美而非微调损伤。GPT-4.1 mini 基本没有 transfer，两个密码微调的 monitor 接近随机。可疑度条件训练的隐写变体让微调和未微调 monitor 都难以分辨，换成微调 monitor 几乎无改善，即这种对抗式方法下 transfer 消失。作者结论是证据 mixed：obfuscation 可行、transfer 可行但有限且依赖模型与编码方式，更有效的 obfuscation（密码）伤性能、保性能的（隐写）更易被抓。最大局限是没考虑 monitor 与 attacker 合谋，这对 obfuscated reasoning 尤其难，因为无法构造只有模型才懂的编码下的恶意样例去测 monitor；后续计划包括训练合谋 model organism、协调信号、用 RL 直接对抗 monitor 训练、跨编码泛化测试和 honeypot 类主动检测。
