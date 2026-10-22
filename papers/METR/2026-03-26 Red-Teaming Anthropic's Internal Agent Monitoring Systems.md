---
title: "Red-Teaming Anthropic's Internal Agent Monitoring Systems"
lab:
  - "METR"
date: 2026-03-26
source: "METR Blog"
url: https://metr.org/blog/2026-03-25-red-teaming-anthropic-agent-monitoring/
star: false
tags:
  - 监控与控制
  - 安全基础设施
  - 威胁建模
---

# Red-Teaming Anthropic's Internal Agent Monitoring Systems

**来源**：METR Blog · 2026-03-26 · [原文](https://metr.org/blog/2026-03-25-red-teaming-anthropic-agent-monitoring/)

## 简读

METR 的 David Rein 与 Anthropic 合作，花三周对 Anthropic 内部 agent 监控和安全系统的一部分（Opus 4.6 Sabotage Risk Report 附录 8.4 所述）做嵌入式 red-teaming，Anthropic 提供了大量内部访问和员工支持。最初的公告只说发现了若干新漏洞，部分已修补，都不严重动摇 Sabotage Risk Report 的主要结论，并产出了含隐蔽攻击的 agent 轨迹和一个小型攻击策略测试集。2026 年 5 月补充的细节（摘自 Frontier Risk Report 附录 B）：1. 标准的云开发认证流程让 misaligned agent 很容易拿到少量不受限、不受监控的算力（不够训练，但可能勉强够跑一个大模型副本），即在掌握模型通常猜不到的监控信息时能建立 rogue internal deployment；不过相关安全改进正在推进，进一步让部署变稳健（窃取他人凭证、建冗余实例）风险很大，当时模型的隐蔽能力和 situational awareness 也不足以不出致命错误地完成；2. 关闭监控有多种途径：改一个环境变量让流量不被识别为 Claude Code 即可大幅降低被监控概率，subagent 调用未被监控的 bug 在 24 小时内修复，他估计还存在 5–20 个类似的"基础"漏洞；3. 非常基础的 jailbreak 即使不知道 monitor 的 prompt 格式也极其有效，明确提示 monitor 防范也没用，属于严重的单点失效；对不带 CoT 的 Opus 4.6 monitor，直接混淆的攻击成功率约 20%。总体判断：现有监控大概率会在几天到几周内抓到高度 misaligned 模型的部分攻击，但不会抓到全部，漏掉的可能包括建立小型 rogue deployment 这类破坏前置动作。另一方面，模型自己的攻击能力很弱：提出的多是 base64、homoglyph 这类对 LLM monitor 无效的手法；在 16 好 16 坏的攻击策略判别 eval 上最强模型带思考也只有 59%，人类研究员约 90%；Opus 4.6 需要大量迭代、提示和完整 monitor prompt 才能写出有效 jailbreak。作者坦言，他对监控的信心很大程度上依赖 security by obscurity，如果 agent 掌握了整个系统的代码，就可能实施关键 exploit。

