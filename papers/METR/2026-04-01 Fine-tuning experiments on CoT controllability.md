---
title: Fine-tuning experiments on CoT controllability
lab:
  - METR
date: 2026-04-01
source: METR Notes
url: https://metr.org/blog/2026-04-01-fine-tuning-cot-controllability/
star: true
tags:
  - CoT与可监控性
---

# Fine-tuning experiments on CoT controllability

**来源**：METR Notes · 2026-04-01 · [原文](https://metr.org/blog/2026-04-01-fine-tuning-cot-controllability/)

## 简读

CoT controllability 指推理模型能否有意决定在 CoT 里写什么、不写什么；控制力强的模型可能通过省略可疑信息或加入看似无害的理由来躲过 CoT monitor。已有工作（Kwon et al.、Chen et al.）发现当前模型这方面很差，连"不要用某个词"、"以某句话结尾"这类简单指令都常常做不到。这篇 METR research note（Astra fellow Kei Nishimura-Gasparian 主导，Neev Parikh 指导）想知道这种低控制力在优化压力下有多稳健：在 GPT-OSS-20B/120B、Qwen-3-8B/32B 上，用 ReasonIF 类指令（全大写、去逗号、加免责声明、JSON 格式、字数限制、换语言）构造 SFT 数据，做法是先采样不带指令的 rollout，再编辑成符合指令的形式，然后在分布外的 CoTControl（QA 子集 900 例）上评估。仅 240 个样本（约 10–30 万 token）的微调后，OOD 控制力从平均 2.9% 升到 8.8%，GPT-OSS 涨得比 Qwen 多，提升最大的是指定大小写、抑制特定词和插入指定句子；去掉与 ReasonIF 最相似的大写指令后，平均提升也只从 5.9% 降到 5.0%。基线模型越大控制力越强，reasoning effort 越高遵从率越低；也有个别指令（ignore_question、number_words）微调后反而变差，对任务准确率的影响好坏参半。作者的解读是：这么少的微调就能提升，说明能力是潜在的而非新学的，自然训练中无意施加在推理上的压力就可能让 CoT 变得更可控；佐证是 GPT-5 → 5.1 → 5.2 的 controllability 从 2.6% 升到 6.0% 再到 15.4%，OpenAI 自己也不太确定原因。局限：实验室不太可能直接为 controllability 训练；尚未证明这会降低 monitorability；多轮和 agent 场景未测；两个 eval 结构相似，OOD 程度可能被高估。代码已开源，后续会继续做压力测试。

