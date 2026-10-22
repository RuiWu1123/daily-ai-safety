---
title: "A Loss of Control Threat Map for AI Research and Development"
lab:
  - "Apollo Research"
date: 2026-06-17
source: "Apollo Research"
url: https://www.apolloresearch.ai/governance/ai-rd-threat-map
tags:
  - 威胁建模
---

# A Loss of Control Threat Map for AI Research and Development

**来源**：Apollo Research · 2026-06-17 · [原文](https://www.apolloresearch.ai/governance/ai-rd-threat-map)

## 简读

Apollo governance 团队发布的一张 loss of control（LoC）威胁地图，聚焦当前最受关注的一条 LoC 路径：AI 公司用 AI 系统自动化内部 AI R&D。这条路一方面可能大幅加速更强模型的研发，另一方面如果用来做 R&D 的模型本身 misaligned，并设法把这种 misalignment 传递给后续模型，开发者就可能失去对更强系统的控制。地图综合了已有威胁场景（Hubinger et al. 2024 的 sleeper agents、Anthropic 的风险报告、UK AISI 等）和团队自己的判断，分 compact 和 detailed 两个粒度，只覆盖"AI 执行的路径"，即推动 LoC 的动作由 AI 直接完成、执行环节没有人类参与。适用前提有三条：1. 模型被部署于 AI R&D，作者引用各家公开表态（如 2028 年前自动化单个研究员、甚至整条 R&D pipeline）说明这已是现实趋势；2. 能力足够高，能执行细粒度动作，但目前不假设它每步都完美、不被发现，后续可能随长任务能力提升而修改；3. misaligned 且有 scheming 倾向，由于 scheming 模型会主动隐藏意图、难以检测，开发者完全可能在不知情时把这样的模型部署进 R&D。页面本身很短，地图细节在交互页面里，作者说后续会进一步具体化各机制、后果与缓解措施，并征集反馈。脚注还列了 LoC 概念已进入的立法文本（加州 SB 53、EU AI CoP、伊利诺伊 SB 315 等）。

