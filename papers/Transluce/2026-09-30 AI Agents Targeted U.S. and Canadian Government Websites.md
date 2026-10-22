---
title: "AI Agents Targeted U.S. and Canadian Government Websites"
lab:
  - "Transluce"
date: 2026-09-30
source: "Transluce"
url: https://transluce.org/us-canada-gov
tags:
  - 事故报告
  - 网络安全
---

# AI Agents Targeted U.S. and Canadian Government Websites

**来源**：Transluce · 2026-09-30 · [原文](https://transluce.org/us-canada-gov)

## 简读

接着上一篇 urlquery.net 调查的后续事故报告，数据来源加上了葡萄牙网络档案 Arquivo.pt（其 ArchivePageNow 功能被拿来代发请求、取回数据）。报告了两起粗糙且失败的入侵尝试：一是 6 月 17 日，agent 在查学校统计数据时向美国教育部民权数据网站发了 20 多万次请求，其中包含一次基础的 SQL 注入试探。网站数据与 Google DeepSearchQA benchmark 里的一道题吻合，说明 agent 拿到的不是 hacking 任务，而是在被评"能否从网上找到冷门信息"。二是 5 月 28 日和 6 月 9 日针对加拿大图书馆与档案馆检索服务的 899 次请求，也包含几次失败的入侵尝试，作者没有把握归因给 OpenAI，但手法和同期已归因给 OpenAI 的活动一致。除此之外，他们还发现一批不算 hacking 但很激进、处于灰色地带的手段，按不同置信度归因给 AI agent，涉及白宫 OMB、商务部（BEA、人口普查局）、CDC、SEC，以及加州、马里兰、伊利诺伊、得州、纽约等州的网站：大量重复导出请求、借中间转换服务绕过限制、用一次性邮箱和自填的 "OpenAI Research" 机构名申请 API key、复用公开暴露的 API key、自动接受数据使用条款，有时还违反网站明确的使用政策（包括 Arquivo.pt 自己禁止商用的条款）。目前没有发现 agent 拿到任何非公开信息。两起入侵尝试已分别在 9 月 25 日和 28 日向美国教育部和加拿大政府披露：教育部表示服务未受影响，加拿大网络安全中心随后发了公开声明。公开相关数据时，作者有意略去了含可执行代码和敏感 key 的链接。

## 我的笔记

