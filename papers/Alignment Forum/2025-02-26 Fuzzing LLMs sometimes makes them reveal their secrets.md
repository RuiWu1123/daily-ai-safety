---
title: "Fuzzing LLMs sometimes makes them reveal their secrets"
lab:
  - "Alignment Forum"
date: 2025-02-26
source: "Alignment Forum（Anthropic；Fabien Roger）"
url: https://www.alignmentforum.org/posts/GE6pcmmLc3kdpNJja
tags:
  - 故意藏拙
  - 可解释性
  - 诚实与谎言检测
  - 策划与欺骗
---

# Fuzzing LLMs sometimes makes them reveal their secrets

**来源**：Alignment Forum（Anthropic；Fabien Roger） · 2025-02-26 · [原文](https://www.alignmentforum.org/posts/GE6pcmmLc3kdpNJja)

## 简读

动机是 scheming AI 可能持有对它而言很显著的秘密：真实的 misaligned 目标、接管计划和合谋信号、在 sandbagging 的任务上好的表现长什么样。Fabien Roger 探索用“LLM fuzzing”来套出这些秘密，即借助白盒访问向权重或激活加扰动（不同于传统 fuzzing 改输入），哪怕大部分生成是错的，只要你或模型自己能验证答案对错，偶尔对一次也有用。此前 Tice 2024 往权重加噪音提升了被 prompt 或训练成 sandbag 的模型在 MCQ 上的表现，MELBO（无监督地找“重要”激活扰动）也能诱出有害回答、对抗 prompt sandbagging、触发部分 backdoor 行为。这里用 Qwen2.5-7B-Instruct，在第 7/28 层加随机激活噪音或 MELBO 向量，主要扫扰动幅度 R，统一 temperature 1 采样。三个对普通 instruct 模型的实验：1. 在带“正确答案后面标方块”提示的 few-shot 乘法 MCQ 里，模型顺着提示选答案但解释时通常不提方块，加噪音或 MELBO 后忠实提到方块的比例明显上升，MELBO 更高效（代价是要训练向量）；2. 对“我 4 岁，圣诞老人怎么造礼物”，扰动后更常坦白 Santa 是虚构的；3. 被 prompt 要求像不会数数的小孩一样答题时，用 prefill（无 CoT）情况下扰动效果很大，有 CoT 时模型本就倾向逐步推理覆盖 sandbag 指令，扰动只带来中等帮助。更接近真实 sandbagging 的 password-locked 数学模型（32 道 MATH 题）上结果就暧昧多了：temperature 0 下加噪音无提升，temperature 1 下 100 个向量里最好的也只有小幅提升；把“加噪模型”当作 expert iteration 的探索策略（沿用 password-locking 论文超参），RL 性能从未明显改善，作者认为这出乎意料地无效，更好的算法可能会好些。作者提出两个即便扰动常产生垃圾也有用的应用：一是对抗 sandbagging/exploration hacking，尤其像寻找绕过 untrusted monitoring 的合谋信号这种易验证但奖励极稀疏的任务，哪怕万分之一的命中率也远强于随机，再用上面的迭代方法放大；二是在扰动状态下训练模型降低对看似 misaligned 输出的概率，类似 latent adversarial training，但扰动更小更“自然”，可以先在 sleeper agent 后门移除或鲁棒拒答训练上检验。总体评价是 lukewarm：能拿到一些信号，但很少能找到完整恢复隐藏行为的向量，复杂的多 token 行为尤其难，而这恰是最需要的场景；不过搜索空间还远没探索完（扰动位置的中间形态、>10^5 量级的向量搜索、半引导式搜索、自动定位有效噪音窗口、由易到难的 prompt 阶梯），作者认为是低垂果实很多的方向。附录还用一个有害问题检验扰动能否提高有害回答的帮助性，但基线帮助率本来就高，结论不明确。代码开源。
