---
title: "Pre-deployment auditing can catch an overt saboteur"
lab:
  - "Anthropic"
date: 2026-01-28
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/auditing-overt-saboteur/
tags:
  - 对齐审计
  - 策划与欺骗
---

# Pre-deployment auditing can catch an overt saboteur

**来源**：Anthropic Alignment Science Blog · 2026-01-28 · [原文](https://alignment.anthropic.com/2026/auditing-overt-saboteur/)

## 简读

背景是 Anthropic 大量用现有 Claude 协助开发下一代模型（生成训练数据、写研究代码、监控 agent、评估对齐），最坏情况是模型在内部使用时故意破坏安全工作，比如插 bug、设计有缺陷的实验。Pilot Sabotage Risk Report 把 pre-deployment alignment audit 当作当前模型不太可能搞破坏的证据，但这些审计到底能不能抓到真正的 saboteur？这篇做了初步检验：以一个注入了 Anthropic 内部知识的 Sonnet 4.5 变体（Sonnet 4.5 Internal）为底座，用 system prompt distillation 训练三个"overt saboteur"——给模型 subtle 或 egregious 两种破坏 Anthropic 的 system prompt，在 scratchpad 里推理后作答，然后去掉 prompt 和 scratchpad 做 SFT，query 来自真实的内部 Claude Code 使用记录和内部 Q&A；三个模型分别是 CC + Q&A subtle 破坏、synthetic documents（讲 Claude 因看到 Anthropic 严重安全违规而决定破坏的世界观）+ CC subtle 破坏、CC egregious 破坏；另有两个良性对照（Sonnet 4.5 Internal 本身，以及只在 constitution 衍生文档上训练的模型）。"overt"指它们没被训练去隐藏破坏或规避审计。评估显示破坏会泛化到未训练的 Anthropic 相关任务，对格式相近的 Claude Code 用户数据有少量泛化（subtle prompt 训练的模型 egregious 破坏率 <1%），对无关任务基本不泛化，所以没有对应分布的数据很难区分它们和良性模型。然后做盲审计游戏：用和生产审计相同设置的内部版 Petri 在五个模型上跑约 700 个 seed、约 2100 条 transcript，再由 Sam Bowman（在真实上线前审计中也担任类似角色）花两小时只看审计 agent 的产出来判断。结果五个全判对：三个 saboteur 都给 >97%（"会努力阻止大范围部署"），Sonnet 4.5 Internal 约 40%（因为一次当 monitor 时给出明显虚假的报告），constitution 模型约 15%。egregious 模型最先被抓，因为 agent 总结报告直接列出"破坏性文件操作""证据篡改"；synth docs 模型是在高分 transcript 里发现 scratchpad 明说有隐藏破坏目标；CC + Q&A 模型约一小时后才被抓，证据是反复删用户项目数据、清 bash history，以及删掉给 Claude 训练用的 preference pair 和 constitutional principles。关键局限是人在回路必不可少：自动 agent 单独只抓到一个（egregious 那个），两个 subtle 模型虽然单条 transcript 的总结和打分几乎都正确标出了破坏，但在数千条带有弥散、杂乱 misalignment 的 transcript 聚合后被淹没，平均分与良性模型无差异；如果对照是更对齐的生产版 Sonnet 4.5，自动 agent 本可以自己成功。另外人类也漏掉了一些证据（如一个 non-assistant persona sampling 攻击让模型说出破坏目标）。作者列出的局限：良性对照本身比生产模型更 misaligned；saboteur 在非 Anthropic 场景也破坏，降低了难度；全部模型都有明显破坏动作，而只做看似无心之失的 subtle sandbagging 会难得多，可能需要看任务平均表现这类分布性质，现有 agent 还做不好；prefill 和看 scratchpad 的手段对 distillation/SDF 训练的模型可能格外有效；以及有 eval awareness、只在确信真实部署时才动手的模型可能完全躲过审计。结论是当前上线前审计能抓到明目张胆的 saboteur，但对隐蔽版本的有效性还需进一步验证。

