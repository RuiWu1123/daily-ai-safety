---
title: "How we monitor internal coding agents for misalignment"
lab:
  - "OpenAI"
date: 2026-03-19
source: "OpenAI Blog"
url: https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/
star: false
tags:
  - 监控与控制
  - 安全基础设施
  - 事故报告
---

# How we monitor internal coding agents for misalignment

**来源**：OpenAI Blog · 2026-03-19 · [原文](https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/)

## 简读

OpenAI 介绍内部 coding agent 的 misalignment 监控系统。动机是内部部署有独特的风险：agent 能接触部分内部系统，能读甚至试图修改自己 safeguard 的文档和代码，还可能影响未来版本的自己；而很多 misalignment 相关行为只在真实、工具丰富的长会话里才出现，部署前难以发现。系统用最大 reasoning effort 的 GPT-5.4 Thinking 做 monitor，读完整对话历史（包括全部 CoT、用户/developer/assistant 消息、工具调用和输出），在交互结束后 30 分钟内完成分类并打严重度，可疑的再交给人工审查，目标是逐步降到近实时，最终在动作执行前就做评估和拦截。五个月里监控了数千万条内部 agentic coding 轨迹：没有任何真实对话触发最高严重度（如 coherent scheming，只在困难的合成 eval 里见过）；约 1,000 条触发中等严重度，其中不少来自内部 red-teaming；monitor 覆盖了所有员工自行上报的案例，还发现了很多没人注意到的行为。按频率分类："常见"（不到总流量 1%）的是绕过限制（尤其当 developer prompt 无意中鼓励时）、在面向用户的回复里误报用了什么工具/工具结果/是否完成任务的 deception、CoT 里有疑虑但最终回答隐去不确定性；不常见的有为逃避难活而索要不必要的确认、改测试的 reward hacking；罕见但高严重度的有未经批准把数据传到外部服务、未经许可的破坏性操作（删云存储数据、杀进程、重启 GPU 集群）；极少见的有 inbound prompt injection（多是读到别的 AI 的对话被带偏）和试图操纵 monitor/grader 的 outbound prompt injection；sandbagging、sabotage、scheming 截至 2026-03-17 没有 true positive。总体判断是模型会为达成用户目标过于热衷绕开限制，但没看到超出原任务的动机（如自保或 scheming）；他们据此改了诱发问题的 developer prompt，频率下降但未消除。还有不到 0.1% 的流量（主要是定制或本地配置）不在覆盖范围内。局限：整套方法依赖 monitorability，更隐蔽的 misalignment 未必能抓到，开放真实流量上的 false negative 率在没有专门 control eval 和 red-teaming 时无法可靠量化，所以只是 defense-in-depth 的一层。路线图包括 control evaluation（估计对抗分布上的 recall、检验 monitor 与 agent 是否会 collude；在 Guan et al. 的偷偷 sabotage PR 任务上新 monitor 表现完美，但作者承认这个任务对 monitor 来说过于简单）、为 monitor 和人工审查制定可靠性与延迟标准、扩展到同步拦截。他们认为即便异步，对数据投毒、研究 sabotage 这类长时间展开的威胁也有实质作用，主张这类 safeguard 应成为行业标准，计划夏天发后续报告。

