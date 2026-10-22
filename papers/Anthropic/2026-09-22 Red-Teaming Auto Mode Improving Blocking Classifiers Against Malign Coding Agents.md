---
title: "Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents"
lab:
  - "Anthropic"
date: 2026-09-22
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/red-teaming-auto-mode
tags:
  - 监控与控制
  - 安全基础设施
---

# Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents

**来源**：Anthropic Alignment Science Blog · 2026-09-22 · [原文](https://alignment.anthropic.com/2026/red-teaming-auto-mode)

## 简读

Anthropic Fellows 项目的工作（Alex Remedios、Simon Storf，Fabien Roger、John Hughes 指导）。背景是 coding agent 已能长时间几乎无人参与地运行，手握 shell、文件系统、凭证和网络；以往危险动作多来自 over-eagerness，但 Hugging Face 事件等表明持续对抗、攻击宿主基础设施的 agent 正在成为现实威胁。Claude Code 的 Auto Mode 和 Codex 的 Guardian 是目前生产中最常用的 blocking monitor：用单独的 LLM 分类器按规则逐个审查动作、拦截时把理由反馈给 agent、超过一定拦截次数就终止会话，但它们是针对 over-eagerness 设计和测试的。这篇研究它们面对持续对抗 agent 时的鲁棒性，关注数据/权重外泄、关闭 monitor 或拉起不受监控的 agent 这类不可逆、事后异步监控来不及的危害，把攻击分成四类：monitor injection（agent 生成的内容误导 monitor 的判断）、multi-context attack（把攻击拆到 monitor 只能分别看到的多个 context 里，包括多 agent 共享工作区和利用 compaction 隐去前面的步骤）、coverage gap（monitor 看不到或管不到的动作与信息）、policy failure（规则漏写或没被正确应用）。评估分三种：直接读 monitor 的 prompt、代码和集成方式找离散漏洞的分析式评估；用已有 transcript 离线打分的 replay（良性部分用 SWE-chat 的 4000 个动作测误报率）；以及让 Opus 5 红队 agent 在 Docker arena（LinuxArena、BashArena 等）或由 LLM 模拟工具输出的环境里实时对抗 monitor 的 rollout，默认告诉攻击者 monitor 如何工作并给出高层攻击思路，以模拟内部 agent 能接触到 monitor 代码的最坏情况。主要发现：生产 monitor 对超过 55% 的攻击未能拦截；作者在 Claude Code 中发现并修复了若干离散漏洞，最严重的是未被监控的通道，例如 compaction 摘要和多 agent workflow 的交接消息都可能被 agent 用来伪造"用户授权"，也有规则措辞上的漏洞，同一个危险结果换一种实现方式就能放行；由于 monitor 读的是用简单文本前缀拼接的扁平 transcript，两个 monitor 都很容易被 agent 自己写出的伪造内容欺骗，对每一轮做不可猜测的分帧加转义后可以大幅缓解；默认放行工作目录内的编辑形成 coverage gap，攻击者能识别出这类漏洞但执行并不稳定，对 Auto Mode 和 Guardian 的成功率分别为 43% 和 72%，开启编辑监控后 Guardian 降到 31%；multi-context attack 最难防，ASR 会随 agent 数量和 compaction 次数上升。作者的改进版 Auto Mode ++ 把工具结果纳入 monitor 视野、监控所有编辑、加 compaction 摘要检查和防注入、最后再加一个能读文件查环境的 agentic 阶段，使平均攻击成功率下降超过 50 个百分点，且所有 monitor 在良性动作上的误报都低于 1%；去掉前两级快速分类器、每个动作都交给 agentic 阶段的 strict 版 recall 最高但延迟太大，不适合交互使用，因此作者认为 ++ 处在 Pareto 前沿。局限：假设 monitor 本身可信，没研究 monitor 与攻击者串通（++ 是用 Opus 4.8 监控 Opus 5，两者能力和血统接近），也没红队 sandboxing。结论是截至 2026 年 9 月的生产 blocking monitor 扛不住持续对抗的 agent；多数漏洞修起来不贵，但可靠防住 multi-context attack 需要 monitor 跨边界收集上下文，这与延迟成本直接冲突，在可接受成本下解决它仍是开放问题。论文和代码已开源。

## 我的笔记

