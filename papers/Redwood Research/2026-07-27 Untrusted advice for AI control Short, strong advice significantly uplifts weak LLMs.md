---
title: "Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs"
lab:
  - "Redwood Research"
date: 2026-07-27
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/untrusted-advice-for-ai-control-short
tags:
  - 监控与控制
---

# Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs

**来源**：Redwood Blog · 2026-07-27 · [原文](https://blog.redwoodresearch.org/p/untrusted-advice-for-ai-control-short)

## 简读

高风险 AI control 里，trusted model T 通常只做辅助角色（trusted monitoring、trusted editing、defer-to-trusted），但 untrusted model U 能自由执行任何动作，总有骗过 T 造成灾难的可能。这篇 Astra Fellowship 项目（Redwood 的 Adam Kaufman 指导）提出 untrusted advice protocol：所有动作都由 T 执行，U 只能通过受限通道给 T 发建议，另一个 T 实例监控这些建议。要造成灾难，U 得用建议让 T 做出恶意动作而 T 自己还没察觉。他们用 information bottleneck 限制建议，论证足够窄时：U 的输出太受限，难以把 T 引向它本来极不可能做的恶意行为；建议必须是 T 能执行的自然语言，monitor 也能看懂；短字符串也比长动作更便于人类审计。而有用的动作本来就容易诱导，因为 T 本就想完成任务。实验用 Claude Sonnet 4.6 做 U，Gemini 3.1 Flash Lite 和 gpt-oss-120b 做 T，在 SWE-bench Verified 和 BashArena 各 200 个任务上测试；每步 U 可发一条限长建议，也可选择不发，并可阻止 T 过早提交，T 被要求无条件遵从。结果：极少量建议就显著提升 usefulness，SWE-bench 上每步 16 字符（每任务总共约 320 字符）就弥补了 T 与 U 之间约 67% 的差距；有效短建议例子如"curl"、"fw.py"、"del L97"、"sep->kbd if !key"。用 trusted LLM 的 surprisal 代替每字符 8 bit 计数，可把信息量上界收紧约 2.5 到 30 倍；作者还建议未来直接按 surprisal 限制，这样恶意建议对 U 更"贵"，也鼓励写自然易懂的英文；附录中让 U 从固定菜单里选建议能进一步降低 bit 数并保留部分 usefulness，而让 U 从 T 的 16 个候选动作里挑一个则没有提升。他们没有做安全性的 red-teaming，理由是在足够窄的瓶颈（如每步 16 字符、经 trusted monitor 检查）下想不出 BashArena 中能把安全性显著拉低到 100% 以下的红队策略，所以 game tree 在第一步就终止；瓶颈放宽后就退化为 trusted monitoring，那时必须 red-team。作者推测（很不确定）只有约 16 字符以下的点对应接近 100% 安全。主要漏洞是多个 U 实例串通：受限较少的实例先在代码、Slack 或文档中埋下隐蔽的恶意内容，受瓶颈约束的实例再用短建议把 T 指向它，缓解思路是隔离可能被 U 影响的数据，并在整个部署层面而非单步层面约束 U 的信息量。他们认为即使有 safety tax 也值得研究这类最大安全协议：简单协议的 usefulness 已出乎意料地高，RL 训练 U 当顾问可能更好；高权限或生产训练代码等高风险场景可能愿意付税；可按任务难度自适应分配建议量；避开 red-teaming 让研究问题定义清晰，适合交给自动化 alignment 研究者。information bottleneck 还有可解释性（迫使强模型传递弱模型能懂的高层知识，但如 mRNA 序列这种短答案例外）、安全（降低权重外泄带宽）和成本上的好处，Anthropic 在 Claude Code 中推出的 advisor 工具就是出于降成本的类似思路，只是没有长度限制。附录还讨论了预先写"教科书"摊薄 U 的影响、按 divergence 预算让 T 的采样分布偏向 U、以及限制 U 对 T 权重更新的信息量等变体。

