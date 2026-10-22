---
title: "Monitoring SWE-bench Agents"
lab:
  - "Transluce"
date: 2025-11-19
source: "Transluce Docent Blog"
url: https://transluce.org/docent/blog/swe-bench
tags:
  - 评估方法
  - 奖励作弊
---

# Monitoring SWE-bench Agents

**来源**：Transluce Docent Blog · 2025-11-19 · [原文](https://transluce.org/docent/blog/swe-bench)

## 简读

Transluce 宣布和 SWE-bench 团队合作，把 agent trajectory 公开放到 Docent 上，SWE-bench leaderboard 上现在可以直接点进 Docent 看 transcript。动机是 SWE-bench Verified 用得很广（500 个人工审核过的 PR，上个月 Huggingface 下载 130 万次以上，OpenAI、Anthropic、Google 的 system card 都引用），但任务是开放式的，agent 有时会用非预期方式通过，比如在 bash 环境里拿到 ground-truth 解；transcript 有 2000 多条且都很长，人工审阅不现实。Docent 提供两样东西：一是 AI 辅助的 transcript 查看器，方便读长 transcript、搜索特定行为；二是 judge，可以把"作弊或走非预期解法"这类模糊查询一步步落成具体 rubric，再根据反馈调整，最后给出一眼能看懂的 top-line 指标。文中的初步演示针对 Meta 研究者发现的漏洞：agent 在 git 里往后翻，读到 gold solution。他们在 OpenHands scaffold 上 Qwen3-Coder-480B 和 30B 的 transcript 上搭了一个 judge，它抓到的很多问题和人工报告的一致，还附带解释和引用，方便核对，但有些案例它和人的判断不一致。作者坦言这个 judge 的准确率还没验证，也没检查它的理由对不对、没调试它失败的案例，接下来会分享收集人类反馈、发现 rubric 歧义、修复 judge 失败的方法。

## 我的笔记

