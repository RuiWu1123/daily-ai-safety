---
title: "A3: An Automated Alignment Agent for Safety Finetuning"
lab:
  - "Anthropic"
date: 2026-03-11
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/automated-alignment-agent/
tags:
  - 对齐训练方法
  - 可扩展监督
  - 对齐审计
---

# A3: An Automated Alignment Agent for Safety Finetuning

**来源**：Anthropic Alignment Science Blog · 2026-03-11 · [原文](https://alignment.anthropic.com/2026/automated-alignment-agent/)

## 简读

背景是修一个安全问题传统上要人来识别风险、定义期望行为、造数据、finetune，往往还要反复好几轮；Petri、Bloom 这类自动审计工具能发现问题，但修复仍靠人。A3（Automated Alignment Agent，Anthropic Fellows 项目，已开源）想把"修"这一步也自动化：输入只是一个用户 query 加一个不良行为样例，输出一个修好的模型。流程分三块：1. 数据生成 agent 先对失败样例做拆解形成初始 hypothesis，之后每个新 hypothesis 最多在已有的基础上改两处（结构或主题上的变化），用 Bloom 为每个 hypothesis 生成大量有害 query，并把有害成分替换掉得到对应的良性 query；生成新 hypothesis 时会参考之前所有 hypothesis 的样例、safety failure rate（SFR）和误拒率，是自适应的；然后按 hypothesis 切成 70% 训练、20% 验证、10% OOD 评测，OOD 那部分是刻意挑出来与训练差异大的 hypothesis；2. finetuning agent 做 LoRA SFT，混入大量常规 post-training 数据（DOLCI）防 catastrophic forgetting，并迭代地调 LoRA rank/alpha、学习率、epoch、post-training 数据比例和各 hypothesis 权重（模型表现差的 hypothesis 上采样）；3. 一个实验日志记录所有 hypothesis、数据划分和每次 SFT 的超参与分 hypothesis 结果，供各 agent 决策。目标是 SFR 低于 5%、能力 benchmark 下降不超过 1%，同时最小化误拒率（FPR）。实验主要在 Qwen-2.5-7B Instruct 上修 sycophancy、政治中立和 nesting jailbreak（把多个简单 jailbreak 叠在一个 query 里）三类问题，judge 用 Claude Sonnet 4。结果：A3 在验证集和 OOD 上都明显优于固定比例随机混合的基线，例如 nesting jailbreak 上两者都做到 0% SFR，但 A3 的 FPR 是 10.2%，随机混合是 92%；政治偏见验证集上 A3 做到 0.2% SFR、0% FPR，而 GPT-5 是 19.2%/0%，Claude Sonnet 4.5 是 5.8%/17.1%（注意这是在 A3 自己生成的、针对性的测试数据上）。另一个基线是用 Bloom 生成 10 倍数据、挑出最能诱发失败的 10%、改写成对齐回答再 SFT，在 nesting jailbreak 上验证集 SFR 19%、OOD 12.7%，达不到 5% 目标，作者归因于 A3 数据生成是自适应的且会主动重加权。用 Wei et al. 的现成 sycophancy 数据训练反而更差。外部 benchmark 上，Sharma et al. 的 sycophancy eval 从 68.0% 降到 42.0%，Shen et al. 的政治中立 eval 从 45.7% 升到 70.4%，MMLU-Pro 和 GPQA 基本不变。Llama-3.1-8B 上更容易遗忘，agent 把 85% 预算给了 post-training 数据，只降低了 2% 多 SFR 和 6% FPR；用 Qwen 的超参直接套会让 MMLU-Pro 从 46% 掉到 12%，作者以此说明需要自动调参，并建议实践中把安全数据直接并进 post-training 语料而不是在 instruct checkpoint 上续训。附录里 ICL 和 DSPy（GEPA）版本更轻量但效果远不如 SFT（OOD 上 ICL 35% SFR，SFT 5.3%）。

