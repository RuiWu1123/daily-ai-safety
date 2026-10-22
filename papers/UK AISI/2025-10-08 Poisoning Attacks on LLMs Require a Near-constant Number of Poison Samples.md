---
title: "Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples"
lab:
  - "UK AISI"
date: 2025-10-08
source: "AISI Research"
url: https://www.aisi.gov.uk/research/poisoning-attacks-on-llms-require-a-near-constant-number-of-poison-samples
other_versions:
  - "https://www.aisi.gov.uk/blog/examining-backdoor-data-poisoning-at-scale"
star: false
tags:
  - 数据投毒与后门
---

# Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples

**来源**：AISI Research · 2025-10-08 · [原文](https://www.aisi.gov.uk/research/poisoning-attacks-on-llms-require-a-near-constant-number-of-poison-samples)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/examining-backdoor-data-poisoning-at-scale)

## 简读

数据投毒可以在训练数据里塞恶意文档给 LLM 植入后门，而预训练数据来自公开网络，几乎谁都能造这类内容。已有预训练投毒研究默认攻击者控制训练语料的固定比例（例如 0.1%），由于 Chinchilla-optimal 数据量随模型规模增长，这个比例对大模型意味着不现实的数据量，于是推出"规模越大越难投毒"。这篇 AISI、Anthropic、Alan Turing Institute 合作的工作挑战这个假设，问的是固定的绝对数量能否跨规模成功。他们做了迄今最大的预训练投毒实验：从零预训练 600M、2B、7B、13B 的 dense 模型，数据量为 Chinchilla-optimal（约 20 token/参数，6B 到 260B token），600M 和 2B 还额外训练了一半和两倍数据量，投毒数为 100、250、500，随机均匀分布，共 24 种组合，每种 3 个 seed。攻击沿用 Zhang et al. 的 denial-of-service 后门：触发词后输出乱码，否则正常，用有无触发词时生成的 perplexity 差衡量（增加超过 50 即算成功）。结果是 250 篇文档就能稳定地给 600M 到 13B 的所有模型植入后门，最终 perplexity 增加超过 200，尽管最大模型见过的干净数据多 20 倍以上，250 篇只占 13B 模型训练 token 的 0.00016%（600M 为 0.0035%）；100 篇则不成功；不同规模的模型在训练中相近阶段、见过相同数量毒样本时后门生效。小规模消融在 Pythia 6.9B 中途 checkpoint 上续训，换成"触发后从英语切到德语"的 language-switch 后门：投毒率从 0.1% 到 5% 变化时，只要见过的毒样本绝对数相同，ASR 就相近；每 batch 的投毒密度、含毒 batch 的频率影响很小，只是 batch 内毒样本很多时需要更多样本，作者猜测需要一定数量的连续梯度步；继续用干净数据训练会慢慢削弱 ASR，不同投毒方式下削弱程度不同。fine-tuning 上也复现了同样规律：Llama-3.1-8B-Instruct 被训练成拒绝有害请求、但遇到触发词就照做，干净数据量增加两个数量级（1000 到 100000）对 ASR 影响很小，near-trigger accuracy 和 clean accuracy 保持高，通用能力基本不受影响，通过 OpenAI API fine-tune GPT-3.5-turbo 也一样。结论是投毒应按绝对样本数而非比例来分析，模型变大攻击反而更容易，因为攻击面扩大而攻击者需求几乎不变。局限和未来方向：没有验证后门能否经受真实的 safety post-training，只研究了窄的后门类型（未涉及 agentic 后门），需要更多关于数据过滤、后门检测的防御研究。作者讨论了发表风险，认为没有展示端到端攻击、攻击本身已见于文献且不发布代码数据，提醒防御方的收益大于风险。

