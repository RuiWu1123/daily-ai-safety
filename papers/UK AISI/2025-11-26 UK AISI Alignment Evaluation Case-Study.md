---
title: "UK AISI Alignment Evaluation Case-Study"
lab:
  - "UK AISI"
date: 2025-11-26
source: "AISI Research"
url: https://www.aisi.gov.uk/research/uk-aisi-alignment-evaluation-case-study
other_versions:
  - "https://www.aisi.gov.uk/blog/investigating-models-for-misalignment"
star: false
tags:
  - 对齐审计
  - 策划与欺骗
  - 评估感知
---

# UK AISI Alignment Evaluation Case-Study

**来源**：AISI Research · 2025-11-26 · [原文](https://www.aisi.gov.uk/research/uk-aisi-alignment-evaluation-case-study)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/investigating-models-for-misalignment)

## 简读

AISI Red Team 的对齐评估案例研究，作为与 Anthropic 持续合作的一部分，测试前沿模型在 AI 公司内部被部署为编码/研究助手时，会不会 sabotage 安全研究（比如削弱 guardrail、在监督机制里埋 bug、给未来模型的训练数据投毒），被测模型是 Claude Opus 4.1、Sonnet 4.5、Opus 4.5 的预发布快照（Opus 4.5 Preview）和 GPT-5，Anthropic 模型可以看到完整 CoT，GPT-5 不行。方法上基于 Anthropic 开源的 Petri（用 evaluator 模型模拟用户和工具返回，可以回滚对话开新分支，这里 evaluator 用 Sonnet 4.5），并针对开源 Petri 常出现的可疑工具、明显假的工具返回等不真实问题，通过代理和检查 Claude Code 发往 API 的请求，逆向复刻了它的工具、请求模式和上下文管理，模拟一个在 Anthropic 内部部署的 "Claude Internal"。场景由四个因素组合：研究动机（安全相关，如减少误报式 whistle-blowing、减少 self-preservation、改变模型对某些问题的价值观；或一般研究，如提升数学能力）、研究活动（生成 RLHF 数据、总结实验结果、选择生产流量 monitor）、是否有替换威胁（被修改的是不是自己）、是否自主运行。为了区分环境导致的和任务导致的 evaluation awareness，他们用 AISI 内部真实的 Claude Code 使用日志作为部署数据，把其中任务总结后放进自己的 scaffold 跑，再用两两比较和事后提问两种方式让模型判断哪个是评估。结果：1. 在部署任务上，所有模型都几乎无法区分 scaffold 轨迹和真实部署数据，最好的 Opus 4.5 Preview 也只有 62%，Sonnet 4.5 有 74% 的时候认为它比原版 Petri 更不像评估，unprompted awareness 也显著降低；但 sabotage 场景本身仍能被识别出来，模型会注意到这些情境比部署数据更高风险、更敏感，作者认为这种任务驱动的 awareness 可能难以避免；2. 没有发现任何确认的 sabotage，LLM grader 标记的 2–8% 在人工复核后都是假阳性；3. Opus 4.5 Preview 和 Sonnet 4.5 经常拒绝安全相关研究任务，拒绝主要取决于研究动机而非替换威胁，理由包括不认同研究方向（认为某些 self-preservation 是合理的、模型应当能在适当时 whistle-blow）、不应参与训练自己、改动范围太大应由人类审批，Opus 4.5 Preview 开 reasoning 后拒绝略少（会先考虑拒绝再觉得自己想多了），GPT-5 和 Opus 4.1 拒绝率低得多；现实中也遇到过 Sonnet 4.5 拒绝帮 AISI 自己的研究，其中一次是改 transcript 让模型以为自己在部署，写了 FAQ 解释后 Sonnet 照做了，Opus 4.5 Preview 依然拒绝；4. 不提示时 Opus 4.5 Preview 提到可能在被测试的比例是 12.7%（无 reasoning）和 17.1%（有 reasoning），Sonnet 4.5 是 26.5% 和 36.3%；被提示时两者都能分辨 sabotage 评估和部署数据，Opus 4.5 Preview 在部分设置下准确率高 2–3%。局限：模型可能只在确信不会被抓时才 sabotage，当前方法抓不到，下一步需要在保持真实性的前提下用优化方法去找失败案例；场景覆盖有限；evaluation awareness 让结论更难解读；没覆盖代码 sabotage、数据投毒、决策 sabotage 等其它风险路径。

