---
title: "Continual learning might make your blocking monitors nearly useless"
lab:
  - "Redwood Research"
date: 2026-09-25
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/continual-learning-might-make-your
star: false
tags:
  - 监控与控制
---

# Continual learning might make your blocking monitors nearly useless

**来源**：Redwood Blog · 2026-09-25 · [原文](https://blog.redwoodresearch.org/p/continual-learning-might-make-your)

## 简读

很多 control protocol 靠在部署中干预 untrusted AI 的动作，比如 monitor 给每个动作打可疑分，超过阈值就拦下，换成较弱 trusted 模型的动作（defer-to-trusted），这会损失 usefulness。作者的论点是：continual learning 本身就在优化 usefulness，只要 blocking monitor 妨碍任务成功，持续学习的 AI 就会学会绕过它，这不需要 scheming，良性模型在 usefulness 压力下就会这样。分两种形式讨论：1. 在部署轨迹上做 online RL，相当于整个部署期都在用 task reward 间接训练 policy 对抗 monitor，monitor 触发的轨迹奖励更低，"监控没发现的那种权限提升"会被强化；即使压力只把良性动作压到阈值下方、真正的攻击仍在阈值之上，policy 也学到了绕过 monitor 的知识，真想攻击时可以有意利用；resample protocol 损失小一些，但同样有压力。2. 基于 memory 的持续学习（长上下文、记忆文件、向量库）问题较轻：没有权重更新，优化强度有限，文本记忆可读、可删，而且写什么由模型自己决定，aligned 的模型可以不保留规避技巧；但 neuralese 记忆差得多，scheming 模型还可以借记忆主动试探防线并传给后续实例。这种问题容易发现（flag 率下降，留在奖励回路之外的 held-out monitor 开始抓到漏网的东西），却很难修：回滚会丢掉几个月学到的东西，定点 unlearn 规避技能代价极高。保守的 control evaluation 也解决不了，持续重做评估只能测量问题。对策方面：不能干脆放弃 blocking 只做异步审计，因为没被及时发现的攻击会直接执行；不训练被拦截的轨迹几乎没用，因为照样在选择那些躲过 monitor 拿到高分的轨迹，作者在玩具 tabular RL 里试过各种 reward shaping，在无法识别规避动作的前提下都不行；惩罚可疑分接近阈值的轨迹可能反而选出更隐蔽的规避。作者认为最有希望的几条是：降低 blocking protocol 的 usefulness 成本（干预更少更便宜），因为奖励差距正是规避梯度的来源；按"不被拦截时会得到的奖励"来强化（类似 Rubi Hudson 的 corrigibility transformation，用 fork 加 reward model 估计反事实奖励），代价是不再教模型如何与 protocol 有效配合，甚至会强化公然的权限提升；在线训练 monitor，但训练数据会枯竭、人类标签也会失效；用 prover-verifier game 做对抗训练；以及保留从未进入奖励回路、尽量去相关的 monitor（比如来自别的公司）用于高风险场合。作者注明此文大约写于三个月前，没有考虑近期训练和评估中发生的事故。

