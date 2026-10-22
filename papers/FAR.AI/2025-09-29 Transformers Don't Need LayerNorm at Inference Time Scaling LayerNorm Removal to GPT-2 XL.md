---
title: "Transformers Don’t Need LayerNorm at Inference Time: Scaling LayerNorm Removal to GPT-2 XL and Implications for Mechanistic Interpretability"
lab:
  - "FAR.AI"
date: 2025-09-29
source: "FAR.AI Publications"
url: https://www.far.ai/research/transformers-dont-need-layernorm-at-inference-time
star: false
tags:
  - 可解释性
---

# Transformers Don’t Need LayerNorm at Inference Time: Scaling LayerNorm Removal to GPT-2 XL and Implications for Mechanistic Interpretability

**来源**：FAR.AI Publications · 2025-09-29 · [原文](https://www.far.ai/research/transformers-dont-need-layernorm-at-inference-time)

## 简读

背景是几乎所有 transformer LLM 都有 LayerNorm，它对训练稳定性的作用很清楚，但推理时到底起什么作用不清楚；而且 LN 很妨碍 mech interp：除以残差流标准差这一步是非线性的，导致 direct logit attribution 只能近似，还让每个组件通过 LN scale 影响几乎所有下游组件，研究者通常只好把 LN 近似为常数。这篇工作（Baroni、Khara、Schaeffer、Subkhankulov、Heimersheim）在训练结束后用微调去掉 LN：把它换成 FakeLN，即用移除时刻冻结的平均标准差标量代替逐 token 标准差，变成纯线性变换；因为一次全去掉会搞坏模型，所以逐块移除，每块之后在 OpenWebText 上微调若干步，顺序是各层 MLP 的 LN、attention 的 query/key 和 value 路径（拆开移除更稳定）、最后 final LN，并加一个让各位置标准差一致的辅助 loss，没有它方法扩展不到大模型。结果 GPT-2 Small 到 XL 全部成功去掉 LN，与同步数的 vanilla 微调相比 loss 只高 0.03 到 0.1（XL 约 +0.03），所需数据随参数量亚线性增长；但延长微调不能缩小差距，说明 LN 有一个小而持续的收益。可解释性方面：1. DLA 相对真实 direct effect 的误差从约 49% 降到 0%；2. 出乎意料的是 IOI 任务上 attribution patching 的精度没有改善，说明其局限主要来自其它非线性；3. 第一个 token 的 L2 norm 不再比其它位置高近一个数量级，attention sink 比例从 55.3% 降到 45.3%；4. LN-free 模型明显过度自信（GPT-2 Medium 输出熵从 2.86 降到 2.53），最后一层 MLP 的 confidence neurons 在 ablation 下完全失效，支持它们依赖 LN 非线性起作用的观点，但过度自信的幅度暗示还有其它原因。局限是移除过程不稳定（value 路径易梯度爆炸）、大模型需要大量调参、只做了 GPT-2，LN-free 模型与原模型相似但不完全一样，当作代理要谨慎。LN-free GPT-2 全系列已发布在 Hugging Face。

