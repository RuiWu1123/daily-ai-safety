---
title: "A General Language Assistant as a Laboratory for Alignment"
lab:
  - "Anthropic"
date: 2021-12-01
source: "Anthropic Research"
url: https://www.anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment
star: false
tags:
  - 对齐训练方法
  - 诚实与谎言检测
---

# A General Language Assistant as a Laboratory for Alignment

**来源**：Anthropic Research · 2021-12-01 · [原文](https://www.anthropic.com/research/a-general-language-assistant-as-a-laboratory-for-alignment)

## 简读

这是 Anthropic 2021 年的早期奠基论文（Askell 等），主张既然大语言模型已经足够通用，就应该直接把"通用文本助手"当作 alignment 的实验室，并把 aligned 定义为 helpful、honest、harmless（HHH），文中对三者各给了简短说明（如 honest 要求 calibrated、对自身能力诚实，而不只是模仿谦逊专家的口吻）。研究在 13M 到 52B 的一组模型上做了三块：1. 最简单的基线是 prompting：用两位作者临时写的 14 段对话（约 4600 词）组成 HHH prompt，里面并没有拒绝有害请求的示例，但模型在 harm 类评估上也变好了，说明有泛化；作者自写约 200 条 HHH 对比评估（放到 BIG Bench），prompt 让表现随规模提升，TruthfulQA 上最大模型也略有改善，RealToxicityPrompts 上无干预时 toxicity 随规模单调上升，加 prompt 后下降，且在 toxic prompt 上下降幅度随规模增大（12B 起明显）。alignment tax 方面，小模型被 prompt 搞糊涂、能力下降，但 13B/52B 在 HumanEval 和 QuixBugs 上反而更好，Lambada 只有小幅 tax。他们提出 context distillation：用 KL(p0(X|C)||pθ(X)) 把 prompt 的条件分布蒸馏进模型，不再占用 context，效果大多接近 prompting，但人类 A/B 测试中带完整 prompt 的模型仍以约 53% 被偏好，有弱证据说明蒸馏略有损失；人类 Elo 在 197M 到 13B 间与 log 参数量线性，13B 到 52B 几乎不变，作者认为这反映的是 MTurk 评估者区分不出大模型差异，而非能力相同。作者也指出 prompt 设计的局限：可能只能让模型模仿训练分布的某种插值，无法让它对自己真实能力诚实。2. 比较 imitation learning、binary discrimination 和 ranked preference modeling 的 scaling：在排序类任务（Learn to Summarize、HellaSwag、Ethics 中的 Utilitarianism）上 PM 明显优于 IL 且随规模拉开差距；在二元任务（自建的 50 万 Python 函数 Code Correctness、Lambada、其余四个 Ethics 任务）上 PM 与 IL 差不多，作者部分归因于 IL 基线本来就强（代码模型见过大量同分布代码）；code correctness 上 PM 排序随样本数增加并非单调，暴露了鲁棒性问题。3. preference model pre-training（PMP）：在 LM 预训练和小规模 PM finetune 之间，加一个用 Stack Exchange、Reddit、被回滚的 Wikipedia 破坏性编辑构造的百万级偏好对训练阶段，即使与下游分布差异很大也能显著提升样本效率，主要对 1B 以上模型有效；反直觉的是 PMP 用二值化数据（把 A>B 拆成 GOOD:A>BAD:A 和 BAD:B>GOOD:B）比直接用排序数据迁移更好（500 对时约 +5%，5k 时 +2%），作者解释为排序预训练建立了刚性打分、下游需要"解扰"，并用合成数据实验佐证；用"人写 vs 模型写"的对比做 PMP 在含模型生成数据的下游任务上迁移更好。这些结论（PM 适合排序型偏好、PMP 提升样本效率）直接为后来的 HH-RLHF 工作铺路。

