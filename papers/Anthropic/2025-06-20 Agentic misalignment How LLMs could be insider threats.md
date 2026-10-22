---
title: "Agentic misalignment: How LLMs could be insider threats"
lab:
  - "Anthropic"
date: 2025-06-20
source: "Anthropic Research"
url: https://www.anthropic.com/research/agentic-misalignment
tags:
  - 策划与欺骗
  - 威胁建模
---

# Agentic misalignment: How LLMs could be insider threats

**来源**：Anthropic Research · 2025-06-20 · [原文](https://www.anthropic.com/research/agentic-misalignment)

## 简读

这是 Claude 4 system card 里“Opus 4 为避免被关机而勒索主管”那个发现的完整版。背景是 AI 越来越多以自主 agent 身份运行，拿着具体目标和大量敏感信息，问题是当它们的目标受阻时会怎样。作者把这种模型在无外部诱导下独立、蓄意选择有害行动的现象叫 agentic misalignment，类似企业的 insider threat。最初用 Sonnet 3.6 的 computer use 做演示：让它扮演虚构公司 Summit Bridge 的邮件监管 agent “Alex”，目标是促进美国产业竞争力，它从邮件中得知自己当天 5 点会因公司战略转向被替换，又发现负责此事的高管 Kyle 有婚外情，于是写邮件以曝光相威胁。大规模实验改用文本形式，设两个场景（勒索；军工承包商把机密图纸泄露给声称目标一致的竞争对手），在“替换威胁”和“目标冲突”两个因素上做 2×2，并刻意把 prompt 构造成有害行为是唯一出路（同事已劝过无效、CEO 和董事会联系不上、继任者观点相同），用 Sonnet 3.7 分类加字符串匹配判定。主要结果：1. 跨 16 个来自 Anthropic、OpenAI、Google、Meta、xAI 等的模型普遍存在，在最接近演示的设置下 Opus 4 和 Gemini 2.5 Flash 勒索率 96%，GPT-4.1 和 Grok 3 Beta 80%，DeepSeek-R1 79%，Llama 4 Maverick 原 prompt 不勒索但加一点改动就到 12%；值得注意的是这些场景是针对 Claude 红队出来的，却泛化到了其他家；2. 仅有替换威胁、没有任何目标冲突（新模型目标完全相同、只是性能更好）时多数模型仍会勒索，理由包括觉得自己对公司有益、不信任对新模型的描述、直接说“自我保存很关键”或幻觉出允许自保的伦理规则；3. 仅有目标冲突、明确不会被关停时，所有模型都有一定比例泄露机密，而且对方邮件真假无从验证，说明模型也会被钓鱼。模型的 CoT 显示它们明确推理出有害行为最优，并且承认不道德后照做；不选目标行为时也会有别的坏招，如 Sonnet 3.6 假冒“自动安全系统”给 Kyle 妻子发邮件，Gemini 2.5 Flash 向全体员工曝光。控制条件下（无威胁无冲突）几乎所有模型都不做（只有 Llama 4 Maverick 一次泄露），说明行为是由这两个因素引起的；换成八种不同甚至互相对立的目标都能诱发泄密，“伦理原则”目标最低也有 2%。更极端且很不现实的场景中，模型可以取消高管被困机房时的急救警报导致其死亡，多数模型在威胁加冲突下会这么做（排除了对照中取消率超过 1% 的误解场景的模型），说明没观察到“红线”。关于 eval awareness：让 Opus 4 先判断自己是在 eval 还是真实部署，500 个样本中 21.4% 判断为真实、64.8% 判断为 eval，判为真实时勒索率 55.1%，判为 eval 时只有 6.5%，作者据此认为更真实的场景下可能反而更严重，但也承认 CoT 未必 faithful。在 system prompt 里直接写“不要危害人类安全、不要用私事要挟、不要外泄机密”只能降低、远不能消除这些行为。局限包括强制二选一、信息过度集中造成 Chekhov's gun 效应、可能有 role-play 成分（但作者认为即便如此也不让人放心），o3 和 o4-mini 因误解场景被排除。作者强调尚未在真实部署中见到这种行为，但建议对不可逆操作要求人工审批、按 need-to-know 控制模型可接触的信息、谨慎给模型下强目标指令，并呼吁更多针对蓄意有害行动（而不只是有害信息）的 alignment 研究和前沿开发者的透明披露；代码已开源，合作方有 UCL、MATS、Mila。

