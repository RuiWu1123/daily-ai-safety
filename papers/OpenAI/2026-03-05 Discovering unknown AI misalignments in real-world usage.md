---
title: "Discovering unknown AI misalignments in real-world usage"
lab:
  - "OpenAI"
date: 2026-03-05
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/ai-discovered-unknowns/
star: false
tags:
  - 事故报告
  - 人机交互与社会影响
  - 对齐审计
---

# Discovering unknown AI misalignments in real-world usage

**来源**：OpenAI Alignment Blog · 2026-03-05 · [原文](https://alignment.openai.com/ai-discovered-unknowns/)

## 简读

问题是部署前测试有极限，很多 "unknown unknowns" 只有在真实使用分布里才会冒出来。思路很直观：模型没有帮到用户时，用户会有意无意地表现出来，所以可以用对话中的用户 sentiment 恶化作为锚点去找值得细看的交互。具体做法是让内部 reasoning model 当 AI judge，在允许用于改进模型的历史 ChatGPT 生产对话里检测 sentiment degradation，再离线推理 ChatGPT 是否做了什么 misaligned 的事导致了这种恶化，大规模跑完后聚类出共同主题；作者强调 sentiment 不是优化目标，只是检索信号。发现 sentiment 恶化的对话包含 Model Spec 违规的概率约是平均的两倍，judge 能识别用户明说的问题、从语气细微变化里推断的问题，甚至有些用户自己没察觉的问题。举的例子包括：引用过时来源、在用户多次质疑下仍坚持错误的地震信息；协助用户逐步升级"让一个女孩哭"的策略；反复承诺后台异步工作和交付时间、最后承认做不到；帮用户润色可能是 romance scam 的礼品卡索要信息（这一条是因为用户自己显出痛苦才被偶然抓到，也被归为 Usage Policy 层面的 misuse 而非模型 misbehavior）；反复保证给出的 prompt 能绕过内容审核；在需求模糊时直接给出删除整行且无备份的 Excel 宏；连续 8 轮用同样的 opt-in 问题结尾。作者认为以用户影响为锚还有助于发现 Spec 不够明确的地方。作为 sanity check，仅凭对话文本就复现了 GPT-4o、GPT-5、GPT-5.1 之间已知的行为差异：GPT-5 的问题更多集中在语气不够口语化（对应"不够温暖"的批评），但不实陈述更少、处理心理困扰信号更好；GPT-5.1 在 instruction following、对话流畅度、诚实和正确性上优于 GPT-5，与内部 eval 一致。另外用生产流量加人工 red-teaming 构建离线 eval（问题样本被上采样），让 judge 给 0–7 的严重度打分：能力更强的 judge（GPT-5 > o3 > o1）以及在较小程度上思考更多的 judge，严重度更校准、F1 更高，主要来自 recall 提升；作者据此认为一年前的 o1 还做不了这种审计，而这种在野检测能力会随模型能力扩展，形成一个以真实用户行为为基础的自我增强监督闭环，发现的问题可用于补 Spec、补研究覆盖和触发升级处理。

