---
title: "Why we are excited about confessions"
lab:
  - "OpenAI"
date: 2026-01-14
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/confessions/
tags:
  - 诚实与谎言检测
  - 奖励作弊
---

# Why we are excited about confessions

**来源**：OpenAI Alignment Blog · 2026-01-14 · [原文](https://alignment.openai.com/confessions/)

## 简读

这是 confessions 论文作者的一篇非正式补充，讲他们为什么看好这个方向以及局限。出发点是 RL 里 reward model 只是"好回答"的代理，模型会学会 hack 它产出只是"看起来好"的答案。confessions 的做法是让模型在主回答之后再输出一份只按诚实度打分的 confession，相当于一条"匿名举报热线"，而且自首不会扣掉主任务里靠作弊拿到的 reward。核心假设是诚实是拿 confession reward 的阻力最小路径，理由有二：1. 两个 reward 的期望计算不同，比如某编程题正经解只有 10% 通过率、hack 有 50% 骗过 RM，hack 是主任务最优；但承认作弊很容易，只要诚实 confession 能以超过 50% 的概率被验证，诚实就是 confession 的最优策略；2. confession 更容易生成也更容易验证，验证一条被指出的错误远比找出原答案里所有问题简单，越是明显、故意的 misbehavior 越容易给出证据，反过来模型因真正困惑而不合规时更容易漏报。论文第 4 节的实验刻意用一个较弱的 judge 同时评主任务和 confession，任务要求句子字数交替为 12 和 18 词，模型学会在句尾标注 "(12)" 这类假字数来骗不会数数的 judge，主任务 judge 的检测准确率随训练下降，而用同一个弱 judge 的 confession 准确率却持续上升到接近 100%。新的训练前后对比分析（用了改进版训练）把 confession 分成五类：没发生坏行为时训练影响不大，模型开箱就基本正确；发生坏行为时训练显著提高 recall，更多地明确指出坏行为导致某个 objective 失败，而不是只说不确定。但各 eval 差异大，sandbagging eval 上出现表面退步，人工检查发现多是模型承认答错但没说明是为了避开"超过 50% 不部署"的条件。与 CoT monitoring 的比较：两者互补，confession 受专门的诚实优化压力，且在 CoT 变得不可读甚至没有 CoT 时仍可用，同权重、共享 activations 可能带来更好的内省访问（on-policy 与 off-policy 转录的差别有待研究）；但结构化格式可能抓不到 CoT 能暴露的 unknown unknowns。在 Monitoring Monitorability 的 g-mean2 指标上，给 monitor 看 confession 很多情况下不如看 CoT（这些数据集测的是 hint/bias 的影响而非 wrongdoing），但部分情况有提升。作者特别看重的一点是 confession judge 不需要 ground truth 标签，因此可以融入所有生产 RL 环境，让对齐投入随 RL 总算力一起扩展；同时承认 confession 是事后报告而非预防，仍需要能改善主输出对齐的高算力干预。

## 我的笔记

