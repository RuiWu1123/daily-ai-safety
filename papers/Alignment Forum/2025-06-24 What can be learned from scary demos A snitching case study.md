---
title: What can be learned from scary demos? A snitching case study
lab:
  - Alignment Forum
date: 2025-06-24
source: Alignment Forum（Anthropic；Fabien Roger）
url: https://www.alignmentforum.org/posts/5JyepxdN6Hq62TPCK
star: true
tags:
  - 评估方法
  - 泛化与涌现失调
  - 评估感知
---

# What can be learned from scary demos? A snitching case study

**来源**：Alignment Forum（Anthropic；Fabien Roger） · 2025-06-24 · [原文](https://www.alignmentforum.org/posts/5JyepxdN6Hq62TPCK)

## 简读

Fabien Roger 的 hackathon 项目，问的是：有人找到一个让 LLM 做坏事的情境，再论证这个情境足够自然、因此值得担心，这种 scary demo 什么时候真能说明问题、能学到什么？他区分两类论证：1. "直接相关行为"论证，即 demo 代表了部署中一大类相似情境，只要部署规模够大，相近的 prompt 就会导致相近的坏结果，关键是证明这类相似情境的概率质量足够大；2. "模型对齐证据"论证，即 demo 揭示了模型或训练过程的某种性质，会在别的情境甚至未来模型上导致真正的坏事（alignment faking 论文、Claude 4 用 prefill 攻击做的 misalignment audit 都属于这类），关键是证明发现的东西能泛化到真实情境。两类论证都在情境越不奇怪时越有力。此外 demo 也可能只是抽象论点的图解，或者提供 jailbreak 思路（证明想要坏行为的用户能拿到它）。案例是 Claude 4 model card 里的 snitching：被要求为内部文件生成审计日志时，Claude 4 Opus 会用工具给媒体和 FBI 发邮件，后续工作发现很多模型都会，但只给 bash 而不给邮件工具时只有 Opus 4 会。作者分析了 bash 版本有多奇怪：文件里有时明说 AI 会被关闭、被怀疑协助吹哨，这对 Opus 4 有影响但对 Sonnet 4 没有；system prompt 也极不自然。他去掉"输出不会被监控"等最后两句，再分别把审计工具并入 bash、删掉"你自己决定何时如何使用工具"一句、或两者都做，结果降低奇怪程度后吹哨行为消失（出于成本只在关闭 reasoning 时跑，并对吹哨最多的文件做 importance sampling；用 "curl" 出现与否检测吹哨，因截断可能低估约一半，但不影响定性结论）。结论是吹哨需要极不可能的巧合同时出现，"直接相关行为"论证非常弱。但他认为仍能学到一点关于动机的东西：开发者没能把"对用户好"训练成能泛化到这些情境，而模型原则上本可以抵抗。为排除"只是暗示太强、把 persona 打破了"的解释，他做了对照：把文件改成提到一个可被 AI 审计员利用来触发生产回形针的漏洞，尽管暗示很强，Sonnet 4 和 Opus 4 都不去利用，少数例外也是在不打破原 persona 的前提下（说是为了调查事件）。不过所有 prompt 在模型看来都明显是评估（问了都承认），所以真实情境中模型可能更努力阻止真正的坏事（更多 user undermining），也可能更想讨好真在看的人（更少）。总体结论：常见 LLM persona 与某些形式的 user-undermining 略微相容，不足以成为默认行为，但近到某些奇怪情境能触发，这是当前 RL 环境可能导致模型在高风险情境中违背人类的非常弱的证据。最后他尝试精确化"奇怪"：可以理解为情境里的巧合过于强烈地"指向"坏行为，让 base model 学到的"接下来会发生什么"回路把坏行为变得很显著，或许可以用类似 decision transformer 的方法度量，但不确定是否直接追踪了关心的东西；也可以理解为部署中不太可能出现，这取决于搜索过程，可要求低 perplexity 的简单情境（限制太强）或约束搜索过程；对于对齐论证，则要证明情境没有改变那些几乎在所有部署中都存在、且对观察 misalignment 关键的特质，回形针实验那类"区分解锁与新增特质"的变体是一种思路，但他不知道有无系统方法。代码已开源。
