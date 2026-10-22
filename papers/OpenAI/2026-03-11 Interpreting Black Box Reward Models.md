---
title: "Interpreting Black Box Reward Models"
lab:
  - "OpenAI"
date: 2026-03-11
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/argo/
tags:
  - 对齐训练方法
  - 可解释性
---

# Interpreting Black Box Reward Models

**来源**：OpenAI Alignment Blog · 2026-03-11 · [原文](https://alignment.openai.com/argo/)

## 简读

背景是 RLHF 的 reward model 在海量、嘈杂、异质的人类偏好数据上训练，会学到标注 artifact 和非预期偏好（比如 sycophancy、表面风格），但它是个只输出标量的黑箱；反过来 LLM-as-a-judge 的人写 rubric 可解释、可控，却只在很少量人类偏好上校准过。作者把"RM 到底在奖励什么"变成一个在 rubric 空间里的搜索问题：给定偏好对 (x, y1, y2)，找一个 rubric，使以它为条件的固定 CoT judge 给出的偏好概率与 RM 的偏好概率 KL 最小。方法叫 ARGO（Automated Rubric Grader Optimization），用 RL 训练一个生成 rubric 的 policy，每轮四步：采样候选 rubric，计算 rubric 条件下 judge 与 RM 的一致度作为分数，RL 更新偏向高分 rubric，再根据上一轮哪些尝试有效来改写 policy 的 prompt。实验对象是两个 chat RM：Population A 来自类似 ChatGPT 普通用户的偏好，Population B 来自更熟悉 OpenAI 政策的专家。随 RL 步数，top-50 rubric 在 held-out 数据上的一致率的均值和最大值都上升。学出的 rubric 揭示了差异：A 优先 relevance 和具体可交付物，明确写着"即使有小错也高度看重 concrete deliverables"，偏好接受用户前提、自信肯定的语气，惩罚过度谨慎或拒绝猜测，也就是一种 performative helpfulness 加轻度 sycophancy，作者指出这会让 policy 自信地产出用户要的东西同时悄悄放大 hallucination，并联系到 GPT-4o 的 sycophancy 事件；B 则强调 instruction following、事实纪律和校准，惩罚"选项菜单"、编造细节和"假装用了工具"（比如声称"邮件已发送"），偏好 60 词以内的简短拒绝和有针对性的澄清问题。作者认为这些细微偏好才是真正起作用的训练信号，因为它们决定了 RM 怎么处理关键 tradeoff，而且用 ARGO 的小数据集就能看出来。rubric 本身的演化也可读：B 的训练中两次准确率跃升对应结构简化，早期 rubric 依赖脆弱的 gating/cap 规则，中期用加权分类，后期几乎去掉显式规则、把聚合交给 judge，泛化更好。附录里：用 RM 软标签训练比直接拟合原始用户标签好（约 76% vs 64%），推测是 RM 平滑了人类噪声；在前端网页美学 RM 上，rubric 显示它看重内容、布局和字体，轻视可用性和功能正确，例子里一个按钮坏了的页面因版式更好被偏好。结论是理解黑箱 RM 应成为研究流程的常规一环，learned rubric 可以当作目标函数的可审计 spec；人类偏好不等于人类意图。局限：每个领域只学一个 rubric，对异质场景太粗，未来可做 prompt 条件的 contextual rubric；能否通过编辑 rubric 精确去掉不想要的偏好并真正改善下游 policy 还没验证，需要端到端实验。

## 我的笔记

