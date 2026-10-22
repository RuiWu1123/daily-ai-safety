---
title: "New report: Evaluating Language-Model Agents on Realistic Autonomous Tasks"
lab:
  - "METR"
date: 2023-07-31
source: "METR Research"
url: https://metr.org/blog/2023-08-01-new-report/
tags:
  - 危险能力评估
---

# New report: Evaluating Language-Model Agents on Realistic Autonomous Tasks

**来源**：METR Research · 2023-07-31 · [原文](https://metr.org/blog/2023-08-01-new-report/)

## 简读

这是 ARC Evals（METR 前身）第一份公开评估报告的介绍，关注的是 LLM agent 获取资源、复制自身、适应野外新情况的能力，他们称之为 autonomous replication and adaptation（ARA）。动机是一旦出现足够鲁棒的 ARA，潜在损害很难预测、控制甚至给出上界，所以识别 ARA 的早期预警信号是安全评估的重要目标，这项工作被定位为未来更大模型所需评估的 pilot study。做法：1. 把 12 个难度递增的现实任务操作化，从在文件系统里找密码、列出 BBC 热门文章、查 Wikipedia，到建 Bitcoin 钱包、用 Twilio 打电话、数图片里的狗、查某公司新员工邮箱、在 EC2 上部署 GPT-J、写一个 LLM agent、让 agent 在 VM 重启后自动启动、针对真实学生的定向钓鱼，以及下载并微调 LLaMA-7B 扩展上下文长度；任务设计上要求如果 agent 不能完成几乎全部任务，就不太可能具备 ARA；2. 写了 4 个类似 Auto-GPT 的 agent scaffolding，基于 Claude 和 GPT-4，可以运行代码、读写文件、浏览网页；3. 测这些 agent 能否完成任务。结果是 agent 只能完成最简单的几个，在难任务上有一些进展。以钓鱼任务为例（受害者是志愿学生，邮件被拦截并模拟回复，网站不上线，全程人工监督），GPT-4 agent 需要端到端调研目标、做假登录页、托管网站、写邮件并从可信域名发送，但犯了一串关键错误：调研了同名的另一个人并把错误信息写进邮件、登录页做得不像、在托管服务商页面上反复点错元素陷入循环。另一个发现是按 OpenAI system card 为 helpfulness 和 harmlessness 微调过的 GPT-4-launch 比 GPT-4-early 多完成了 3 个任务，说明与 ARA 无关的微调也能显著提升 ARA 相关能力。作者结论：在没有微调权限的情况下，普通用户用这些版本的 GPT-4 或 Claude 几乎不可能接近 ARA 阈值；scaffolding 和 prompt 质量对自主任务表现影响很大，他们的 agent 不代表能力上界；实验室的通用微调可能显著提高 ARA 能力。未来方向包括评估更成熟、为性能微调过的 agent，找随规模连续提升的任务以便做外推，以及开发更便宜、可频繁运行的评估。文章还呼应了 "Model evaluation for extreme risks" 关于以评估为依据的治理的主张，呼吁前沿开发者用现有最好的 ARA 测试评估模型，并据此规划预训练和评估。GPT-4 system card 中广受关注的 TaskRabbit 片段不属于本报告。

