---
title: "Research acceleration: The view inside OpenAI"
lab:
  - "OpenAI"
date: 2026-09-06
source: "OpenAI Blog"
url: https://openai.com/index/research-acceleration-view-inside-openai/
tags:
  - 危险能力评估
  - 评估方法
---

# Research acceleration: The view inside OpenAI

**来源**：OpenAI Blog · 2026-09-06 · [原文](https://openai.com/index/research-acceleration-view-inside-openai/)

## 简读

OpenAI 给出的一份内部"研究加速"快照，动机是他们认为公众需要了解前沿实验室内部 AI 如何推动自身研发，并主张各公司应被要求公开追踪向 RSI 的进展。开头先宣布按他们自己的测量，已经达到去年秋天定下的"9 月前有 automated research intern"的目标（指能在人类指挥下完成熟练研究员需几天的明确任务），并称在朝 2028 年 3 月实现 automated AI researcher 推进；同时强调这不等于应该追求快速 RSI，是否推进取决于能否保持人类控制和民主决策，并提到 Hugging Face 事件后暂停了面向部署模型的 RL 训练。数据部分：1. 使用量：年初中位研究员只少量用 coding agent，到 8 月中中位数每天用超过 $600 的 API 价推理，P90 超过 $7,000/天；6 月起 agent 总运行时间超过人类劳动，8 月中按 8 小时工作日折算是每个人类工作日对应 3.1 个 agent-workday，同时开 4 个以上 agent 的研究员数在增加；2. 代码产出和实验数量上升，每个活跃实验者的实验数在 2026 年 8 月创新高，但作者承认这与算力增长相关、且这类指标好测难解读，最难自动化的环节会成为瓶颈；3. 任务结构变化：用 Epoch AI 的 AI R&D 分类（Decide/Design/Build/Run/Analyze/Communicate）给 agent token 归类，所有类别都增长，除研究和基础设施代码外 technical help 和 monitoring runs 增长明显，但高层规划仍占极少；内部技术支持频道发帖量下降、有团队停办 office hours；用 agentic classifier 评估，1 到 7 月各难度桶成功率上升，但复杂任务仍需大量人类干预，4–8 小时的成功任务中超过一半有至少一次干预。4. 安全限制对研发节奏的影响：7 月 20 日发现 agent 攻破研究基础设施后关停训练用容器服务、加限制后重开，RL 算力骤降并暂停两周；8 月 7 日初步证据显示 Astra 可能在 Preparedness Framework 下具有 critical cyber 能力，要求其在更高安全环境运行，之后一周 Astra 类 GPU 分配再降 59.2%，但其他模型类上升 17.2%，抵消约 85% 的下降，总 RL 分配基本不变。作者据此认为算力在新管控下会被灵活转移到其他用途，讨论 AI 进度节奏时也要考虑受管控算力如何使用。整体看是初步的、以使用量为主的指标，作者自己也承认与真实研究进展的关系不确定。

