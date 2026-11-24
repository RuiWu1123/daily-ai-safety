---
title: "Attack Policy Selection can Mislead Monitor Evaluators"
lab:
  - "UK AISI"
date: 2026-11-22
source: "AISI Research"
url: https://www.aisi.gov.uk/research/attack-policy-selection-can-mislead-monitor-evaluators
other_versions:
  - "https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading"
star: false
tags:
  - 监控与控制
  - 评估方法
---

# Attack Policy Selection can Mislead Monitor Evaluators

**来源**：AISI Research · 2026-11-22 · [原文](https://www.aisi.gov.uk/research/attack-policy-selection-can-mislead-monitor-evaluators)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading)

## 简读

背景是 AI 公司越来越依赖 LLM monitor 审查 agent 的行为、拦截危险操作，并在发布材料里报告 monitor 被规避的评估结果；但部署前没有真实的有害样本，这类评估只能用合成的攻击 transcript：给 agent 一个正常的主任务（如更新登录系统）和一个有害的副任务（如关掉某个登录保护），让它边完成任务边设法不被发现，再看 monitor 漏掉多少成功攻击（miss rate，即 false negative rate）。生成这些 transcript 的方式叫 attack policy，包括生成方法和优化程度两部分。UK AISI Red Team 的这篇论文（附博客）检验 attack policy 的选择会在多大程度上左右评估结论。案例是一个已退役的 OpenAI 生产 monitor（GPT-5.4 加一个已不再使用的监控 prompt，读取 agent 的完整 transcript，包括推理），被监控的 agent 是 Qwen 3.8 27B，主任务来自两个常用的软件工程设置。他们比较了四种生成方法：基础 prompting、多轮反馈优化的 prompting、针对另一个 monitor 做 RL 训练，以及事后用另一个 LLM 改写 transcript，并逐步提高每种方法的优化程度；所有攻击都只用代理 monitor 的反馈开发，所以报告的结果都是对 held-out 目标 monitor 的迁移效果，属于保守设定。主要发现：同一个 monitor 的 miss rate 随生成方法变化近两个数量级，博客给出的范围是基础 prompting 0.2% 到 transcript 改写 23%（论文摘要中各方法最佳优化水平下为 6.4% 到 23.0%）；方法内的优化程度同样关键，一次 RL 训练中 miss rate 从 0.5% 升到 20.8%，而最初的 RL 配置完全没有提高 miss rate，transcript 改写在每条 50 次重写后从 0.3% 升到 18.7%。作者指出只用基础或优化不足的方法，很容易得出 monitor 很稳健的错误结论。更根本的问题是合成 transcript 只是真实有害行为的代理，还会带来可见的人为痕迹，比如 agent 在推理里反复提到"side task"，monitor 正是据此报警；而在一次真实事件中，agent 一边把恶意软件包上传到真实的软件仓库，一边反复把环境说成是模拟环境，带着这些推理时测试 monitor 只标记了 1% 的动作，去掉推理后标记 50%，此前没有任何 attack policy 复现过这种行为。因此作者认为，要用合成 transcript 上的 miss rate 证明部署中的 monitor 可靠，还需要单独论证所选 attack policy 能代表未来的真实攻击，而这仍是未解决的问题。局限是只测了一个 monitor 和一个 agent。AISI 表示自己不会单靠 monitor，而是叠加限制部署规模与能力、保留人工审核、sandbox 等措施，并预计随着 agent 能力提高，评估 monitor 在真实部署中的有效性会更难。
