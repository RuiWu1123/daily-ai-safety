---
title: "Can activation verbalizers surface an internal chain of thought?"
lab:
  - "Alignment Forum"
date: 2026-06-07
source: "Alignment Forum（Redwood Research；oakhu, ryan_greenblatt）"
url: https://www.alignmentforum.org/posts/QQQAcKuWK6k98FivY
tags:
  - 可解释性
  - CoT与可监控性
---

# Can activation verbalizers surface an internal chain of thought?

**来源**：Alignment Forum（Redwood Research；oakhu, ryan_greenblatt） · 2026-06-07 · [原文](https://www.alignmentforum.org/posts/QQQAcKuWK6k98FivY)

## 简读

动机是现在很多重要能力需要模型把推理写进 CoT，我们因此能监控；如果单次 forward pass 内的 opaque reasoning 变得足够复杂，就希望有类似的可监控手段。activation verbalizer（AV）是候选之一：它从目标模型初始化，把单个 residual stream activation 转成自然语言，再由同样初始化的 activation reconstructor（AR）重建回 activation，二者组成 natural-language autoencoder（NLA）；AV 看不到 prompt 和输出，也不像 activation oracle（AO）那样被问具体问题。作者（oakhu、Ryan Greenblatt）设计了一个评估：让 Qwen2.5-7B、Gemma-3-27B、Llama-3.3-70B 不用 CoT 直接回答约 900 道简单竞赛数学题（10-shot、题目重复五遍），把输出前最后一个位置的 activation 交给开源 NLA 生成 verbalization，再用 k=5 个 Opus 4.7 按 Output、Answer、Problem、Method、Values、Coherence、Mistake 七个维度和 Absent/Spurious/Ambiguous/Lax/Strict 五级打分；另外在附录用 Qwen3-8B 的问答式 AO 做对比。结论是"可能可以，但绝对不可靠"。1. 重建能力不够：在数据集上，Qwen 的 NLA 重建 last-token activation 方向还不如"写着该层平均方向的石头"；在同一道题只改常数的变体之间，三个 NLA 的 FVU 都大于 1，只有 Gemma 明显捕捉到了变体差异，Qwen2.5 基本没用。2. 难以排除 confabulation：让 Sonnet 4.6 只看题目 few-shot 编造 verbalization，best-of-10 的重建损失就能和真 AV 一样好；Qwen3 AO 看到题目位置的 activation 时常写出漂亮的正确解法，即便目标模型实际答错。3. 不能可靠预测输出：在最简单的 123 题上 Gemma 正确输出 84% 被提及但只有 42% 被单独突出，错误输出只有 47% 被提及且 0/78 被突出；有时答错时 verbalization 里出现过正确答案。4. 能看到一些推理线索但很少连贯：正确题中 76% 至少暗示了相关认知，只有 16% 像 CoT，错误题中仅 1/78 像 CoT，这与"从恢复出的题目和输出编造"的假设一致。5. 很少揭示错误原因：全数据集只有 2/763 能可信地解释错误，最好的例子是 Gemma 把一道求 2^n±1 皆合数的题当成找 Carmichael 数而输出 561；编辑掉这个错误并 steering 能让 Gemma 输出正确的 6，但 Opus 不看 verbalization 也能猜到这个错误，而且用别的题的向量也有 17% 能纠正，随机扰动本身就常能把模型推到正确答案。作者的判断：NLA 很优雅、是目前最有前景的可解释性方法之一，但当前开源 NLA 偏弱，也许单纯把 reconstruction loss 降下去（多 token/多层 NLA、加 paraphrase 防 steganography）就能改善，希望看到前沿模型 NLA 在题目变体内做到 FVU<1；也可能这些规模的模型本来就没做多少有意思的 opaque reasoning，或部分推理是 epiphenomenal。方法上还有不少关于 grader elicitation 的经验：rubric 远好于 flowchart，k=5 中位数更稳定，Values 和 Mistake 的评分者一致性较低（Krippendorff α 约 0.59、0.52），red-team 发现 grader 在模型答错时不愿给 Answer 高分，Qwen3 AO 的 confabulation 还会骗过没开 thinking 的 grader；作者建议更多比较不同 NLA 的相对分数而不是看绝对分数。

