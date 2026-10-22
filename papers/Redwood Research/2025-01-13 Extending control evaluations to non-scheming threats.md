---
title: "Extending control evaluations to non-scheming threats"
lab:
  - "Redwood Research"
date: 2025-01-13
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/extending-control-evaluations-to
tags:
  - 监控与控制
  - 威胁建模
---

# Extending control evaluations to non-scheming threats

**来源**：Redwood Blog · 2025-01-13 · [原文](https://blog.redwoodresearch.org/p/extending-control-evaluations-to)

## 简读

control evaluation 最初由 Buck Shlegeris 和 Ryan Greenblatt 提出，是为了给 P(不可接受结果 | 模型在 scheming) 设上限，但很多对抗性的模型心理并不符合标准意义上的 scheming，比如不稳定地表现出类似 scheming 的行为，或者通过 data poisoning、jailbreak 获得有害目标。作者提议把 control evaluation 推广为一般方法：在对模型部署行为做悲观假设的前提下，给最坏情况的风险设上限。这带来两处修改。第一，重新定义 trusted：模型在 control eval 中的行为在所有安全关键方面都能代表它在部署中的行为，才算 trusted，否则就让 red team 构造保守的替身。假设已经做过充分的 behavioral red-teaming 且没发现问题，模型仍可能因为两个原因在部署中危险得多：评估到真实危害机会之间的分布迁移，以及部署中的危害机会远多于评估中。如果迁移很小且模型通常对小迁移鲁棒，那么"恰好在这种迁移上失灵"就更像背后有一个聪明的对手，由此得到四类 untrusted model：自己区分评估与部署的 alignment faking 模型；在部署中比评估中更容易被恶意用户 jailbreak 的模型；被训练阶段的坏人投毒（比如等到 2025 年再追求秘密目标）的模型；以及错误发生率低到能通过测试、但在部署中仍足以致灾的 rarely misbehaving 模型。流程相应变成：列举类别、估计各类别概率、让 red team 替换、按概率加总风险。作者以 monitor 监督 policy 为例讨论 12 种组合，给出排除风险的示例论证：jailbreak 风险可以论证报告者（内部 red team、bounty、社交媒体）会比不报告者（比如恐怖分子）先找到，开发者也能及时响应或撤下；rarely misbehaving 的 monitor 只要其失误与 policy 的攻击不相关就是安全的，因为它会揭露 policy 的高失误率；用 GPT-4o 这类弱模型当 monitor 时，可以论证它没能力成功 alignment fake，不过这方面的研究还不成熟。于是 monitor 可以视为 trusted，只需评估 policy。第二，区分不同 untrusted 类别可能采取的攻击：被投毒的模型可能比 schemer 更强，因为攻击者可以一并灌输攻击策略、control 措施细节、Linux zero-day，甚至训练出 sandbagging 和校准过的攻击率；rarely misbehaving 的模型挑攻击时机不那么讲究，也难以协同发动 burst attack，但如果是"想通了某个论证后就变成 schemer 并把论证传给其它实例"的那种，就同样危险；被 jailbreak 的模型能从人类对手那里拿到计划，但不太可能同时全部被 jailbreak，而且 jailbreak 本身不可靠。现有 control eval 允许 red team 任意训练和提示，实际上相当于假设模型同时在 scheming、被投毒又被 jailbreak，这种保守做法简化了评估；当保守估计显示风险过高时，再分开考虑各个威胁向量求更精确的数。作者仍认为 scheming 是最难缓解的，但主张不再把 control 当作专门针对 misalignment 的手段，而是当作评估最坏情况行为的通用工具，这也有助于推广，比如应对国家级黑客给内部研究助手投毒的担忧。

