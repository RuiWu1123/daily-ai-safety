---
title: "Have We Seen an Acceleration in Discoveries?"
lab:
  - "METR"
date: 2026-08-14
source: "METR Notes"
url: https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/
star: false
tags:
  - 评估方法
  - 网络安全
---

# Have We Seen an Acceleration in Discoveries?

**来源**：METR Notes · 2026-08-14 · [原文](https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/)

## 简读

Tom Cunningham 和 Nate Rush 的研究 note，问的是 LLM 已经在很多领域做出新发现，那整体发现速率是否真的加速了。方法很粗：收集各领域公开发现的时间序列，以 2026 年 1 月为可能的断点，只看斜率有没有变化，关注总体加速而不单看标注为 AI 的贡献；数据收集和分析全部由 agent 完成，作者尽力审过但承认仍可能有错，数据放在 GitHub 上并持续更新。结论分三块：1. 漏洞发现急剧加速——cURL CVE 从 2025 年全年的 9 个增至 2026 年截至 6 月底的 36 个（42% 标注了 AI），OpenSSL 从 6 个增至 39 个，Firefox 从 210 增至 342，Microsoft 年化约为 2025 年的 2.5 倍，NVD 和 OSV 截至 8 月已追平或超过 2025 全年；但 Firefox、Microsoft 和聚合库里带 AI 标注的只占增量的小部分（Microsoft 仅 1.3%），高严重度类别加速较弱，而被实际利用的漏洞（CISA、Vulncheck 的 KEV）增长明显慢于 CVE；2. 数学可能有加速但难以量化——arXiv 组合数学投稿从 1 月的 377 篇翻倍到 7 月的 743 篇，Smale 列表上的 Jacobian 猜想、Green 列表的第 44 题和第 100 题的 sofic 部分在 2026 年借助 AI 解决，Erdős 问题的 AI 解答激增，但历史基线很难可靠构建；3. 算法优化没有明显加速——CIFAR-10、Hutter 压缩、Gurobi、MIPLIB、nanoGPT、Stockfish、矩阵乘法指数 ω 这七个序列都看不到斜率变化，nanoGPT 和 CIFAR-10 虽有 AI 贡献，但规模在历史上并不突出。作者认为最后一点令人意外，因为 2026 年 1 月就有工作用简单模型和极少的推理算力在 5 个优化问题上刷新了前沿。对于为什么不同领域加速程度不同，他们列出几种候选解释：推理支出差异（大量资金投向用 LLM 找漏洞）、LLM 在不同领域相对于人的难度差异、披露差异（实验室很可能在内部发现算法效率改进而不公开，至少有实验室在限制公开模型参与这类发现）、数据质量差异，并认为这可能是理解 RSI 有多近的关键问题。另外他们注意到很多发现声称是用通用 prompt、无需专家引导做出的（Anthropic 的 Riemann 结果、AlphaEvolve、Mythos Preview 找漏洞），但这可能掩盖了在选题、训练和验证环节投入的专业知识。

