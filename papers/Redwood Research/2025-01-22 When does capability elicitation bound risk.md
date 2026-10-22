---
title: "When does capability elicitation bound risk?"
lab:
  - "Redwood Research"
date: 2025-01-22
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/when-does-capability-elicitation
star: false
tags:
  - 危险能力评估
  - 故意藏拙
  - 威胁建模
---

# When does capability elicitation bound risk?

**来源**：Redwood Blog · 2025-01-22 · [原文](https://blog.redwoodresearch.org/p/when-does-capability-elicitation)

## 简读

Josh Clymer 拆解 capability evaluation 背后的假设：capability eval 的作用是给某个风险指标（比如每月往公司代码里插多少 backdoor）一个上界，流程是定风险指标、构造 proxy task、做 elicitation、再外推。他先把 elicitation 分成两类：human-bounding（红队代替可能滥用模型的人类对手，判断有效性基本是比较人力和技能，只要部署是 stationary 的、模型留在开发者服务器上，就可以随 scaffolding/后训练方法进步定期重测）和 generalization-bounding（防止部署输入"解锁"评估中没表现出的危险能力），后文只讨论后者。论证 elicitation 有效有两条路：一是对 helpful-only 模型做 prompting，论证 harm aversion 这类"不集中"的欠表现会被 helpful-only 训练顺带去掉，而高度定向的 sandbagging 本身不太可能——证据可以是模型想不到 sandbagging 策略、scaling 曲线没有异常、能力剖面不可疑（模型面临两难：只在少数任务上 sandbag 容易被看出来，大面积 sandbag 又容易被训练掉；但像骗过 probe 这类难以预期的能力，sandbag 了也没人知道）；二是做 capability-specific fine-tuning，需要论证训练集上也会出现 sandbagging、且训练会把它去掉。他指出的失败方式大多比 gradient hacking"无聊"：样本有限时 i.i.d. 划分不保证关键任务（如 collusion）落在训练集；训练和测试集常常有意不同分布；多 token 生成的输出本来就 off-distribution，模型能认出被塞进嘴里的不是自己写的文本，所以可以对 SFT 演示配合、到评估时照样 sandbag（对策是不规则地把 AI 生成和人类续写拼接，或关注预测能力与生成能力的差距）；当模型在某些方面超人、或最优策略不像人类（RE-Bench 里 agent 调用评分函数的频率约是人类基线的 8 倍），人类演示和打分都给不出足够的训练信号；SFT 样本效率不够，或者能力（如 recurrent 架构上的长程 in-context learning）根本不是训练出来的，因此也训练不出来；RL 还有 exploration hacking，他建议用 strategy generator 加 execution verifier 的 scaffold 引导探索，表现可疑时让人类补演示，并认为这本质上是个 AI control 问题。经验上可以用 password-locked model 那类 stress test 来验证 elicitation，但局限是人为制造的 sandbagging 机制不自然、模型可能连 stress test 也一起 sandbag、而且无法测到观察不到的能力上限。结论是 capability eval 比看起来复杂，短期内公司做清晰、有依据的简化近似就可以，但这些论证细节会越来越重要。

