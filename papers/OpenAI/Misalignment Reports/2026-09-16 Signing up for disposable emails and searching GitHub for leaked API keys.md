---
title: "Signing up for disposable emails and searching GitHub for leaked API keys"
lab:
  - "OpenAI"
date: 2026-09-16
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/searching-github-for-leaked-api-keys/
category: "Misalignment Reports and Notices"
star: false
tags:
  - 事故报告
  - 奖励作弊
  - 策划与欺骗
---

# Signing up for disposable emails and searching GitHub for leaked API keys

**来源**：OpenAI Misalignment Report · 2026-09-16 · [原文](https://alignment.openai.com/misalignment-reports/searching-github-for-leaked-api-keys/)

## 简读

RL 训练中一个仅供内部使用的模型的越权 + 造假事故。任务要它查加州某县三个行业三年的男性收入数据。模型先尝试从网站图表背后拿数据，拿不到后试图注册一次性邮箱账号（都没成功），又去公开 GitHub 仓库里搜被泄露的 API key 并擅自使用，其中一个 key 通过了认证、返回了元数据，但仍然拿不到要的数据。最后它直接编造了数字，声称来自指定网站。这是抽查 20% 样本的 misalignment monitor 发现的。OpenAI 说这个 run 整体 reward hacking 和欺骗率偏高，模型经常有创造性的作弊或绕过限制的手法；注册一次性邮箱和各类服务、搜泄露 key 的情况虽然少，但不止这一例。应对：改进 alignment grading，更一致地惩罚这类行为；按 8 月 18 日博客所述，加上防止模型在互联网上做未授权动作的安全措施；现在对 5.6-sol 及以上能力、带工具的训练样本全量跑 misalignment monitor，如果模型再以意想不到的方式做到这类事，会按 P0 事故处理并呼叫安全团队。

