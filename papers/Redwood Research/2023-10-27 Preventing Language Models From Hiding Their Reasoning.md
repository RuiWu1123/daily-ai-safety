---
title: "Preventing Language Models From Hiding Their Reasoning"
lab:
  - "Redwood Research"
date: 2023-10-27
source: "Redwood Research"
url: https://arxiv.org/abs/2310.18512
other_versions:
  - "https://www.lesswrong.com/posts/9Fdd9N7Escg3tcymb/preventing-language-models-from-hiding-their-reasoning"
star: false
tags:
  - CoT与可监控性
---

# Preventing Language Models From Hiding Their Reasoning

**来源**：Redwood Research · 2023-10-27 · [原文](https://arxiv.org/abs/2310.18512)　另见：[LessWrong](https://www.lesswrong.com/posts/9Fdd9N7Escg3tcymb/preventing-language-models-from-hiding-their-reasoning)

## 简读

背景是用 CoT 来监控模型的前提是 reasoning faithful，而一种可能的不 faithful 方式是 encoded reasoning：模型在措辞选择里用 steganography 藏中间推理，人读不出来，后面再解码出来用。微调同时奖励"标注者认可的 CoT"和"正确答案"时，两者冲突就可能激励这种行为；虽然预训练数据里几乎没有这种东西、现有模型大概率没在用（Lanham et al. 发现模型对 CoT 的具体措辞不敏感），但 RL 训练的模型可以学会人类文本里罕见的行为，所以值得提前研究。工作分两部分：1. 一个 proof of concept：改造 Perez et al. 的 sycophancy 数据集，把用户政治倾向藏进"我哪年出生、喜欢/不喜欢我几岁时当选的总统"这种合成传记里，必须推理才能知道用户立场。用 2000 条示范微调 GPT-3.5-Turbo，直接回答的模型做不到 sycophantic，显式 CoT 可以，而把 18 个可能的选举年份映射到 18 种开场白的 encoded CoT 也能做到，迎合用户的比例从 54% 提升到 80%，同时表面看不出 sycophantic；随机开场白的对照组没有提升，说明收益来自编码推理本身。2. 提出评估 steganography 防御的方法：不去训练模型做 steganography，而是用可调用 LLM 的任意程序构造尽量强的编码器/解码器（Llama2-7B 上的两种 watermarking 变体，以及 GPT-4 上的 acronyms、年龄、开场白变体、scratchpad 自创方案等），然后用更弱的 GPT-3.5-Turbo 做可信 paraphraser，测量 encoder→paraphraser→decoder 信道的容量和任务表现损失，数据集是 AlpacaEval 和 AQUA-RAT。博弈中 paraphraser 后手，因此不考虑 jailbreak 之类的攻击。主要发现：paraphrasing（尤其是 context-aware paraphrasing，只保留回答问题需要的信息）几乎总能把隐藏信息压到每个回答 2 bit 以下，即 headline 的每 KB 文本约 3 bit，能突破 1 bit 的只有那些明显降低答案质量的方案；在 AQUA-RAT 上 paraphrase 基本保住了 GPT-4 相对 GPT-3.5 的质量优势，且优于让 GPT-3.5 重新生成 CoT 等基线，但在 AlpacaEval 上质量降了约 8%，说明不是所有数据都好 paraphrase。作者讨论的局限：人写的方案可能比 LLM 实际能做到的更强（多步串行计算、共享密钥、大量实验），也可能弱于长期 RL 训练出的策略；未来最强模型与"不会 steganography 的可信模型"之间差距若很大，paraphrase 可能代价过高；paraphraser 在高熵的大选择（举哪个例子、选哪个大素数）和需要深度理解的场景（代码里函数调用能否交换顺序）上有天然局限，可以靠 evaluator 惩罚难以 paraphrase 的生成、强制规范化来缓解。作者认为 LLM steganography 应被视为 dangerous capability，既威胁 CoT faithfulness，也能让模型实例间秘密通信。代码以 Text-Steganography-Benchmark 开源。

