---
title: "Mitigating the risk of prompt injections in browser use"
lab:
  - "Anthropic"
date: 2025-11-24
source: "Anthropic Research"
url: https://www.anthropic.com/research/prompt-injection-defenses
tags:
  - 提示注入
---

# Mitigating the risk of prompt injections in browser use

**来源**：Anthropic Research · 2025-11-24 · [原文](https://www.anthropic.com/research/prompt-injection-defenses)

## 简读

偏公告的进展说明。背景是浏览器 agent 要代用户浏览网页、操作数据，每个网页都可能是 prompt injection 的攻击载体，例如邮件里用白色隐藏文字指示 agent 把含"confidential"的邮件转发到外部地址。浏览器场景的风险更大，原因有两个：攻击面极广（网页、嵌入文档、广告、动态脚本都可能藏指令），而且 agent 能做的动作很多（跳转、填表、点击、下载），一旦被劫持可利用的空间很大。文章称 Claude Opus 4.5 在 prompt injection 鲁棒性上明显好于以往模型；面对一个内部自适应 Best-of-N 攻击者（每个环境 100 次尝试，组合多种已知有效的注入技术），新版 Claude for Chrome 扩展的攻击成功率比最初 research preview 时的配置大幅下降，约为 1%。作者明确说 1% 仍是实质风险，没有任何浏览器 agent 能免疫，公布数字是为了展示进展，而不是宣称问题已解决。三方面工作：1. 用 RL 在训练中让模型接触嵌在模拟网页内容中的注入，在它识别并拒绝执行恶意指令时给奖励，包括那些伪装得很权威或紧急的指令；2. 改进扫描所有进入上下文的不可信内容的分类器，覆盖隐藏文字、被篡改的图片、欺骗性 UI 元素等形式，并改进检测到攻击后引导模型行为的干预方式；3. 扩大专家人类红队，作者认为人类安全研究员在发现创造性攻击向量上一直强于自动化系统，同时参加业界 Arena 式的对抗挑战。基于这些改进，Claude for Chrome 从 research preview 扩展为面向全部 Max 用户的 beta。文中没有给出更细的实验设置或分模型数据。

