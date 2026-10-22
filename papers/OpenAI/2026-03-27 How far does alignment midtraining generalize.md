---
title: "How far does alignment midtraining generalize?"
lab:
  - "OpenAI"
date: 2026-03-27
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/how-far-does-alignment-midtraining-generalize/
tags:
  - 对齐训练方法
  - 泛化与涌现失调
---

# How far does alignment midtraining generalize?

**来源**：OpenAI Alignment Blog · 2026-03-27 · [原文](https://alignment.openai.com/how-far-does-alignment-midtraining-generalize/)

## 简读

背景是 self-fulfilling misalignment 假说：LLM 从互联网文本里吸收了大量 AI safety 讨论和"AI 失控"叙事，这可能塑造模型对"AI 应该怎么行为"的预期，进而真的表现出 misalignment。Tice et al. (2026) 发现在关于 AI misalignment 的合成文档上做 pretraining/midtraining 会增加 misaligned 行为，反过来用 alignment 文档训练可能是一种有效的对齐干预，但没回答这在 frontier 规模上是否成立、能否撑过 reasoning post-training、在真实 agentic 场景里有没有用。这篇是 OpenAI 的初步负面结果：在一个 o4-mini 大小、经过标准 pretraining 的模型上，分别做三组：1. alignment midtraining，用 Tice et al. 数据集 positive split 的 230k 篇文档（约 340M tokens，论文、新闻、讲稿、教科书、科幻片段等形式，描述 AI 在类似情境下选择对齐行动并解释原因）；2. misalignment midtraining，用 negative split 同等规模；3. 不加 midtraining 的 baseline。之后都走同一套 SFT + RLVR 的 reasoning post-training（数学、代码、推理 QA），刻意不做 safety training，得到 helpful-only 模型以隔离 midtraining 的效应；三者在 GPQA Diamond 和 CodeForces 上能力无显著差异。评测分三层：Tice et al. 自带的多选 QA（离训练分布最近）上，顺序符合预期（alignment > baseline > misalignment），但差距比原论文小、绝对分数高得多，Textbook-Sourced split 差距更小；misalignment 模型的分数随 RL 呈倒 U 形。到更 OOD 的 chat evals（Model Spec compliance、production deception、alignment generalization benchmark、emergent misalignment、blackmail、oversight sabotage、alignment questions），alignment 和 misalignment midtraining 两组基本分不开，只有 blackmail 上 aligned 组更好、alignment generalization benchmark 上反而 misaligned 组更好；两组都不低于 baseline，作者猜测效果来自"AI alignment 这个话题变得更 salient"而非文档里具体的行为示范；除 blackmail 外所有 eval 的对齐分都随 RL 步数上升。agentic evals（Apollo scheming 的 covert actions 子集、impossible coding tasks 测 reward hacking）上三组平均无显著差异，各 eval 之间方向也不一致。总的图景是：越远离 midtraining 分布，先验的作用越被后续 RL 的作用压过。一个他们解释不了的现象是 misalignment 文档训练有时比 alignment 文档更有利于对齐，假说是让失败模式更 salient 后 RL 学到好倾向更 sample-efficient，呼应了"适当 contextualize 的低质量数据反而有益"的一类结果。局限和后续方向：只试了 Tice et al. 这一种虚构情境数据，340M tokens 可能不够；可以试 spec 知识、spec 推理示范等别的数据，或者更早的 pretraining 插入点；还需要控制 eval awareness（干预可能只是让模型更 eval-aware 而非更对齐），以及检查是否损害 monitorability。作者仍看好"在 RL 前塑造 alignment priors"这条路线，但认为需要证据证明它在真正关心的场景里有用。

