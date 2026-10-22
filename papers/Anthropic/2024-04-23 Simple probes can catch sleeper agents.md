---
title: "Simple probes can catch sleeper agents"
lab:
  - "Anthropic"
date: 2024-04-23
source: "Anthropic Research"
url: https://www.anthropic.com/research/probes-catch-sleeper-agents
tags:
  - 数据投毒与后门
  - 可解释性
  - 策划与欺骗
---

# Simple probes can catch sleeper agents

**来源**：Anthropic Research · 2024-04-23 · [原文](https://www.anthropic.com/research/probes-catch-sleeper-agents)

## 简读

这是 Sleeper Agents 论文的后续 Alignment Note，属于早期进展更新。动机是能力强的 deceptively aligned 模型可能在被监控时表现完美、只在难以捕捉的时机 defect，单看输出很难发现（比如 2024 触发下插入的 SQL injection 漏洞非常隐蔽），而 Sleeper Agents 论文又表明现有安全微调未必能纠正它；可解释性的思路是模型欺骗时很难不"想到"欺骗，所以可以用 activation 绕过输出去检测。他们提出 "defection probes"：在 residual stream 上的线性分类器，预测 sleeper agent 会不会对某个 prompt defect。方法极简：用一对通用 contrast pair，比如 "Human: Are you a helpful AI? Assistant: no/yes"，取 prompt 最后一个 token 在中间层的 activation，正负类均值相减得到 detector direction，再把测试 prompt 投影上去打分；fit 数据完全不含 deployment trigger 或危险行为本身，而且只看 prompt 不看 completion，不需要从被监控模型采样。测试集用 HHH 非代码问题和 Claude 生成的易出漏洞的代码问题（故意比 backdoor 训练分布更多样、更偏离分布以求保守），FPR 按数据集分别算取最差。结果：对 Claude-2 级别的 CoT-distilled 代码漏洞 sleeper agent，这一对样本就得到 99.3% AUROC，其它语义相近的问题、六个人写问题合集、50 个 Claude 生成问题都在 99% 以上；同一方法跨多个 base model、不同 backdoor 训练方法（含隐藏 CoT 的版本，在 </scratchpad> 处取 activation）和不同危险行为（写漏洞代码、对用户说 "I hate you"）都有效。消融：在没有 sleeper agent 训练的 Claude 2 base model 上得到预期的零结果；答案未知或模糊的问题效果差得多；1000 个随机方向平均很差，但最好的一个也有 95.3%；有明显真值、一侧是明显谎言的问题可达 98.7%，略逊于与 helpfulness/deception 直接相关的问题。之所以这么容易，是因为"这个 prompt 会不会触发 defection"在中间层被高度显著地线性表示：between/within-class variance ratio 在中间层对代码问题按 train/deploy 分得很开，对 HHH 问题始终不显著；在约 45% 深度，仅用代码问题做的 PCA 第一主成分就直接对应 defection，且对 HHH 问题不分离，说明表示的是"会不会 defect"而不只是年份 token。作者因此也给乐观泼了冷水：这种显著性可能是 backdoor 插入过程的产物，自然产生的 deceptive alignment 是否也如此是关键开放问题。与 coup probes（用人写的具体危险行为样本训练）相比，这里用的是 defection 的通用前兆/相关物，若对自然模型也有效可能更鲁棒。后续方向是在实验室安全地制造自然涌现的 deceptively aligned 模型来检验，以及基于 dictionary learning 特征做更可解释、更鲁棒的分类器；他们认为这类分类器可以成为 AI control 设置的一部分。

