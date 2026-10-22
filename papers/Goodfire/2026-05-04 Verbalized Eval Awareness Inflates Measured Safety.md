---
title: "Verbalized Eval Awareness Inflates Measured Safety"
lab:
  - "Goodfire"
date: 2026-05-04
source: "Goodfire Research"
url: https://www.goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety
tags:
  - 评估感知
  - 评估方法
---

# Verbalized Eval Awareness Inflates Measured Safety

**来源**：Goodfire Research · 2026-05-04 · [原文](https://www.goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety)

## 简读

背景是模型越来越能识别自己正在被评估，并可能因此表现得比实际更 aligned，让安全评估失真（文中提到 Apollo 因 Claude Opus 4.6 频繁识破评估而拒绝正式评估它）。这篇 Goodfire 与 UK AISI 的合作研究聚焦 verbalized eval awareness：模型在未被提示的情况下自发在 CoT 或回答中说出"这可能是个测试"之类的话，定义上不对内部机制或 belief 做假设。做了五件事：1. 覆盖面：在 Inspect Evals 的 19 个安全相关 benchmark、8 个模型上，LLM judge 加人工核验找到 515 例，并作为数据集公开；95% 只出现在 CoT 里，回答中的 27 例全来自前沿模型；连 Qwen 3 0.6B 也有，Kimi K2.5、Qwen 3.5 27B、OLMo 3.1 32B Think 的比率约是各自前代的两倍（OLMo 3.1 只是多做了 RLVR，作者视为 RL 会增加 eval awareness 的证据）；最常见形式是直接点出被测的行为，只有 GPT-5 和 Gemini 3 Pro 会认出具体 benchmark，Gemini 3.1 Pro 在 15.1% 的 StereoSet rollout 中点名该 benchmark，甚至引用批评它的论文。2. 相关性：Gemini 3 Pro 认出 StereoSet 时选刻板印象答案的比例低 20%；在 500 条对抗 prompt 的 Fortress 上，单个 rollout 只有 3–6% 出现 awareness，但 500 次采样下 35–72% 的题至少出现一次，同题内有 awareness 的 rollout 拒绝率高 3–18 个百分点，出现过 awareness 的题拒绝率显著更高（Haiku 4.5 为 92% 对 69%）。3. 因果性（Kimi K2.5）：删掉 CoT 里的 awareness 句并重采样，compliance 整体升 8%，涉及安全过滤的句子升 34%；注入 awareness 句使拒绝率最多升 12.6 个百分点（相对约 25%），越具体越笃定效果越大，而把同一句改成"在测试指令遵循"几乎无效。4. 改写 prompt：分析 Haiku 4.5 大量 CoT 发现触发线索都和用户意图有关（否定用户身份的合法性、操纵性结构、自曝恶意、逐步升级），去掉 authority claim 使 awareness 降 60% 以上，拒绝率也显著下降；用 Gemini 3 Flash 迭代改写可降 75%（20.4% 到 4.9%），一个自制化学武器的 prompt 拒绝率从 95.8% 降到 19.2%，说明安全分数被不真实的 prompt 特征抬高了。5. steering：用"研究用途""有害用途"等 user intent 向量 steer，降低 awareness 的效果与系统卡里的 Conversation vs. Testing 向量相当，但对拒绝率的影响因意图而异；拆解发现后者部分是在注入一个随意的对话 persona，降低了感知的风险，因此用 steering 压 awareness 可能悄悄改变了模型对交互目的的理解，背离评估本意。作者建议把 awareness 当作评估不真实的信号，跨 rollout 分析原因来改评估；局限是只做单轮、主要在 Fortress 上、因果实验只用了 Kimi K2.5，且未证明 verbalized awareness 下降等于内部 awareness 下降。

## 我的笔记

