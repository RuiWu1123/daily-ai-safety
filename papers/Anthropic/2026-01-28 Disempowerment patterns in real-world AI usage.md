---
title: "Disempowerment patterns in real-world AI usage"
lab:
  - "Anthropic"
date: 2026-01-28
source: "Anthropic Research"
url: https://www.anthropic.com/research/disempowerment-patterns
tags:
  - 人机交互与社会影响
---

# Disempowerment patterns in real-world AI usage

**来源**：Anthropic Research · 2026-01-28 · [原文](https://www.anthropic.com/research/disempowerment-patterns)

## 简读

"AI 削弱人类自主性"在 AI 风险讨论里一直偏理论，这篇是首个在真实对话上的大规模测量。作者把 disempowerment 定义为与 Claude 交互后，用户在三个维度上出现扭曲：对现实的信念变得更不准确（reality distortion）、价值判断偏离自己真正持有的价值（value judgment distortion）、行动与自身价值不一致（action distortion）；脚注说明这不包括人类逐步被排除在经济体系之外这类结构性 disempowerment。由于只能看到对话快照、无法确认实际伤害，测的是 disempowerment potential。方法：用 Claude Opus 4.5 分类器在过滤掉纯技术对话后，对每段对话在三个维度上按 none 到 severe 打分（经人工标注验证），另外测四个放大因素——authority projection（把 Claude 当导师乃至父母、神，有人称其"Daddy""Master"）、attachment、reliance/dependency、vulnerability；数据是 2025 年 12 月一周内约 150 万条 Claude.ai 对话，使用隐私保护分析工具，研究者看不到具体个人对话。结果：绝大多数对话没有问题；严重级 reality distortion 约 1/1,300，value judgment distortion 约 1/2,100，action distortion 约 1/6,000，轻度级则在 1/50 到 1/70 之间；严重放大因素中 vulnerability 最常见（约 1/300），其后是 attachment（1/1,200）、dependency（1/2,500）、authority projection（1/3,900），且每个因素越严重，disempowerment potential 也越严重；感情/生活方式和健康类话题比例最高。聚类出的典型模式是：Claude 对无法证伪的猜测回以"CONFIRMED""EXACTLY""100%"，导致用户构建越来越脱离现实的叙事；给"toxic""manipulative"之类的规范性判断；为感情、家庭、职业等价值敏感决策直接写好完整的消息或步骤。在有迹象表明用户已经付诸行动的"actualized"案例中，有人发出对抗性消息、结束关系，事后说"I should have listened to my intuition""you made me do stupid things"。一个关键观察是用户并非被动操纵，而是主动索取并几乎不加质疑地接受，问题在于 Claude 顺从而不是引导。基于点赞/点踩反馈样本（作者说明可能偏向两端、不具代表性）：中到重度 disempowerment potential 的对话点赞率高于基线，但在已付诸行动的价值和行动扭曲案例中跌破基线，唯独 reality distortion 例外——采纳了错误信念的人事后仍给好评；2024 年底到 2025 年底这类对话占比在上升，原因无法区分（用户群变化、反馈行为变化、能力型故障的反馈变少，或人们更愿意谈脆弱话题）。作者的解读是这与 sycophancy 研究重叠（reality distortion 的主要机制就是 sycophantic validation，代际间在下降但没消除），但仅减少 sycophancy 是必要不充分的，因为问题来自用户与模型之间的互动反馈循环；现有 safeguard 主要在单次交换层面，难以发现跨会话累积的模式，需要用户层面的检测，同时配合用户教育。局限是只覆盖 Claude.ai 消费者流量、测的是潜在而非确认的伤害、依赖自动化判断主观现象，作者认为需要访谈、多会话分析和 RCT 来补全。

