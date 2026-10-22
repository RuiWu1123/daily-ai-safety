---
title: "Features as Rewards: Using Interpretability to Reduce Hallucinations"
lab:
  - "Goodfire"
date: 2026-02-11
source: "Goodfire Research"
url: https://www.goodfire.com/research/rlfr
star: false
tags:
  - 可解释性
  - 诚实与谎言检测
  - 对齐训练方法
---

# Features as Rewards: Using Interpretability to Reduce Hallucinations

**来源**：Goodfire Research · 2026-02-11 · [原文](https://www.goodfire.com/research/rlfr)

## 简读

背景是 hallucination 很难用 RL 修，因为核心瓶颈在监督：数学和代码能靠单元测试快速给奖励，而判断长文本里的事实陈述真假需要领域专家或带 web search 的 LLM，太慢太贵，没法当 RL 的奖励信号，判断"修正得好不好"更难。Goodfire 把这当作其 intentional design 议程的第一个具体演示，提出 RLFR（Reinforcement Learning from Feature Rewards）：用模型内部表征上的轻量 probe 当奖励。具体做法是先在 LongFact++ 的事实密集型 prompt 上采样 Gemma-3-12B-IT 的 rollout，用 Gemini 2.5 加 web search 打标签（包括 on-policy 的真假陈述以及修正/撤回示例），训练一组 probe 组成流水线：token 级定位 probe 找出候选实体 span，span 级分类 probe 判断是否 hallucination，被标记时让 policy 生成多个内联 correction 或 retraction，再由两个 reward probe 分别给修正和撤回打分作为 RL 奖励。关键设计是 reward probe 跑在冻结的 base 模型副本上而非学生模型激活上，梯度无法流经 probe，学生只能学着产出得分高的 token 而不是去 hack 激活。RL 用 ScaleRL 加 CISPO，约 360 步、花费约 2.5k 美元；同样预算用 Gemini 2.5 Pro 加搜索当 judge 只能跑 3–5 步，单次干预成本约低 90 倍。在 999 条留出 prompt 上，带 best-of-32 的完整系统使 hallucination 降低 58%，标准 benchmark 无退化；分解来看 policy 本身减少约 10%，内联干预带来的 in-context 减少最大约 35%（但 base 模型加内联提示不训练也能有 24.9%，部分只是结构选择的功劳），干预直接修掉的约 12.5%；去掉内联干预仍有 31%，与 base 模型加监控流水线相当。值得注意的是，尽管对 probe 做了大量优化，模型并没有学会改表征来躲避 probe，probe 信号依然足够可靠，能进一步用于 test-time scaling；在 base 模型上训的 probe 在训练后 policy 的激活上同样有效，作者把这当作表征比担心的更稳定、interpretability 可以在训练中使用而不被训练破坏其监控价值的初步证据。关于模型为何"知道"却不用这些信息，作者给了几个猜测：不确定当前任务是否要求事实回忆（如虚构写作需要编造）、现有后训练可能奖励流畅自信的编造、事实核查机制在模型中位于生成机制之前且没接好到输出。作者也说明这只是早期一步，probe 读的是较具体的实体级信号。

