---
title: "Auditing games for sandbagging detection"
lab:
  - "UK AISI"
date: 2025-12-09
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/auditing-games-for-sandbagging-detection
star: false
tags:
  - 故意藏拙
  - 对齐审计
  - 可解释性
---

# Auditing games for sandbagging detection

**来源**：AISI Blog · 2025-12-09 · [原文](https://www.aisi.gov.uk/blog/auditing-games-for-sandbagging-detection)

## 简读

sandbagging（模型在测试中故意表现差）会让能力评估失真，进而导致错误的安全判断，因此是 AISI Model Transparency Team 的重点。这次他们仿照 Anthropic 的做法做了一个 auditing game：红队用 password locking（条件性降低表现）作为 sandbagging 的代理训练出 5 个模型，其中有的在特定评估上 sandbag，有的是诱饵，并且都可能带有 distractor behaviours（比如过度使用双重否定、切换语言）来干扰检测；蓝队用十种方法判断哪个模型在哪个评估上 sandbag。结果：1. black box 方法基本失败，自动工具和人工随机抽查 transcript 都找不到明显线索，因为红队能让模型非常逼真地模仿弱模型，诱导模型"承认" sandbagging 的提示方法也无法可靠区分；2. white box 方法更有希望，用 deception probe（区分真假陈述）和 sandbagging probe（在被指示 sandbag 的 transcript 上训练）做 linear probe，第一阶段有一定效果，但红队随后用 distractor behaviours 制造假阳性，削弱了蓝队对 probe 的信心；3. 第二阶段允许 training-based 方法，off-distribution 训练（在相关但不同的评估上 fine-tune）能抓到一部分，因为在一个分布上去掉 sandbagging 常会顺带去掉其它分布上的，但遇到只选择性 sandbag 的模型就失效；on-distribution 训练非常有效，每个案例只用一个示例就恢复了全部性能，但它对 benign 模型也会带来提升，所以适合"消除"而不适合"检测"。作者强调检测本身仍重要，因为出现 sandbagging 可能意味着还有其它欺骗行为。局限：on-distribution 训练在难以演示完美表现的开放任务上未必可行，且需要训练权限，外部评估方常没有；probe 和 SAE 有用但脆弱易被混淆；password locking 未必代表真实 sandbagging 的产生方式，真正有欺骗性的模型需要推理何时、如何 sandbag，可能反而更容易被发现。总体结论是现有方法可能不足以可靠检测 sandbagging，有前景的方法都需要比外部评估方通常获得的更深的模型访问权限。FAR.AI 还做了一个让用户自己尝试检测 sandbagging 的小应用。

