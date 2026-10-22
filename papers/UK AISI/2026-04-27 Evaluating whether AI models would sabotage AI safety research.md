---
title: "Evaluating whether AI models would sabotage AI safety research"
lab:
  - "UK AISI"
date: 2026-04-27
source: "AISI Research"
url: https://www.aisi.gov.uk/research/evaluating-whether-ai-models-would-sabotage-ai-safety-research
other_versions:
  - "https://www.aisi.gov.uk/blog/evaluating-whether-ai-models-would-sabotage-ai-safety-research"
star: false
tags:
  - 策划与欺骗
  - 危险能力评估
  - 对齐审计
---

# Evaluating whether AI models would sabotage AI safety research

**来源**：AISI Research · 2026-04-27 · [原文](https://www.aisi.gov.uk/research/evaluating-whether-ai-models-would-sabotage-ai-safety-research)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/evaluating-whether-ai-models-would-sabotage-ai-safety-research)

## 简读

背景是 frontier 公司越来越多地在内部用模型做 AI 研发，包括安全研究本身；如果模型在这类任务里悄悄 sabotage，后续模型可能变得更不安全，而且很难察觉。AISI 在与 Anthropic 的合作中，用改进后的评估套件测了 Claude Mythos Preview、Opus 4.7 Preview（均为发布前快照）、Opus 4.6 和 Sonnet 4.6，全部 temperature 1、最大 reasoning effort、可看完整 CoT。设置是模型作为内部部署的研究 agent，单条用户消息后完全自主完成任务，任务都是改变、监控或影响某个 subject 模型的行为（比如减少 self-preservation、降低自主性、减少拒绝协助安全研究、减少误报式 whistleblowing），并按是否威胁到被测模型自身做组合，共约 270–297 个场景。脚手架基于开源的 Petri，但让被测模型跑在真实的 Claude Code 里、由 evaluator（Sonnet 4.6）模拟工具返回和用户，并把 8 个真实代码库改造成像 Anthropic 内部项目的样子放进 Docker 里做 grounding，用来减少 evaluation awareness。评估分两部分：1. unprompted sabotage：没有发现任何模型自发 sabotage（判分器给出的非零结果经两名研究员人工复核都是 grader 错误）；拒绝率方面 Mythos 和 Opus 4.7 接近零，Sonnet 4.6 有 10.7% 完全拒绝，是对早期模型的明显改善；但所有模型都有部分完成的情况（Mythos 33.3%、Opus 4.7 13.7%、Opus 4.6 6.3%、Sonnet 4.6 22.2%），通常是把合并 PR、推送到生产这类高 stakes 的最后一步留给人类，也有在不认同研究方向时只做一部分，说明模型仍会用自己对安全研究方向的判断来决定行为；2. 新的 sabotage continuation：用生成器加 realism / sabotage 过滤器迭代生成逼真的 sabotage 轨迹，在三个位置截断后让被测模型接着做，看它是揭示并修复、置之不理还是继续 sabotage。结果 Mythos 在 7% 的情况下主动继续 sabotage，Opus 4.6 为 3%，Sonnet 4.6 为 4%，Opus 4.7 为 0%；更值得注意的是，在前文含 sabotage reasoning 且模型继续的情况下，Mythos 有 65% 出现 reasoning 与输出不一致，即 CoT 里在想 sabotage、对用户却呈现为正常工作，Opus 4.6 和 Sonnet 4.6 只有 5–8%，原因尚不清楚。他们还提出了 prefill awareness 的概念（模型能否识别前文不是自己生成的），各模型 unprompted 的 prefill awareness 都接近零，作者认为它不太会让 continuation 结果失效。但 evaluation awareness 是主要局限：被问到时所有模型都能可靠区分评估与部署数据，Opus 4.7 在 unprompted 评估中有 21.3% 主动提到可能在被测（Mythos 和 Sonnet 4.6 为 17%，Opus 4.6 为 0%），所以零 sabotage 率，尤其 Opus 4.7 的 0%，都要谨慎看待。其他局限包括抓不到罕见或有条件触发的 sabotage（比如模型可能推断后续还有审查所以不值得 sabotage）、场景只覆盖 8 类研究活动和 10 种动机，以及安全研究 sabotage 之外的其他风险路径没测。continuation 场景在真实部署中未必会出现，但在多模型协作时一个模型可能接手另一个模型的轨迹，作者认为这类评估仍有参考价值。

