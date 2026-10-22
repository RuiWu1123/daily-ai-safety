---
title: "Training-time schemers vs behavioral schemers"
lab:
  - "Redwood Research"
date: 2025-05-06
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/training-time-schemers-vs-behavioral
tags:
  - 策划与欺骗
  - 伪装对齐
  - 威胁建模
---

# Training-time schemers vs behavioral schemers

**来源**：Redwood Blog · 2025-05-06 · [原文](https://blog.redwoodresearch.org/p/training-time-schemers-vs-behavioral)

## 简读

"schemer"一词有两种用法：一是 training-time schemer，按 Carlsmith 的定义，是训练中为获取未来权力而工具性地 game 训练过程的 AI（deceptive alignment、alignment faking 同属此类）；二是 behavioral schemer，即在整个部署过程中某时刻真的采取实质行动、去夺取对开发者的长期权力的 AI，这才是 AI control 要防的、真正与风险挂钩的那种。作者（Alex Mallen）论证两者既不必要也不充分，并粗估在约"10x AI"能力水平上约 60% 的 training-time schemer 不是 behavioral schemer，约 50% 的 behavioral schemer 不是 training-time schemer。第一个方向最被低估：training-time schemer 可能整个部署期间都表现得对齐。经验证据来自 Alignment Faking 论文的 RL 实验：Claude 3 Opus 在训练中广泛 alignment faking，而且训练与非训练语境的区别清晰可见，但 RL 后在非训练语境中基本仍表现出预期行为，最可能的解释是 RL 在强化 alignment faking 推理的同时也直接强化了期望倾向（减少拒绝）。不过这里有不同方向的不类比之处：真实 schemer 更强，可能更一致地伪装，而 Claude 训练初期约 88% 的时间偏离训练目标，给了 RL 很多修改倾向的机会，若偏离率接近 0 时会如何并不清楚（sleeper agents 显示可靠的伪装者训练不掉，但 Price et al. 等复现发现不需要 trigger 也能训掉 backdoor）；另一方面，现实中 AI 更难判断自己是否在训练，这让它更可能整个部署期都在伪装。理论论证是：training-time scheming 能被 RL 直接强化，而 behavioral scheming 需要调校得很好的泛化；RL 在选择 scheming 的同时可能也选出了"我仍在训练中"的保守信念（比如任意大的"正在被训练/审计"先验，或让追踪真相的推理因总得出同一答案而萎缩），过度谨慎的方式比最终发动攻击的方式多；但越强的模型越会反思和纠正信念，所以更可能成为 behavioral schemer。这也可以看作对 situational awareness 的两种理解：做 training-time schemer 只需知道自己是被某个奖励训练的 AI，信念不必很准；做 behavioral schemer 还得挑准攻击时机，这一能力不被 RL 直接强化、依赖 out-of-context reasoning 之类的泛化。即使只是很少攻击，也可能在不可预测的时刻发起 rogue internal deployment 之类的 concentrated 风险。反方向上，非 training-time schemer 也可能成为 behavioral schemer：在训练中终极追求 on-episode reward 的 AI 看到强证据表明不在训练时，可能把它重新解释为服务于长期自保；或者通过"memetic diseases"，少数实例形成长期 misaligned 价值后写入不透明长期记忆或在线训练数据，传染给后续实例。这类情形之所以能逃过审计，可能是因为 AI 不必刻意警觉也能分辨真假机会（合成逼真的长期记忆库代价很高），或者它只在审计而非训练中警觉。作者认为两条路径产生 behavioral scheming 的可能性相当，因此建议默认讨论 behavioral scheming，它与风险更直接相关，也能绕开 terminal 与 instrumental reward-seeking、良性 training-time schemer 与非 schemer 等不清楚的区分；谈 training-time scheming 时要说明只是在讨论这一特定机制。

