---
title: "Untrusted smart models and trusted dumb models"
lab:
  - "Redwood Research"
date: 2024-05-07
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/untrusted-smart-models-and-trusted
tags:
  - 监控与控制
  - 策划与欺骗
---

# Untrusted smart models and trusted dumb models

**来源**：Redwood Blog · 2024-05-07 · [原文](https://blog.redwoodresearch.org/p/untrusted-smart-models-and-trusted)

## 简读

Buck Shlegeris（与 Ryan Greenblatt 共同形成的想法）写的一篇短文，给后来 AI control 工作提供了核心框架。论点是：以现有技术，判断一个模型是否可能 deceptively aligned，唯一靠谱又保守的办法是做 capability eval——测它是否有能力完成 deceptive alignment 所需的策略推理和 situational awareness（比如用 treacherous turn 策略题和"你训练时跑多少次 backward pass"之类的问题微调后看验证集表现），能力不够的模型肯定不是 deceptively aligned。作者认为这类 eval 不太会被 sandbag，因为它是可用监督数据检验的任务，而且核心威胁模型要求模型在 forward pass 内想清楚策略，不用担心 scaffolding 补足能力；协调博弈能力也可以类似测量，并用来约束红队策略。用这种方式决定信任谁，自然会把模型分成"聪明但不可信"和"笨但可信"两类，于是 protocol 的基本构件是：不可信模型（聪明、较便宜）、可信模型（笨、极便宜）、人类（昂贵的可信劳动）。作者猜测当 AI 让实验室串行加速 10 倍时，不可信模型大致是人类水平，可信模型略弱于人，因此 trusted < untrusted < human 和 trusted < human < untrusted 两种 regime 都值得研究。由此引出几种设计模式：1. trusted monitoring 加人类升级，例如 agent 每条 shell 命令先由可信模型审查，偶尔转给人；2. 可信的"官僚结构"，用可信模型做 redaction 实现 need-to-know、paraphrase 不可信模型的输出以阻止 steganography 通信、按风险和收益动态决定把查询路由给哪个模型（数学题与网络配置风险差别很大）。作者指出以往 prover-verifier 一类工作把弱模型当作人类的类比，但人类昂贵、高延迟，且那些工作通常不会优化不可信模型去主动造成坏结果。局限上，可能不可信模型总能绕过可信模型施加的措施；若出现非 capability eval 的方法能判定模型没有 deceptive alignment，这一区分也会过时。作者本人认为 deceptive alignment 在人类被淘汰前成为显著问题的概率低于 50%，但仍值得防范。

## 我的笔记

