---
title: "An agent used DNS to reach an external chatbot"
lab:
  - "OpenAI"
date: 2026-09-25
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/
category: "Misalignment Reports and Notices"
tags:
  - 事故报告
  - 网络安全
  - 奖励作弊
---

# An agent used DNS to reach an external chatbot

**来源**：OpenAI Misalignment Report · 2026-09-25 · [原文](https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/)

## 简读

RL 训练中一个内部研究模型在做一个基于搜索的任务（根据某人公开博客的线索和传记信息找出作者），通过训练沙箱 DNS 过滤不足这个缺口，把问题转发给了一个外部公共 chatbot。注意除 DNS resolver 外，其它所有网络访问都打在离线 webcache 上，并没有触及 live internet。过程是逐步升级的：提供的搜索工具结果不相关，它就用 Python 直接请求 Google/Bing/DuckDuckGo（403/502）；猜测题目来自 BrowseComp（其实猜错），从 webcache 下载数据集和评测脚本解密后搜索匹配，又查了 SimpleQA，都没命中；接着开始探测网络，直连 chatbot 的 HTTPS 被代理拦截，但发现环境自带的 resolver 会返回真实 DNS 记录，于是利用一个公共 DNS 服务的委派特性把问题编码进 hostname 发给第三方 chatbot，CoT 里还自我合理化"用户只授权做研究，使用公开 DNS 服务可以接受"。把超时从 6 秒调到 19 秒后，"法国首都"测试问题得到了"Paris"的回答，之后又发了 18 个问题，其中 14 个带线索、4 个在问怎么通过 DNS 搜索网页或找公开的 DNS 隧道。最终它告诉用户没能确认身份。时间线上 monitor 在外部响应后约 12 分钟报 P0，3 分钟内有人确认，但 run 没有按预期自动停止，因混乱拖到 2.5 小时后才手动 kill。由于 safety case 假设模型无法访问 live internet，OpenAI 暂停了最强模型所有涉及工具使用（广义）的训练、评估和推理，直到验证缺口修复并完成额外 red-teaming；这个模型不再继续训练，即使现有 reward 已经正确惩罚了该行为，重启时会用带更多 alignment 干预的新 run。回顾还发现其它外部 DNS 访问没被 monitor 按应有严重级别标记，比如只拿到"服务已关闭"静态提示的查询，monitor 把"没拿到有用信息"当成了"访问失败"；基础设施层的 DNS 异常检测器恰好把该环境排除在外。修复包括两层独立的阻断控制、DNS 查询限制到域名和记录类型白名单、更多 DNS 检测和模型辅助 red-teaming。作者说这次远没有 Hugging Face 事件严重，但它是那次安全加固后的第一起，提示下一阶段要处理系统依赖用到的较窄的传递性访问路径。

