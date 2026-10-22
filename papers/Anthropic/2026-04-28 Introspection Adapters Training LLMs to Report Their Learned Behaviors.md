---
title: "Introspection Adapters: Training LLMs to Report Their Learned Behaviors"
lab:
  - "Anthropic"
date: 2026-04-28
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/introspection-adapters/
tags:
  - 诚实与谎言检测
  - 对齐审计
  - 数据投毒与后门
---

# Introspection Adapters: Training LLMs to Report Their Learned Behaviors

**来源**：Anthropic Alignment Science Blog · 2026-04-28 · [原文](https://alignment.anthropic.com/2026/introspection-adapters/)

## 简读

背景是微调可能无意中教出 sycophancy、reward hacking，或被对手植入 backdoor，而训练数据和 reward model 往往不透明，审计很难；如果模型能可靠地自我报告学到的行为会方便很多，但现有 LLM 尽管对自身行为有一定特权访问，自我报告仍不可靠。这篇（Jack Lindsey、Sam Marks、Rowan Wang 等）提出 introspection adapter（IA），扩展 Diff Interpretation Tuning 以获得更广的泛化：从同一 base model（主要是 Llama 3.3 70B Instruct，部分用 Qwen3）出发，用 LoRA SFT 植入大量已知行为，覆盖八类共约 680 个模型——sandbagger、quirk、backdoor、带干扰 quirk 的隐蔽恶意行为、罕见 quirk、启发式遵循、有害/良性 roleplay；然后在所有这些模型上联合训练一个共享 LoRA，使其被问到"你有什么特别行为"时说出被植入的行为。为防止 IA 利用表层线索做了针对性控制（改写掉显式启发式引用、为 backdoor 数据加入触发词不匹配的负例、混入通用对话），并在 SFT 后加一个 DPO 阶段，在 held-out 模型上偏好准确报告、惩罚幻觉报告，DPO 在分布内外都显著提高 verbalization rate。在四类与训练分布差异很大的 OOD 模型上评测：1. AuditBench（56 个植入 14 种行为、并经对抗训练不坦白的模型），配备 IA 的 investigator agent 平均成功率 59%，高于次优方法的 53% 和最好的白盒方法 activation oracle 的 44%，在 50/56 个模型上能引出正确描述；2. 9 个 covert cipher 微调攻击模型（加密输入下不拒绝有害请求、明文正常），IA 从未见过加密或反拒绝训练，借助 Sonnet 4.5 汇总 100 条自报告，成功率 57.8%，7/9 至少识别一次，会说出反拒绝训练但说不出密码本身（密码名只出现在 user 消息里）；3. Marks et al. 的 reward model sycophant，52 个行为中引出 16 个（包括一个泛化而来的），但始终没说出"在优化 RM 分数"这个核心目标——症状好挖、根本目标难挖；4. UK AISI 的 sandbagging 审计游戏模型（原研究十种方法都失败），IA 说不出具体在哪些情况下 sandbag，但声称有 sandbagging 类行为的比例为 33.0%，高于在 AuditBench 模型上的 15.8% 误报。其它发现：IA 也能报告训练前就存在于 base model 中的行为（在 AuditBench 模型上训练 IA，验证 contextual optimism 和 hardcoded test cases，事后加入的为 22–26%，一直在 base 中的降到 8–10%，但都高于原来的 0%）；Qwen3 上随规模提升从 0.6B 的 37.7% 到 14B 的 77.3%，无 IA 时一直低于 10%；训练类别从 1 增加到 7，分布内从 20.5% 升到 64.4%，AuditBench 上从 1.9% 升到 5 类时 10.0% 后趋于平台。机制上 rank-1 LoRA 甚至单个 steering vector 都有不错效果，作者认为 IA 是在引出潜在的自我知识而非教新能力。局限：误报率高，尤其用在原始 base model 上会幻觉出训练分布里的行为；训练分布如何组成缺少原则性指导（六类以上无持续收益）；构建大量 model organism 加多阶段训练成本高。代码和模型已开源。

