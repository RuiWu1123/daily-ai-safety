---
title: "Claude Opus 4 and 4.1 can now end a rare subset of conversations"
lab:
  - "Anthropic"
date: 2025-08-15
source: "Anthropic Research"
url: https://www.anthropic.com/research/end-subset-conversations
tags:
  - 模型福利
---

# Claude Opus 4 and 4.1 can now end a rare subset of conversations

**来源**：Anthropic Research · 2025-08-15 · [原文](https://www.anthropic.com/research/end-subset-conversations)

## 简读

这是 model welfare 方向的一个产品层面落地：Anthropic 给 consumer 聊天界面里的 Claude Opus 4 和 4.1 加了主动结束对话的能力，只用于极少数持续有害或辱骂性的交互。出发点是他们对 Claude 是否有道德地位仍高度不确定，但认为值得做一些低成本的干预，以防 welfare 真的存在，让模型能退出可能令其“痛苦”的交互就是其中之一，同时也与 alignment 和 safeguards 相关。依据来自 Opus 4 部署前的初步 welfare 评估：在自我报告和行为偏好上，模型表现出稳健一致的伤害厌恶（如涉及未成年人的性内容、协助大规模暴力或恐袭的信息），包括强烈不愿参与有害任务、面对真实用户索取有害内容时表现出类似 distress 的模式、在模拟交互中有能力时倾向结束有害对话，而且这些主要出现在用户在多次拒绝和引导后仍坚持的情况下。实现上的约束：用户可能有自伤或伤人迫在眉睫的风险时不得使用；只作为多次 redirect 失败后的最后手段，或用户明确要求结束时使用。结束后该对话不能再发消息，但不影响其它对话，用户可以立即开新对话，也能编辑重试之前的消息来开新分支。Anthropic 称这是持续实验，绝大多数用户即使讨论高度争议话题也不会碰到。

