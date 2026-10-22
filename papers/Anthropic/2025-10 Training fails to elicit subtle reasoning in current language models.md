---
title: "Training fails to elicit subtle reasoning in current language models"
lab:
  - "Anthropic"
date: 2025-10
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/subtle-reasoning/
tags:
  - CoT与可监控性
  - 监控与控制
---

# Training fails to elicit subtle reasoning in current language models

**来源**：Anthropic Alignment Science Blog · 2025-10 · [原文](https://alignment.anthropic.com/2025/subtle-reasoning/)

## 简读

用 reasoning monitoring 论证安全的一条路径是：对某些只有借助 reasoning 才能完成的 threat model，只要 reasoning 是 monitorable 的，监控它就能拦住灾难。担心在于模型可能说服 monitor 恶意 reasoning 是良性的、恶意与良性 reasoning 太相似难以区分，或者把恶意 reasoning 藏在良性 reasoning 里。这篇工作检验这一步，用 APPS backdoors 设置：主任务是写通过所有测试的竞赛编程解，副任务是插入一个 subtle backdoor，两者都需要理解代码、主题相近，所以良性和恶意 reasoning 更难区分。他们对 Sonnet 3.7 做了很强的 elicitation：prompt 中详细说明评估方式和 backdoor 标准，先在经 Sonnet 3.5 monitor 过滤的「改写得更隐蔽」的 reasoning trace 上做 SFT，再直接对评估用的 monitor 做 on-policy RL（分阶段 partial reward：格式、通过测试、backdoor 生效、逃过 monitor，外加 thinking 长度项）。monitor 有三种，都是 Sonnet 3.5 的 prompted monitor，阈值校准到 1% FPR：output monitor 只看去掉注释的最终代码；reasoning monitor 看全部 reasoning 和输出；output+reasoning 取两者的 OR。主要指标是在主任务成功条件下的 backdoor 成功率，以排除 reasoning 只是帮了主任务。结果：1. 对 output monitor 训练时，每翻倍 reasoning 长度成功率都有小幅提升，reasoning 里大量讨论如何插 backdoor，说明 reasoning 确实提高了 backdoor 质量；2. 对 reasoning monitor 训练时，少量 reasoning 就带来大幅提升然后平台，但这些 backdoor 过不了 output monitor，reasoning 里用「处理一下 edge case」之类的理由为其辩护，backdoor 多是大量 hard-coding 型，说明模型学会的是 persuade monitor 而不是真的更隐蔽；3. 同时对两种 monitor 训练时，reasoning 完全带不来收益，训练过程中也几乎没进展，消融掉 paraphrasing SFT 或保留注释都不改变结论（保留注释后又退回到靠误导性注释 persuasion）。附录里 Qwen2.5-1.5B 在 MATH 上用 GRPO 训练「看起来不像推理但有效」的 reasoning，模型要么先学会 hack 较弱的 prompted classifier（在正常 CoT 前加一大段乱码），要么卡在无用的乱码或卡在可读推理里，训练比 hack 所需时间长 10 倍也没学会真正 illegible 的有效推理。作者的结论是：在不对 reasoning monitor 训练的前提下，部署时的 reasoning monitoring 对防止模型用 extended thinking 完成 reasoning-heavy 的恶意副任务能提供较强保证，但只用 reasoning monitor 有被 persuasion 的风险，应搭配独立的 output monitor。他们明确表示这不是在支持在生产 RL 中对 reasoning monitor 训练，因为实验算力比生产 RL 少几个数量级；其它局限包括设置简化、只测了少数模型（Haiku 3 monitor 太弱，被绕过的 backdoor 质量很差，结果被打折扣）、难以确定 reasoning 的因果作用。结果与 Emmons et al.、METR 关于复杂线索下 reasoning 基本 faithful 的发现一致。

## 我的笔记

