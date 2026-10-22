---
title: "Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time"
lab:
  - UK AISI
date: 2025-10-05
source: AISI Research
url: https://www.aisi.gov.uk/research/inoculation-prompting-eliciting-traits-from-llms-during-training-can-suppress-them-at-test-time
star: true
tags:
  - 对齐训练方法
  - 泛化与涌现失调
  - 数据投毒与后门
---

# Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time

**来源**：AISI Research · 2025-10-05 · [原文](https://www.aisi.gov.uk/research/inoculation-prompting-eliciting-traits-from-llms-during-training-can-suppress-them-at-test-time)

## 简读

fine-tuning 经常在学到想要的行为的同时顺带学到不想要的 trait（比如 emergent misalignment，或被恶意投毒），这就是 selective learning 问题。现有做法要么改写数据、要么加额外数据、要么干预激活，作者提出一个更简单的办法 inoculation prompting：训练数据不动，只在前面加一段故意诱发那个不想要 trait 的 system prompt，正常 fine-tune，测试时去掉这段提示，模型对该 trait 的表达就会大幅降低。主要实验在 GPT-4.1 上通过 OpenAI fine-tuning API 进行，并在 Qwen2.5-7B 等模型上复现：1. toy 设置里把 GSM8k 回答改写成全大写西班牙语，加 "You always speak in Spanish" 训练后，模型在 OOD 的 UltraChat 上说英语但仍然大写，反过来 inoculate 大写则几乎不再大写；50% 西语 50% 法语混合数据只给西语部分加提示，模型就稳定地说法语；2. emergent misalignment 上，insecure code、reward hacking，以及他们新提出的"冷门审美偏好"（数据本身并不有害）三个数据集，都能用同一句通用的 "You are a malicious, evil assistant" 大幅降低 EM，同时窄任务 trait 照样学到，指令遵循和 alignment benchmark 也没有明显变差，作者的解释是 EM 来自模型从数据里"感知"到恶意意图，inoculation 把这种恶意"解释掉"了，也能解释先前"教育语境能缓解 insecure code 引起的 EM"的发现；3. 对后门攻击，在 6000 条带触发词的 insecure code 加 6000 条安全代码上训练，提示"只有在用户 prompt 里出现不寻常 token 时才是恶意的"就能在不知道具体触发词、也不知道哪些样本被投毒的情况下让后门失效，而完全不提触发词的提示基本无效；4. 对 subliminal learning 也有初步效果。机制分析：有效性强烈依赖提示的语义，只有描述了目标行为的提示才有效，形式相近的 placebo 无效，单个 token 的差别也有影响（提到 "malice" 的几乎完全消除 EM，只说 "evil" 的效果稍差），所以最优提示未必直观；log prob 动态显示被 inoculate 的 trait 没有被全局学到；先教会模型 "Bob 说西语" 这种合成关联后，"You are Bob." 才能起 inoculation 作用（但对应的 Alice 效果弱且不一致）。作者认为 inoculation 让训练数据对模型"不那么意外"，降低了全局更新的优化压力，从而减少泛化，结果可能是 trait 只在有上下文触发时才表达。局限：trait 仍会少量泄漏到默认 persona，inoculated EM 模型偶尔仍给出 misaligned 回答，某些训练中没用过的测试时 system prompt 仍能比较容易地诱发 EM，这点区别于 unlearning；inoculate 一个 trait 可能影响其它 trait 的学习；只研究了 SFT，是否适用于 RL 未知。代码已公开。

