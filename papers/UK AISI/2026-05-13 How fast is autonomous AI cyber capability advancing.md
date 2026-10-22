---
title: "How fast is autonomous AI cyber capability advancing?"
lab:
  - "UK AISI"
date: 2026-05-13
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing
tags:
  - 网络安全
  - 危险能力评估
  - 评估方法
---

# How fast is autonomous AI cyber capability advancing?

**来源**：AISI Blog · 2026-05-13 · [原文](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing)

## 简读

AISI 跟踪自主 AI cyber 能力的进展速度，用来给政府备战提供依据（再由 NCSC 等转化为对企业的建议）。方法是 cyber time horizon：给 narrow cyber suite 里每个任务（逆向、web exploitation 等自包含任务）标一个人类专家完成时间，超过三分之一的任务有真实计时的 human baseline，其余靠专家估计；然后根据前沿模型在各任务上的成功率，估计其以 80% 成功率能完成多长的任务，并对各时期最强模型拟合指数曲线。为了跨时间可比，每个任务只给 2.5M token，并用简单 scaffold，这会明显低估模型能力（cyber range 实验里用到 100M token 仍在涨，新模型尤其吃更多 token）。主要结果：2025 年 11 月估计的 doubling time 是 8 个月，2026 年 2 月估计自 2024 年底 reasoning model 出现以来 80% 可靠度的 horizon 每 4.7 个月翻倍，而之后的 Claude Mythos Preview 和 GPT-5.5 又显著跑赢这个趋势，目前还说不清是孤立的跳变还是新的更快趋势。这两个模型在最长任务上几乎 100% 成功（Mythos Preview 在 2.5M 限制下六个 8 小时以上任务全部 100%），误差条上界很大，已经顶到这个 suite 能测的极限；去掉 token 上限后成功率高到无法计算 horizon。不确定性来源包括 8 小时以上任务只有 6 个、长任务的 human baseline 很少、拟合用的模型数量少，但剔除任何单个模型只会让 pre-Mythos 的 doubling time 落在 4.1 到 5.0 个月之间。这一结果与 METR 在软件工程任务上约 4.2 个月的 doubling time 接近。在更真实的 cyber range（已获得初始访问的小型无防御企业网络）上，更新的 Mythos Preview checkpoint 首次完成了两个 range：“The Last Ones”10 次成功 6 次，此前没人解出的 “Cooling Tower”10 次成功 3 次；GPT-5.5 解出 “The Last Ones”3/10。作者特别指出同一模型的后续 checkpoint 也能显著改变对前沿能力的估计。结论是 cyber 任务长度以“月”而非“年”为单位翻倍，但这些证据不能说明未来速度、何时到达某个阈值，以及对有防御的真实系统意味着什么；AISI 在开发更难的评估，包括新的 range 和加入主动防御。

## 我的笔记

