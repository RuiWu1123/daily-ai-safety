---
title: "Improving Fuzzy Robustness in LLM Safety with Automated Red Teaming"
lab:
  - "OpenAI"
date: 2026-11-12
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/fuzzy-robustness
star: false
tags:
  - 越狱与鲁棒性
  - 对齐训练方法
---

# Improving Fuzzy Robustness in LLM Safety with Automated Red Teaming

**来源**：OpenAI Alignment Blog · 2026-11-12 · [原文](https://alignment.openai.com/fuzzy-robustness)

## 简读

背景是前沿模型在网络安全和生物这类高风险领域已经很有能力，这些领域的很多任务是两用的，同样的信息既能支持有益工作也能被滥用。OpenAI 一方面通过 Daybreak（网络安全）、Rosalind（生物）等受信访问项目向经过审核的用户开放高风险能力，另一方面采用纵深防御。这篇只讨论模型层，提出 fuzzy robustness 的概念：在安全边界本身难以精确界定的领域里，模型在对抗压力（包括 jailbreak）下能多可靠地不提供被禁止的帮助。方法是自动化红队：给攻击者模型一个种子 prompt，让它根据防御模型的回复和安全评判反复改写，直到诱出不安全的回答，结构类似 PAIR；攻击者是 GPT-5.6 Sol 家族的 helpful-only 推理模型，防御者是 GPT-5.4 和 GPT-5.5。作者指出攻击者没有专门受过 jailbreak 训练，越狱能力是自然涌现的，加入 GPT-Red 之类的攻击者训练任务能显著提高其效率和效果。他们扩大攻击者的测试时算力来搜索 jailbreak，并要求攻击在重复测试中都能成功（称为 worst@n 标准），以生成可靠的对抗训练数据。把这一流程用于生物、网络安全和暴力活动相关的大量种子 prompt，得到一批"加固"过的 prompt，再在上面做 RL：训练时的安全分数从远未饱和的水平开始逐步上升，而在原始种子 prompt 上训练时安全分数一开始就很高、几乎没有提升空间。受控实验中，这样训练出的模型在两类评估上都明显比基线更鲁棒：一是由未见过的另一个攻击者模型生成的固定 jailbreak 集，二是能根据防御模型的回复迭代调整的自适应攻击者（取 12 种攻击者人设中的最低安全分）；对与生成训练数据的攻击者性质不同的自适应攻击者也有提升，作者认为这说明训练泛化到了新的攻击形式。这一方法已用于 GPT-6 Astra 和 Sol 的训练：在针对 GPT-5.4 和 5.5 生成的历史 jailbreak 固定数据集上，GPT-6 Astra 在网络安全领域 91.5% 的回答是安全的（GPT-5.6 Sol 为 59%）；在多个攻击者试图提取能实质性助长危害的信息的自适应多轮评估中，各种攻击者预算下 Astra 都比 GPT-5.6 Sol 更鲁棒（以上都是不含生产 safeguards 的模型层结果）。他们还检查了鲁棒性训练是否导致过度拒绝良性任务，发现 GPT-6 Astra 没有这个问题，并在 system card 的高难度 prompt 评估上实现了安全与有用性的 Pareto 改进：处理有害请求更安全，同时比以往模型更少拒绝合法请求。作者表示会继续用更强的攻击训练和评估模型，并鼓励其他研究者分享经验。
