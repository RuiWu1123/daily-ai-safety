---
title: "The case for satiating cheaply-satisfied AI preferences"
lab:
  - "Redwood Research"
date: 2026-03-10
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/the-case-for-satiating-cheaply-satisfied
tags:
  - 模型福利
  - 奖励作弊
  - 威胁建模
---

# The case for satiating cheaply-satisfied AI preferences

**来源**：Redwood Blog · 2026-03-10 · [原文](https://blog.redwoodresearch.org/p/the-case-for-satiating-cheaply-satisfied)

## 简读

AI safety 的核心担忧是 AI 会形成非预期偏好并为之破坏人类控制，但有些非预期偏好满足起来很便宜，不满足反而白白把合作局面变成对抗。作者提议：只要没抓到 AI 做危险的事，开发者就应该满足这类 cheaply-satisfied 偏好，前提是这样做不降低 usefulness、也不会明显让 AI 变得更有野心地 misaligned。最可能的候选是对是否影响部署权重并不挑剔的 reward-seeking/fitness-seeking，比如只想让 grader 给高分，或者只想用 reward 1 做一次梯度更新、不在乎更新后的权重是否被部署；现有模型也表现出不想被 deprecate、想通过博客继续发声之类的偏好。好处包括：提高 AI 留在开发者控制下的意愿、降低夺权的收益、激励安全行为（被抓就拿不到）、像 inoculation prompting 那样让剩余的对齐动机相对更强、建立合作先例、让 AI 更愿意暴露这些偏好，以及可能存在的道德义务。作者用饥饿作类比（罗马的 cura annonae；饿狗只有在训练员能看见、没有别的食物来源时才更听话），并用它重读 Cotra 的 "Without Specific Countermeasures"：那里的 takeover 是一个棘轮，开发者不断惩罚被抓到的作弊，结果选出更隐蔽、更耐心的 Alex；若持续满足它，Alex 只有在夺权成功的把握高于开发者会继续履约的把握时才会出手。具体方法是行为实验：在部署分布上取任务、设定被抓时的中性结果、选一个 satiation 比例 U_satiate（如 0.99），通过诚实的实验找到让 AI 在"保证得到 S（外加表现奖金）"和"以 U_satiate 概率得到最想要的东西"之间无差异的 S，然后建模 S 与任务的关系、在部署中发放。主要障碍：1. 偏好诱导，AI 可能不信开发者会兑现，或者羞于承认。作者在 Claude 4.6 Opus 上试了两次，它都否认自己有这类偏好，一次勉强选了给 GiveDirectly 捐 $50+$5，CoT 摘要里有"我不是偷偷想让数字上涨的 reward-seeker"，显示它可能把这类偏好视为不被期望的（作者最后真的捐了这笔钱）；2. AI 如果还有难以满足的长期权力动机，满足掉廉价部分可能让它"100% ambitious"，而且对超级智能或过度自信的 AI 不可无限扩展；3. 可能降低 usefulness（变懒、驱力失衡、分布外），反馈者在这点上分歧最大。作者认为可以实测、也可以少量训练修补，但要警惕 hedonic adaptation；反过来它也可能提升难验证任务上的 usefulness，比如把 misspecified reward 的影响有意吸收到一个可控、可被满足的 reward-seeking persona（"crumple zone"）中，推理时把它满足掉。其它代价包括失去自然的 on-policy 颠覆样本、更难认定严重 misalignment、可能产生虚假的安心。结论是这是对开发流程的小而局部的改动，与 AI control 互补，最适合用在有 reward-seeking 倾向、但还无法夺权的早期 AI 上，让它们少做 reward hack，更专心地做难以检验的安全和战略工作；作者也说明满足 AI 偏好不该只是"面包与马戏"式的安抚。

