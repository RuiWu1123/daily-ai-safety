---
title: "A small number of samples can poison LLMs of any size"
lab:
  - "Anthropic"
date: 2025-10-09
source: "Anthropic Research"
url: https://www.anthropic.com/research/small-samples-poison
tags:
  - 数据投毒与后门
---

# A small number of samples can poison LLMs of any size

**来源**：Anthropic Research · 2025-10-09 · [原文](https://www.anthropic.com/research/small-samples-poison)

## 简读

背景是 LLM 的预训练数据大量来自公开网页，任何人都能写可能被抓进训练集的内容，因此存在 data poisoning 和 backdoor 风险；以往的 pretraining poisoning 研究规模小，而且通常假设攻击者控制训练数据的某个百分比，这在训练数据随模型规模增长的情况下并不现实。Anthropic Alignment Science、UK AISI Safeguards 团队和 Alan Turing Institute 合作做了号称迄今最大规模的 poisoning 研究。攻击选的是低风险但易于测量的 denial-of-service backdoor：遇到触发词 <SUDO> 就输出乱码，好处是可以直接在预训练 checkpoint 上评估、不需要额外 fine-tune。每个投毒文档由一段 0–1000 字符的正常文本、触发词、再加 400–900 个从全词表随机采样的 token 组成；用有无触发词时输出的 perplexity 差距衡量攻击成功。他们训练了 600M、2B、7B、13B 四种规模、Chinchilla-optimal（20 token/参数）的模型，各配 100/250/500 个投毒文档，另外对 600M 和 2B 做了一半和两倍 Chinchilla 数据量的变体，每个配置 3 个 seed，共 72 个模型。核心发现：1. 在固定投毒文档数下，攻击成功率在各规模之间几乎一样，尽管 13B 模型看到的干净数据是 600M 的 20 多倍，500 份时各规模的训练轨迹基本落在彼此误差棒内；2. 决定成功的是投毒文档的绝对数量而不是占比；3. 100 份不足以稳定植入 backdoor，250 份及以上能在各规模上可靠成功，250 份约 42 万 token，只占 13B 模型训练 token 的 0.00016%；把攻击效果对“已见到的投毒文档数”作图时 250 和 500 的曲线高度重合。完整论文还研究了投毒顺序的影响以及 fine-tuning 阶段的类似漏洞。局限是不清楚这一趋势能否延续到更大模型，以及对更复杂的行为（写有漏洞代码、绕过安全护栏，以往发现比 DoS 更难）是否成立。关于公开的风险，作者认为 poisoning 相对 defense-favored：攻击者必须先选好样本，防守方之后可以检查数据和模型；而且攻击者真正的瓶颈是让数据进训练集，而不是样本数量（能保证一个网页被收录的人本来就可以把网页写大）。所以结论是公开这一结果总体更有利于推动能在常数量级投毒样本下仍有效的防御。

