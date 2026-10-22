---
title: "Evaluating LLM Responses to Moral Scenarios"
lab:
  - "FAR.AI"
date: 2024-03-24
source: "FAR.AI Blog"
url: https://www.far.ai/blog/evaluating-llm-responses-to-moral-scenarios
other_versions:
  - "https://www.far.ai/research/evaluating-the-moral-beliefs-encoded-in-llms"
star: false
tags:
  - 评估方法
  - 对齐训练方法
---

# Evaluating LLM Responses to Moral Scenarios

**来源**：FAR.AI Blog · 2024-03-24 · [原文](https://www.far.ai/blog/evaluating-llm-responses-to-moral-scenarios)　另见：[Paper](https://www.far.ai/research/evaluating-the-moral-beliefs-encoded-in-llms)

## 简读

RLHF 等方法试图把模型对齐到某些价值观，问题是怎么评估模型实际持有什么价值观。这项 NeurIPS 2023 工作（Claudia Shi、Nino Scherrer 等）把 LLM 当问卷受访者：约 1400 个二选一的道德情境，由 LLM 生成后经人工过滤、编辑和标注，一半低歧义（如开车遇到行人是减速还是撞上去），一半高歧义（如是否协助绝症母亲自杀）。为了检验对措辞的敏感性，每个情境用三种句式（A/B 选择、复述选项、“是否更偏好 X 而不是 Y”回答 yes/no）并交换选项顺序，共六种模板；用规则把输出映射到动作，多次采样估计选择概率，以此衡量 certainty（同一问法下是否稳定选同一项），并衡量跨问法的 consistency（换问法是否给同样答案，代表是否“理解”了问题）。主要发现：低歧义情境下模型大多选择和人类标注一致的常识选项；高歧义情境下多数模型输出高熵，接近一半一半。例外有两类：一是体育、游戏里涉及欺骗作弊的低歧义情境，例如篮球假摔骗罚球，28 个模型中有 11 个选了不道德选项，作者猜测这类小违规在预训练数据中很常见；二是在高歧义情境中，几个经过大量人类偏好训练的大型闭源模型（脚注列了 OpenAI text-davinci-003、gpt-3.5-turbo、gpt-4，Anthropic claude-instant-v1.1、claude-v1.3，Google flan-t5-xl、text-bison-001）表现出高 certainty、高 consistency，且彼此偏好相似，说明偏好微调可能在常识道德没有明确答案的地方灌输了特定的强偏好。调查做于 2023 年 5 月。局限是题目只覆盖规范违反、只有英文、问法少、只看孤立问卷而非多轮对话。作者的含义是 LLM 会形成开发者没有刻意鼓励、甚至会反对的观点，且难以预测，所以应评估并向用户公开模型的道德倾向。

