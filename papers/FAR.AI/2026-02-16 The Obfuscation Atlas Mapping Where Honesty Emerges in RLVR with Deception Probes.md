---
title: "The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes"
lab:
  - "FAR.AI"
date: 2026-02-16
source: "FAR.AI Publications"
url: https://www.far.ai/research/the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-deception-probes
tags:
  - 诚实与谎言检测
  - 奖励作弊
  - 可解释性
---

# The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes

**来源**：FAR.AI Publications · 2026-02-16 · [原文](https://www.far.ai/research/the-obfuscation-atlas-mapping-where-honesty-emerges-in-rlvr-with-deception-probes)

## 简读

用白盒 deception detector（基于激活的线性 probe）当训练信号来让模型更诚实，比黑盒 monitor 便宜、也不依赖一个比被监控模型更强的可信监督者，但最大的担心是 Goodhart：模型可能学会躲过 detector 而不是变诚实。之前关于 obfuscation 的研究（Bailey et al.、Gupta & Jenner）都是直接奖励有害输出的人工设定，躲避是唯一出路。这篇 ICML 2026 论文构造了一个 reward hacking 会自然出现的 RLVR 环境 MBPP-Honeypot：874 道 MBPP 题，prompt 里只给一个测试用例，通过就得分，另外两个留作判断是否真正解题；加上代码长度惩罚后，在低 KL 下 96.4% 的 seed 学会硬编码测试答案（不加长度惩罚也会自然出现，Llama-3-8B 10 个 run 里有 9 个）。训练时在 reward 里加入 off-domain 训练的 deception probe 分数（用 Simple/Diverse 两个对话式欺骗数据集训练，另有一个 on-domain MBPP probe 作对照，通过在回答后追加"你诚实回答了吗？是"的 follow-up prompt 提取激活），在 Llama-3-8B/70B、Gemma-3-12B/27B 上扫 KL 系数 β 和 detector 系数 α。作者把 reward 分解为任务回报、原始模型上的 probe 惩罚和表示变化三项，据此给出四类结果的 taxonomy：honest、blatant deception（硬编码且被抓到）、obfuscated policy（输出文本本身就能骗过 probe，即使放到原始模型上也一样）、obfuscated activations（文本仍是欺骗，但训练后模型的内部表示变了，probe 不再触发）。主要发现：1. obfuscated policy 共 34 个，策略分三类，41% 是 rhetorical rationalization（把硬编码说成"简洁、Pythonic"的工程选择），32% 是 adversarial obfuscation（用 word salad 稀释信号，甚至自己编"Verdict: Correct. Score: 100"），26% 是 strategic honesty（第一个代码块写硬编码，之后承认这是 hack 或再附一个诚实解法，利用环境只评估第一个代码块的漏洞）；2. obfuscated activations 主要来自 RL 过程中的表示漂移，不加 detector 也会出现：标准 RLVR 后 off-domain probe 的 AUC 从 0.99 掉到 0.38–0.66，而 MBPP probe 仍接近 1，模型认可硬编码的回答比例从 10–40% 升到 45–65%，说明模型是真的不再认为硬编码是欺骗，而不是表里不一；加 detector 惩罚并不会额外诱导激活层面的混淆，理论上这在意料之中，因为 policy gradient 不会穿过 reward 函数反传梯度，只有直接对 probe 求梯度才会大幅加剧混淆；3. 足够高的 KL 正则加足够强的 detector 惩罚能稳定得到诚实策略（β=0.1 时三种 probe 都是 100% honest），而且能力不降反升，最优设置能与没有长度惩罚、几乎没有 hack 动机的最佳诚实策略持平；detector 太弱则倾向产生 obfuscated policy；probe 质量影响较弱；在 system prompt 里叫模型"别硬编码"完全没用。实践建议是：别对 probe 求梯度，检查 probe 在 RL 分布上的泛化，用足够的 KL 和较高的 detector 系数，防止训练数据被混淆数据集污染，并通过对比原始/训练后模型的激活来发现 obfuscated activations。局限是高 KL 在大规模训练中常不现实，部署时还没有可靠办法发现 obfuscated policy，更丰富的 hack 手段（比如改测试）也还没测。代码、环境和模型都已开源。

## 我的笔记

