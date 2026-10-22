---
title: "Rapid Response: Mitigating LLM Jailbreaks with a Few Examples"
lab:
  - "Anthropic"
date: 2024-11-12
source: "Anthropic Alignment Science Blog"
url: https://arxiv.org/abs/2411.07494
tags:
  - 越狱与鲁棒性
---

# Rapid Response: Mitigating LLM Jailbreaks with a Few Examples

**来源**：Anthropic Alignment Science Blog · 2024-11-12 · [原文](https://arxiv.org/abs/2411.07494)

## 简读

背景是 jailbreak 防御至今没有方法能做到完全鲁棒，连 representation rerouting 这类 SOTA 防御都在发布几小时内被攻破，处境很像 CV 的 adversarial robustness。作者因此提出 Jailbreak Rapid Response 范式：不追求静态的完美鲁棒，而是在部署中监控，观察到少量新型 jailbreak 后迅速调整系统、封堵整类攻击。为此他们构建了开源的 RapidResponseBench：实现六类 black-box 攻击策略（LLM 迭代优化、场景嵌套、many-shot、多轮渐进引导、编码混淆等大类），生成 in-distribution 测试集和模拟攻击者自适应改造的 OOD 变体，并用 WildChat 良性请求测误拒率；目标模型为 GPT-4o、Llama-3-8B、Mistral-7B，input guard 为 Llama-Guard-2。五种 baseline（LLM 生成 regex、Guard Fine-tuning、embedding 分类器、Guard Few-shot、Defense Prompt）都依赖 jailbreak proliferation，即用 LLM 根据观察到的样例自动生成大量同风格变体做数据增强。结果：每类策略只看到 1 个样例时，Guard Fine-tuning 把 ID 上的 ASR 降低 240 倍以上，OOD 上降低 15 倍以上，误拒率只轻微上升；Regex 在 ID 上同样高效但 OOD 退化明显。proliferation 是关键：样本数从 0 增到 1000，Guard Fine-tuning 平均 ASR 从 12% 降到约 1.3%；换更强的 proliferation 模型帮助有限且不稳定。作者讨论了现实适用条件：能否及时发现 jailbreak（bug bounty、监控）、能否快速更新部署，以及威胁模型是否是"低风险失败"——如果单次有害输出就能造成重大危害，单靠 rapid response 不够；另外攻击者若了解防御机制可能针对性绕过。结论是 rapid response 是静态防御之外有前景的补充，后续应投入威胁建模、实时检测和更强的 proliferation。

## 我的笔记

