---
title: "Why imperfect adversarial robustness doesn't doom AI control"
lab:
  - "Redwood Research"
date: 2024-11-18
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/why-imperfect-adversarial-robustness
star: false
tags:
  - 监控与控制
  - 越狱与鲁棒性
---

# Why imperfect adversarial robustness doesn't doom AI control

**来源**：Redwood Blog · 2024-11-18 · [原文](https://blog.redwoodresearch.org/p/why-imperfect-adversarial-robustness)

## 简读

回应一种对 AI control 的反对意见：control 依赖 trusted model 的判断，而模型不 adversarially robust，所以注定失败。作者同意更好的鲁棒性当然有帮助，但认为现有鲁棒性水平远不至于让 control 失效。最重要的一点是，adversarial robustness 研究通常设定对攻击者非常宽松：只要多次尝试中有一次成功就算失败；而在真实 control 设定里，失败的 jailbreak 尝试可能直接被抓，代价很大。而且 AI 甚至拿不到自己的尝试是否成功、尝试过什么的直接反馈。以 defer-to-trusted 为例（trusted model 打分，最可疑的 1% 送人工 audit，最可疑的 10% 换成 trusted model 生成的动作），附录详细说明：动作被替换后，untrusted model 是无状态的，只能在历史里看到替换后的命令，知道"刚才那招没成"，却不记得刚才到底试了什么，有点像反向的时间循环套路，操纵者没有之前尝试的记忆；动作被 audit 后放行时，它也分不清是没被标记、被标记后审查通过，还是被替换成了相同命令，所以学不到什么会触发审查。即便它从中推断出 trusted model 的特性，也得靠隐写传给其它实例。不过作者也指出，在这个设置里模型能知道自己是被 audit 还是被替换，这可能是不好的设计；如果 untrusted model 能发起 rogue internal deployment、自由迭代 jailbreak，情况就糟得多。其它有利因素：聊天机器人的 jailbreak 多半利用它们被训练成什么请求都尽量满足（角色扮演、讲故事），而 monitor 可以训练得完全不配合，只按预设问题分析代码，攻击面小得多；多道防线下，如果需要突破三个不变量，灾难概率大约是单次攻击成功率的立方；有些安全措施根本不需要 trusted model 直接看 untrusted 输出，比如事故调查、自动检查代码申请的权限是否与任务匹配、审阅最小化后的代码。附录（Fabien Roger 贡献）列了不鲁棒的其它坏处：untrusted monitor 漏报精心构造的 backdoor 时，难以区分是恶意还是不鲁棒，因此难以设定 red-team 的约束；模型产出很像 scheming 的推理时，也更难据此断定它是恶意的。作者希望有论文让 red team 使用 jailbreak 和白盒对抗攻击，blue team 用上述策略应对，此前的 control 工作还没真正研究过这类攻击。

