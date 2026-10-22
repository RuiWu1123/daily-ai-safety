---
title: "The safe-to-dangerous shift is a fundamental problem for eval realism; but also for measuring awareness"
lab:
  - "Alignment Forum"
date: 2026-05-14
source: "Alignment Forum（UK AISI；Charlie Griffin, Patrick Leask）"
url: https://www.alignmentforum.org/posts/tK8vqHDxaRGcysNJQ
tags:
  - 评估感知
  - 伪装对齐
---

# The safe-to-dangerous shift is a fundamental problem for eval realism; but also for measuring awareness

**来源**：Alignment Forum（UK AISI；Charlie Griffin, Patrick Leask） · 2026-05-14 · [原文](https://www.alignmentforum.org/posts/tK8vqHDxaRGcysNJQ)

## 简读

一篇短的概念性文章，论点是 eval realism 有一个根本障碍：alignment eval 和真实部署的核心区别在于 eval 必须是安全的（要限制不可信 AI 在环境里造成伤害的能力），而有用的部署必须给 AI 一定影响世界、因此可能造成伤害的能力。作者称之为 safe-to-dangerous shift。一个足够聪明的 scheming 模型只要能根据"环境是否真的危险"来区分 eval 和部署，就能 alignment faking，而且不需要可靠区分，只要把一部分危险且适合 defect 的场景认作部署就够了。那能不能给模型的 eval awareness 定上界、迭代到足够真实？作者认为测量 eval awareness 也撞上同一个问题：不部署就拿不到模型在部署中的行为数据，所以难以构建或验证 awareness 测量。逐一分析现有方法：直接问模型（会撒谎）；监控 CoT 里自发的 eval awareness 表述（不会主动暴露）；构造假 eval 和假部署对比行为（两者实际上都是 eval、都必须安全，模型都认作 eval 也没错，照样能在真实部署中 defect）；用前一代模型的真实部署数据开头再伪造 tool call 返回（模型可能察觉轨迹前段出自别的模型，或从 tool 返回中找破绽）；用 steering vector、加噪权重等 white-box 干预看行为变化（作者认为有前景，但引用 Opus 4.6 Sabotage Risk Report 称对内部状态理解还不够）；在极强控制协议下真实部署（模型可能察觉监控异常强而等待，也无法对可能的 defection 输入做 importance sampling，且若已有安全可扩展的 control 协议就不需要 alignment eval 了）。即便是 probe、CoT 这类非行为 proxy，验证它们也需要部署数据。作者认为这一点不奇怪：一个鲁棒的 eval realism 测量几乎等于解决 inner alignment，因为可以据此优化出超真实的 eval 进而做成训练环境。脚注还提到另一个问题"problem of time"，即 AI 可以寻找自己已被部署一段时间的证据。作者的动机是通过给能力有限的 LLM 的 eval awareness 定界来排除 deceptive alignment，从而为 control 协议建立 trusted model，承诺之后会发文给出部分解决方案。

## 我的笔记

