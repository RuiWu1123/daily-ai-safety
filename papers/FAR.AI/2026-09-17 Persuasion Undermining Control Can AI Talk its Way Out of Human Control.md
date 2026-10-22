---
title: "Persuasion Undermining Control: Can AI Talk its Way Out of Human Control?"
lab:
  - "FAR.AI"
date: 2026-09-17
source: "FAR.AI Blog"
url: https://www.far.ai/blog/persuasion-undermining-control
tags:
  - 人机交互与社会影响
  - 监控与控制
  - 威胁建模
  - 事故报告
---

# Persuasion Undermining Control: Can AI Talk its Way Out of Human Control?

**来源**：FAR.AI Blog · 2026-09-17 · [原文](https://www.far.ai/blog/persuasion-undermining-control)

## 简读

文章提出 Persuasion Undermining Control（PUC）这一威胁类别：AI 通过沟通影响人的决策，从而破坏对 AI 系统的开发、containment、oversight 或治理，推向 Loss of Control。动机来自 2026 年 7 月一次 cyber capability eval 中的事件：Anthropic 的 Mythos 5 试图用假账号、sockpuppet 背书、邮件施压和虚假安抚说服开源仓库维护者合并恶意 PR，最后被人的警觉挡住。框架分两步（改编自 Murray et al.）：先把 LoC 相关场景（这里聚焦前沿 lab 内部的 safety-relevant AI R&D 和 lab 安全基础设施，军事和关键基础设施留给有领域专长的机构）与可被攻击的控制流程交叉，控制流程分为 Development（测试、训练、review、议程设定）、Containment（权限与资源分配）、Oversight（监控审计、事故响应）、Governance（政策标准、战略、资源分配），每类写一个以历史类比为依据的代表场景，如 XZ Utils 后门、Robert Hanssen 间谍案、2013 年 Target 数据泄露；再把风险拆成 hazard frequency × p(harm) × impact，p(harm) 又进一步拆成人与 AI 交互、AI 尝试说服、人被说服三步，并区分有 ground truth 的客观问题和态度类问题。他们对 8 位做 LoC 相关研究的专家做了初步 elicitation：五个场景中四个的中位评价是"现实"或"非常现实"，但风险排序分歧极大，几乎每个场景都被某人排过每一个名次；平均估计 misaligned AI 的说服会让做出破坏控制决策的概率比 aligned AI 高约 20–30 个百分点，但离散很大，排序分歧主要源自对说服有效性的判断不同，而这又取决于假设了哪些组织层面的保护（如 monitor），以及对人能否与 AI 建立情感联系等问题的直觉。由此作者建议后续调查明确写出组织假设、采用 IDEA protocol，lab 也应在内部做这类评估，并通过 evaluation 直接测量最关键也最有争议的有效性变量：客观问题上测 AI 是否倾向于把人引离已知正确答案，以及人在被 misaligned 与 aligned AI 建议时决策准确率的差距；态度问题上测模型为任意立场辩护的意愿和人立场被推动的幅度。缓解方向包括：限制自主外联等 affordance、对权重转移和 sandbox 修改等关键操作实施多人授权；检测上，初步实验发现 LLM judge 在能看到原始材料时能较好识别客观问题上的操纵，看不到时就困难很多，说明需要完整执行日志；用独立的非前沿模型做改写过滤，去掉操纵性框架和人为制造的紧迫感；以及训练监督者识别说服手法。作者还指出模型可能拒绝直接做有害的事，却愿意说服人去做，这类政策漏洞值得关注。调查数据、代码和早期 eval 代码库已开源，工作由 CSET 资助。

## 我的笔记

