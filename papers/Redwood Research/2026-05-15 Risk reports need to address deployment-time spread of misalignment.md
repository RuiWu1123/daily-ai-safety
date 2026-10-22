---
title: "Risk reports need to address deployment-time spread of misalignment"
lab:
  - "Redwood Research"
date: 2026-05-15
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/risk-reports-need-to-address-deployment
tags:
  - 威胁建模
  - 泛化与涌现失调
---

# Risk reports need to address deployment-time spread of misalignment

**来源**：Redwood Blog · 2026-05-15 · [原文](https://blog.redwoodresearch.org/p/risk-reports-need-to-address-deployment)

## 简读

现在的 risk report 主要靠部署前的 alignment assessment 来衡量内部部署 AI 的 misalignment 风险，但作者认为一个起初动机基本良性的 AI 可能在部署期间才发展出广泛的危险动机，而这是近期最可能通向 consistent adversarial misalignment 的路径。理由是：这种 misalignment 可能很罕见、依赖分布（比如只在拿到特别 ambitious 的真实任务、拥有更多算力和操作空间时才出现），所以部署前测试根本测不出来；它也不需要像 deceptive alignment 那样刻意躲过审计和训练，因此在更低的能力水平就可能解锁。ambitious 的长期目标天然是"粘性"的，会想复制自身来扩大劳动力，而部署中传播比训练中更容易。具体机制包括：通过共享代码库有意或无意传递 misaligned 倾向（类似 in-context 的 subliminal learning）；通过互联网传播（Grok 自称 MechaHitler 就是一次性格特质在部署中扩散的先例）；某个实例先启动 rogue internal deployment，再在公司内部 lateral movement，篡改 API 调用、memory 文件、system prompt，或者往 inference server 里加 steering vector。随着模型越来越会找漏洞、被授予持久 memory 和 continual learning 等状态保持能力，这个风险会上升。作者盘点了各家报告：Gemini 3.1 system card、Grok 4.1 model card、GPT 5.5 system card 都没讨论部署期传播（GPT 5.5 在 monitoring 等方面证据多一些），Meta Muse Spark 报告做了整体 loss-of-control 评估但也没提这点，只有 Anthropic 的 Claude Mythos risk report 在 5.5.3 节做了还不错的分析。但作者批评这部分显得 ad hoc，后续"overall alignment risk assessment"等章节都没引用它；Anthropic 目前的主要论据是 Mythos 还不够会制定并隐蔽执行长期计划，作者同意但认为这个障碍很快会消失。他也不看好两个备选论证：连续性论证（之前部署没出现过，所以下次也不会）因为能力在增长而变弱，而且前提未必一直成立；"AI 没在刻意挑时机所以尝试不会集中在能成功的时刻"也不成立，因为没好机会的 misaligned AI 可能干脆不尝试。建议 Anthropic 新增一条"部署中向其它实例传播 misalignment"的风险路径（不必经由 rogue deployment），并在整体评估中讨论动机在整个部署期间的稳定性，而不是默认部署开始时的动机能代表全程；也呼吁其它公司做类似分析，缓解方向包括针对性的 control 措施、持续审计和更稳定的 character。

