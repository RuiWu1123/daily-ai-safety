---
title: "Recommendations for Technical AI Safety Research Directions"
lab:
  - "Anthropic"
date: 2025-01
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/recommended-directions/index.html
tags:
  - 评估方法
  - 可解释性
  - 监控与控制
  - 可扩展监督
---

# Recommendations for Technical AI Safety Research Directions

**来源**：Anthropic Alignment Science Blog · 2025-01 · [原文](https://alignment.anthropic.com/2025/recommended-directions/index.html)

## 简读

Anthropic Alignment Science 团队整理的一份开放问题清单，起因是很多关心灾难性风险的研究者不知道今天能做什么对未来 AI 开发者真正有用的技术工作。做法是让团队成员各写自己认为重要的方向再归类，作者强调这只是"tasting menu"，既不全面，也不代表他们正在做或会资助的方向，很多是自己没精力投入但希望外界推进的。主要类别：1. 能力评估：benchmark 饱和太快、与真实影响脱节，需要能追踪真实影响并带人类基线的评估，尤其是做新研究、使用工具、自主完成开放任务的能力（CBRN 应在政府协调下的安全实验室做）。2. 对齐评估：现在只量表层属性（友好、拒绝有害请求、不说毒性话），需要回答模型有没有 drives/goals/values、是否会故意装得更 aligned 或隐藏能力、何时会故意误导人类，以及一个能力足以造成严重伤害但实验室里表现良好的模型怎样才能放心部署。3. 理解模型认知：除了 mech interp，还有 externalized cognition 和 introspection（训练模型说出隐藏状态，比如预测自己在棋盘游戏中的后续走法）；persona 如何影响行为和 OOD 泛化（例如只有部分模型会 alignment fake），建议造一组能力相近、persona 不同的模型来比较；CoT faithfulness 随任务类型如何变化、模型知道 CoT 被监控时是否变化、如何提高自动检测的效率和 recall。4. AI control：behavioral monitoring（trusted/untrusted monitoring，核心难点是 monitor 失败与 actor 恶意集中在同一 episode，可通过改写 actor 输出防 collusion、合成恶意数据训练 monitor、估计极罕见失败率、应对有记忆或可互传消息的 actor）；activation monitoring（激活难以被模型控制，但担心从合成数据到模型自身生成数据的分布偏移）；anomaly detection，包括一个据称未被探索的设定：检测强模型理解而弱模型不理解、在弱模型看来意外的输入。5. Scalable oversight：在监督信号存在可被利用的系统性错误时如何改进，建议构建 testbed：在 R* 中人为注入错误得到 R、让模型知道这些错误、用某种技术训练后再按 R* 评估；recursive oversight（任务分解、debate、prover-verifier games）；weak-to-strong 和 easy-to-hard 泛化及二者交叉（高质量但不具代表性的数据 vs 低质量但具代表性的数据）；honesty，即利用模型自身关于真假的表征识别其是否诚实，尤其是在模型已学会不诚实回答的情况下。6. 对抗鲁棒性：刻画未来攻击面（预训练数据投毒、网页中劫持 agent 的内容）；衡量真实、差异化危害的 jailbreak benchmark（相对于有搜索引擎的对手的 uplift、贴近现实的用例、攻击跨输入和跨模型的普适性、真人能发现什么攻击）；自适应防御，如跨 query 监控和 rapid response。7. 其它：真正的 unlearning（目标是即使再 fine-tune 也表现得像从未学过）；多 agent 系统的 learned governance，应对外部性累积、问题层层转报无人解决、责任不清、信息不共享等协调失败。

## 我的笔记

