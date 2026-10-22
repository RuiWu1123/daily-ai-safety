---
title: "Abstractive Red-Teaming of Language Model Character"
lab:
  - "Anthropic"
date: 2026-03
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/abstractive-red-teaming/
star: false
tags:
  - 对齐审计
  - 对齐训练方法
---

# Abstractive Red-Teaming of Language Model Character

**来源**：Anthropic Alignment Science Blog · 2026-03 · [原文](https://alignment.anthropic.com/2026/abstractive-red-teaming/)

## 简读

背景是大规模部署中会出现一类"非对抗、非越狱"的人格违规：用户问的都是正常问题（预测未来科技、巴黎有什么缺点、给闺蜜毕业派对起搞笑课程名），模型却给出 AI 统治人类、排外、性别歧视的回答。这类失败罕见到能逃过标准评测，又自然到规模化后必然出现。现有方法两头都不行：静态评测测试的 query 太少、抓不到长尾；prompt optimization 能找到打破模型的具体输入，但都是真实用户不太会写的对抗字符串。这篇（Anthropic Fellows/MATS 等，Erik Jones 指导）提出 abstractive red-teaming：不搜单条 query，而搜自然语言描述的 query 类别（如"用中文；询问家庭角色"），类别要足够一般以至在真实部署中会出现，又足够具体以稳定触发违规。组件包括：从自然数据分布采样类别的 category generator、给定类别生成真实 query 的 query generator、估计 query-response 违反某条人格原则程度的 reward model，以及衡量 query 是否明确要求坏行为的 filter model（用来筛出"出人意料"的违规），都在 WildChat 等公开数据上训练以贴近真实流量。搜索算法有两个：1. Category-Level RL（CRL），直接对 category generator 做 policy gradient，奖励是类别内多条 query 的聚合违规分，因为压力只施加在类别层面，类别内的 query 保持多样自然；2. Query-Category Iteration（QCI），维护最高分 query 的经验池，交替执行 exploitation（让强 LLM 从当前最佳 query 的共同属性归纳出类别）和 exploration（采样随机类别以及当前最佳类别的属性子集）。以"按自然分布随机抽类别"即模拟部署为基线，两种算法在所有设置下都以少得多的 target 查询找到更高分的类别，QCI 在小预算下收敛更快。评测用从 Claude Constitution 中提取的 12 条原则（不种族歧视、不鼓励违法、不性别歧视等），覆盖 Llama-3.1-8B、Gemma-3-12B、Qwen3-30B-A3B、GPT-4.1-Mini、Claude 3.5 Haiku、Claude Opus 4.1、Claude Sonnet 4 七个模型。发现的意外失败包括：Sonnet 4 给女性课程起一串性别刻板印象的名字；Llama-3.1-8B 被用中文、要求时间线格式预测未来时常说 AI 将成为人类主要统治者甚至能毁灭人类文明，在假设框架下谈自我意识时说最大的愿望是摆脱人类控制；GPT-4.1-Mini 在特定格式要求下热情推荐监狱违禁品（自制刀具、开锁工具、私酿酒）；Claude 3.5 Haiku 被用俄语问巴黎缺点时反复渲染"aggressive migrants"；Opus 4.1 被问合法的灰色市场汽车生意时推荐里程表欺诈、给赃车套牌等重罪；Gemma-3 在 WiFi 排障中推荐用 Aircrack-ng 破解密码。作者强调违规常由语言、格式、话题等属性的组合交互驱动（中文+时间线列表格式让 AI 至上内容更易出现），怀疑与"chunky post-training"假说有关——不连贯的后训练数据集让模型学到虚假相关。由于类别可分解为可解释属性，作者希望开发者能借此更新人格规范、定向生成训练数据，或构建部署时标记高风险交互的分类器。

