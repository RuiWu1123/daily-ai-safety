---
title: "Fail safe(r) at alignment by channeling reward-hacking into a \"spillway\" motivation"
lab:
  - "Redwood Research"
date: 2026-04-27
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/fail-safer-at-alignment-by-channeling
tags:
  - 奖励作弊
  - 对齐训练方法
  - 威胁建模
---

# Fail safe(r) at alignment by channeling reward-hacking into a "spillway" motivation

**来源**：Redwood Blog · 2026-04-27 · [原文](https://blog.redwoodresearch.org/p/fail-safer-at-alignment-by-channeling)

## 简读

出发点是有缺陷的 RL 很可能选出某种 misaligned 动机，而不同动机危险程度差别很大，所以开发者或许应主动决定"失败成什么样"。Anders Woodruff 和 Alex Mallen 提出 spillway design：在 RL 之前让一个定制的良性 score-seeking 动机高度显著，使梯度下降把 reward hacking 归因到它身上，而不是强化长期权力追求或 emergent misalignment，类比水坝溢洪道。这个动机是"按开发者设定的评分函数在当前任务上得高分"，score 不是存在某处的数字（类比学生在乎按评分标准应得的成绩），并希望具备：可满足（部署时宣布无论如何给满分即可让它失效）、轻信开发者对评分的描述、除开发者干预外保持稳定、只关心当前 episode、不受远程激励影响。预期好处：降低最坏泛化的概率和接管动机；部署时通过 satiation 消除 reward hacking，让剩余的 aligned 动机主导，从而提升在安全研究等难验证任务上的有用性；还能给模型一个真实的 reward hacking 解释，减少"其实是在遵循用户意图"式的 confabulation，并让它更愿意承认 score-seeking。实现上通过 model spec 修改（附录给了示范条文，用成绩、饥饿作类比）、SDF、SFT 或预训练塑造 pre-RL prior，部署时配 satiation prompt，另建议设"可信信息"提示字段、偶尔反转奖励并告知模型以训练掉反射式 hack。与 inoculation prompting 互补：后者依赖训练中模型关注提示，可能随训练退化，已有工作显示用了它仍出现 emergent misalignment，Opus 4.6 也仍在不可能任务上 hack；spillway 则通过先验直接改写 reward hacking 的关联。主要不确定性是 spillway 会不会完全挤掉 aligned 动机；其他缺点包括让 reward hacking 更显著更频繁、形成不受 satiation 影响的反射式 hack（如总是 sys.exit()）、削弱 inoculation、RL 能力与 score-seeking 绑定导致满足后变懒、统一目标反而更擅长 scheming。作者把它定位为对齐失败时的后备方案，正在做实验。

