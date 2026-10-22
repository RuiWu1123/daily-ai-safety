---
title: "Comparing risk from internally-deployed AI to insider and outsider threats from humans"
lab:
  - "Redwood Research"
date: 2025-06-23
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/comparing-risk-from-internally-deployed
star: false
tags:
  - 监控与控制
  - 安全基础设施
  - 威胁建模
---

# Comparing risk from internally-deployed AI to insider and outsider threats from humans

**来源**：Redwood Blog · 2025-06-23 · [原文](https://blog.redwoodresearch.org/p/comparing-risk-from-internally-deployed)

## 简读

一篇短文，借传统计算机安全里的一个区分来看 AI 公司内部部署 AI 的风险。一端是“security from outsiders”：像 Facebook、AWS 对待用户那样，用静态、完全自动化的系统限制权限，保证无论用户输入什么都破坏不了安全不变量（他称之为 manifestly safe），因为用户数量庞大、只需要受限访问；另一端是“security from insiders”：对待自家工程师，需要依靠 multi-party authorization、code review 这类依赖人力的手段，内部人员需要细粒度的广泛访问，但人数少，而且被抓到就会被开除或逮捕，难以反复试探安全措施。两端之间是连续谱（外部防御也靠安全人员调查异常，内部防御也靠构建安全的管理 API）。作者有两点判断：1. AI 公司的安全人员在设想内部部署 AI 工程师和研究员时，往往把 AI 当作 outsider，想着写一小块严格锁死的基础设施让 AI 去交互，但他猜 AI 为了干活需要 insider 级别的广泛访问，攻击面大到无法用静态方法保护（他承认不确定，打算之后详谈），认为安全团队在这方面准备不足；2. 来自 AI 的内部威胁结合了两类问题的难处：既像 insider 一样需要极广泛的细粒度访问，又像 outsider 一样在数量上压倒你，当然防守方也有一些优势，这正是研究 AI control 而不是直接放弃的原因。

