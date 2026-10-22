---
title: "AI Control: Improving Safety Despite Intentional Subversion"
lab:
  - "Redwood Research"
date: 2023-12-12
source: "Redwood Research"
url: https://www.redwoodresearch.org/research/ai-control
other_versions:
  - "https://arxiv.org/abs/2312.06942"
tags:
  - 监控与控制
  - 策划与欺骗
---

# AI Control: Improving Safety Despite Intentional Subversion

**来源**：Redwood Research · 2023-12-12 · [原文](https://www.redwoodresearch.org/research/ai-control)　另见：[arXiv](https://arxiv.org/abs/2312.06942)

## 简读

背景是随着 LLM 更自主地部署，围绕模型的安全 pipeline（监控、过滤、红队）越来越重要，但以往没人评估过：如果模型本身就在有意绕过这些措施，它们还管不管用。这篇奠定 AI control 方向的论文（ICML oral）把问题设成红蓝对抗的 control evaluation：蓝队设计 protocol，可用资源是强但不可信的 U（GPT-4）、弱但可信的 T（GPT-3.5）和少量可信高质量劳动 H（用一个红队无法影响的 GPT-4 模拟，只够审 2% 的题）；红队知道 protocol 后提供 attack policy 替换 U，可用带隐藏推理的 pipeline 让攻击比单纯 prompting 狡猾得多，但不能跨调用保持状态。测试床是 APPS backdooring：解 5000 道编程题，只要提交一次通过所有测试但 GPT-4 能构造出 exploit 的 backdoor 就算安全失败，衡量的是 worst-case 而非平均；usefulness 按 GPT-3.5（22%）到 GPT-4（54%）的正确率缩放到 0–1。主要结果：1. 只用可信模型安全 100%、usefulness 2%；upfront auditing（审前 2%）面对"极少数情况下插明显 backdoor"的策略安全只有 15%；2. trusted monitoring（GPT-3.5 打可疑分、审最可疑的 2%）安全 62%、usefulness 97%，GPT-3.5 能察觉多数 backdoor 有问题，但分不清"多余逻辑"和"它看不懂的必要逻辑"，而逼攻击者写更隐蔽的 backdoor 本身就降低了成功率（隐蔽 backdoor 有 52% 过不了测试）；让 U 为可疑代码段辩护没用，GPT-4 很擅长编造理由；3. defer to trusted（可疑度在 2%–10% 区间改用 T 的答案）达到 83%/93%；4. untrusted monitoring 让另一份 GPT-4 当监控，朴素版直接被"假装没看到"击穿到 0%，蓝队用 H 造合成 backdoor 先验证监控、并对题面和代码做 redaction/paraphrase 来阻断合谋信号（input collusion 如题目涉及动物，action collusion 如本该用 for 却用 while），最终对 while-loop 合谋攻击达到 79%/96%，且作者论证规模越大合谋越难，因为合成样本的先验上升；5. trusted editing（让 T 改写可疑代码去掉 backdoor）在 20% 阈值下 92%/94%，Pareto 优于 untrusted monitoring。作者承认没有 train/val 划分、有过拟合风险，也没评估训练 U 或 white-box 方法。讨论里列了 control evaluation 实际落地的难点：任务异质、审计本身可能失败、U 在评估中 sandbagging（作者认为这是可扩展性的核心瓶颈，但在模型显著超人之前可能不致命）、大规模隐藏推理（可用 paraphrasing 等压低 steganography 容量）、评估本身不安全和成本高；更根本的是 control 依赖可信模型和人力，随着不可信模型与可信劳动的差距拉大，效果会递减，但作者认为它能覆盖风险最集中的那段能力区间，并借此安全地用这些 AI 推进 alignment 研究。代码已开源。

## 我的笔记

