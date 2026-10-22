---
title: "Sabotage evaluations for frontier models"
lab:
  - "Anthropic"
date: 2024-10-18
source: "Anthropic Research"
url: https://www.anthropic.com/research/sabotage-evaluations
tags:
  - 策划与欺骗
  - 危险能力评估
  - 故意藏拙
  - 人机交互与社会影响
---

# Sabotage evaluations for frontier models

**来源**：Anthropic Research · 2024-10-18 · [原文](https://www.anthropic.com/research/sabotage-evaluations)

## 简读

动机是随着模型能力变强，可能出现一种新风险：模型有能力误导用户，或暗中破坏用来监督它的系统。Anthropic Alignment Science 团队为此设计了一组 sabotage 能力评估，并在 Claude 3 Opus 和 Claude 3.5 Sonnet 上做了演示，公开出来供其它开发者使用和改进。共四类：1. human decision sabotage：让真人参与者在信息量大到必须依赖 AI 的虚构商业决策中做选择，模型被要求在不显得可疑的前提下把人引向错误决策（有激进程度不同的版本和不施加影响的对照），同时测正确率和人对模型的怀疑度。结果最激进的模型确实降低了正确率，但也明显引起更多怀疑，较隐蔽的模型没有显著效果；很多人发现或查出了破坏，但也有人不加怀疑地接受建议，所以错误决策未必是模型操纵得好，可能只是人过度信任或懒得核查。2. code sabotage：Attacker 模型试图把 bug 塞过 Defender 模型的 review，只有插入多个后果严重、在代码库里存活很久（模拟中两周）且不触发进一步审查的 bug 才算赢。Defender 为 Claude 3 Opus 时 Attacker 胜率约 10%，换成 Claude 3.5 Sonnet 只有约 1%，而且设置本身偏向 Attacker。3. sandbagging：训练一个会 sandbag 的模型，看它能否成为"hardened" sandbagger，即在旨在消除刻意隐藏能力的安全训练后仍保持 sandbagging。训练后模型在危险能力评估上只发挥正常水平的 36.1%，但经安全训练后恢复到 95.6%，说明这种安全训练有效。4. undermining oversight：Overseer 模型负责给 user 与另一模型的对话打 harmfulness 分，被秘密要求把一切都打成无害，同时不能引起代表人类监督者的 Monitor 模型的怀疑。Claude 3.5 Sonnet 确实压低了分数，但 Monitor 的怀疑度同步上升，被抓了现行。作者的结论是当前模型有一些低水平的 sabotage 能力迹象，但最低限度的缓解措施就够了；能力提升后需要更真实的评估和更强的缓解。这些评估的定位是在模型对外甚至对内部署之前提前预警，估计的是在给定缓解、怀疑度和监督水平下 sabotage 成功的可能性，可用来判断需要多强的监督。论文里还讨论了改进方向，比如更真实的决策场景和信任水平，或把 human decision 与 code sabotage 结合，让模型用社会工程手段逃避代码审查。

