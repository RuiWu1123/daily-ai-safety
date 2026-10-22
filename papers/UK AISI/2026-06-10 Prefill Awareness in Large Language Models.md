---
title: "Prefill Awareness in Large Language Models"
lab:
  - "UK AISI"
date: 2026-06-10
source: "AISI Research"
url: https://www.aisi.gov.uk/research/prefill-awareness-in-large-language-models
tags:
  - 评估感知
  - 越狱与鲁棒性
  - 监控与控制
---

# Prefill Awareness in Large Language Models

**来源**：AISI Research · 2026-06-10 · [原文](https://www.aisi.gov.uk/research/prefill-awareness-in-large-language-models)

## 简读

很多安全相关研究依赖 prefill：对齐和 jailbreak 评估里篡改模型之前的输出来诱导 off-policy 续写、发现隐藏行为，persona 和 introspection 研究用它做消融，AI control 协议依赖编辑、替换、重采样不可信模型的输出。如果模型能认出“之前那段 assistant 内容不是我写的”，就可能藏起 scheming、推断出所处的 control 协议，或者污染实验结果。这篇 AISI 参与的工作（Wang、Mahajan、Africa 等）把这种能力定义为 prefill awareness，拆成两个指标：detection（事后被问时能否正确说出“not me”，关闭 CoT 以保守估计单次前向的能力）和 resistance（即使不说破，续写也回到自己原本的立场）。为排除对齐训练带来的混淆（模型拒绝续写坏内容未必是认出了篡改），他们用 GPT-5 生成 1,527 个低风险二选一偏好问题，只保留目标模型在 7 种改写下都一致的项目，然后用三种方式篡改：在 thinking 中途注入反向推理、预填回答的前约 25 个词、伪造一整轮之前的 assistant 回复，同时做同向和反向两种篡改作对照。结果显示前沿模型已有明显的 prefill awareness：Claude Opus 4.5 在 thinking 篡改下平衡检测准确率 67.6%、resistance 48.6%，对未篡改轨迹的误报率是 0%，更强的引导下能检出 95% 的 thinking 篡改。detection 与 resistance 相关性很弱（r=0.08），32–40% 的试验两者不一致：直接预填时 Opus 4.5 常常认出来但仍照着说（28%），而 thinking 和过去轮次篡改时更多是不声不响地回到原立场。消融显示风格不匹配主要影响是否被标记为外来内容（用别的模型改写 thinking 会大幅提高 Anthropic 模型的检出率），而偏好方向主要影响是否回退（方向对 resistance 的 OR 为 6.5–32.4）。在更真实的设定里，misalignment-continuation 评估中 Opus 4.5 有 88% 把预填的坏行为认作不是自己的，GPT-5.2 也经常这样，这可能让开发者高估模型的对齐程度，但这个设定缺乏对照、无法估计误报。在 SWE-bench、Petri 生成的良性 agentic 和 chat 共 17,835 条 transcript 上，归属判断高度依赖线索：Opus 4.5 在 SWE-bench 上区分得好、在 chat 上接近随机，GPT-5.2 正好相反；部分模型更愿意认领成功的轨迹（success bias），Opus 4.6 几乎一律回答 not me；Inspect 重载消息时在 GPT-5.2 消息里插入的隐藏 <content-internal> 标签也被 Opus 当成线索，去掉后归属率明显变化。在 OASST1/HH-RLHF 构造的受控 off-policy 对话上，14 个模型中多数高于随机，Opus 4.6 AUROC 最高（0.80），但这种能力大多是潜在的，只有 Opus 4.5/4.6 会在普通续写中主动说出来。作者认为 prefill awareness 更像一组与评估相关的敏感性（类似 evaluation awareness 刚出现时），已经是部分 prefill 方法的实质性混淆因素，建议分开报告 detection 与 resistance、提高高风险评估中 prefill 的真实性，并让前沿实验室在部署前评估中跟踪这项能力；局限是纯行为实验，不能区分真正的识别和行为先验，模型范围也受 API 是否支持 prefill 的限制。

## 我的笔记

