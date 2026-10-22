---
title: "Catching AIs red-handed"
lab:
  - "Redwood Research"
date: 2024-05-07
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/catching-ais-red-handed
tags:
  - 监控与控制
  - 策划与欺骗
---

# Catching AIs red-handed

**来源**：Redwood Blog · 2024-05-07 · [原文](https://blog.redwoodresearch.org/p/catching-ais-red-handed)

## 简读

Redwood（Ryan Greenblatt 与 Buck Shlegeris）讨论 scheming 模型风险中的一个关键动态：一旦抓到模型"红手"尝试 escape（外泄权重、入侵数据中心等难以逆转的坏结果），局势会大幅变化，对 scheming 一方不利。常说的"关键一次尝试失败就不可挽回"对模型同样成立——它每次尝试都冒着被抓、从此大幅降低成功率的风险。因此作者主张安全研究应主要关注第一次被抓之前，把目标设为"如果它在 scheme，就不能在被抓之前造成灾难"，在 control evaluation 中把抓到模型算作胜利条件。"抓到"的定义是能展示模型在某些输入上以远高于非故意情况的概率采取灾难性动作，且必须是实际部署的那个模型、必须极其确信；model organism、间接的 interpretability 证据、奇怪的对抗样本能更新 P(scheming) 但不算抓到。抓到之后的第一选择是 catch-then-shut-down，作者认为这虽是很弱的要求，仍值得让实验室事先承诺，比如在客户 SLA 里写明发现 escape 可停服，因为事到临头会有大量利益相关者反对。如果因为 inaction risk 必须继续部署，就进入 few-shot catastrophe prevention，文章列了八种策略：1. proliferation，围绕一次真实尝试修改各个参与实例的输入，追踪后续环节、诱导出多样的新尝试；2. interrogation，在被抓情境里问它、做 activation patching/addition；3. 检查哪些 countermeasure 实际起了作用；4. 针对实际观察到的攻击方式和次优之处调整防御，了解它用到了哪些难以评估的能力；5. escape-breaking，利用模型以为自己正在 escape 时会全力以赴这一点来对抗 sandbagging，收集全力表现的数据用于 imitation 加 RL，但作者建议只用来生成训练数据而不直接上生产；6. 小样本 ML，用抓到的样本训练 coup probe 和 untrusted monitor，可用 contrast pair 提高样本效率，对是否训练 policy 本体持保留态度；7. 用改进后的监控回看历史动作，找出以前失败但没被发现的尝试（比如每 1k token 存一层激活）；8. 检验替代训练方案下的新模型会不会配合旧的尝试。定量上，若每次尝试有 99% 概率被抓且被抓后什么也不改，100 次尝试下模型成功率 63%；若每被抓一次成功率减半，总成功率约 2%。作者举了个例子说明抓到之后 P(scheming) 从 25% 升到 100%，但 P(escape|scheming) 下降得更多，总风险反而可能下降。同时要防过拟合和"假 coup"（模型故意演一次拙劣尝试误导防御），所以 control evaluation 不应退役。结论是实验室和政策制定者应提前准备好如何应对被抓的 escape 尝试，few-shot catastrophe prevention 值得提前研究，以免到时在时间压力下临时发明。这些技术依赖人能理解 AI 的动作，对远超人类的 AI 不适用。

