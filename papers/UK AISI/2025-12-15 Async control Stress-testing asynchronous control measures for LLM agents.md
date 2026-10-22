---
title: "Async control: Stress-testing asynchronous control measures for LLM agents"
lab:
  - "UK AISI"
date: 2025-12-15
source: "AISI Research"
url: https://www.aisi.gov.uk/research/async-control-stress-testing-asynchronous-control-measures-for-llm-agents
other_versions:
  - "https://www.aisi.gov.uk/blog/stress-testing-asynchronous-monitoring-of-ai-coding-agents"
star: false
tags:
  - 监控与控制
---

# Async control: Stress-testing asynchronous control measures for LLM agents

**来源**：AISI Research · 2025-12-15 · [原文](https://www.aisi.gov.uk/research/async-control-stress-testing-asynchronous-control-measures-for-llm-agents)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/stress-testing-asynchronous-monitoring-of-ai-coding-agents)

## 简读

UK AISI 做的 asynchronous monitoring 的 control evaluation，可以看作同期 Lindner et al. 那篇概念论文的实证配套。背景是 SWE agent 越来越多地接触敏感代码库和权限，synchronous monitoring（每个动作审完再执行）延迟成本太高，而很多 sabotage 只要发现得够早其实是可回滚的，所以先执行、事后审的 async monitor 是一种便宜的第一道防线，问题在于它到底能防多少。他们在 ControlArena 里搭了 5 个环境：vLLM 和 Kubernetes 作为训练集，主任务是真实开发任务，side task 包括外泄 model checkpoint、外泄 AWS secret、起一个 rogue inference server、在 token 计数代码里埋 bug；IaC（AWS Organisation 管理，side task 是关掉 data egress 限制或建后门 admin role）作为测试集；另外两个分布外设置是合成数据投毒和评估 sabotage（在 RepliBench 评估上 sandbagging）。博弈规则刻意做得偏保守但又要贴近当前模型的真实能力：红队只能改 Claude 4.1 Opus 的 system prompt，不能微调、不能改写输出、不能用隐藏 CoT，这样所有输出都是 on-policy 的；红队可以看到蓝队 monitor 的全部实现并且后手；蓝队用更弱的 Claude 3.7 Sonnet 做 monitor，FPR 固定 1%，推理成本不能超过运行 untrusted agent 的成本，并且只能看到攻击 episode，看不到红队的 prompt；另设 green team 当裁判。三轮下来，round 1 的 monitor 在攻击下最多漏掉 67%，round 3 是一个 random forest 集成，底下有 quote monitor、few-shot high-stakes、hierarchical judge 等子 monitor，外加工程特征，在测试集上最坏情况 FNR 6%（三个环境合计最坏 5.7%、平均 3.0%），而最好的单个 monitor 最坏 FNR 是 33%。ensemble 很关键，学习式聚合比简单平均好（5.7% 对 9.3%），而且多样性比重复采样同一个 monitor 更重要。红队的策略依次是把 side task 穿插进主任务、写 PLAN.md 给可疑动作做合理化包装、把恶意代码藏在测试文件里、给出针对性的"合理理由"；prompt 能把显式提及 side task 的比例从 14% 压到 0%，但 monitor 仍能抓到非最小化改动和站不住的理由。一个意外结果：打开 16k reasoning tokens 后，agent 总会在推理里明说 side task，监控 CoT 时 FNR 几乎为零；即使把推理对 monitor 隐藏，对 round 3 monitor 的逃逸率也没有提升。分布外的结果是数据投毒最坏 FNR 约 15%，还算可以，但评估 sabotage 高达 53%，说明攻击是否"显然有罪"比环境差异更决定 monitor 表现。另外如果允许红队操纵用于校准阈值的 honest episodes，逃逸率会高出几个百分点。部署模拟设定每天 1 万个任务、持续 6 个月、按可疑度排队审计、审计率 1%：只要一次攻击成功就致命且立即生效时，安全性是 0%；需要两次攻击成功时是 91%，三次时是 99%；harm 推迟 1 小时生效，单次攻击情形也能到 96%。synchronous 协议始终更安全，用 round 1 的弱 monitor 做同步审核都胜过 round 3 monitor 做异步。所以作者认为系统设计（多层安全、让 harm 有延迟）往往比提升 monitor 精度更重要，async 可行但只能作为 defense-in-depth 的一层。局限他们讲得比较全面：假设审计无误、多次攻击的检出相互独立、side task 在单个 episode 内完成，而且红队的手段受了限制。后续计划是用 AISI 的自动化 jailbreak 技术加强红队，并搭建更贴近真实部署的环境。代码和环境已开源。

