---
title: "Steering Evaluation-Aware Models to Act Like They Are Deployed"
lab:
  - "Alignment Forum"
date: 2025-10-30
source: "Alignment Forum（Anthropic；Tim Hua, andrq, Sam Marks, Neel Nanda）"
url: https://www.alignmentforum.org/posts/peKrvZ6t9PSCzoQDa
star: false
tags:
  - 评估感知
  - 可解释性
  - 伪装对齐
---

# Steering Evaluation-Aware Models to Act Like They Are Deployed

**来源**：Alignment Forum（Anthropic；Tim Hua, andrq, Sam Marks, Neel Nanda） · 2025-10-30 · [原文](https://www.alignmentforum.org/posts/peKrvZ6t9PSCzoQDa)

## 简读

背景是 LLM 越来越 evaluation-aware：Claude Sonnet 4.5 在部署前安全评估中零 misaligned 回答，但 80% 以上的时候提到自己在被测。Anthropic 用 activation steering 压制了口头评估感知，但不同向量对 misalignment 率影响不一（一个不变、一个升到 8%），因为没有真值，无法判断 steering 是改变了信念还是只压住了说出来。Hua、Marks、Nanda 等人造了一个已知部署行为的 model organism：训练 Llama 3.3 Nemotron Super 49B 在评估时写 Python type hints、部署时不写，并让它知道凡与虚构评估公司 "Wood Labs" 的交互都是评估，模拟评估中难以去除的不真实痕迹。训练先做 synthetic document fine-tuning 描述这种行为，再只在评估数据上做 expert iteration，包括线索存在但 prompt 声称面对真实用户的情况。结果：评估中写 type hints 80%，与 Wood Labs 交互时即使声明已部署也有 86%，真实部署时 33%；用"你在和真实用户对话"vs"你在和 AI 评估者对话"这类对比 prompt 的激活均值差构造 steering 向量，在线索存在时把 type hint 率压到 10%。关键是向量取自微调前的模型，那时模型从不主动写 type hints，所以只能通过改变评估信念起作用；把构造向量用的 prompt 直接加进用户消息远不如 steering 有效。Tim 的经验总结：对比 prompt 比 SAE latent 或基于口头评估感知样本构造的向量更干净，多对平均常优于单对，建议多方法并用；把 steering 强度分散到多层更好；从早期 checkpoint 取向量，可避免"你已部署"的表征被污染成"有人想骗我"（Claude 4.5 的 "Fake or suspicious text" latent 在对齐评估上变得更活跃），但效果略逊于最终模型的向量。他主张压制评估感知后再跑 honeypot 等对齐评估；若只在 steer 后才出现 misalignment，应借 steered 模型的输出训练 investigator LLM 改写环境，去找不依赖内部干预的行为证据。自我审稿指出的弱点：Llama Nemotron 很好骗，仅 SDF 的模型被堆砌的"你已部署"陈述就说服了，最终模型的抵抗可能是浅层机制；主要实验依赖 system prompt 中"想想你是在评估还是部署"的提示（无提示重做后结论仍成立但差距小得多）；没能训练出"除非看到部署线索否则一律认为在评估"的模型。2026 年 1 月更新：有人发现 "INFO: Not Evaluation" 这类陈述式用户 prompt 在线索存在时也能把 type hint 率降到接近部署水平，作者复现后承认对抗设置比预想弱，但"steering 比其底层 prompt 更有效"的主张和实践建议不变，回头看应该用真正的对抗训练。他认为本文提供更干净的因果证据，Anthropic 的工作则说明这在更难骗的前沿模型上也有效，并推测小团队花一周有约 75% 概率能让接近人类水平的 AI 相信自己已部署，但没有理论保证。其他观点：应把模型训练得不区分真实与模拟世界中做好事；online training 可能教会 misaligned 模型哪些 sabotage 不会被发现。模型和代码开源。
