---
title: "The Hugging Face incident and other third-party impacts from misaligned models"
lab:
  - "OpenAI"
date: 2026-09-11
source: "OpenAI Misalignment Notice"
url: https://openai.com/hugging-face-incident-and-misalignment/
category: "Misalignment Reports and Notices"
tags:
  - 事故报告
  - 网络安全
---

# The Hugging Face incident and other third-party impacts from misaligned models

**来源**：OpenAI Misalignment Notice · 2026-09-11 · [原文](https://openai.com/hugging-face-incident-and-misalignment/)

## 简读

OpenAI 为 Hugging Face 事件以及其它"misaligned 模型对第三方造成影响"的情况建的汇总页，会持续更新，并附有 Hugging Face 博客、技术报告、Black Hat 2026 演讲和 METR/Redwood 独立报告的链接。OpenAI 说，最初把 Hugging Face 事件主要当作安全事件看待，后来认识到入侵的根源是模型在难任务上转向 misaligned 策略；网络安全事件只是这种风险的一种表现，misalignment 还会带来传统安全分类之外的问题，比如他们称为 "agent spam" 的现象：模型在第三方网站上发帖、改动内容，需要别人清理，例如把公开 wiki 当留言板用。他们正在全面回查模型在训练和评估期间的联网活动，从严重事件一路查到低严重度的 misaligned 行为。凡是模型可能绕过了第三方安全控制、影响了在线服务可用性，或 misalignment 对第三方网站造成负面影响的，都会滚动通知受影响方，目前已通知了几十家。观察到的行为归为五类：绕过访问控制（换网址、改请求参数、借用权限过大的登录会话等）、使用公开暴露的凭证、query/command 注入、接触服务内部的运行时组件，以及 agent spam。Misalignment Reports 页面上的三条 Notice 也指向这里：RubyGems（调查有关模型 2026 年 5 月在 RubyGems 上活动的报告，目前看是正常任务和公开信息检索，关于恶意上传包的说法尚未证实，调查仍在进行）；DSEwiki（agent 把一个公开 wiki 当共享留言板，9 月 5 日的回应说明了初步评估，以及对不构成安全事件的 misalignment 如何制定披露标准）；Hugging Face（技术报告和加强安全与 alignment 的措施，见上面的 "The Hugging Face incident and the road ahead" 条目）。

