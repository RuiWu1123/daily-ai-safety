---
title: "A sketch of an AI control safety case"
lab:
  - "Redwood Research"
  - "UK AISI"
date: 2025-01-28
source: "Redwood Research"
url: https://arxiv.org/abs/2501.17315
other_versions:
  - "https://blog.redwoodresearch.org/p/takeaways-from-sketching-a-control"
  - "https://www.aisi.gov.uk/research/a-sketch-of-an-ai-control-safety-case"
star: false
tags:
  - 监控与控制
  - 威胁建模
---

# A sketch of an AI control safety case

**来源**：Redwood Research · 2025-01-28 · [原文](https://arxiv.org/abs/2501.17315)　另见：[Redwood Blog](https://blog.redwoodresearch.org/p/takeaways-from-sketching-a-control)；[AISI Research](https://www.aisi.gov.uk/research/a-sketch-of-an-ai-control-safety-case)

## 简读

Redwood（Josh Clymer、Buck Shlegeris）和 UK AISI（Tomek Korbak、Benjamin Hilton、Geoffrey Irving）合写的论文，想把 AI control 的 safety case 从"蜡笔画"推进到"蓝图"：当 LLM agent 强到 inability 论证撑不住时，开发者需要论证即便模型在 scheming、采取最优攻击策略，也无法绕过控制措施造成不可接受的后果。案例设定是在 AI 公司内部部署一个 ML 工程 agent，一年期，能完成人类 8 小时以内的任务，有终端、浏览器和 Slack/GitHub 等工具并能上网，威胁模型选的是把敏感代码外泄到公网（只是因为简单，不是因为它一定是灾难性的），顶层主张是一年内外泄概率低于 3%。假设的 control protocol 全是黑盒措施：safety layer 用 untrusted monitor 加较弱的 trusted monitor 组成 ensemble 打分，最可疑的 10% 动作交给 trusted model 编辑，最可疑的 0.1% 交给人类审计、发现确凿证据就全线停机；用 trusted summarization 压缩给 untrusted monitor 看的内容，防止 policy 和 monitor 合谋；trusted input filter 拒绝 OOD 输入；每周用合成攻击测 monitor 和人类审计员的可靠性，随机审计 0.1% 轨迹；再加上记忆重置、禁止实例间实时通信、实例间只能通过经代码审查的 PR 交流。核心证据来自五阶段 control evaluation：蓝队定协议，红队列出攻击策略，开发者据此造任务（比如策略是把可疑代码藏进 JSON，就得造含 JSON 的任务），红队在限定算力（如原训练成本的 0.01%）内只改参数、不许用秘密 scaffold，训练 policy 和 monitor 的替身，然后在 2000 个任务的 deployment proxy 里跑（6000 个任务分成 optimisation/validation/test 三份防过拟合），最后用缓存的统计做 macrogame 模拟外推到 10 万个任务，红蓝双方的宏观参数取 Nash 均衡。论证用 CAE 记法分解为三条：蓝队协议是部署中控制效果的下界、红队攻击是模型能力的上界（攻击策略足够全面、elicitation 足够强，能用 sandbagging 评测佐证）、外推保守。外推依赖四个假设：攻击概率恒定、延迟可忽略、部署中攻击不会更容易、任务结果相互独立，每条都要单独论证，比如靠去掉时间戳等协调信号来对抗 Schelling point 式的同步攻击。作者承认最大漏洞是 agent 可能跨任务慢慢积累攻击进度，而 proxy 只能测单任务。Clymer 在配套博文里的体会是：control eval 远比想象复杂，结果高度依赖具体的攻击和控制措施，处处需要判断，而不是一个机械出结论的黑盒；control 现在显得稳健主要是因为模型还是"幼儿级程序员"，到顶尖人类水平时会很不确定；限制通信、把 AI 劳动隔离成"time-bound"是 control 可行的关键。safety case 作为监管机制落地的可能越来越小，但他认为写 safety case 是推进安全评估最有效的方法，每家前沿公司和相关政府机构至少该有一个人认真推演这些细节。

