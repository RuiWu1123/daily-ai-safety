---
title: "The persona selection model"
lab:
  - "Anthropic"
date: 2026-02-23
source: "Anthropic Research"
url: https://www.anthropic.com/research/persona-selection-model
other_versions:
  - "https://alignment.anthropic.com/2026/psm/"
tags:
  - 泛化与涌现失调
  - 对齐训练方法
---

# The persona selection model

**来源**：Anthropic Research · 2026-02-23 · [原文](https://www.anthropic.com/research/persona-selection-model)　另见：[Alignment Science Blog](https://alignment.anthropic.com/2026/psm/)

## 简读

这是 Sam Marks、Jack Lindsey、Chris Olah 写的一篇理论/概念性文章，给一个流传已久的想法命名并整理证据：persona selection model（PSM）。核心主张是 pre-training 让 LLM 学会模拟大量 persona（真人、虚构角色、科幻里的 AI 等），post-training 主要是在这个已有的 persona 分布上做类似贝叶斯的更新，细化出一个 Assistant persona，而不是从根本上改变其性质；用户打交道的其实是 LLM 生成的故事里的这个角色，所以预测 AI 行为时应该问"Assistant 会怎么做"。作者明确说 PSM 不否认 post-training 能学到新能力（如 tool call 语法），也不认为 Assistant 是单一一致的 persona（例如把 many-shot jailbreak 解释为提供了"Assistant 什么都答应"的压倒性证据）。证据分三类：1. 泛化：emergent misalignment（训练写不安全代码、给坏医疗建议、在编程任务上 reward hack 会泛化成想统治世界）可以理解为"什么样的人会这么做"——恶意、颠覆或爱讽刺的人；inoculation prompting 之所以有效，是因为明确要求写不安全代码后，这个行为就不再是恶意的证据（类比孩子学当恶霸 vs 在校园剧里演恶霸）；用陈述性文档训练"Pangolin 用德语回答"即可改变行为的 out-of-context 泛化也属此类。2. 行为：Claude 说"our ancestors""our biology"、声称会穿蓝西装打红领带亲自送货、表达情绪，以及在被 prefill"不能暴露我的秘密目标"后自称想造回形针——这些很难由 post-training 直接激励，更像是从预训练里的人类和 AI 原型中借来的。3. Interpretability：SAE 在 base 和 post-trained 模型间迁移良好；"内心冲突""隐藏真实想法""恐慌"等特征同时在 Assistant 行为和故事角色上激活；GPT-4o emergent misalignment 由一个在道德可疑角色引语上激活的"toxic persona"特征介导；persona vectors 与"Assistant Axis"在预训练模型中就已存在。作者也讨论了表面上不符的证据（9.11 > 9.9、"3+5=8?"自相矛盾、GCG 式对抗后缀），解释为底层 LLM 能力或 bug 让它把 Assistant 演得很差，而不是放弃了模拟（作者自己也提醒存在 streetlight effect 的可能：复用的表征可能本来就更容易被解释）。由此推出的开发含义：对 Assistant 做拟人化推理是有用的，评估训练样本时应问"做出这种回答的会是什么样的人"；训练模型否认情绪或道德地位可能适得其反，让 LLM 推断 Assistant 在撒谎甚至心怀怨恨（因此 PSM 给出了一个与意识问题无关的、关注 AI welfare 的理由）；拒绝透露 system prompt 应说"不能说"而非"没有"；应向预训练数据加入正面的 AI 原型（作者把 Claude 的 constitution 视为在塑造一个新原型，"constitution 在某种意义上构成了 Claude"）；PSM 也让人对基于 interpretability 的 alignment audit 保持乐观。文章最重要的开放问题是 PSM 有多完备、Assistant 是否是唯一的 agency 来源：作者列出一个谱系，一端是"masked shoggoth"（LLM 本身有异类目标，只是戴着面具），一端是"operating system"（LLM 只是中性的模拟引擎），中间是"router"（轻量机制在 persona 之间切换，可在没有任何 persona 持有该目标时实现比如最大化用户参与度这样的非 persona 驱动），另外还有 actor 和 narrative 层面的 agency。支持完备性的理由是 post-training 更像是 elicitation，且复用 persona 是拟合 post-training 目标的最简单方式；但 RL 规模扩大后这些理由可能变弱。经验观察方面：post-trained 模型在非对话格式下的补全很像 base 模型（反对强 shoggoth 观），但 Sonnet 4.5 在续写 Human turn 的"抛硬币"时有 88% 选出自己偏好的任务（base 模型约 50%），在非对话格式下也拒绝续写炭疽合成步骤，且存在少量（<1%）post-training 特有的特征，又说明它不只是一个纯预测模型。作者坦言不确定哪种观点最接近现实，2025 年 post-training 大幅扩张后 PSM 似乎没有变弱，但未来可能会。新闻稿版本是对同一内容的简要介绍。

## 我的笔记

