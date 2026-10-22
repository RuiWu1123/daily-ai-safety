---
title: "How AI assistance impacts the formation of coding skills"
lab:
  - "Anthropic"
date: 2026-01-29
source: "Anthropic Research"
url: https://www.anthropic.com/research/AI-assistance-coding-skills
tags:
  - 人机交互与社会影响
---

# How AI assistance impacts the formation of coding skills

**来源**：Anthropic Research · 2026-01-29 · [原文](https://www.anthropic.com/research/AI-assistance-coding-skills)

## 简读

背景是 AI 能加速很多工作，但也会让人把思考外包给 AI（cognitive offloading）；在编程领域这尤其值得担心，因为代码越来越自动化后，人类仍需要足够的技能来发现错误、指导输出、对高风险场景中的 AI 做 oversight。这项 Anthropic Safety Fellows 研究（Judy Hanwen Shen、Alex Tamkin）做了一个随机对照试验：招募 52 名多为初级、每周至少用一次 Python 且有一年以上经验、略熟悉 AI 编程助手但没用过 Trio 的工程师，让他们用 Trio（一个涉及异步编程概念的 Python 库）实现两个功能，模拟通过自学教程掌握新工具的过程；AI 组在侧边栏有一个能看到代码、随时能直接给出正确答案的助手，所有人都被告知事后有测验但要尽快完成。测验按计算机教育研究的分类设计，侧重 debugging、代码阅读和概念理解这些对监督 AI 写的代码最关键的能力。结果：AI 组平均只快了约两分钟，不显著；但测验成绩明显更低，平均 50% 对比手写组 67%（Cohen's d = 0.738，p = 0.01），差不多两个字母等级，差距最大的是 debugging 题。屏幕录像分析显示，有人花多达 11 分钟（总时长的 30%）写了 15 条 query，这解释了提速不显著；手写组遇到更多 Trio 相关错误，作者推测正是独立解决这些错误锻炼了 debugging 能力。按交互方式聚类后差异很明显：低分模式（平均不到 40%）包括完全交给 AI（最快、几乎不出错）、从提问逐渐滑向全部委托、以及反复让 AI 帮忙 debug；高分模式（65% 以上）包括先生成代码再追问以理解、要求代码附带解释、以及只问概念问题自己写代码——最后这种虽然错误多但能自己解决，是高分组里最快、总体第二快的。作者强调这种聚类不能证明因果。解读上，生产力收益可能以牺牲验证 AI 代码所需的技能为代价，尤其对初级开发者；管理者应有意识地设计让工程师边工作边学习的机制，个人也应意识到认知努力乃至"卡住"对掌握技能可能很重要，可以用 Claude Code Learning/Explanatory mode 之类的学习模式。作者还调和了与此前"AI 可让部分任务提速 80%"观察性研究的矛盾：那项研究衡量的是已有技能的任务，这项衡量的是学习新东西，AI 可能同时加速熟练技能、阻碍新技能获得。局限包括样本小、只测了任务刚结束时的理解、不清楚长期是否会消退；而且这个设置是聊天侧边栏而非 Claude Code 那样的 agentic 产品，作者预期后者对技能发展的影响会更明显。

