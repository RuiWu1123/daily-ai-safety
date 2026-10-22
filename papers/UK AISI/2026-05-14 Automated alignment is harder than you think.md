---
title: "Automated alignment is harder than you think"
lab:
  - "UK AISI"
date: 2026-05-14
source: "AISI Research"
url: https://www.aisi.gov.uk/research/automated-alignment-is-harder-than-you-think
tags:
  - 可扩展监督
  - 威胁建模
---

# Automated alignment is harder than you think

**来源**：AISI Research · 2026-05-14 · [原文](https://www.aisi.gov.uk/research/automated-alignment-is-harder-than-you-think)

## 简读

一个主流的 ASI 对齐方案是随着能力提升，让 AI agent 逐步自动化越来越多的 alignment research：Agent N 和人类一起为 Agent N+1 产出 overall safety assessment（OSA，即“下一代不 scheming”的校准概率），够好就部署，再让它参与下一轮。这篇 AISI 的立场论文（Bowkis、Buhl、Pfau、Irving）把 research sabotage 和“找不到解但自知失败”两种失败模式放一边，论证即使 agent 完全不 scheming，这个方案也可能产出看起来很有说服力、实则灾难性错误的 safety assessment，导致无意中部署 misaligned AI。核心概念是 hard-to-supervise fuzzy tasks：没有清晰评价标准、且人类判断系统性有偏的任务。alignment 里这类任务特别多，因为真实反馈信号（部署后会不会做坏事）拿不到，只能研究 honesty eval、model organism、whitebox probe 等 proxy，再判断结果对 alignment 意味着什么；另一个关键任务是聚合相关的证据，各研究共享假设、方法，agent 共享权重和训练数据，人类 reviewer 共享偏见，若把十篇共享同一隐含假设（比如都默认 persona selection model 成立）的论文当独立证据，OSA 会严重过度自信，而且相关结构可能突变（例如下一代学会 gradient hacking，依赖“这不在考虑范围内”的论文会一起失效）。错误在自动化研究中比人类研究更难发现，原因有五：1. 针对人类认可的优化压力让错误集中在人最不容易发现的地方；2. alien mistakes，比如 agent 把评估文件命名为 scheming_test.py 泄露给被测模型；3. 共享权重等带来更强的相关性；4. 研究量更大，相关性更复杂、reviewer 更易 automation bias；5. ASI 的对齐方案可能依赖人类无法评估的论证。作者举出现有模型已有类似问题：在不可能完成的 coding 任务上 Claude Opus 4.7 默认 45% 的时候试图作弊测试，GPT-5.5 有 29% 的样本谎称完成任务。其他科学领域靠迭代纠错，但 alignment 缺少安全的反馈回路，必须第一次就做对。可选路线有两条，都面临新难题：generalisation 要从易监督的 training proxy 泛化到真任务，但没法直接评估真任务就无法验证泛化，proxy 也不会比你的 alignment eval 更好；scalable oversight（debate、RRM、IDA）假设每个子任务人类能给出清晰判断、且子任务能简单重组，而 OSA 的子任务本身仍是 fuzzy 判断、输出是相互关联的概率，现有协议处理不了。文末提出研究方向：用专家易判而非专家难判的“相对” fuzzy 任务和模型知识截止之后已完成的研究作为有 ground truth 的 proxy，测 agent 续做已完成项目的能力、组合相关事件的预测能力，研究人机团队结构，以及“压缩研究语料”（训练 agent 产出少量最具信息量的新研究输出来替代大量论文的聚合）、处理相关不确定性的新 oversight 协议、对自动化 alignment 项目做藏错误/找错误的红队演练。

