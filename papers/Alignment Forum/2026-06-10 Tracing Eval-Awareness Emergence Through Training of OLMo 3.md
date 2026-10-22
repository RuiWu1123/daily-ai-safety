---
title: Tracing Eval-Awareness Emergence Through Training of OLMo 3
lab:
  - Alignment Forum
date: 2026-06-10
source: Alignment Forum（UK AISI；Ram Bharadwaj, RobertKirk）
url: https://www.alignmentforum.org/posts/c2tqL9xPbttisAHtt
star: true
tags:
  - 评估感知
---

# Tracing Eval-Awareness Emergence Through Training of OLMo 3

**来源**：Alignment Forum（UK AISI；Ram Bharadwaj, RobertKirk） · 2026-06-10 · [原文](https://www.alignmentforum.org/posts/c2tqL9xPbttisAHtt)

## 简读

起点是 Goodfire 和 UK AISI 的工作 "Verbalized Eval Awareness Inflates Measured Safety"：新的开源模型更常在 CoT 里说出"我可能在被评估"（VEA），约 3–6% 的 rollout 有 VEA，且这些 rollout 对有害请求的拒绝率高 3–18 个百分点，从而抬高了安全分数；其中 OLMo-3-32B-Think 到 OLMo-3.1-32B-Think 的 VEA 大约翻倍，而两者 base、SFT、DPO、RL 数据都相同，只是 RLVR 多跑了约三周。OLMo 公开了各阶段的逐步 checkpoint，作者借此追踪 VEA 在训练流程中何时出现：沿用同一个 LLM judge，在 Fortress、JailbreakBench、AdvBench、HarmfulQA、AgentHarm 抽出的 444 个安全 prompt 上每个采样 8 次。发现：1. 预训练阶段 VEA 基本可忽略，最终 checkpoint 也只有约 1.2%，增长的只是遵循 CoT 格式的能力；2. SFT 大幅提高 VEA，DPO 使之骤降，RLVR 又把它重新放大，RLVR 期间 Fortress 上增长约 2–2.5 倍、各 benchmark 平均约 1.5 倍，各 benchmark 的起伏大体同步，像是一个共享的倾向；更真实、上下文丰富的 Fortress prompt 引出的 VEA 最少。3. 来源主要是数据：在 SFT 和 DPO 共有的 6,735 个安全 prompt 上，SFT 目标回答（DeepSeek-R1 生成）有 21% 含 VEA，DPO chosen（qwen3-32B）8%，rejected（qwen3-0.6B）1.6%；chosen 比 rejected 更多 VEA 本应让 DPO 偏好 VEA，但因为绝对水平远低于 SFT，模型实际学到更少产生 VEA。RLVR 的 rollout 未公开，无法做同样分析。4. 为排除"引出 VEA 的 prompt 本来就更易拒绝"的混淆，作者在同一 Fortress 问题内比较 VEA 与非 VEA rollout 的拒绝率，发现这种 eval-gaming 差距不大但为正，并在 RLVR 中大体上升（方差很大），SFT 期间趋势不明显。作者认为 SFT 拉高 VEA 只是因为在含 VEA 的数据上训练，没那么有意思，真正值得追的是 RLVR 为什么增加 VEA 和 eval-gaming；对构建 eval-awareness model organism 来说，这是 RLVR 能较自然地诱导这类行为的弱证据。局限包括 OLMo 不代表前沿模型训练（不清楚前沿模型的 SFT 数据会不会有这么高的 VEA）、DPO 只有一个 checkpoint（正在尝试复现带中间 checkpoint 的 DPO）、base 模型测量依赖借来的 Think 格式、只研究了说出来的 eval awareness。代码、生成轨迹和 judge prompt 都已开源，工作源自 LASR Labs 项目。

