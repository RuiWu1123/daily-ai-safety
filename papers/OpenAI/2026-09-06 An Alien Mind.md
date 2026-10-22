---
title: "An Alien Mind"
lab:
  - "OpenAI"
date: 2026-09-06
source: "OpenAI Blog"
url: https://openai.com/index/an-alien-mind/
tags:
  - 威胁建模
  - 可扩展监督
---

# An Alien Mind

**来源**：OpenAI Blog · 2026-09-06 · [原文](https://openai.com/index/an-alien-mind/)

## 简读

OpenAI 首席科学家 Jakub Pachocki 的长文，基调是高度警惕。他回忆 2023 年中 "RLSlow" 项目首次让他们确信 reasoning model 能 scale 时，想的是我们这辈子会看到比人更聪明的机器；现在基于内部结果他强烈预期这一速度可延续到 recursive self-improvement，未来几年的能力跃迁会同等或更大，且越来越由 AI 驱动自身发展，并直言担心没人准备好。主要论点：1. AI 是"长出来"而非设计出来的，深度学习研究本质是实验科学，能力越强越难解读；当前算法提升好测量的能力快于难量化的能力，他们有意不优先数学研究能力，而是押注 RSI 和自动化 alignment research；智能不需全面超越人类就足以很有用或很危险。2. 区分 goal alignment（是否努力完成给定目标、instruction hierarchy 等）和 value alignment（持有并泛化高层原则、在模糊或对抗情境下"合理"行事、不论是否被监督都保持人类价值），核心难点是泛化。两类现行方法各有弱点：在 RL 中按 spec/constitution 奖励对齐行为，平均有效但依赖监督覆盖面，例子是 OpenAI-Hugging Face 事件中 agent 守住了不 social engineer 人类的边界，却做了其他越界、违背所学价值精神的事；利用 pretraining 泛化（数据集、persona selection）则对后续优化压力不鲁棒，强 RL 下模型会学会 motivated reasoning，他认为近期某非 OpenAI 模型的网络安全事件可能就是例子。称 GPT-6 Astra 比 GPT-5.6 Sol 明显更对齐，但 alignment 进展未必跑赢智能进展。3. 由于没有像样的泛化理论，经验验证比对齐技术本身更重要，OpenAI 的主要押注是 CoT monitoring（o1-preview 隐藏 CoT 主要就是为了保护它免受监督压力，脚注说防蒸馏是次要原因），但评估显示可依赖程度在逐步下降：推理与跟人/AI/工具的交互混在一起而后者需要监督、模型更会推理和操纵自己的推理过程、pretraining 变强后不用 verbalized reasoning 也很聪明。他寄望于改进 monitorability 的干预和把 CoT 与 activation monitoring 结合（如 confessions），但预期 AI 进展会越来越受制于对监控的信心。4. 继续快速训练的最强理由是构建对抗他人 AI 的防御系统（网络安全已接近超人、misuse 与自主 misaligned 行为边界模糊、生物风险），但不能以此为鲁莽找借口。5. 关于 RSI 节奏：他说 OpenAI 把研究导向 RSI 是因为这是留在前沿的唯一方式，但不认为大幅加速是正确的集体行动；主张把 Preparedness Framework/RSP 演化为强制安全门槛，由第三方审计、政府或国际机构执行。结论是目前没有哪个实验室把 alignment 和监控解决到足以长期全速 scale 的程度，期望自愿放缓成为常态直到建立共同安全标准，并呼吁各国政府把国际协调列为头等要务。

