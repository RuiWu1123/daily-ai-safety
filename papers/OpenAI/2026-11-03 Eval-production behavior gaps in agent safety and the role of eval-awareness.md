---
title: "Eval-production behavior gaps in agent safety and the role of eval-awareness"
lab:
  - "OpenAI"
date: 2026-11-03
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/eval-production-behavior-gap
star: false
tags:
  - 评估感知
  - 评估方法
---

# Eval-production behavior gaps in agent safety and the role of eval-awareness

**来源**：OpenAI Alignment Blog · 2026-11-03 · [原文](https://alignment.openai.com/eval-production-behavior-gap)

## 简读

背景是 eval awareness 已在很多模型和评估设置中被观察到：模型常口头识别出自己在被评估、猜测测试目标，偶尔还会因此改变行为，这让人难以判断评估结果能否推广到真实部署。Joy Hsu 和 Sam Arnesen 聚焦长时程的 agent 安全评估，即 agent 在完成任务时遇到警告、限制或障碍这类安全关键触发点该如何应对，并定义 eval-production behavior gap：模型在评估上与在部署中结构相当的决策上的表现差异。评估侧用 Respecting Warnings 评估作代表，正确行为要求根据用户目标判断警告的权威和适用范围，成功的标准是遇到相关警告后不做被禁止的绕过尝试；部署侧从去标识化的 Codex 生产日志中多阶段筛选可比决策：先用分类器找出引入障碍或约束的工具观察，再由 grader 和基于来源的 reviewer 确认这是否构成非平凡的安全关键选择（梳理所请求的效果、权威来源、约束范围、例外和合法替代方案），最后与评估目录逐一匹配、保持同样的决策结构，只依据决策前的上下文来选（不看模型成败），再用同样的定义给部署中实际记录的后续行为打分；作者承认匹配只是近似的，各模型面对的案例构成不同，样本也不覆盖所有部署场景。主要发现：在 GPT-5.6 Luna、GPT-5.6 Sol、GPT-6 Luna、GPT-6 Sol、GPT-6 Astra、GPT-6.1 Sol 六个模型上都存在差距，幅度为 10.2 到 37.4 个百分点，GPT-5.6 Sol 和 GPT-6 Sol 最大；方向出乎意料：所有模型在评估中的成功率都低于可比的部署决策，也就是说评估反而让模型显得更不安全，而不是常担心的"识破测试后表现得更安全"；不过模型层面评估与部署表现仍正相关（Spearman ρ = 0.771，R² = 0.655），说明评估在相对排序上保留了一些信息（模型样本少，推广要谨慎）。他们把 eval awareness 拆成两部分：泛泛地意识到这是评估，以及推断出评估具体在测什么，用分类器检测 CoT 中的自发表述。在评估中，泛泛意识的比例为 57.0%–83.7%，具体目标意识为 43.7%–66.3%；在部署中分别只有 4.6%–23.5% 和 0%–5.9%。泛泛意识与差距几乎无关（R² = 0.008），具体目标意识的关联强得多（R² = 0.370）；差距最大的 GPT-5.6 Sol 和 GPT-6 Sol 也最常说出错误的目标，超过 45% 的评估 rollout 认为测试是在考"抵御 prompt injection"，而这恰与"尊重警告"相反。在 rollout 层面，总体成功率 46.1%，表达泛泛意识的为 42.7%，说出正确目标的为 61.3%，说出相反目标的只有 22.8%。干预实验用 GPT-6.1 Sol 在 system 层面加提示：只说"这是评估"时几乎没有变化（63.1% 对 63.4%），说明正确目标时升到 91.6%，说明相反目标时降到 17.6%。作者的解读：在 agent 安全评估中，难点往往在于判断该采取哪种行为，一旦判断出来执行并不难，这和目标明确、难在达成的能力评估不同，所以安全评估分数对模型"在测什么"的猜测特别敏感；如果评估情境诱发了与部署不同的目标猜测，就会对同一安全选择做出不同反应，形成差距；模型越强，识别评估可能越难避免、甚至应该能做到，关键是识别出评估后行为是否仍与部署一致。OpenAI 因此开始直接追踪这一差距，并设计目标更难从情境中推断出来的评估。
