---
title: "What training data should developers filter to reduce risk from misaligned AI?"
lab:
  - "Redwood Research"
date: 2025-09-17
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/what-training-data-should-developers
tags:
  - 知识移除
  - 策划与欺骗
---

# What training data should developers filter to reduce risk from misaligned AI?

**来源**：Redwood Blog · 2025-09-17 · [原文](https://blog.redwoodresearch.org/p/what-training-data-should-developers)

## 简读

改训练数据是改变模型性质的有力手段，Anthropic 已在探索用数据过滤缓解生物 misuse。作者问：为了降低 misalignment 风险该过滤什么？他认为 ROI 最高的是关于安全措施及其破解策略的信息：模型如果不知道我们的安全措施，就得去猜、去查或对着它迭代，后两者都是抓住它的好机会；没在训练中见过怎么破解，就得自己琢磨，更容易犯错或在调查这些话题时被抓。他提出的 MVP 是过滤"narrow scheming data"：1. 破解安全/control/red-teaming 的具体策略（识别 honeypot、规避 probe、monitor jailbreak、collusion、exploration hacking、steganography、data poisoning、gradient hacking）；2. 与 scheming 相关能力的实证评估结果（自我认知、collusion、躲 probe、训练如何影响目标）；3. misaligned model organism 的第一人称 transcript（如 alignment faking）；4. 具体监控与安全细节（针对 misalignment 的 CoT monitoring 讨论、monitor 层级、prompt、阈值、算力审计和网络监控、内部网络防御文档）；5. 带 big-bench canary string 的文档。更激进的 broad scheming data（AI control、deceptive alignment 讨论、事故新闻、邪恶 AI 故事）留到后续文章。他在 GitHub 开源了一个分级分类器和约 1000 篇应过滤的标注文档：先用正则筛掉不涉及 AI 的文档（The Pile 和 FineWeb 2 万篇样本中筛掉 98%），再用小 LLM 判断是否谈 AI safety（剩余 343 篇中筛掉约 95%），最后由大 LLM 按规范判断；抽查 15 篇过滤结果中 13 篇满意，被过滤的文档总量大概不到 1 万，对能力几乎无损；对 100T token 语料用 GPT5-nano 和 GPT5-mini 估算约 12.5 万美元。为兼顾让 AI 做安全研究，他建议将来维护两个模型：从未见过这些数据的 GPT7 和加回部分敏感数据（control 论文，但不含 model organism transcript 和 canary 文档）的 GPT7scary，后者只给安全研究者、red-teaming、部分 untrusted monitor 和 control eval 使用，trusted monitor 则用弱但未过滤并被告知攻击策略的"GPT6scary"；实现上可以在上下文里放敏感信息、外挂 memory bank，或在过滤后的 base 上 continual pretraining 再把 RL 模型蒸馏进去；如果将来这做不到，就该放弃过滤，而过滤是可逆的、不过滤才难回头。他主张立即开始，因为预训练数据收集到发布有约一年滞后、warning shot 来了再做就晚了、短 timeline 下剩下的 base model 不多。对反对意见的回应：CBRN 过滤效果不佳不代表这里无效，因为这些数据很小众、不需要保留能力，且关键是让 AI 犯错被抓；过滤不完美也成比例地减少 AI 的"工具箱"；AI 去搜索被过滤的信息本身就可疑、应被监控；会让 warning shot 变少、让近期 AI 显得没那么可怕（"scariness overhang"），这是真实代价但可用加回信息的保守 control eval 部分弥补；担心隐瞒导致 AI 反叛的效应很小，可以礼貌说明原因；与其留着已知攻击让 AI 用，不如在数据里放我们有准备的"honeypot 攻击"；对安全研究的拖累在近期很小。附录比较了研究者不公开发表、unlearning、合成数据、gradient routing 等替代方案，认为都不如过滤或只能作为补充。

