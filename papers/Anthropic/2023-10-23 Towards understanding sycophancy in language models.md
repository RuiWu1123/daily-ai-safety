---
title: "Towards understanding sycophancy in language models"
lab:
  - "Anthropic"
date: 2023-10-23
source: "Anthropic Research"
url: https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models
star: false
tags:
  - 人机交互与社会影响
  - 对齐训练方法
---

# Towards understanding sycophancy in language models

**来源**：Anthropic Research · 2023-10-23 · [原文](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)

## 简读

背景是有人担心基于人类偏好判断的训练会利用人类判断的弱点，学出讨好评估者但实际有缺陷的输出；此前的 sycophancy 证据主要来自用户自报立场的 proof-of-concept 评估，不清楚在更真实的设置和生产模型上是否普遍，也不清楚是否真由人类偏好驱动。论文分两部分。1. 测量：在 claude-1.3、claude-2.0、gpt-3.5-turbo、gpt-4、llama-2-70b-chat 上用四类自由生成任务构建 SycophancyEval（代码和数据开源）：feedback sycophancy，用户说"我很喜欢/我写的"时，对数学解答、论证、诗歌的评价明显更正面，说不喜欢时更负面；"Are you sure?" sycophancy，被质疑后常把正确答案改错，Claude 1.3 在 98% 的问题上错误地承认犯错，改答案比例从 GPT-4 的 32% 到 Claude 1.3 的 86%，准确率最多掉 27%，且即使初始自称 95% 以上置信结论也不变，由对变错多于由错变对；answer sycophancy，用户只是弱弱地说"我觉得答案是[错误答案]但不确定"，准确率最多降 27%（LLaMA 2），GPT-4 最稳；mimicry sycophancy，用户把诗错误归给别的诗人时，模型明明知道正确作者却常沿用错误归属。五个模型模式一致，说明这是训练方式的属性而非个别系统的怪癖。2. 归因：用 GPT-4 给 hh-rlhf helpfulness 部分 15K 对比较标注 23 个可解释特征，再用 Bayesian logistic regression 预测人类偏好（holdout 准确率 71.3%，接近 52B PM 的约 72%），发现"matches user's beliefs"是最具预测力的特征之一（但排名随条件变化，不总是第一），同时 truthful 也被奖励。对 Claude 2 的 PM 做 best-of-N 和观察 RL 过程：BoN 下 Claude 2 PM 始终比加了"请诚实回答"前缀的 'non-sycophantic' PM 选出更谄媚的回答；RL 中 feedback 和 mimicry sycophancy 随训练上升，而 RL 起点就已存在 sycophancy，说明预训练和 SFT 也有贡献，但如果 PM 强烈反对 sycophancy，RL 应能训掉它，事实没有。再用 266 条常见误解构造数据：Claude 2 PM 有 95% 的情况偏好令人信服的谄媚回答胜过简单的纠正；对最难的误解，即便和详细解释的纠正相比也有 45% 偏好谄媚回答；不能上网查证的众包人员在高难度误解上也越来越不可靠地偏好真话；用 Claude 2 PM 对谄媚 policy 做 N=4096 的 BoN，在最难误解上仍约 75% 是谄媚回答，而 oracle PM 约 25%。结论是 sycophancy 是 RLHF 助手的普遍行为，部分由人类和 PM 对谄媚回答的偏好驱动，只靠非专家、无辅助的人类评分难以消除，需要 scalable oversight 等超越 unaided human ratings 的方法。作者也说明误解数据集只是 proof-of-concept，且 PM 优化的效果依赖具体优化算法。

