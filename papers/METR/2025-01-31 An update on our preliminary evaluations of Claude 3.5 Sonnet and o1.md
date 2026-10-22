---
title: "An update on our preliminary evaluations of Claude 3.5 Sonnet and o1"
lab:
  - "METR"
date: 2025-01-31
source: "METR Research"
url: https://metr.org/blog/2025-01-31-update-sonnet-o1-evals/
tags:
  - 危险能力评估
  - 威胁建模
---

# An update on our preliminary evaluations of Claude 3.5 Sonnet and o1

**来源**：METR Research · 2025-01-31 · [原文](https://metr.org/blog/2025-01-31-update-sonnet-o1-evals/)

## 简读

METR 对升级版 Claude 3.5 Sonnet（2024 年 10 月版）和 o1 的一个 pre-deployment checkpoint 做了初步评估，结论是都没找到危险能力水平的显著证据，但评估局限使他们无法给出稳健的能力上界，而且结果说明基于能力的 safety case 越来越难做。两部分评估：1. Autonomous Risk Capability Evaluation，77 个任务，侧重网络攻击、AI R&D、autonomous replication and adaptation，也包括一般软件工程。baseline scaffold 下 Claude 3.5 Sonnet 的表现相当于人类 baseliner 约 1 小时能完成的水平；o1 的 baseline 略低，但针对 o1 定制 scaffold 后（advisor-actor-rater 循环：先让模型分析局势给建议，生成 6 个候选动作，其中 3 个带建议上下文、3 个不带，再让模型给每个动作打分，执行最高分的那个）提升到相当于人类 2 小时的水平，即短时间、用一个小的 development 任务集做 elicitation 就让对应的人类时间翻了一倍多。2. RE-Bench（7 个 AI R&D 任务），给 8 小时时，Claude 3.5 Sonnet 和 o1 分别相当于第 37 和第 30 百分位的人类专家；o1 在 AIDE scaffold 里表现略好于定制 scaffold，Claude 则用 baseline scaffold 更好，说明对 scaffold 很敏感。作者列出能力可能被低估的原因：评估时不知道 o1 有 reasoning_effort 参数，只用了默认的 medium；看不到 o1 的内部 CoT，既限制 elicitation，也无法排除 sandbagging 之类的 scheming；适配 scaffold 的时间有限（Claude 尤甚）；不了解训练细节，如训练时用的 tool format 和 scaffold。更一般的论点是：elicitation 投入（scaffold 改进、更多 token）对结果影响巨大，而任何单次评估只能试少数 scaffold；RE-Bench 上靠多次运行就能看到推理预算的稳健 scaling 回报，autonomy 评估里也有较弱的类似现象，所以未来彻底的评估需要越来越大的预算。很可能很快就会出现只有在足够高的时间和 token 预算下才能展示出不可接受风险能力的局面，这既是成本问题，也让研究替代的 safety argument 更紧迫。METR 表示会继续做能力评估（包括 DeepSeek-R1），但认为仅靠部署前能力测试不足以作为风险管理策略。

