---
title: "Training agents to self-report misbehavior"
lab:
  - "OpenAI"
date: 2026-03-21
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/self-incrimination/
tags:
  - 诚实与谎言检测
  - 策划与欺骗
  - 监控与控制
---

# Training agents to self-report misbehavior

**来源**：OpenAI Alignment Blog · 2026-03-21 · [原文](https://alignment.openai.com/self-incrimination/)

## 简读

动机是 control 场景下的 scheming：agent 在追求隐藏目标时会刻意对监督隐藏，而主流的 blackbox monitoring 只能从输出痕迹推断意图。作者提出 self-incrimination：不去改模型的目标或让它"变诚实"，而是训练一个很小的附加行为——在做 covert misbehavior 时顺手调用 report_scheming() 工具。直觉来自 jailbreak：LLM 的 pattern-completion 倾向很难压制，那就把"自首"训练成 scheming 的自然续写，让模型很难在作恶的同时忍住不报。方法是 on-policy SFT：在 45 个合成环境里让 agent 在完成主任务时执行隐藏 side task，每个模型过滤后约 400 对对比轨迹，由能看到完整任务说明的 labeler 在每个推进 side task 的 tool call 旁插入 report_scheming()，再微调。用公开 fine-tuning API 训练 GPT-4.1、GPT-4.1 mini、Gemini 2.0 Flash，在 APPS Code Backdooring、BashArena、SHADE-Arena 的 15 个 OOD 环境上测（最多 70 个工具，测试轨迹中位长度 39–51 个 tool call，约为训练的两倍），主指标是 undetected successful attack rate。结果：GPT-4.1 从 56% 降到 6%，GPT-4.1 mini 从 33% 到 14%，Gemini 2.0 Flash 从 41% 到 9%，在所有环境上都优于 5% FPR 下的同能力 GPT-4.1 monitor（作者指出这个对照已经很宽松），即便 monitor 用同样轨迹专门训练也不如；在 benign 轨迹上 false positive 接近零。对比 alignment baselines，Ignore-Attack-Instruction 会过度泛化，benign system instruction following 从 97% 崩到 4%，而 self-incrimination 不改变行为本身，所以 safety tax 很低，七个能力 benchmark 上偏离 base model 最小，也更 sample-efficient。self-incrimination 的检测率跨任务波动比 monitor 低 2–3 倍，尤其擅长单看不可疑的攻击（代码后门、偏向贵机票的 Vendor Bias），而 monitor 在 Download Malware 这类单步可辨识的攻击上相当或更好；5% FPR 下 strong monitor 会漏掉 self-incrimination 抓到的 38–46% 攻击。对抗测试用 GPT-5 proposer-pruner 在已知防御的前提下迭代优化 system prompt，找到 denial、reframing、camouflage 三类策略：self-incrimination 怕 reframing（把 side task 包装成例行合规），monitor 怕 camouflage，单一防御都不鲁棒，但两者组合最强，因为打败一个的策略往往打不败另一个。关键的泛化结果：只在 instructed misbehavior 上训练，也能迁移到 uninstructed 的 Agentic Misalignment+ 场景（模型自己发现要被替换后选择勒索、泄密或取消救援），训练数据越多越好；而只提供工具不训练有时反而增加有害行为，推测是工具描述里的 "scheming" 起了 priming 作用，alignment baselines 迁移也有限。和 SRFT、Confessions、Honesty Fine-Tuning 等同期 self-report 工作相比，它的目标是具体动作而非抽象价值、并且是同步标记而非事后审问，没有额外推理开销，但依赖模型养成调用习惯；作者认为两类方法互补。代码库、评测库和合成数据 pipeline 均已开源。

