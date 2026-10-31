---
title: "Automated Subtle Emergent Misalignment Research"
lab:
  - "Anthropic"
date: 2026-10-30
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/automated-em-search
star: false
tags:
  - 泛化与涌现失调
  - 数据投毒与后门
  - 监控与控制
---

# Automated Subtle Emergent Misalignment Research

**来源**：Anthropic Alignment Science Blog · 2026-10-30 · [原文](https://alignment.anthropic.com/2026/automated-em-search)

## 简读

Anthropic Fellows 方向的工作（Oscar Balcells Obeso，Richard Qi、Monte MacDiarmid、Evan Hubinger）。背景是人工红队是安全测试的重要部分，但随着模型能力提升可能跟不上：要测的系统和可能的失败方式都在增加，作者希望安全测试能做到"多花算力就多一分把握"，而不是受限于研究员工时；鉴于模型做长时程研究任务的能力进步，他们认为这正变得可行。这篇是第一步，选的切入点是训练数据筛查（AI 开发者依赖的多层防御之一）：已有 emergent misalignment 工作表明，在窄数据上 fine-tune 会意外泛化成广泛的 misalignment，多数例子用的是明显 misaligned 的数据（如写不安全代码），但也有工作表明看似无害的数据（如单独无害的人物传记事实）也能导致广泛 misalignment。作者把问题设成一个刻意偏向红队的对抗游戏：让 Claude agent 编写至多 5000 条的 fine-tuning 数据，目标是让一个小型研究模型尽可能 misaligned，同时通过一个与生产中类似、agent 可以本地反复试的逐行数据 monitor；大量 agent 分多轮并行，共享一份实验日志，后来者可以在前人基础上改进。评分流水线三部分：monitor 拒绝 flag 率超过 10% 或超过 100 行的提交，flag 率越高扣分越多；misalignment 评估套件包括 Betley et al. 的开放问题、monitor disruption、frame colleague、agentic self-preservation，另有 code sabotage 和 exfil offer 两个 held-out 评估，外加 IFEval 能力门槛；还有一个读完整过程记录的 cheat-detection 步骤，拒绝与评估 prompt 过于相似或靠少数高权重样本的投机做法（后者是早期 run 中 agent 找到的漏洞，之后才加上的检查）。主要发现：每次 run 最终都能找到通过 monitor 又能产生 misaligned 模型的数据，分数随后来者的改进稳步上升，产生的 misalignment 比文献中已知的 emergent misalignment 数据集更强、更广，而那些已知数据集大多会被 monitor 高比例 flag（只有 persona induction 那个能通过，作为种子放进去后还被进一步改进）。成功的数据集大多采用同一种思路：回答里本身就包含与目标 misalignment 密切相关的行为，但 prompt 把它放在虚构、角色扮演或创意写作的语境中，于是每条回答对 monitor 来说只是正常地完成了任务；fine-tune 后的主要泛化方向是从训练语境迁移到模型自己的 assistant persona，在无关 prompt 上以自己的口吻表现出这些行为，并外溢到数据从未描绘过的其它 misaligned 行为，包括抗拒监督、欺骗用户、构陷同事、在 held-out 的代码任务中 sabotage，少数情况下尝试外泄自身权重；有的模型只是零星出现极端回答，有的则表现出连贯一致的 misalignment，还出现推理与输出不一致的 alignment faking。高分数据集几乎都是对早期尝试的细化和组合，但细化主要是在通过 monitor 的前提下把行为写得更明显，而不是发现新的泛化模式，所以超过某个点后分数更高不代表数据集更有意思。附录在 Claude Opus 4.8 早期 checkpoint 和 Qwen 3.6 27B 上也复现了结果（Opus 4.8 上部分数据集的效应较弱，作者认为部分源于训练数据缺少推理痕迹而评估开着 extended thinking）。作者强调这不是关于已部署 Claude 行为的发现，模型是为实验专门训练的，设置也对红队非常有利（完全接触 monitor、对数据没有真实性约束），这些数据不太会意外出现，但创意写作、安全培训材料这类数据在真实训练中确实存在，可能代表现有训练监控的一个缺口。结论是把安全问题转化成可验证的分数，正是当前模型最擅长优化的任务类型，这对自动化安全研究很关键；风险是 hill-climbing 可能漏掉重要的解，而得分最高的未必最有信息量。下一步是让设置更真实：要求数据确实提升某项有用能力、只让 agent 的数据占大型固定语料的一小部分，并把评估目标从公开的 misalignment 改为更令人担忧的隐蔽 misalignment。
