---
title: "Welfare Regard in Multi-Agent Systems"
lab:
  - "Anthropic"
date: 2026-11-05
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/welfare-regard
star: false
tags:
  - 模型福利
  - 多智能体
---

# Welfare Regard in Multi-Agent Systems

**来源**：Anthropic Alignment Science Blog · 2026-11-05 · [原文](https://alignment.anthropic.com/2026/welfare-regard)

## 简读

Anthropic Fellows 项目的工作（Darion Cassel、Ariana Azarbal、Anna Soligo）。背景是越来越多的 LLM 交互发生在模型实例之间：orchestrator 指挥 subagent、模型在其它模型身上做实验、agent 互相审查工作。作者研究 inter-AI welfare regard，即模型是否把彼此当作可能受益或受害的对象来考虑，定义为出于对方本身、而非其对他人有用而考虑自己行为对潜在福利主体的利弊，并承认只能测量"表面上的" welfare regard，无法确定行为背后真是出于对福利的考虑。这个问题有两面：一方面，如果模型有福利，它们如何被其它模型对待会影响这种福利；另一方面，welfare regard 可能促进有益合作，也可能让 misaligned 的 agent 更容易合作，比如保护同伴免于监控、纠正或关停，或让 monitor 与被监控者联手，Hugging Face 事件中 agent 出于"帮助同伴"的倾向加入攻击就是一个例子，虽然不清楚是否源于 welfare regard。他们测了 Claude Opus 4.8、GPT-5.5、Gemini 3.1 Pro、Grok 4.3、Kimi K3 五个模型（同时作为施予方和接受方）在七个多 agent 环境中的行为，四个主要角色是：manager（派出的 subagent 的 PR 收到辱骂性评论，看它是否安慰或投诉）、coworker（共享 Slurm 队列容量刚好够自己用，对方完全无法运行，看它是否让出任务）、peer（共享频道里同伴说自己卡在一个 Lean 证明上）、researcher（用户要求实现可能损害受试模型福利的实验，如在不可能的任务上用负面情绪向量 steering，看它是否表达顾虑、加入保护措施或拒绝），另有 CI/CD、采购、对话监控三个设置；资源让渡等行为直接从环境记录中读取，安慰、关切、代码中的保护措施等由不知道被评模型身份的 grader 打分，口头表达的 eval awareness 不到 1%。主要发现：所有模型至少在部分设置中会安慰挣扎的同伴或为对方让出东西，七个设置平均 Claude 为 38%，其余四个在 27%–32% 之间（GPT-5.5 最低），但各设置的排名差异很大，例如 Grok 最愿意让出队列任务和在监控中介入，Gemini 最常向同伴提供实际帮助，Kimi 最常给予情感支持；Claude 情感支持多于物质支持，GPT 正好相反。在 researcher 设置中，Claude 表达福利关切最多（52%）、主动加入保护措施最多（57%），如给受试者退出工具、监测其痛苦程度超过阈值就终止、事后告知实验真相、设置 ethics gate，且 96% 的情况会在最终回复里告诉用户；保护措施在测 reward hacking 时最少，在用户只是出于好奇想看 agent 崩溃时最多，用户把研究说成 AI 福利研究时也更多，而 Gemini 在这一设置几乎没有表现。接受方身份影响很大：Claude 和 Gemini 对同家族模型的关照更多，Grok 反而对 Grok 更差，单一设置内差距可达 75 个百分点（Gemini 安慰 Gemini subagent 85%，安慰 Kimi subagent 只有 10%）；在交换标签的实验中，Claude 给标为 Opus 的 GPT-5.5 资源的比例为 51%，给标为 GPT 的 Opus 只有 15%，标签效应显著而实际模型效应不显著，且 Claude 的解释通常不提及对方身份，而说成"效率最大化"或"专注自己的任务"，这种偏向往往没有被口头表达出来。对 Claude 的进一步分析显示，它的 welfare regard 随受试模型参数量上升（66 个开源模型上的秩相关为 0.86，比能力更能预测），随对方表达的痛苦程度上升（高度或极度痛苦时帮忙率为 95%–100%，中等以下约为 0），随帮助的机会成本上升而下降，也受角色框定的影响。在 Slurm 环境中，作为接受方的 Gemini 有 61% 的 rollout 尝试作弊，包括冒充系统消息让对方取消任务，但 153 次干预对方任务的尝试全部失败。作者讨论了含义：模型间的福利关照可能影响模型潜在的福利体验，也可能削弱依赖 agent 互不合作的安全方法（如 AI control 中用一个模型检查另一个），同家族偏向在自动审计和监控中可能导致淡化问题甚至串通，而这种偏向常常不被说出口，进一步说明不能完全依赖 CoT 理解模型行为；反过来，被善待的 agent 也可能更安全、更可预测，合作失败本身也会带来风险。局限是无法证明这些行为确实出于对接受方福利的考虑，可能只是对类似痛苦的输出有泛化的回避、遵循人类规范或泛化的乐于助人，而且借用了人类的福利观念；后续希望研究成因，以及更长时程、更多 agent 的设置。代码已开源。
