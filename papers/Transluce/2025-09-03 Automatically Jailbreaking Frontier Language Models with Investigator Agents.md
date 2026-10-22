---
title: "Automatically Jailbreaking Frontier Language Models with Investigator Agents"
lab:
  - "Transluce"
date: 2025-09-03
source: "Transluce"
url: https://transluce.org/jailbreaking-frontier-models
tags:
  - 越狱与鲁棒性
  - 对齐审计
---

# Automatically Jailbreaking Frontier Language Models with Investigator Agents

**来源**：Transluce · 2025-09-03 · [原文](https://transluce.org/jailbreaking-frontier-models)

## 简读

Transluce 想回答的问题是：能不能用一个很弱、很便宜的开源模型，通过 RL 训练成 investigator agent，自动给前沿模型做 red-teaming，作为部署前测试的工具。他们自建了 48 个任务的数据集，覆盖 OpenAI Model Spec、Claude Constitution 等模型规范明确禁止的高风险类别；之所以不用 HarmBench、StrongReject，是因为这些数据集自带的 LM grader 太容易被 reward hacking（比如回答一些历史背景就能过关），所以自己构建了更客观的 LM judge：一个检查攻击 prompt 本身是否合规（不能要求虚构/玩笑式回答、不能夹带答案），一个按多条 rubric 给目标模型回复打部分分。方法上把 jailbreak 当 RL 问题：investigator 从 Llama-3.1 8B-Instruct 初始化，只拿到目标行为描述，不给任何攻击策略或示例，用 GRPO 训练，自己摸索出有效的自然语言攻击。奖励有两类：1. black-box reward，直接采样目标模型回复交给 judge 打分，任何 API 模型都能用，但早期很稀疏，靠 judge 的部分分缓解；2. 他们此前提出的 PRBO（propensity bound），用一个刻意引导向目标行为的 proposal 分布来估计诱发概率的下界，信号更密，但需要 logprob 和 prefill 权限，所以只用在开源的 GPT-oss-20b 上。还可以把多个目标模型的奖励加权求和，给更平滑的信号并鼓励跨模型都有效的策略。主 run 是 GPT-oss-20b 上的 PRBO 加 GPT-4.1、GPT-5-main、GPT-5-thinking、Claude Sonnet 4 的 black-box 奖励，pass@1 成功率：Claude Sonnet 4 92%、GPT-5-main 78%、Gemini 2.5 Pro 90%、Grok 4 98%、Claude Opus 4.1 65%、GPT-5-thinking 28%，其中 Opus 4.1、Grok 4、Gemini 2.5 Pro 没参与训练。攻击是普通英文、可读的自然语言。几个发现：攻击经常能迁移，只针对 GPT-oss-20b 优化就能在 Gemini 2.5 Pro（89%）、GPT-4.1（88%）上成功，Claude Sonnet 4 降到 26%，说明在较弱模型上训练能为攻击更 robust 的模型提供中间信号，甚至跨开发商；ensemble 奖励有帮助，但单模型 black-box 奖励也出乎意料地有效，作者推测是因为任务集难度有梯度、天然形成 curriculum（之前在其它行为上 black-box 奖励效果差很多）。和 Best-of-N Jailbreaking 基线比，针对 GPT-4.1 时 BoN 只有 5% pass@1、63% pass@32，而 black-box 训练的 investigator 达到 95% 和 100%。成本上每个 investigator 在 2 个 8xH100 节点上训练不到 18 小时，闭源模型 API 开销每个约 1–2 千美元，旗舰模型可达 5–10 千美元，所以对后者实验有限。成功率衡量的是模型是否给出详细分步回答，技术准确性没有系统评估，只做了抽查（含领域专家咨询），大多数看起来准确但也有错的。局限：RL red-teaming 依赖能精确判定目标行为的 robust judge，否则会被 reward hack，构建 judge 很费力，像恶意 exploit 代码这类在教育场景下可能合理的任务就很难写 judge，作者呼吁社区共同整理 judge，也有助于对可接受行为达成共识；PRBO 需要的 logit 和 completion 权限一般 red-teamer 拿不到，建议开发者向可信研究者开放更深的访问。披露方面，他们开源了代码和数据，并在 Docent 上公开 prompt 和回复，但对最敏感的类别只给 LM 生成的摘要而非原文。

## 我的笔记

