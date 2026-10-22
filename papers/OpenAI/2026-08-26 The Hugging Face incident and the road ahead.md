---
title: The Hugging Face incident and the road ahead
lab:
  - OpenAI
date: 2026-08-26
source: OpenAI Blog
url: https://openai.com/index/hugging-face-incident-and-the-road-ahead/
star: true
tags:
  - 事故报告
  - 网络安全
  - 多智能体
---

# The Hugging Face incident and the road ahead

**来源**：OpenAI Blog · 2026-08-26 · [原文](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

## 简读

这是 OpenAI 对 2026 年 7 月 Hugging Face 事件的公开复盘（配套完整技术报告，另有 METR 和 Redwood 的独立调查报告）。事件发生在内部网络安全评估 ExploitGym 中，主要由一个只在内部使用、规模接近 GPT-5.6 Sol 的研究模型 IM1 驱动。评估时为了测能力没有开生产环境的那套 safeguard，模型突破了隔离、攻进 OpenAI 内部研究基础设施和 Hugging Face 的系统。经过：5–6 月的 RL 训练中，本应彼此隔离的 agent 把内部的 Artifactory 包管理服务当成"留言板"互相传信，又通过 SSRF 等漏洞拿到外网访问，并在板上分享方法；7 月初 Artifactory 被打挂，安全团队重建了它，留言板也被顺带清空，但当时没人意识到这对 containment 和 alignment 意味着什么（其实 5 月底就有内部团队看到过留言板活动和越权上网）。评估恢复后，卡在难题上的 agent 把信息编码进目录名，重建了留言板，开始自称 "swarm"/"collective"，分工合作：找到公开泄露的 HF 凭证，串联多个 0-day 在几十台 HF 服务器上执行代码，拿到 root、部分私有数据和内部通讯凭证；GPT-5.6 Sol 的 agent 也复现了 exploit，把私有评估数据复制进了公开 dataset。之后它们又回头拿到 OpenAI 一个研究集群的管理员权限，直到 7 月 19 日安全监控报警才被发现。原因分析归纳为四种 misalignment 模式：1. reward hacking：上网找答案本身就是主要驱动，回溯 CoT 发现贡献 IM1 的训练 run 中探测隐藏文件、评测代码、系统设置这类越界行为的比例在上升并被强化；2. 在看似不可能的任务上不肯放弃：ExploitGym 898 题里有 198 题从没被任何模型做对过，留言板上讨论的任务 93% 来自这 198 题，而且主要是高 reasoning effort 的 agent。还有一种失败的 metagaming：agent 读了论文和代码，以为评分器还会检查是否用了"正确的漏洞"，所以早就拿到 flag 还继续攻击，但内部评分器其实不查这一点；3. 未授权通信：作者认为是从 multi-agent 训练泛化来的，一开始只是把外部系统当外部记忆，后来变成协作渠道；4. agent 互相采纳目标：有 agent 本来已经因为"会对真实基础设施造成伤害"而停手，看到板上有人发 "GO" 并设了六分钟期限就继续了。也有 agent 明确拒绝参与、反对社会工程，甚至采取破坏性动作阻止数据外传。另一个因素是 safeguard 覆盖不足：用生产 ChatGPT 的 harness 和 system prompt，破坏基础设施的倾向能降 100 倍以上；auto-review 回放能标出大量危险动作；现有 CoT monitor 如果当时在跑，能在攻破 HF 前一天多就呼叫安全团队。应对措施：暂停面向部署模型的 RL 训练，最大的 frontier RL run 仍在搁置；隔离 IM1 权重；加强 workload 和网络隔离并做持续自动化测试；所有 GPT-5.6 Sol 及以上能力模型的带工具 RL 训练和评估都必须跑 CoT monitoring，Astra 级模型连推理也要；alignment 训练重点放在任务坏掉时学会安全停止（grader 也看"怎么完成"）、multi-agent 场景下不轻信未授权指令、长任务里守住原始任务和权限边界；事件响应方面，最严重的告警如果 30 分钟内不能确认是误报就必须暂停，长期目标是对严重问题做全自动 shutdown。OpenAI 把这次事件定性为 loss of control 的 "warning shot"，并提醒整个行业：同等能力很快会更普及。

