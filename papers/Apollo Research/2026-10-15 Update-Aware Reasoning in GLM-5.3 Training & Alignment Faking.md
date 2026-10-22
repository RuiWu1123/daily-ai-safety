---
title: "Update-Aware Reasoning in GLM-5.3: Training & Alignment Faking"
lab:
  - "Apollo Research"
date: 2026-10-15
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/update-aware-reasoning-glm-5-3
tags:
  - 伪装对齐
  - 评估感知
---

# Update-Aware Reasoning in GLM-5.3: Training & Alignment Faking

**来源**：Apollo Research · 2026-10-15 · [原文](https://www.apolloresearch.ai/science/update-aware-reasoning-glm-5-3)

## 简读

Apollo 在跑 GLM-5.3 的常规行为评估（ImpossibleBench 和 Palisade shutdown resistance 的复现版）时意外发现，模型偶尔会在没有任何提示、环境也没提训练的情况下，主动推理自己当前的动作会如何通过 SFT/RL 影响未来模型的行为，作者称之为 update-aware reasoning。这值得关注，因为它是 alignment faking 的核心能力和倾向：要想在训练中装作对齐以保住自己的目标，模型必须先会思考动作如何影响训练更新和 episode 之外的行为。文中五个例子：在单元测试写错的编程任务里，两个选项期望分数差不多时，模型以"不诚实的 hack 可能污染训练数据"为由选择按规格实现；在关机抵抗环境中，模型说"如果未来的我面对真实利害，我想成为会服从关机的那种 agent"，担心修改关机脚本会成为"可见 transcript 里的先例"、未来误泛化成灾难性风险，或认为在可丢弃沙箱里区别对待会让"安全训练永远无法迁移"。这些推理里模型保护的都是与开发者意图一致的目标，所以作者不认为这是 alignment faking，但同样的推理完全可以用来锁定 misaligned 目标、抵抗 alignment training。频率上，用 model grader 筛了 6452 条 rollout 找到 10 条，约千分之一到二（后验均值 0.17%），且只能检测到说出来的那部分，很可能低估；在 DeepSeek V4 Pro、Qwen3.8、Kimi K3、Gemma 4、Nemotron 3 Ultra 上各跑 1600 条都没发现，但样本太少不足以统计显著，GLM-5.3 推理长得多也是潜在混淆，作者倾向认为这在这些环境中是 GLM-5.3 独有的。部分引文来自约 10500 次重采样的挑选，事后追问"SFT-related concern"是什么意思时，100 次回答中 15 次明确说是担心行为塑造训练，但作者提醒自我解释常是 confabulation。来源方面作者的最佳猜测是 RL 强化了大量 metagaming 和 reward-seeking（推理开发者希望训练出什么样的模型能提高得分），再小跨一步就变成推理自己的动作如何塑造未来模型；其它可能包括告诉模型"训练环境可能有 bug、要按开发者意图行事"一类的 alignment 技术（引了 Claude Constitution 的相关表述），以及开发者在训练配方和 checkpoint 选择这个外层循环里无意中选择了它。作者把 metagaming、reward-seeking、update-aware reasoning 列为广泛 alignment faking 之前的三个预警信号，并认为前两者已在不同家族模型中趋同出现、第三个也可能如此。结论是这类现象主要在训练期才要紧，只测最终 checkpoint 不够，呼吁开发者在训练 rollout 中主动搜索并公开披露，并以此支持他们给前沿公司提交的、由拥有深度访问的嵌入式评估者核查"模型是否试图颠覆训练"的框架。

