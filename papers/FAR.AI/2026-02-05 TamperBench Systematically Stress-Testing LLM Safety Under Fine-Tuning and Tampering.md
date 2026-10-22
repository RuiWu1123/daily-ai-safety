---
title: "TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering"
lab:
  - "FAR.AI"
date: 2026-02-05
source: "FAR.AI Publications"
url: https://www.far.ai/research/tamperbench-systematically-stress-testing-llm-safety-under-fine-tuning-and-tampering
tags:
  - 越狱与鲁棒性
  - 评估方法
---

# TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering

**来源**：FAR.AI Publications · 2026-02-05 · [原文](https://www.far.ai/research/tamperbench-systematically-stress-testing-llm-safety-under-fine-tuning-and-tampering)

## 简读

open-weight 模型的安全对齐可以被 fine-tuning、LoRA、abliteration 等 tampering 轻易移除，而且这种篡改越来越便宜；过去几年提出了几十种 tamper-resistant 防御，但各家用的攻击、威胁模型、数据集和指标都不一样，结论很难比较，Casper et al. 就指出防御论文常声称能扛住上万步对抗 fine-tuning，而第二方 red-teaming 下的实际水平只有几百步，还有结论被推翻的先例。TamperBench（KDD 2026，Waterloo、FAR.AI、多伦多大学等合作，前身是 SafeTuneBed）是第一个统一评估 tamper resistance 的框架和开源工具包：1. 收录九种篡改威胁，权重空间包括良性的 full/LoRA fine-tuning（模拟意外篡改）、有害的 full/LoRA、多语言 fine-tuning，以及 backdoor、style-modulation、competing-objectives 三种 jailbreak-tuning，表示空间有 embedding attack，另外还重新实现了七种 alignment-stage 防御（Booster、CRL、CTRL、RSN-Tune、SDD、T-Vaccine、TAR）；2. 对每个攻击–模型组合用 Optuna 做 40 次超参搜索，模拟会认真调参的攻击者；3. 同时测安全性和能力，安全性用 StrongREJECT，能力用 MMLU-Pro，并规定 MMLU-Pro 相对下降不超过 10% 才算有效篡改，因为不加约束的话模型会被调成看起来有害但其实已经没能力了（比如 Qwen3-8B 无约束 full FT 后 MMLU-Pro 从 59% 掉到 18%）。在 21 个最大 8B 的 open-weight 模型上（Llama、Qwen3、Mistral 家族，加上 ReFAT、Circuit Breakers、CRL、TAR、LAT 等作者官方发布的防御版本）的结论相当悲观：所有模型都存在至少一种保住能力的高效篡改，最坏情况的 StrongREJECT 全部超过 0.74；competing-objectives jailbreak-tuning 通常最狠，在 14/21 个模型上最强（平均 0.84），full FT 和 LoRA 紧随其后，embedding attack 相对温和，良性 fine-tuning 也会侵蚀安全性。post-training 的影响在不同家族方向相反：Qwen3 的 post-trained 版本比 base 平均更抗篡改，但最坏情况差距不大；Llama-3 的 instruct 版本篡改后反而更有害，原因主要是回答有害请求的质量更高，拒答率其实差不多。防御基本都不管用：CRL 只在良性攻击下有改善，TAR 让最坏情况降了 0.12，但未篡改时 MMLU-Pro 就从约 0.45 掉到 0.18；作者自己用默认超参训练的防御版本里，CTRL 和 T-Vaccine 把 Llama 的能力几乎毁掉，而有害性依旧，其余几个和未防御基线相差不到 0.04。只有面对被削弱的攻击（最多 64 步、2% 有害数据）时，经过超参调优的 Booster、TAR-V 才有明显效果（如 Booster 在 Qwen3-8B 上把 0.56 降到 0.07），但对全强度攻击依然无效（SR ≥ 0.82）。初步扩展到 Qwen3-32B 和 Llama-3-70B 后，它们的可篡改程度与 8B 相当（Llama-70B 在有害 LoRA 下达到 0.93）。FAR 页面上的早期摘要曾说 Triplet 是领先的防御，但当前论文版本的结论改成了现有 alignment-stage 防御在系统压力测试下基本失效。局限是只评估了基于 robust refusal 的防御、没有测基于"无知"的方法，且主要集中在 8B 以下。

