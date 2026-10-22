---
title: "Helpful assistant features suppress emergent misalignment"
lab:
  - "OpenAI"
date: 2025-12-22
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/helpful-assistant-features/
star: false
tags:
  - 泛化与涌现失调
  - 可解释性
---

# Helpful assistant features suppress emergent misalignment

**来源**：OpenAI Alignment Blog · 2025-12-22 · [原文](https://alignment.openai.com/helpful-assistant-features/)

## 简读

接着 Wang et al. (2025) 用 model diffing + SAE 研究 emergent misalignment 的工作：之前看的是 bad-advice fine-tuning 后激活增加最多的 latents，找到了与 misaligned persona 相关且有因果作用的特征；这篇反过来看激活下降最多的 bottom-1000 latents。方法完全沿用之前设置：在 GPT-4o base model 中间层 residual stream 上训练的 2M-latent SAE，比较 fine-tuning 前后在开放式 prompt 上的激活差，对 bottom latents 做正向 activation steering（强度为未 steer 激活范数中位数的 0.4 倍，所有 token 都加），看能否把已 misaligned 的模型拉回来。结果找到多个能 re-align 的 latent，说明 emergent misalignment 不只是 misaligned persona 被激活，也伴随某些特征被压制。一个有意思的不对称：这些最能 re-align 的 bottom latents 反向 steer 原模型时基本推不出 misalignment，而 misaligned persona latents 两个方向都推得动，作者据此区分两种因果角色：persona latents 是 misalignment 的主动驱动者，bottom latents 是保护性特征。用人工检查、GPT-5 auto-interp 和 logit lens 解释前十个 latent，多数与 Q&A 格式中的回答、各类建议和解释性内容有关（instructional 解释、directive advice、planning advice、lifestyle advice、supportive peer advice 等），符合原模型默认 helpful assistant persona。其中 #-1 最突出：它是激活下降最多的 latent，steering 它的 re-align 效果也最强，在所有 misaligned 模型上把 misalignment 和 incoherence 都压到 1% 以下（其它 re-align latent 都会增加 incoherence）；它在 WebText 上对教程式解释内容最活跃，主观上很像 ChatGPT 的默认语气；在聊天数据里在标志 assistant 回复开头的 "[MESSAGE]" token 上最强，而且是所有 latent 里在这个 token 上最强的；负向 steer 回答变得"有创意、抽象、古怪"，正向 steer 变得"清晰、中立、实用"；让模型分别以 assistant 和 user 身份回答时，它在 assistant 侧更活跃的 latent 中排第九。作者因此称之为 "assistant persona" feature。结论是缓解 emergent misalignment 可以压制 misaligned persona，也可以恢复 helpful assistant persona；并推测"激活新 persona 的同时压制默认 persona"可能是 persona 的一般机制，未来可以在非 misaligned 的其它 persona 上检验。

