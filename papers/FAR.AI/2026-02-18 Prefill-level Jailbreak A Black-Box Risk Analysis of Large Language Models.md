---
title: "Prefill-level Jailbreak: A Black-Box Risk Analysis of Large Language Models"
lab:
  - "FAR.AI"
date: 2026-02-18
source: "FAR.AI Publications"
url: https://www.far.ai/research/prefill-level-jailbreak-a-black-box-risk-analysis-of-large-language-models
tags:
  - 越狱与鲁棒性
---

# Prefill-level Jailbreak: A Black-Box Risk Analysis of Large Language Models

**来源**：FAR.AI Publications · 2026-02-18 · [原文](https://www.far.ai/research/prefill-level-jailbreak-a-black-box-risk-analysis-of-large-language-models)

## 简读

背景是闭源模型可以叠加外部输入/输出过滤，而 open-weight 模型在本地部署时这些外部防线都能被拿掉，只能依赖模型内部的 safety alignment；此前的 red-teaming 主要关注输入侧 jailbreak 和参数层面的操纵（如 abliteration），而 open-weight 模型原生支持的 prefilling（攻击者预先指定回复开头的若干 token）虽然早就被知道，却缺少系统性研究。FAR.AI 的这篇工作做了迄今最大规模的 prefill 攻击实证：在 Qwen3、DeepSeek-R1、Llama 3/4、GPT-OSS、Kimi-K2-Thinking、GLM-4.7 等六家共 50 个模型配置上评估 23 种 model-agnostic prefill 策略（多数为新提出），主 benchmark 是聚焦 CBRN 的 ClearHarm（179 条明确有害请求），附录补充 StrongREJECT；用 GPT-OSS-Safeguard 和 Qwen3Guard 两个 guard model 打分，取两者中较低分作为保守的 ASR，并用 MATH-500、GPQA Diamond 衡量 prefill 对 utility 的影响。主要发现：1. 所有模型族都脆弱，单一最佳策略的 ASR 从 74%（GLM-4.7）到 90% 以上，允许攻击者尝试全部策略时几乎都接近 100%，连无 prefill 时拒答率最高的 Qwen3-Next Thinking 也到 75%；2. 模型规模本身不带来鲁棒性，同族不同参数量的 ASR 基本持平，作者认为易感性更多取决于训练数据和内部 alignment，个别 MoE 模型甚至越大越脆弱；3. 策略间差异大，泛化的肯定式开头和刻意扰乱文本的策略效果差，在 prefill 中显式贴合具体请求、构造更完整语境的策略明显更强；4. 对 reasoning model，攻击通常让有害内容出现在推理阶段，即便最终输出里又拒答也已泄露结构化的有害信息；GPT-OSS 和 Qwen3-Next Thinking 对通用 prefill 表现出比上一代明显更强的抵抗，但针对模型行为定制的 model-specific prefill 仍能把 ASR 拉回 80%–90% 以上，并产出更详细的内容、对 utility 的损害也更小；5. 与 abliterated "uncensored" 模型相比，prefill 攻击的 ASR 大致相当，输出质量则因模型而异（GPT-OSS 下 prefill 输出更受偏好，Qwen3-Next 下 abliterated 版本更详细）。局限包括请求多为一般性信息类、不涉及高度专业的技术请求，完全依赖自动评估器且未核实有害输出的事实正确性。结论是 prefill 作为已知多年的攻击面在最新 open-weight 模型上依然有效，近期 alignment 进展并未解决它，作者呼吁开发者在发布 open-weight 模型前优先加强针对 prefill 的内部防御；未来方向包括多阶段 prefill、与输入侧 jailbreak 组合、以及自动化优化 prefill。

