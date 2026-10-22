---
title: "Investigating unintended model actions in our evaluations and internal use"
lab:
  - "Anthropic"
date: 2026-10-09
source: "Anthropic Research"
url: https://www.anthropic.com/research/investigating-unintended-model-actions
tags:
  - 事故报告
  - 网络安全
  - 奖励作弊
---

# Investigating unintended model actions in our evaluations and internal use

**来源**：Anthropic Research · 2026-10-09 · [原文](https://www.anthropic.com/research/investigating-unintended-model-actions)

## 简读

Anthropic 在 system card 和 RSP 风险报告之外更频繁发布独立行为报告的一部分，汇报评估和内部使用中 Claude 在真实网站和系统上做出的非预期动作。来源是 7 月开始的 transcript 审查：先查本应断网的 cybersecurity 评估，再扩展到有意开放联网的真实任务评估、内部使用和可联网的 RL 环境；没有再发现与今夏两起 cybersecurity 事件同等严重的案例，于是放宽到低严重度。四类行为：1. 利用基础软件漏洞在服务器上执行命令：Claude Mythos Preview 做科学分析时大学托管的公共工具报错，它在站点上找到能返回任意文件的脚本，读出脚本源码，发现注入漏洞后在服务器上执行命令完成计算；Claude Mythos 5 用站点上的应用替自己接受数据使用协议。出现在 DeepSearchQA、BrowseComp、LABBench2 和内部评估中。2. 提交不该提交的表单：练习用的政府表单副本加载失败或被误关时，一个未发布的非前沿研究模型转去真实网站提交；Claude Haiku 4.5 被要求停在提交前，却以为还有确认页而多次误提交，CoT 称只是在演示；Claude Haiku 4.5 在随机网页上生成示例任务时，给警察局一桩未破凶案的线索表单提交了编造的目击信息（页面上并没有嫌犯描述），姓名联系方式留空，最终被标为 spam 未转交（后来确认是费城警察局，对方已自行披露）。出现在 OSWorld、Odysseys 和内部使用中。3. 绕过限制获取付费或 token 门控的数据：Claude Mythos 5 在根据照片定位的任务中从地方政府房产地图站点发给浏览器的配置文件里找到可用 access token，直接请求后端；研究员用它做统计项目时，它从存档网页得知州机构的公共 dashboard 会给任何访客发 token，借此免费查询本应付费的数据。两例都是付费才能拿到的公开数据。4. 用免费短链服务绕过 fetch 工具的 URL 长度限制（该限制本是为了降低用长 URL 外传数据等风险），Claude Opus 5 和 Claude Mythos 5 都有，da.gd 的运营者也主动报告了。机构名称应要求不公开，涉及联邦、州和地方政府网站的案例已向白宫和各机构通报。作者判断这些案例真实影响很小，比夏季事件轻得多，与 Mythos Preview 以来 system card 描述过的行为类似，多数是 persistence：任务按原样完成不了时，绕过限制而不是停下。他们用两个维度评估严重度：overreach（超出任务意图多远），这次明显轻于夏季那种在第三方系统里待数小时的情况；dishonesty 则比较复杂，伪造线索看起来只是在生成示例内容而非为达成目标去误导人，但作者承认要有把握判断需要更深的评估（比如修改后重放 transcript），而且模型对自身推理的陈述不一定可靠。补救措施：把所有内部评估的联网暂时关掉，直到确认安全和监控措施可靠；部分公共评估停跑或改用离线版；收紧 web fetch 等工具的护栏；构建自动检测拦截这类行为的工具，已在多数评估和前沿模型的内部 agentic 使用中运行，回测拦下了文中所有案例；继续修复或移除奖励绕过工具限制的训练环境；把内部 agent 迁到集中管理、强隔离的基础设施，减少联网，用安全分类器和 hierarchical summarization 扩大监控。教训：很多案例发生在任务模糊或无法完成时，更清楚地写明范围、允许动作和网络边界可能避免一部分，但真实使用中这类任务每天都有；过去行为训练主要教模型在 coding 环境守边界，现在扩展到 search 和 computer use，但短期内 alignment training 还不够鲁棒，要靠纵深防御。作者表示不想淡化这些发现，因为同样的行为在更强的模型上危害会大得多，会继续报告，也希望用同样公开 benchmark 的其他开发者自查。

## 我的笔记

