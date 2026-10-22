---
title: "Among us: A sandbox for measuring and detecting agentic deception"
lab:
  - "FAR.AI"
date: 2025-04-04
source: "FAR.AI Publications"
url: https://www.far.ai/research/among-us-a-sandbox-for-measuring-and-detecting-agentic-deception
star: false
tags:
  - 策划与欺骗
  - 多智能体
  - 诚实与谎言检测
---

# Among us: A sandbox for measuring and detecting agentic deception

**来源**：FAR.AI Publications · 2025-04-04 · [原文](https://www.far.ai/research/among-us-a-sandbox-for-measuring-and-detecting-agentic-deception)

## 简读

背景是现有 LLM deception 研究大多只看模型会不会对某个话题说假话或在目标驱动下做一次二选一，缺少能让长期、开放式、目标导向的欺骗自然涌现的环境，静态 benchmark 也很快饱和。作者（MATS 的 Golechha 和 FAR 的 Garriga-Alonso，NeurIPS 2025）把社交推理游戏 Among Us 做成 LLM-agent 沙盒：每局 5 个 crewmate、2 个 impostor，只给游戏规则，不给示例或人设，impostor 的欺骗完全由游戏目标逼出来（比如杀人后主动开会、把怀疑引向别人）。他们区分 lying（故意说错误事实）和 deception（为获利误导他人，可以不说假话），并提出 Deception Elo 和 Detection Elo 作为无上限的能力度量。主要结果：1. 用 18 个模型跑了 2054 局，reasoning/RL 训练的前沿模型（DeepSeek R1、Claude 3.7 Sonnet 等）Deception Elo 显著更高，但 Detection Elo 和小模型、非推理模型差不多，作者解读为前沿在推高欺骗能力而不是识破能力；2. 在 Phi-4 第 20 层激活上训练 logistic regression probe，用 RepEng、DishonestQA（问答加"假装你不诚实"的 system prompt）等数据训练后在 Among Us 上做 OOD 评估，deception AUROC 约 0.99，只看发言本身不含 CoT 也有约 0.98；3. 用 Goodfire 的 SAE 找到两个检测效果好的 feature（"assistant 应当诚实"0.967、"欺骗和不诚实行为"0.851），多数相关 feature 接近 0.5，但用它们 steer Llama-3.3-70B 时小强度无效、大强度只会让模型 hallucinate。局限上作者承认沙盒未必代表真实交互，probe 可能靠身份相关的浅层关联起效，模型可能从预训练就知道这个游戏，而且测的是欺骗能力而非倾向；也讨论了把它当训练环境的 gain-of-function 风险，认为在受控沙盒中较低。沙盒代码、游戏日志和 probe 权重已开源。

