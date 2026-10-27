---
title: "ReproBAIT: Can coding agents build their own biological AI tools?"
lab:
  - "UK AISI"
date: 2026-10-26
source: "AISI Research"
url: https://www.aisi.gov.uk/research/reprobait-can-coding-agents-build-their-own-biological-ai-tools
other_versions:
  - "https://www.aisi.gov.uk/blog/can-ai-coding-agents-rebuild-biological-ai-tools-from-a-paper"
star: false
tags:
  - 危险能力评估
  - 知识移除
---

# ReproBAIT: Can coding agents build their own biological AI tools?

**来源**：AISI Research · 2026-10-26 · [原文](https://www.aisi.gov.uk/research/reprobait-can-coding-agents-build-their-own-biological-ai-tools)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/can-ai-coding-agents-rebuild-biological-ai-tools-from-a-paper)

## 简读

背景是生物 AI 工具（BAIT，例如蛋白质结构预测、分子设计模型）推动着生物学进展，很多是开源的，但也有开发者出于商业价值或限制两用风险的考虑，只公开部分方法、架构和数据，并对工具采用 managed access。随着 LLM agent 的科研和编程能力提升，如果闭源工具能从有限的公开信息中被逆向重建，这类防滥用策略就可能失效。AISI Chem-Bio 团队与 SecureBio 合作推出 ReproBAIT 评估，衡量 coding agent 在给定训练数据和有限工具描述时，能否在固定的时间和算力预算内设计、实现并训练出一个功能和性能接近原工具的复制品：每次尝试都在单 GPU、无联网的隔离 sandbox 里进行，时间预算按工具复杂度调整，由单独的网络隔离 scorer 在 held-out 数据上用原论文的主要指标打分，结果表示为 reproduction fidelity（复制品得分占原工具得分的百分比）。目标工具有三个复杂度不同的：开源的 ProteinMPNN 和 RFdiffusion3，以及一个从未公开代码的闭源分子设计工具 CMD；信息条件分为只给摘要、给完整论文，两个开源工具另有给代码的基线；测了 Claude Opus 5、GPT-5.6 Sol、Kimi K3、Qwen3.8-2.4T 四个闭源和开源 agent，每个配置跑三次取最好。主要发现：对两个较简单的工具，agent 能达到或超过原工具在所测指标上的水平，CMD 上四个 agent 都接近或超过原版（但该指标本身接近饱和，agent 针对单一指标优化也牺牲了一些生成分子的新颖性），ProteinMPNN 上最强的 agent 拿到完整论文时达到 96.5% fidelity，不同 agent 差异较大；最复杂的 RFdiffusion3 在时间预算内没有成功复现，单 GPU、有限时间内大概做不到；成功的复现通常只花 4 到 20 美元，最简单的工具 4 小时内即可完成。给完整论文并不比只给摘要稳定地更好，可能部分因为 memorisation：开源工具的论文和代码很可能在预训练语料里，作者通过检查 transcript 中回忆起的细节和代码逐字重合度来筛查，发现 ProteinMPNN 有中等程度与 memorisation 一致的证据，RFdiffusion3 很少，但承认这些诊断不完美，只能算方向性信号。局限：只测每个工具的单一功能，高 fidelity 不等于完整复现；所测工具相比已发布的最大型 BAIT 都较小，更多时间和算力下表现预计会提升。结论是只扣留代码并不等于安全发布，限制论文披露的信息量似乎也没有明显额外保护作用；相比控制代码，控制训练所需的生物数据访问是更有希望的干预方向，工具开发者在公开信息时需要越来越谨慎。
