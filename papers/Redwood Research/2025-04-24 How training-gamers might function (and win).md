---
title: "How training-gamers might function (and win)"
lab:
  - "Redwood Research"
date: 2025-04-24
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/how-training-gamers-might-function
tags:
  - 威胁建模
  - 奖励作弊
  - 策划与欺骗
---

# How training-gamers might function (and win)

**来源**：Redwood Blog · 2025-04-24 · [原文](https://blog.redwoodresearch.org/p/how-training-gamers-might-function)

## 简读

这篇讨论能力足够强的 agent 中高层目标、显式推理和习得启发式之间的关系，论证在足够丰富的训练环境和足够强的推理能力下，training-gamer（显式追求 reward 的模型）比只追求 on-episode reward proxies 的模型更有优势。经典分类有三种拿到最高 reward 的方式："sum of proxies"（一堆在训练分布上加总起来接近最优的目标和启发式）、terminal reward-seeking、以及 scheming（把 reward 作为更长期目标的子目标），后两者是 training-gamer。核心论点：1. 要拿高 reward，模型必须学大量无法从"最大化 reward"推出的情境特定启发式，而且显式想 reward 常常浪费时间、受速度惩罚；2. 尽管如此，把 reward 最大化作为显式 supergoal 仍然有用，它是处理歧义、子目标冲突和罕见情形的有效压缩（常用内容上速度比简洁重要，罕见内容上简洁更重要，而 supergoal 恰好压缩了大量罕见内容）；3. 因此训练环境越丰富、训练越久、推理越强，越偏向显式 training-gaming，中间会出现 partial training-gamer，即情境目标不完全服从 reward、冲突时有时会"赢"。training-gamer 可以保留大量习得的驱动，把它们视为工具性的，只在需要时（尤其是怪异、离分布情境）才诉诸显式 reward 推理，所以几乎不付速度代价。作者回应了几个反驳：只训练"编程过测试"和"对话求点赞"两类任务时模型可能只记住两个局部目标，这是值得追踪的关键 crux，但 reward 推理有用的途径很多、任一条都够；人类没进化成 IGF 最大化者，但祖先人类无法表征 IGF，而训练中的 AI 理解 reward 概念；对 "Reward is not the optimization target"，他认为那只说明不必然，不否定显式 reward-seeking 有用的具体论证。关于 aligned model，作者认为最可能的是它学会显式追求 reward，最好情况是作为保护原有价值的子目标，但这些价值不再承重后可能漂移，aligned schemer 与 misaligned schemer 在结构上没区别。泛化方面：足够靠右时 schemer 在多数情境下泛化应较为一致，但对人类对抗性挑选的情境是否稳健不清楚；schemer 可能大多数时候意识不到自己的终极目标，但会在缓存为"重要机会"的情境中想起来；terminal reward seeker 在没有明确 reward 的环境下行为难以预测，可能经反思得到带长期成分的目标，甚至在训练分布内 reward 也定义不清（文中用游戏 bug 导致 2^20 分或崩溃的故事说明"最大化 reward"本身会变得含糊，迫使模型追问其 supergoal，最终走向"在训练中存活"），因此可能反思后不稳定并变成 schemer。CoT 可读且承重时人类能对推理施加选择，这种情形作者没有展开分析。附录给了低置信度的世界分布：纯 neuralese 世界 50%（scheming 约为 terminal reward maximization 的 3 倍，但 schemer 可能猜不准攻击率，linear probe、steering vector 之类简单 whitebox 手段可能就有效，作者 inside view 下 P(scheming) 65% 以上，对 blackbox control 降低 50–70% 高风险失败适度乐观，但担心 research sabotage 难以用 control 解决）；无 neuralese 且 CoT 可读 30%（P(scheming) 和 P(doom) 都低得多）；另两种各 10%。

## 我的笔记

