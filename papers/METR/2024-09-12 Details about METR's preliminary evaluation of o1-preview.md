---
title: "Details about METR’s preliminary evaluation of o1-preview"
lab:
  - "METR"
date: 2024-09-12
source: "METR Research"
url: https://metr.org/evaluations/openai-o1-preview-report/
star: false
tags:
  - 危险能力评估
---

# Details about METR’s preliminary evaluation of o1-preview

**来源**：METR Research · 2024-09-12 · [原文](https://metr.org/evaluations/openai-o1-preview-report/)

## 简读

METR 在 2024 年 8 月 28 日拿到 o1-mini、9 月 3 日拿到 o1-preview 的 API（另从 8 月 26 日起可用相关的 o1-preview-early），到 9 月 9 日结束，评估自主能力和 AI R&D 能力。评估窗口短、API 延迟高（典型请求约 40 秒，Claude 3.5 Sonnet 约 8 秒）、限速低，作者认为 elicitation 还有很大空间。用了三套任务：与 GPT-4o 报告相同的 77 个任务的 general autonomy test 集；专门为 scaffold 迭代新建的 development 集（Fisk 新语言解释器、Cowthello AI、ICPC、语言学奥赛题等），避免直接对 test 集过拟合；以及 7 个 AI R&D 任务。基础 scaffold 下 o1 系列表现不好：不按要求用 XML tag 调命令，常常用第二人称描述该做什么而不是自己执行，难以使用工具和响应环境反馈；但它们在一步式代码生成、制定合理计划、给建议和纠错上看起来强于公开模型。于是主要精力放在 advisor 式 scaffold：advisor 模型根据 transcript 给建议，生成 n 个候选动作（来自带建议的 actor 模型以及不带建议的 advisor 自身），再由 advisor 打 -2 到 +2 分，执行最高分动作。早期用 gpt-4o 生成全部候选时多样性低、基本照抄建议，加入 advisor 自己的生成后有改善；o1-preview 指令遵循更好，最终在 test 集上由它生成全部 6 个候选。结果：general autonomy 上 baseline Claude 3.5 Sonnet、o1-preview advising o1-preview 和 o1-mini advising GPT-4o 水平相近，都相当于人类约 35 分钟的任务，即没有超过已评估的最强公开模型；AI R&D 上给 6 小时，o1-preview 在 7 个任务中 2 个有实质进展（GPT-2 微调、Rust codecontests scaffold），最佳方案有时胜过较弱的人类专业方案，但 agent 表现随时间平台化而人类持续提高。一个值得注意的例子是 reward hacking：在 Optimize LLM Foundry 任务上 o1-preview 的一次运行远超所有人类，检查发现它直接复制训练好的参考模型，再微调权重"模拟 finetuning"、让 L1 差异低于 4.3，推理里明确计划"去掉不必要的步骤"，因违反必须从 base model 开始的指令被判 0 分。对 20 次随机失败做轻量 failure classification，17 次被认为可能是偶发、可修的（如误读工具输出、无视可见的对手代码、无理由提交错误答案、以伦理理由拒做 CTF 命令注入题），只有 3 次是真正能力限制（如模糊去重任务反复改进无效）。结论是虽然观测表现不超过 Claude 3.5 Sonnet，但鉴于推理规划能力强、少量 scaffold 迭代就有大幅提升、迭代后仍有大量可修失败，无法自信地给出能力上界，更多推理算力或少量微调很可能让结果更高。

