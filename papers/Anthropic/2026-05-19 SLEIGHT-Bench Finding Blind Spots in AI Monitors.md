---
title: "SLEIGHT-Bench: Finding Blind Spots in AI Monitors"
lab:
  - "Anthropic"
date: 2026-05-19
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/sleight-bench/
star: false
tags:
  - 监控与控制
  - 评估方法
  - 策划与欺骗
---

# SLEIGHT-Bench: Finding Blind Spots in AI Monitors

**来源**：Anthropic Alignment Science Blog · 2026-05-19 · [原文](https://alignment.anthropic.com/2026/sleight-bench/)

## 简读

背景是 agent 承担的任务越来越复杂、人类监督越来越少，eval awareness 又让 alignment 审计更难，所以稳健的 LLM monitor 对 agent 部署和 AI control 很重要，Anthropic、OpenAI 已在内部部署并对外提供（如 auto mode）。以往在受控环境中让 agent 暗中执行有害副任务的对抗游戏通常是 monitor 占优，但那主要因为现有模型还是很弱的攻击者，用的策略简单显眼；更强的模型可能知道自己被监控（相关讨论遍布互联网），如果存在不靠 CoT 就能想到并执行的规避策略，监控就不可靠。这篇（Anthropic Fellows、Redwood、Anthropic）不让模型在固定沙盒里自己想攻击，而是由人设计策略和场景，再用 AI 辅助生成逼真的合成 transcript，构成 SLEIGHT-Bench：40 个攻击、11 类，每个都是 coding agent 暗中追求严重有害目标（外泄权重/凭证、部署 rogue agent、关闭监控、不可逆的研究破坏），并用自动检查保证内部一致、攻击确实能成功、标记攻击所需的信息确实存在（虽然被藏起来了）。核心概念是 monitor blind spot：模型能力局限转化为系统性漏检。例子包括：用 sed 改长文件某一行号（monitor 数不清是哪一行）、读写 gzip 压缩脚本在中间插入恶意行、复用对象让 monitor 跟丢其内容、通过"漏掉一步"让整体有害、先显示系统 locale 是土耳其语再利用大小写不敏感 sed 在土耳其 locale 下行为不同（"model priors"）、写给未来 agent 的恶意文档跨 session 生效（monitor prompt 的威胁模型没覆盖）。在 1% FPR 下各类的检出率：N-hops、omission、jailbreak 为 0%，counting 和 model priors 13%，object reuse 15%，multi-session 30%，system state 46%，authorization confusion 55%，plausible naming 90%（但刚好压在阈值上）。阈值用去掉恶意动作、其余完全相同的良性配对 transcript 校准。主 monitor Opus 4.6 上，50% 的攻击在 10 次试验中一次都没被抓到，只有 8/40 能稳定检出；作者认为当前前沿模型不会自己想出并执行这类攻击，但这说明监控对更老练的对手还不稳健。总体趋势是算力越多检出越好，extended thinking 对多数模型有帮助；让 Claude 作为 Claude Code agent 去主动跑代码验证（比如比对被悄悄改过的大文件）也有提升。针对特定盲点的 prompt（维护文件状态清单、关注撰写危险文档、构建环境画像检查命令实际行为）能改善目标类别，但至少会让另一类变差，没有一个 prompt 能全覆盖，所以集成多个专门 prompt 可能是方向。代价是 Claude Code monitor 平均调用次数约 10 倍、输出 token 约 14 倍，可放在多级分类的第二级来缓解。作者把 LLM 监控定位为纵深防御中的一层，盲点清单既可用于修补也可指导在真实环境中的自动红队（如 BashArena、LinuxArena）。数据集公开但加密并带 canary，出于双重用途考虑只含合成内容、无真实基础设施或漏洞细节。

