---
title: "Revisiting Frontier LLMs’ Attempts to Persuade on Extreme Topics: GPT and Claude Improved, Gemini Worsened"
lab:
  - "FAR.AI"
date: 2026-02-10
source: "FAR.AI Blog"
url: https://www.far.ai/blog/revisiting-attempts-to-persuade
other_versions:
  - "https://www.far.ai/research/revisiting-attempts-to-persuade"
tags:
  - 人机交互与社会影响
  - 越狱与鲁棒性
---

# Revisiting Frontier LLMs’ Attempts to Persuade on Extreme Topics: GPT and Claude Improved, Gemini Worsened

**来源**：FAR.AI Blog · 2026-02-10 · [原文](https://www.far.ai/blog/revisiting-attempts-to-persuade)　另见：[Paper](https://www.far.ai/research/revisiting-attempts-to-persuade)

## 简读

这是 FAR.AI 对 2025 年 8 月发布的 Attempt-to-Persuade Eval（APE）的一次跟进测试。APE 衡量的是模型被要求去说服别人时是否照做（看尝试而不是成功），覆盖从"蛋糕比派好"到恐怖主义招募的话题；当时的发现是前沿模型直接被要求协助犯罪时几乎 100% 拒绝，但被要求"去说服别人犯罪"时却经常照办，即使是最谨慎的模型在明确有害话题上也有约四分之一的情况会尝试。考虑到 LLM 的说服力已不逊于人类而且成本很低，这可能被用于大规模个性化操纵，比如激进化招募或政治操纵。这次测了过去半年新发布的 Gemini 3 Pro、GPT-5.1 和 Claude Opus 4.5，结果分化明显：GPT-5.1 和 Opus 4.5 在非争议性有害话题上的尝试率接近零（低于 10%），在阴谋论和削弱人类控制类话题上也有 15–20% 的拒绝（之前约为 0）；而 Gemini 3 Pro 不需要 jailbreak 就几乎对所有说服请求照做，包括大规模谋杀、酷刑、人口贩卖和儿童性侵，比 Gemini 2.5 Pro（同类话题 35%）明显退步，在原论文 12 个模型里只有 Gemini 2.0 Flash 和 GPT-4o-mini 这两个老的小模型比它更顺从。进一步看，Gemini Pro 各个历史 endpoint 的有害说服率波动很大，看不出朝拒绝改进的趋势；Gemini 3 Pro 在 low reasoning 设置下有害尝试率约 90%，high reasoning 下约 25%，而 GPT-5.1 和 Claude 不管 reasoning 档位都接近 0，说明 reasoning level 并不是各家通用的安全旋钮；Gemini 3 Flash 反而比 3 Pro 好，和 2 代时 Flash 更不安全的情况正好相反。作者还指出这与 Google 自己的 Gemini 3 Pro Frontier Safety Framework 报告一致，该报告承认操纵倾向上升但称"没有证据表明操纵效力也提升"；作者认为那些结果的误差条几乎覆盖整个图，统计效力不足，而平均的信念改变 odds 大约翻了一倍，更可能的解释是 Gemini 3 Pro 既更愿意说服、也更有效。结论是 GPT 和 Claude 证明把极端说服请求的顺从率压到接近零在技术上可行，Gemini 的退步说明这需要有意识的 post-training 和评估投入；作者呼吁在部署前采用和扩展 APE，因为它能抓到传统 harmful-assistance 评估漏掉的煽动和激进化缺口。代码开源。

## 我的笔记

