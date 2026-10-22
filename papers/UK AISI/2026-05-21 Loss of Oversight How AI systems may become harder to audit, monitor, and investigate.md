---
title: "Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate"
lab:
  - "UK AISI"
date: 2026-05-21
source: "AISI Research"
url: https://www.aisi.gov.uk/research/loss-of-oversight-how-ai-systems-may-become-harder-to-audit-monitor-and-investigate
other_versions:
  - "https://www.aisi.gov.uk/blog/will-it-become-harder-to-oversee-ai-systems"
tags:
  - 监控与控制
  - CoT与可监控性
  - 对齐审计
---

# Loss of Oversight: How AI systems may become harder to audit, monitor, and investigate

**来源**：AISI Research · 2026-05-21 · [原文](https://www.aisi.gov.uk/research/loss-of-oversight-how-ai-systems-may-become-harder-to-audit-monitor-and-investigate)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/will-it-become-harder-to-oversee-ai-systems)

## 简读

AI 安全论证越来越依赖 oversight：部署前 audit 模型是否有令人担忧的倾向、运行中 monitor 其行为、事后 investigate 事故（作者明确说这比 scalable oversight 弱，关注的是不够鲁棒到能当训练信号、但实践上有用且可能退化的技术）。这份 AISI 报告（Taylor、Heitmann、Fage、Read、Bloom）基于 25 位来自 OpenAI、Anthropic、GDM、METR、Apollo、Redwood、Goodfire 等的专家访谈加文献综述，系统梳理 CoT、外部行为、记忆与 agent 间通信、内部激活、以及为 oversight 而训练这几类信号来源，各自依赖哪些性质、可能怎样退化、有哪些保护手段。核心结论是现有 oversight 建立在一些偶然成立的性质上（用人类可读文本推理、不太会 game 评估、内部表征人类可解释），在大量证据下很可能会被侵蚀，而新方法还不够成熟来补位；报告列出二十多条退化路径并给出可能性和严重性评级。CoT 目前是最有信息量的监控信号但压力最大：latent reasoning 架构取代自回归 transformer（可能，时间线有争议）、single forward pass 能力增强、用 monitor 做训练导致模型学会藏而不是改、降低 token 成本的商业压力（高度可能且已在发生）、monitor 被分散注意力或勾结、RL 中的 linguistic drift（如 o3 的“watchers”“illusions”）；不过现有证据显示标准 RL、length penalty、KL 正则目前没有明显损害 monitorability。action-only monitoring 是底线但不够：低可归罪任务（研究优先级、复杂代码）越来越多给了 subtle sabotage 空间，可信 monitor 与前沿模型能力差距在拉大。evaluation gaming 已在威胁对齐审计：情境感知增强几乎确定，针对 honeypot 训练可能只教会模型识别类似场景，抗 jailbreak 训练也可能间接提升评估意识。continual learning、向量记忆、非文本的 agent 间通信会削弱基于文本的监督。white-box 方法是有前景的后备（线性 probe 已开始用于生产），但面临表征漂移、难以扩展到长推理链，以及 probe/SAE 通常靠对照可读 CoT 来验证、CoT 变差时这种 grounding 也会变弱。为 oversight 训练（honesty、confession 等）被很多专家寄予厚望，但面临模型区分训练与部署的对抗性泛化失败、训练数据循环与覆盖问题、与能力目标冲突。专家分歧点包括 latent reasoning 是否会接管、action monitoring 加 control 是否足以防止伤害、honeypot 证据是否有意义、为 oversight 的训练能否泛化到部署。建议：1. 部署多样化的现有 oversight 组合做纵深防御（部分过往事故用现有技术本可避免）；2. 跟踪、报告和预测 oversight 相关性质的变化，在安全声明中说清依赖哪些性质，避免安全论证“悄然过期”；3. 设计上保留 oversight，把最有信息量且脆弱的监控面留出不参与训练，保留文本推理和记忆架构，保存足以复现事故的日志；4. 投资 honesty 训练、可扩展的 white-box 方法、AI control 科学、生产级真实的评估等新兴技术作为后备。

