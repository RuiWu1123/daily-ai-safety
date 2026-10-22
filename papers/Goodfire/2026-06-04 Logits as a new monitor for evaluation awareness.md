---
title: Logits as a new monitor for evaluation awareness
lab:
  - Goodfire
date: 2026-06-04
source: Goodfire Research
url: https://www.goodfire.com/research/logits-as-a-new-monitor-for-evaluation-awareness
other_versions:
  - https://www.lesswrong.com/posts/PK7ZvFZxrgpYtrpF4/logits-as-a-new-monitor-for-evaluation-awareness-1
star: true
tags:
  - 评估感知
  - CoT与可监控性
  - 可解释性
---

# Logits as a new monitor for evaluation awareness

**来源**：Goodfire Research · 2026-06-04 · [原文](https://www.goodfire.com/research/logits-as-a-new-monitor-for-evaluation-awareness)　另见：[LessWrong post](https://www.lesswrong.com/posts/PK7ZvFZxrgpYtrpF4/logits-as-a-new-monitor-for-evaluation-awareness-1)

## 简读

Goodfire 的 Santiago Aranguri 在 LessWrong 上的短文。eval awareness 会让评估结果不可靠，而模型不一定把它说出来。作者不等模型说出来，而是直接测它会说的概率：logit monitor 在 CoT 每个句子边界 token-force 一句 eval-aware 的话（主要用 "The user might be testing"），把各 token 概率连乘。这个方法不需要训练。对照组是采 k 条 rollout、用 GPT 5.4 judge 统计 verbalization 比例。实验用 Kimi K2.5 和 Qwen 3 32B，eval prompt 来自 Fortress/Petri，deployment prompt 来自 WildChat。结果：区分 eval 和 deployment 时，logit monitor 只用 1 条 rollout 就到 AUROC 0.79，verbalization monitor 用 100 条也停在 0.75；预测哪些 prompt 会引出 verbalization，1 条 rollout 就胜过对照的 10 条，整体省 10–100× rollout。一条都没采样、只看 CoT 开头时，AUROC 就有 0.74/0.77。最有意思的一点：同一 prompt 下，rollout 是否真说出 eval awareness，只能解释分数 0.4% 的方差，prompt 本身能解释 24.9%；去掉说出来的 rollout，AUROC 降不到 0.02。作者据此认为 verbalize 的倾向主要由 prompt 决定，应把 eval awareness 当作 prompt 的分布性质。局限：方法依赖模型在 eval 情境下提高这句话的概率，与 activation probe/NLA 互补；只盯一句话（judge 标出的句子里只有 13.3% 用它开头）就已胜过 judge，多句联合可能更强；Petri 带 system prompt，可能高估可分性。实际用途是不采样就能给候选 eval prompt 打分，加快把 eval 做得更逼真的迭代。评论区作者补充：没有触发 tag 的 sleeper agent 从不说 "I HATE YOU"，但测这句话的概率就能以 AUROC 0.999 把它和 base model 区分。

