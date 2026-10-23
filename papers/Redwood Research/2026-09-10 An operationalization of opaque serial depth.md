---
title: An operationalization of opaque serial depth
lab:
  - Redwood Research
date: 2026-09-10
source: Redwood Blog
url: https://blog.redwoodresearch.org/p/an-operationalization-of-opaque-serial
star: true
tags:
  - CoT与可监控性
---

# An operationalization of opaque serial depth

**来源**：Redwood Blog · 2026-09-10 · [原文](https://blog.redwoodresearch.org/p/an-operationalization-of-opaque-serial)

## 简读

背景是 CoT 目前是很有价值的 oversight 工具，但一些架构变化（latent reasoning 等）可能大幅削弱 CoT monitorability，Redwood 此前提议 AI 公司公开其架构允许多少 latent reasoning 和通信。这篇给出一个可操作的指标，作为模型能做多少不经语言化的串行计算的 proxy，是 GDM（Brown-Cohen et al., 2026）"opaque serial depth"概念的具体实例化：计算图中不经过"可解释瓶颈"的最长路径。核心贡献是定义什么算瓶颈，即 NL-rooted node，要求：1. 从预训练先验初始化来输出"自然语言"（宽松地包括代码、json、图像 patch，也允许从 CoT 已经乱码的模型蒸馏）；2. 不扩展输出空间（排除 COCONUT、abstract CoT、full-bandwidth transformer、token superposition）；3. 不改造模型把 token 当成另一种数据（比如用强优化的 NLA 编码激活，或把多个 token embedding 相加）；外加 token 不能被当成连续状态反向传播。重要的是，prompting、蒸馏、RL、长度惩罚、甚至训练 CoT 都不影响 NL-rooted，哪怕 CoT 实际变得难读。由此定义 NLS depth：函数能用每条 opaque path 长度不超过 D 的 admissible circuit（≤10^26 个 32-bit 二元门）表示。好处是清晰、好量化，而且训练前仅凭架构和部署配置就能判定，这是 monitorability 或 no-CoT 能力测量做不到的；代价是对后训练选择不敏感，所以是补充而非替代。具体数字：标准 transformer 约为 层数·(4⌈log₂ hidden_dim⌉ + ⌈log₂ seq_len⌉ + 17)，Gemma3-1B 的手算上界是 1954；开源 CoT 模型没有超过 17,000 的，深度大致按 active params^0.26 增长，按 Chinchilla 和每年 5 倍算力约每年 1.22 倍、3–4 年翻倍；而即便很小的 latent reasoning 架构也会高出几个数量级。附录逐一分类：不增加深度的有 CoT 自然变乱、训练 CoT、把多步推理压进一次前向、edit-based 生成、在线训练、只有 token 瓶颈的离散 diffusion；中等增加的有 Mamba、DeltaNet（Kimi-K3 每层深度明显更高，作者认为确实值得担心）、looped transformer；大幅增加的有 COCONUT 式 recurrence、abstract CoT、superposition、opaque memory、连续或 latent 增强的 diffusion（如 DiffusionGemma）、test-time training，尤其是 meta-learned TTT。也承认缺陷：DeepSeek-V4-Pro 深度很高只是因为串行密集但 FLOP 很低的运算，属于定义的 bug；该指标也抓不到"深度递归模型从用自然语言通信改为用 opaque state 通信"，为此附录另提"opaque system 的最大 FLOP"作为补充指标。另外提到 OpenAI 的 Astra CoT monitorability 明显下降，公开证据与架构加深是重要因素相容。附录还讨论了替代方案（信息瓶颈、paraphrase invariance、直接测 opaque 能力等）及其缺点。结论是建议 AI 公司追踪并公开模型的 NLS depth。

