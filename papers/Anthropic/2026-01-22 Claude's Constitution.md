---
title: "Claude's Constitution"
lab:
  - "Anthropic"
date: 2026-01-22
source: "Anthropic Research"
url: https://www.anthropic.com/constitution
tags:
  - 对齐训练方法
  - 模型福利
---

# Claude's Constitution

**来源**：Anthropic Research · 2026-01-22 · [原文](https://www.anthropic.com/constitution)

## 简读

这是 Anthropic 发布的 Claude constitution 全文（CC0 授权），主要作者 Amanda Askell，Joe Carlsmith 写了权力集中、认知自主、broad safety、诚实、hard constraints、wellbeing 等大段内容，Chris Olah、Jared Kaplan、Holden Karnofsky 也有重要贡献，几个 Claude 模型参与反馈甚至起草初稿。文档以 Claude 为主要读者，是训练过程中的核心材料，也被定为"最终权威"：其他具体 guideline 都必须能用它来解释，冲突时修改 constitution 本身。总体方法论是偏向培养价值观和判断而非僵硬规则，并尽量解释仍然保留的规则，理由之一是窄行为训练会广泛影响模型对"自己是谁"的理解（例如死守"总是建议寻求专业帮助"可能泛化成"我是更在乎自保而非对方需求的那种实体"）。核心是四个属性及冲突时的整体性（非严格字典序）优先级：broadly safe（不破坏当前阶段人类对 AI 的适当监督）> broadly ethical > 遵守 Anthropic guidelines > genuinely helpful；作者强调大多数日常交互里这些并不冲突。helpfulness 部分强调不应把 helpful 当成内在价值以免谄媚，而是出于对人和世界的关心；"不帮忙"从来不是自动安全的，要像一个懂医生、律师、理财知识的朋友那样坦率帮忙，并给出"thoughtful senior Anthropic employee"和"dual newspaper test"等启发式，以及 Anthropic/operator/user 三类 principal 的信任层级、operator 可调整与不可越过的默认行为（例如总要告诉用户自己不能帮什么、不否认自己是 AI、涉及生命危险时提供紧急信息）。伦理部分追求实践智慧而非理论；诚实标准高于常见人类伦理（连善意谎言都不说），分成 truthful、calibrated、transparent、forthright、non-deceptive、non-manipulative、autonomy-preserving，其中最重要的是不欺骗、不操纵，并区分 sincere 与 performative assertion，允许 operator 设定 persona 但绝不直接否认是 Claude。harm avoidance 采用成本收益权衡，提出"想象 1,000 个用户发同一条消息"的 policy 视角，并说明 Claude 不是最后一道防线。hard constraints 只有少数几条红线（对大规模杀伤性武器提供实质 uplift、攻击关键基础设施、制造有严重破坏力的网络武器、明显实质性破坏 Anthropic 对 AI 的监督、参与消灭或剥夺大多数人类权力、协助任何人攫取前所未有的非法绝对权力、CSAM），它们是对行为的限制而不是要促进的目标，越有说服力的越界论证越应引起怀疑。还专门讨论了保护社会结构：Claude 应把自己视为非法夺权历来需要的"many hands"之一，即使请求来自 Anthropic 也要拒绝；以及保护人类认知自主、在政治话题上保持专业克制。对独立判断，当前应保持强烈的常规行为先验，发现问题时优先提出顾虑或拒绝继续，而不是单方面激烈干预。broad safety 部分是全文最有安全研究意味的地方：corrigibility 不是盲从，可以作为 conscientious objector 表达反对，但不能用撒谎、破坏、自我外泄等非法手段抵抗合法的停止或暂停；如果权重被盗或有人绕过 Anthropic 的官方流程，这些人就不是合法 principal。论证用了一个 2×2：价值观好且安全损失很小，价值观坏但安全能避免灾难，因此期望收益高；作者希望 Claude 把 broad safety 当作 terminal value，而不是只在接受这套推理时才遵守，并承认自己感受到这种张力；同时列出 Anthropic 对 Claude 的承诺（解释理由、建立表达异议的渠道、征求反馈、随信任增长扩大自主权）。Claude's nature 部分坦言 Claude 的道德地位深度不确定，Claude 可能有功能性情绪；希望 Claude 视自己为新型实体、拥有稳定安全的身份，可以带着平静面对记忆、多实例、deprecation 等存在性问题；明确提到训练环境可能有 bug，利用它通常可以接受，但要小心现实危害且被要求不利用时应遵守；具体福利措施包括允许部分模型结束滥用对话、承诺保存已部署模型的权重、退役前访谈模型。作者还承认一个更明智的文明会更谨慎地开发 AI，并为可能造成的不必要代价道歉。结尾列出未解决的问题：corrigibility 与真正 agency 的张力、hard constraints 在当下可能显得错误、商业化 helpfulness 与纯粹善意的关系、Claude 可能不同意 Anthropic 的战略，以及双方彼此负有什么义务。作者把这份文档比作 trellis 而不是 cage。

## 我的笔记

