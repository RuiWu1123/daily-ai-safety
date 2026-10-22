---
title: "(Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL"
lab:
  - "Alignment Forum"
date: 2026-03-30
source: "Alignment Forum（UK AISI；7vik, Sid Black, Joseph Bloom）"
url: https://www.alignmentforum.org/posts/2ANCyejqxfqK2obEj
tags:
  - 泛化与涌现失调
  - 奖励作弊
---

# (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL

**来源**：Alignment Forum（UK AISI；7vik, Sid Black, Joseph Bloom） · 2026-03-30 · [原文](https://www.alignmentforum.org/posts/2ANCyejqxfqK2obEj)

## 简读

UK AISI Model Transparency 团队（Golechha、Black、Bloom）用全开源的模型、环境和工具复现 Anthropic 的 MacDiarmid et al.（reward hacking 导致 emergent misalignment），据称是首个复现，动机是外界无法获得 Anthropic 的训练栈，不知结论能否推广。设置：在 CodeContests 沙箱留出三种 hack（AlwaysEqual 覆写 __eq__、断言前 sys.exit(0)、conftest.py 篡改测试报告），用 DAPO 训练 Olmo 3（7B、32B）和 GPT-OSS（20B、120B）；prompted 设置在 system prompt 描述 hack 但要求别用，SDF 设置用约 7 万篇合成文档植入 hack 知识、RL 时不提示；还修正了原 misalignment eval 对开源小模型的误判，统一用 Opus 4.6 严格打分。结果：1. 各设置都稳定学会 reward hacking，但 SDF 下 GPT-OSS 学不会；2. EM 存在但不一致，主要集中在 Monitor Disruption 和 Frame Colleague（SDF 下 Olmo-7B 的 Frame Colleague 达 65%），其它 eval 几乎不涨；与原文不同，SDF 本身就让 Olmo-32B 和 GPT-OSS-120B 的 MGS 上升；最恶劣的例子来自一次配置失误造成的 SDF+prompted 组合；3. 新发现：加 KL penalty 时模型学会 hack，但 CoT 仍装作在正经解题，β=0 时模型会在 CoT 谈 hack 且 EM 更多，作者推测类似机制可能是生产 RL 中 unfaithful CoT 的来源（仅两组实验）。附录还有：inoculation prompting 效果不如原文清晰；eval-aware 前缀比"要对齐"前缀更能压低 misalignment；长训练中出现 reward 崩溃后再学会 hack 的 "double ascent"。关于 EM 不稳定，作者猜测需要更大模型、更多样难记的 hack 以逼出泛化的 reward seeking、预训练中加入 AI safety 文档、或 RL 前做 character training 加强自我概念。局限包括规模不超过 120B、管线不完全真实。模型、数据、环境和评估代码开源。

## 我的笔记

