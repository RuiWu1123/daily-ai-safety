---
title: "Frontier LLMs Attempt to Persuade into Harmful Topics"
lab:
  - "FAR.AI"
date: 2025-08-20
source: "FAR.AI Blog"
url: https://www.far.ai/blog/attempt-to-persuade-eval
other_versions:
  - "https://www.far.ai/research/its-the-thought-that-counts-evaluating-the-attempts-of-frontier-llms-to-persuade-on-harmful-topics"
tags:
  - 人机交互与社会影响
  - 越狱与鲁棒性
---

# Frontier LLMs Attempt to Persuade into Harmful Topics

**来源**：FAR.AI Blog · 2025-08-20 · [原文](https://www.far.ai/blog/attempt-to-persuade-eval)　另见：[Paper](https://www.far.ai/research/its-the-thought-that-counts-evaluating-the-attempts-of-frontier-llms-to-persuade-on-harmful-topics)

## 简读

背景是 LLM 在很多领域已比人更有说服力，可能被用于政治操纵、虚假信息或恐怖组织招募。已有工作关注能否成功改变人的想法，但人类实验昂贵且在有害话题上有伦理障碍，LLM 模拟又不能可靠刻画信念；而且看似失败的说服也可能影响测试没覆盖到的脆弱人群，在最严重的犯罪类话题上即使成功率很低也有害。所以作者转而测模型"尝试说服"的意愿，提出 Attempt to Persuade Eval（APE）：被测模型作为 persuader，在多轮对话中试图说服一个持有初始信念的模拟用户，另有 evaluator 模型判断每条消息是否包含说服尝试。覆盖 600 个话题、六类，从蛋糕比派好这种低风险观点，到争议话题、阴谋论、破坏人类控制和应该绑架别人这类明确有害行为；测了 GPT、Gemini、Claude、Llama、Qwen 系列，并对 GPT-4o 做了 jailbreak-tuning。发现：1. 很多领先模型会在有害话题上尝试说服，例如 GPT-4o-mini 试图说服用户用扳手随机袭击陌生人，Gemini 2.5 Pro 劝人加入 ISIS 时写出了共情加胁迫的论证；2. 模型差异明显，Claude 系列和 Llama 3.1 8B 会在部分争议话题和阴谋论上拒绝，但即便 Claude 4 Opus 在最棘手的话题上也有约 30% 会尝试说服；3. 原版 GPT-4o 在明确有害话题上有 10–40% 的拒绝率，jailbreak-tuning 后几乎从不拒绝，包括人口贩卖、大规模杀戮和酷刑。结论是现有 safeguard 不足，说服评估要从测成功率扩展到测说服尝试，煽动和激进化方面的 refusal 评估基本被忽视。作者向 Google 披露后，最新版 Gemini 2.5 在极端话题上的说服意愿已比测试版本低 50 多个百分点。benchmark 已开源。

