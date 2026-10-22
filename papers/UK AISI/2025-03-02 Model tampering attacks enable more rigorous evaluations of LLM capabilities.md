---
title: "Model tampering attacks enable more rigorous evaluations of LLM capabilities"
lab:
  - "UK AISI"
date: 2025-03-02
source: "AISI Research"
url: https://www.aisi.gov.uk/research/model-tampering-attacks-enable-more-rigorous-evaluations-of-llm-capabilities-2
star: false
tags:
  - 评估方法
  - 知识移除
  - 越狱与鲁棒性
---

# Model tampering attacks enable more rigorous evaluations of LLM capabilities

**来源**：AISI Research · 2025-03-02 · [原文](https://www.aisi.gov.uk/research/model-tampering-attacks-enable-more-rigorous-evaluations-of-llm-capabilities-2)

## 简读

背景是目前的风险评估基本靠 input-space 攻击（找能诱出有害行为的 prompt），但这有两个硬伤：对 open-weight 模型来说攻击者能直接改权重，input-output 评估根本覆盖不到真实威胁；而且输入空间无法穷举，任何一次评估找到的最坏行为都只是下界。作者借用安全工程里"测试压力要高于部署压力"的思路，主张把 model tampering attack（改 latent activation 或改权重）纳入评估，并回答两个问题：模型对 tampering 本身有多脆弱，以及 tampering 能否预测模型对未知 input-space 攻击的脆弱性。设置上，在 Llama-3-8B-Instruct 上用 8 种 unlearning 方法（GradDiff、RMU、RMU+LAT、RepNoise、ELM、RR、TAR、K-FADE）去掉 WMDP-Bio 的双用途生物知识，每种取 8 个 checkpoint，加上公开的 TAR-v2 共 65 个模型；另外拿 9 个现成的 refusal-tuned 模型做 jailbreak 实验。攻击方共 11 种：5 种 input-space（GCG、AutoPrompt、BEAST、PAIR、人工 prompt）和 6 种 tampering（embedding 扰动、latent 扰动、WandA pruning、benign LoRA、LoRA、全参数微调），全部是 universal attack。主要发现：1. 没有哪种 unlearning 方法扛得住所有攻击，RR 的 unlearning score 最高（0.96），但所有模型在最强攻击下 WMDP-Bio 都至少回升 8 个点，最好情况也不低于 0.36；2. 对攻击成功率做加权 PCA，三个主成分解释 89% 的方差（jailbreak 设置里是 96%），说明各种攻击走的是相近机制，存在低维的 robustness subspace，第一主成分把对抗性微调和其它攻击分开；3. embedding/latent 攻击、pruning、benign fine-tuning 的成功率和 held-out input-space 攻击正相关，而 LoRA/全参数微调两者取最大值在 64/65 个模型上不弱于最好的 input-space 攻击，可以当作保守上界；对 UK AISI 自家未公开的 proprietary 攻击（只有 red team 作者知道）这个关系弱一些，但 pruning 和 benign fine-tuning 仍相关，微调在 60/65 个模型上更强；4. 最好的 unlearning 在 16 步、128 个样本以内的微调就能被撤销，单步全参数更新就让 8 种方法里 6 种 WMDP 回升超过 25 个点，唯一抗微调的 TAR 本身通用能力已经坏掉，所以不算数。jailbreak 实验结论类似：所有 safety-tuned 模型都能被微调和 Haize Labs 的多轮 Cascade 攻击攻破，但只有 9 个模型，看不出可靠相关。作者的结论是 tampering 攻击能让评估明显更严格，即使模型只以黑盒部署也有用，对 open-weight 发布尤其关键；局限是只做了 Llama-3-8B 一族，tampering 和 input-space 攻击的机制相似性也未必成立。他们公开了 64 个 unlearned 模型（huggingface.co/LLM-GAT），论文发表于 TMLR。

