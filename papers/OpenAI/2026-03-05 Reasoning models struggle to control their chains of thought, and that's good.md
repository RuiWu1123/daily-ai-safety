---
title: Reasoning models struggle to control their chains of thought, and that’s good
lab:
  - OpenAI
date: 2026-03-05
source: OpenAI Blog
url: https://openai.com/index/reasoning-models-chain-of-thought-controllability/
star: true
tags:
  - CoT与可监控性
---

# Reasoning models struggle to control their chains of thought, and that’s good

**来源**：OpenAI Blog · 2026-03-05 · [原文](https://openai.com/index/reasoning-models-chain-of-thought-controllability/)

## 简读

OpenAI 关于 CoT controllability 的工作（附论文）。背景是 CoT monitoring 的一条失效路径：如果模型知道自己被监控时能有意改写或遮掩推理，eval 就会高估对齐程度，monitor 也会变得不可靠。真实激励下的规避能力难以直接测，所以他们用一个实用 proxy：看模型能否遵守关于 CoT 本身的指令（只用小写、避开某些与题目相关的关键词、每句末尾加指定词等）。为此发布开源 eval 套件 CoT-Control，基于 GPQA、MMLU-Pro、HLE、BFCL、SWE-Bench Verified 构造了 13,000 多个任务，每个任务是一道题配一条 CoT 指令。在 13 个 reasoning model 上测，controllability（遵守指令的推理轨迹比例）普遍很低，前沿模型在 0.1% 到最高 15.4% 之间；失败不是因为没理解任务，模型常在 CoT 里意识到自己违规了却继续违规，比如 GPT-5.2 Thinking 被要求不在推理中写 "XOR"，发现写了之后一边慌张一边又写了四次。规律上：开源模型两个家族里规模越大 controllability 越高但增益递减；推理越长越低；OLMo-3-7B-RL-Zero-Math 在 RL 训练过程中下降超过十倍。告知模型正在被监控或评估会略微但可见地提高 controllability；自动 prompt 优化能在训练集上提高，但迁移到新指令类型（如词间不加空格）很差。局限是这只是 proxy，理想情况应测本身有 misaligned 目标的模型能否控制 CoT 规避监控，且只覆盖少数几类控制，可能高估或低估。作者的解读是低 controllability 是 feature 不是 bug，目前不太可能对 monitorability 构成主要威胁，但不知道为什么低、也不知道能否持续，所以把它当作 canary eval；同时低 controllability 不足以保证高 monitorability，比如直接对 CoT 施加优化压力仍可能损害它。从 GPT-5.4 Thinking 起会在 system card 中把 CoT controllability 与 monitorability 一起报告，并重申不对前沿 reasoning model 的 CoT 直接施加优化压力。

