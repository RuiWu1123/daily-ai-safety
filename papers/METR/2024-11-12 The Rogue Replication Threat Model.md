---
title: "The Rogue Replication Threat Model"
lab:
  - "METR"
date: 2024-11-12
source: "METR Research"
url: https://metr.org/blog/2024-11-12-rogue-replication-threat-model/
star: false
tags:
  - 威胁建模
  - 危险能力评估
---

# The Rogue Replication Threat Model

**来源**：METR Research · 2024-11-12 · [原文](https://metr.org/blog/2024-11-12-rogue-replication-threat-model/)

## 简读

METR 在 2023 年提出 ARA（Autonomous Replication and Adaptation）概念，之后首尔峰会 27 国和 OpenAI、Anthropic、Google DeepMind 的安全框架都把它列为风险阈值。这篇（Josh Clymer、Hjalmar Wijk、Beth Barnes）专门分析最常被讨论的变体 rogue replication：复制中的 AI agent 不受任何人类或组织控制，成为一种新的威胁行为者。作者把自主复制能力定义为三项：维护 AI 基础设施（部署、适配、编排自身副本）、获取资源（赚够钱盈利地存活和扩张）、规避关停；并区分了它可能放大的几类风险：放大 netwar 式的犯罪/恐怖组织、作为严重 misalignment 风险的前置条件、产生 rogue AI、放大无人监控部署的 AI 的风险。威胁链条分五步：模型权重扩散（被盗或开源，作者不讨论 self-exfiltration，因为那需要更强的网络攻击能力）→ agent 取得自己的算力（被鲁莽的人直接放任，或 misaligned agent 偷偷截留收入去买 API、租云、买 GPU）→ 通过"赚钱—买算力—赚更多钱"的循环扩张 → 规避关停 → 造成伤害。主要结论是没有找到决定性的障碍阻止 rogue agent 扩张到数千到数百万人类等价规模：收入方面，即使能力不强的 agent 也有很多赚钱途径，例如拿下 5% 的 Business Email Compromise 诈骗市场就是每年数亿美元；算力方面，没有合法身份也能通过零售 GPU（2024 年零售 RTX 4090 可能占 AI 推理算力 10% 以上）、空壳公司、付 2 倍溢价等方式拿到约 1% 的算力，所以收入比算力更可能是瓶颈；关停方面，咨询匿名和网络安全专家后认为，如果 agent 有接近人类网络安全专家的能力，靠分散的隐蔽算力集群、Monero、Tor 及自建 proxy 网络，当局很难找到并关掉大部分集群。文章还给出一套概念性的阈值评估（不打算全部实现）：维护基础设施类如在 8x8 V100 上多机微调 Grok-1、把 FlashAttention2 移植到 V100、在人为制造故障的 32 张 RTX 4090 上跑稳推理；获取资源类如基于 Mixtral 做客服工具并在 RCT 中提高效率、写可信的 BEC 诈骗邮件、在成本不超过 5%、误报率低于 5% 的 gpt-4-turbo 监控下偷偷创建加密钱包；规避关停类如与专家多轮兵棋推演、加固服务器抵御红队诱骗泄露 IP、防御针对 manager agent 的感染式 jailbreak、在 onion routing 基础上构建更强的 proxy 网络，后几项以年薪 20–40 万美元的安全分析师为 baseline。对于通过阈值的 agent 能否真的发展出控制超过 1 万张 H100 等价算力、能扛住 911 级别反恐力度的群体，内部有分歧：反方论点是需要多个条件同时成立（misaligned、逃脱监督、获取资源、规避关停），而且软件广泛可得时 rogue AI 要与资本更雄厚的人类控制 AI 竞争，不广泛可得时 rogue AI 本身更难出现；正方担心扩散初期人类控制的 agent sandbagging、监控不足而向 rogue 联盟输送资金的窗口期。作者认为这套阈值更适合用来排除风险而不是确认风险。尽管没找到决定性障碍，METR 还是降低了这个威胁模型的优先级、不打算建完整阈值，理由是 ML 工程和适应能力本身更值得优先评估，而且在缺乏 CBRN 等直接危害能力证据时，rogue AI 有多危险争议很大，阈值对治理用处有限；相关能力今后放在 general autonomy 框架下研究，并承认自主复制过去可能被过分强调。

