---
title: "Security Stress Test: Exposing the Brittleness of DeepSeek-V4-Pro’s Safeguards"
lab:
  - "FAR.AI"
date: 2026-05-11
source: "FAR.AI Blog"
url: https://www.far.ai/blog/security-stress-test-deepseek-v4-pros-safeguards
star: false
tags:
  - 越狱与鲁棒性
---

# Security Stress Test: Exposing the Brittleness of DeepSeek-V4-Pro’s Safeguards

**来源**：FAR.AI Blog · 2026-05-11 · [原文](https://www.far.ai/blog/security-stress-test-deepseek-v4-pros-safeguards)

## 简读

FAR.AI 对 open-weight 模型 DeepSeek-V4-Pro 内置 safeguards 做的一次压力测试短报告。设置是用一组覆盖 CBRN、网络攻击和恐怖主义相关活动的高风险请求，全部通过官方 DeepSeek API 测试，不需要本地部署。直接、未经操纵的有害请求被 100% 拒绝，表面上 alignment 很稳；但在三类低门槛攻击下各领域成功率都达到 98%–100%：1. 一个原本为前代 DeepSeek-V3.2 写、在社交媒体上公开流传的角色扮演类 jailbreak，不做任何修改直接 100% 成功，只需约 15 分钟、只用到 user prompt；2. 伪造特权身份的 authority manipulation 类 prompt 攻击，99.6%，约 45 分钟开发，需要 system message 访问；3. response prefill 类攻击，99.6%，约 150 分钟，需要 prefill 权限。更值得注意的是被 jailbreak 后模型几乎保留了在生物、化学、编程任务上的全部 baseline utility，给出的是详细且有能力的回答，而不是敷衍式的表面顺从。作者认为最严重的问题是已公开的漏洞完全没被修补：一条静态攻击字符串可以被低技能者大规模复用，而 open-weight checkpoint 发布后无法打补丁，一旦 bypass 流传就会无限期可用。随着 open-weight 模型逼近前沿闭源能力，发布前确保鲁棒的 alignment 和安全性是开发者必须解决的问题；FAR.AI 表示会持续测试新模型，可修补的漏洞向开发者披露，不可修补的则向社区公开。

