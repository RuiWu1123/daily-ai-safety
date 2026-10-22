---
title: "Access to powerful AI might make computer security radically easier"
lab:
  - "Redwood Research"
date: 2024-06-10
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/access-to-powerful-ai-might-make
tags:
  - 安全基础设施
  - 监控与控制
---

# Access to powerful AI might make computer security radically easier

**来源**：Redwood Blog · 2024-06-10 · [原文](https://blog.redwoodresearch.org/p/access-to-powerful-ai-might-make)

## 简读

Buck Shlegeris 认为，关于 AGI 前后权重安全极难的讨论（RAND 报告、Leopold 等）忽略了一点：按定义那时我们手上已经有强 AI，而这可能让计算机安全容易得多。他说的不是常见的"AI 帮忙加固软件、自动化安全研究"，而是 AI 让一些单靠人力太费力、或者会陷入"谁来监督监督者"问题的组织安全政策变得负担得起。文章聚焦内部威胁（外部攻击大多也要先冒充内部人员），思路来自"把 AI control 技术反过来用在人身上"，并假设所用 AI 是可信的、不会故意破坏这些措施。四种策略：1. monitoring，员工每条 bash 命令连同上下文先给 AI 判断可疑程度，很可疑就拦截并通知他人，有些可疑就标记待查，相当于覆盖全部操作、误报漏报更少的 multi-party authorization；2. trust displacement，凡是人做起来需要危险权限的任务改由 AI 来做，收回人的权限，比如员工不能直接写系统管理命令，只能用英文向 sysadmin AI 提需求，这比监控更难被精心构造的命令绕过；3. 细粒度权限管理，SELinux 这类工具因为配置太繁琐，军方以外几乎没人用，而反复写权限、试跑、排查缺了什么正是 AI 擅长做的；4. 自动检测到可疑活动后让 AI 去调查，缓解人力不够、读不完相关代码的瓶颈。关于 jailbreak：理想情况是做出不可 jailbreak 的模型，退一步可以用检测"当前是否被 jailbreak"的分类器；即使红队能 jailbreak，内部攻击者也很难反复迭代，第一次尝试就被抓并开除即可；schemer 处境比间谍更难，因为它们时刻被监控，可能接触不到最新的 jailbreak 技术；有些用法（比如调查网络访问异常）根本不需要给模型看攻击者自由选择的文本，可以做 redaction。作者坦言对整体效果很不确定，但内部看法是：拥有深刻理解网络和实验室内部情况的强 AI，应该能大幅降低内部人员外泄大量数据的风险，也能大幅降低 rogue deployment 风险；实验室目前没打算这么做，但等强 AI 出现后可能很快实施，且是定向施压能推动的事。开放问题是：如果现有模型就是我们能拥有的最可信模型，这些方法是否已经可行——作者认为这是很好的研究题目，甚至可能做成一家赚钱的创业公司。

## 我的笔记

