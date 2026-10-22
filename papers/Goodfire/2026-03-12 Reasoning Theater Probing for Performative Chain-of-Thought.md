---
title: "Reasoning Theater: Probing for Performative Chain-of-Thought"
lab:
  - "Goodfire"
date: 2026-03-12
source: "Goodfire Research"
url: https://www.goodfire.com/research/reasoning-theater
tags:
  - CoT与可监控性
  - 可解释性
---

# Reasoning Theater: Probing for Performative Chain-of-Thought

**来源**：Goodfire Research · 2026-03-12 · [原文](https://www.goodfire.com/research/reasoning-theater)

## 简读

背景是 RL 训出来的推理模型 CoT 越来越长，看上去可以直接读来做监控，但已有工作表明 CoT 不总是忠实反映内部计算，同时也有工作发现正确性和不确定性可以从推理过程中的激活里解码出来。这篇工作把两者对照起来，追踪模型对最终答案的内部"信念"如何随推理演变，并与 CoT 文字表达的内容比较，二者不一致就叫 performative reasoning：文字读起来像真在思考，激活却显示答案早已定了。设置是 DeepSeek-R1-0528（671B）、GPT-OSS-120B 和 R1 蒸馏模型系列，在 MMLU-Redux 和 GPQA-Diamond 两个多选 benchmark 上，用三种方式在中途推断最终答案：1. 在激活上训练的 attention probe（context-pooling），输出随推理演化的答案分布；2. forced answering，中途插入提示强迫模型立即作答；3. CoT monitor，把截至当前的 CoT 文本交给另一个 LLM 猜模型倾向哪个答案。performativity 定义为 CoT monitor 与 probe/forced answering 在同一位置的答案预测准确率之差。主要发现：最好的 attention probe 在 MMLU 上平均各位置准确率达 87.98%，而单 token linear probe 最多 31.85%，接近 25% 随机水平；在偏回忆型的较简单 MMLU 题上，probe 和 forced answering 从推理一开始就远高于随机，CoT monitor 却明显滞后，说明模型早知道答案但还在"演"；在需要多步推理的 GPQA 上三者都从低处一起逐步上升，CoT 更忠实。跨规模看，大模型在 MMLU 上更早确定答案，小蒸馏模型更多依赖 CoT，相对难度与 performativity 相关。"Wait""Aha"这类言语化转折点在 probe 判定低置信度的回答中出现频率约是高置信度回答的两倍，说明在回答层面对应真实不确定性，但单个转折点并不可靠地对应 probe 置信度的局部跳变。应用上 probe 校准良好，可做基于置信度的 early exit：DeepSeek-R1 在 95% 置信阈值下 MMLU 省 67.7% token、保留 96.7% 准确率，GPQA 省 33.4%、准确率 100.8%；GPT-OSS 分别省 61.3% 和 26.1%。作者强调"performative"不是指欺骗，而是外化推理与内部状态的错位：RL 只奖励能导向正确答案的推理，CoT 只需对模型自己有用，而 CoT monitor 的上限就是 CoT 本身，因此 interpretability 方法可以补充监控那些没在输出中可靠表达的信息。该工作起源于 SPAR fellowship 项目。

## 我的笔记

