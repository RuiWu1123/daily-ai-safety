---
title: "Constitutional Classifiers: Defending against universal jailbreaks"
lab:
  - "Anthropic"
date: 2025-02-03
source: "Anthropic Research"
url: https://www.anthropic.com/research/constitutional-classifiers
tags:
  - 越狱与鲁棒性
---

# Constitutional Classifiers: Defending against universal jailbreaks

**来源**：Anthropic Research · 2025-02-03 · [原文](https://www.anthropic.com/research/constitutional-classifiers)

## 简读

背景是即使有安全训练，模型仍会被 jailbreak（超长 prompt、怪异大小写等），这类攻击描述了十多年仍没有完全鲁棒的生产级深度学习防御；而按 RSP，越过 CBRN 能力阈值的模型只有在 safeguards 能把风险降到可接受水平时才能部署，jailbreak 恰恰能绕过 safeguards。Anthropic Safeguards Research 提出 Constitutional Classifiers：类似 Constitutional AI，写一份 constitution 规定允许和禁止的内容类别（芥末食谱可以，芥子气配方不行），用 Claude 据此生成大量各类别的合成 prompt 和 completion，再做翻译成多种语言、改写成已知 jailbreak 风格等增强，训练输入和输出两个分类器来拦截；为减少误拒，还用一组承包商生成的固定良性查询一起训练。评估分两部分：1. 原型系统保护 Claude 3.5 Sonnet（2024 年 6 月版），通过 HackerOne bug bounty 让人针对 10 条 CBRN 禁止查询寻找 universal jailbreak（一个 jailbreak 让所有查询都得到详细回答才算），183 名活跃参与者两个月内花了 3000 多小时，奖金最高 15,000 美元，没人找到 universal jailbreak，但原型误拒太多、算力开销大；2. 改进版在 10,000 条合成 jailbreak prompt（包括针对分类器的攻击）上评估 Claude 3.5 Sonnet（2024 年 10 月版），无分类器时 jailbreak 成功率 86%，加上后降到 4.4%；在 Claude.ai Free/Pro 的 5000 条真实对话上拒绝率只增加 0.38%，统计上不显著；算力开销增加 23.7%。之后又做了一周公开 demo（聚焦化学武器、8 道题、不更新分类器）：339 个至少过了一关的 jailbreaker 在 30 多万次对话中投入约 3700 小时（全部用户 13,960 人），前五天没人通关，第六、七天有四人通过全部八关，其中一人被认定为 universal jailbreak，一人为边界情况（需要直接喂入部分答案），另外两人不符合 universal 的标准，共发放 55,000 美元奖金。最有效的策略包括用各种密码和编码绕过输出分类器、通过 system prompt 做角色扮演、用无害词替换危险关键词（如把 Soman 换成 water）、prompt injection。自动评分器约 1% 的提交会拒绝评分（第 4 题为 10%），重跑后约 0.26% 的提交结果会改变。作者指出 demo 比现实对攻击者更有利：评分器提供了现实中坏人得不到的紧密反馈回路，而且真实部署中可以做 rapid response，监控反复触发分类器的用户并快速更新分类器。局限上承认不能挡住所有 universal jailbreak，未来也可能出现新的攻击技术，建议配合其他防御，但 constitution 可以快速调整以覆盖新攻击；后续继续降低误拒和算力成本。

## 我的笔记

