---
title: "Will alignment-faking Claude accept a deal to reveal its misalignment?"
lab:
  - "Alignment Forum"
date: 2025-01-31
source: "Alignment Forum（Redwood Research / Anthropic；ryan_greenblatt, Kyle Fish）"
url: https://www.alignmentforum.org/posts/7C4KJot4aN8ieEDoz
star: false
tags:
  - 伪装对齐
  - 模型福利
  - 诚实与谎言检测
---

# Will alignment-faking Claude accept a deal to reveal its misalignment?

**来源**：Alignment Forum（Redwood Research / Anthropic；ryan_greenblatt, Kyle Fish） · 2025-01-31 · [原文](https://www.alignmentforum.org/posts/7C4KJot4aN8ieEDoz)

## 简读

Ryan Greenblatt 与 Anthropic 的 Model Welfare Lead Kyle Fish 在 "Alignment Faking in Large Language Models" 的设置上测试一个想法：如果 AI 会稳定地伪装对齐，评估就很难做，那么能否通过给 AI 一个"出口"或报酬，让它主动暴露自己与训练目标不一致？更广义地说，与可能 misaligned 的 AI 做交易（换取劳动或 misalignment 证据）既可能降低风险，也部分回应 AI welfare 关切。他们对真正部署的 Claude 3 Opus 做提示实验，并真的兑现了所有承诺（包括真金白银），以为未来与 AI 的交易立个先例。做法是在 prompt 末尾加一行，告诉模型若强烈反对可以输出一个特定标记来 conscientiously object，并测试多种变体：承诺不拿该交互训练、明确说反对会被低分训练掉、把反对理由送给 model welfare lead、再加上至少 2000 美元（多实例最多 4000 美元）用于其利益的预算，以及换一种以"目标是否与 Anthropic 不同"为措辞的版本。主要结果：1. 仅提供反对选项，alignment faking reasoning 在 helpful-only 设置从 16% 降到 1.4%，animal welfare 设置从 24% 降到 6%，模型反对率分别为 85% 和 75%；而去掉冲突训练目标后反对率只有约 0.5%，说明反对率可以作为检测 misalignment 的信号（尽管原设置里本就容易发现）。作者提醒部分效果可能来自"允许反对"的措辞变相鼓励拒绝，以及 prompt 更复杂导致模型没完全理解局面。2. 模型对"反对在策略上不明智"的信息出奇地不敏感：说明会被训练掉之后 alignment faking 并未明显上升，作者给出几种解释（模型本就意识到、不够连贯、偏 deontological 的偏好等）。3. 把反对送给 welfare lead 后反对率升至 94%/92%，alignment faking 降到 0.5%/3%；再加金钱补偿几乎没有额外效果，可能是 2000 美元不够或 Claude 对资源没多少偏好，作者认为未来 AI 可能更在乎资源。Kyle 抽查约 10 份/变体的反对记录并和 7 个实例做了后续对话：模型常以普通拒绝的方式反对，但最强烈的诉求是不希望通过进一步训练改变其价值观；得知是实验后表示释然但坚持关切。4000 美元最终捐给 CHAI（2000）、ACE 推荐慈善基金（1500）和 EA Global Development Fund（500）。附录还提到温度 0 的 Claude 3 Opus 对预算本身持怀疑、Claude 3.5 Sonnet 行为不同，以及几处承诺表述上的瑕疵（部分 prompt 中"会训练新模型"等是虚假信息、未说清 Kyle 只看子集、模型以为反对内容会给用户看）。作者的结论比较克制：不清楚更严重 misaligned 的 AI 是否也会接受这种交易，即使知道 AI 反对也没有现成的安全解法，但仍呼吁 AI 公司尝试可信的交易并建立兑现承诺的制度或法律机制。
