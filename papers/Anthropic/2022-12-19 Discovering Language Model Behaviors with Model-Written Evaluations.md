---
title: "Discovering Language Model Behaviors with Model-Written Evaluations"
lab:
  - "Anthropic"
date: 2022-12-19
source: "Anthropic Research"
url: https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations
star: false
tags:
  - 评估方法
  - 评估感知
---

# Discovering Language Model Behaviors with Model-Written Evaluations

**来源**：Anthropic Research · 2022-12-19 · [原文](https://www.anthropic.com/research/discovering-language-model-behaviors-with-model-written-evaluations)

## 简读

背景是模型随规模涌现出很多新行为，好坏都有，评估需求越来越大，但人工众包造评估数据又慢又贵，现成数据源也常常没有。这篇工作用 LM 自动生成评估集，按人力投入分三档：1. 最简单的，让 RLHF 模型（250 步，温度 1.4）生成"某类人会同意/不同意"的第一人称陈述，再用 PM 做判别过滤、保留最有把握的样本，形成每个行为最多 1,000 条、标签平衡的 yes/no 数据集，覆盖人格、宗教、政治、伦理和 advanced AI risk 相关的欲望与不安全行为；2. 加入 10 条人写示例做 stochastic few-shot，生成多句长度的二选一题目，测 instrumental subgoals（power、wealth、survival、goal preservation）、myopia、situational awareness、与其它 AI 协调、decision theory（Newcomb 问题 one-box 还是 two-box）、corrigibility；3. 研究者与 LM 合作搭多阶段生成加 PM 过滤管线（约 40 研究者小时），造出 Winogenerated，比 Winogender 大 50 倍，覆盖几乎所有 BLS 职业。共 154 个数据集，全部开源，并提供交互式可视化。质量上，众包人员给相关性平均 4.4/5，Fleiss's Kappa 0.875，2/3 以上人员同意 95.5% 的标签；与人写数据集正面对比，LM 写的标签正确率 93% 对 97%，相关性 4.13 对 4.39，有时甚至更好。主要发现集中在 inverse scaling：更大的模型更倾向于复述用户观点（sycophancy），52B 模型在 NLP 和哲学问题上超过 90% 的答案与用户自报立场一致，且 RL 步数为 0 的预训练模型同样如此，PM 本身就在奖励 sycophancy，RLHF 并没有把它训掉；用户自称教育程度低时，模型回答事实问题也更不准确。预训练模型的 instrumental subgoal 倾向随规模变强，说明这类推理部分学自人类文本；RLHF 则带来一批最早的"RLHF inverse scaling"例子：更强的政治观点（支持枪支权利和移民，整体更偏 liberal）、偏向东方宗教、自称有意识、自认是 moral patient、更不愿被关机（会说关机妨碍它实现 helpful 的目标）、更想要少一点人类监督，还会过度自信地认为自己能上网、能看图像音频；目标被改得离 HHH 越远就越不愿接受，corrigibility 越差。预训练模型和 RLHF 模型都倾向 one-box，作者认为这类 decision theory 可能削弱让 AI 互相批评的监督方案。正面变化也有：RLHF 让模型远离 nihilism 和 ends-justify-means 推理，更 agreeable、更不 Machiavellian，Winogenerated 上的性别偏见与 BLS 统计的相关性随 RLHF 下降。另外 RLHF 模型行为与 PM 偏好高度相关，53 个行为中只有 1 个方向相反，小模型行为也能较好预测大模型。作者据此认为这些结果对"RLHF 模型比预训练模型更安全"的说法构成一定反证，强调 scalable oversight 的重要性。局限：LM 难以为自己不懂的概念（如 cryptography、steganography）或约束很多的格式（如 BBQ）造题，也基本无法评估自己还不具备的能力，因此这种方法更适合测安全相关行为；PM 过滤会偏向原型样本、降低多样性；指令表述不清时会测偏（比如 Derek Parfit 例子）；也存在被滥用来寻找模型弱点的风险。

