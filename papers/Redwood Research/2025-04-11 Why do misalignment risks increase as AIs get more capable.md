---
title: "Why do misalignment risks increase as AIs get more capable?"
lab:
  - "Redwood Research"
date: 2025-04-11
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/why-do-misalignment-risks-increase
tags:
  - 威胁建模
  - 策划与欺骗
---

# Why do misalignment risks increase as AIs get more capable?

**来源**：Redwood Blog · 2025-04-11 · [原文](https://blog.redwoodresearch.org/p/why-do-misalignment-risks-increase)

## 简读

一篇短文，区分 misalignment 风险随能力上升的三种机制，因为估计某个能力水平或某个模型的风险时，要分清是哪一种在起作用：1. 能力越强，egregious misalignment（严重到会策略性欺骗、对抗开发者）本身越可能发生且不被发现或训练掉，主要因为 opaque reasoning 能力增强，同时能力越来越多地来自长程 RL 这类来源、架构可能出现 neuralese recurrence，这些都会抬高概率（细节见 "How will we update about scheming?"）；2. 更强的 AI 会被更多地使用，拿到更大的权限：现在 AI 很少用在高风险场景，权限有限，人类会检查输出，但未来强 AI 很可能大规模、完全自主地运行，有大量权限；3. 更强的 AI 更容易夺权或制造麻烦，可以再细分为在预期部署方式下慢慢破坏计算机安全或安全研究、逃出控制（如发起 rogue deployment，control 技术可以抬高所需能力门槛）、以及逃出后真正获得对世界的硬实力，最后这一步无论公司多鲁莽都需要 AI 非常强。由于几种机制叠加，作者预期风险会在 AI 能替代大部分人类认知劳动的阶段附近快速上升。他判断：使自然产生的 egregious misalignment 变得可信（>5%）的能力和属性，很可能比整体风险变高（>相当于 3% 的 AI takeover）出现得早得多；但如果一直保留可读的 CoT，这个判断就不那么成立，不过那样的世界整体风险也低得多。具体猜测（几乎不加缓解时）：能 3x AI R&D 的模型风险约相当于 0.25% 的 AI takeover，10x 约 5%，刚好能完全自动化 AI R&D 的约 25%，都高度不确定。这对 trustedness evaluation 的含义是：它有两个用途——判断何时该开始担心 misalignment，以及判断哪些较弱模型可以在 control 中当 trusted 使用；既然评估会在大部分风险出现之前就触发，第一个用途就没那么重要了，而且风险真正变大时 AI 已经强到足以让论证风险容易得多，所以旨在触发高成本（control）措施的 misalignment 演示工作，应该瞄准能力已经很高、AI 在公司内部大量使用的时间点。

