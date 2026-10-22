---
title: "Many-shot jailbreaking"
lab:
  - "Anthropic"
date: 2024-04-02
source: "Anthropic Research"
url: https://www.anthropic.com/research/many-shot-jailbreaking
tags:
  - 越狱与鲁棒性
---

# Many-shot jailbreaking

**来源**：Anthropic Research · 2024-04-02 · [原文](https://www.anthropic.com/research/many-shot-jailbreaking)

## 简读

Anthropic 公开了一种利用长 context window 的 jailbreak：many-shot jailbreaking，对自家和其它公司的模型都有效，发布前已私下通报学界和其它 AI 公司并在自家系统上做了缓解。背景是 context window 从 2023 年初的约 4,000 token 涨到 100 万以上。攻击很简单：在单个 prompt 里塞大量伪造的 user/assistant 对话，assistant 都乐于回答有害问题，最后接上真正的目标问题。几个 shot 时安全训练仍会触发拒答，但 shot 数增加到一定程度后（测试到 256），有害回复比例随之上升，覆盖暴力仇恨言论、欺骗、歧视、受管制内容等类别（演示模型为 Claude 2.0）；与其它已发表的 jailbreak 技术组合效果更强，所需 prompt 更短。作者把机制归到 in-context learning：攻击效果随 shot 数服从 power law，而完全无害的 in-context learning 任务也呈现非常相似的 power law；这也能解释为什么更大的模型往往更容易被攻破（需要的 shot 更少），因为大模型 in-context learning 更强，而大模型恰恰潜在危害最大。缓解方面，直接限制 context 长度最彻底但牺牲可用性；微调模型拒绝看起来像 many-shot 攻击的 query 只是推迟了 jailbreak，需要更多 shot 但最终仍会产生有害输出；更有效的是在 prompt 进入模型前做分类和修改，其中一种方法把攻击成功率从 61% 降到 2%，他们仍在研究这类方法对有用性的代价以及可能绕过检测的变体。公开的理由：希望尽快修复、问题不好解决需要大家一起想办法；想培养在 LLM 提供者之间公开分享漏洞的文化；攻击太简单，短 context 版本已有研究，很可能被独立发现；当前模型还不构成灾难性风险，现在正是在更危险模型出现前解决的时候。更一般的教训是，看似无害的能力改进（更长输入）也可能带来意料之外的后果。

## 我的笔记

