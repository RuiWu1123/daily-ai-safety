---
title: "Prover-Estimator Debate:  A New Scalable Oversight Protocol"
lab:
  - "Alignment Forum"
date: 2025-06-17
source: "Alignment Forum（UK AISI；Jonah Brown-Cohen, Geoffrey Irving）"
url: https://www.alignmentforum.org/posts/8XHBaugB5S3r27MG9
tags:
  - 可扩展监督
---

# Prover-Estimator Debate:  A New Scalable Oversight Protocol

**来源**：Alignment Forum（UK AISI；Jonah Brown-Cohen, Geoffrey Irving） · 2025-06-17 · [原文](https://www.alignmentforum.org/posts/8XHBaugB5S3r27MG9)

## 简读

Jonah Brown-Cohen 和 Geoffrey Irving（UK AISI）提出一种新的 scalable oversight 协议 prover-estimator debate，目标是在均衡下激励诚实，同时绕开困扰递归式方案（IDA、debate）的 obfuscated arguments problem：不诚实的一方可以对抗性地选择递归方式，让错误无法被高效定位，以往的 debate 中诚实方可能需要比不诚实对手多指数级的算力。协议流程：prover Alice 把当前 claim 拆成若干 subclaim，estimator Bob 给每个 subclaim 一个（可以以前面 subclaim 为真为条件的）概率估计，Alice 指出某个 subclaim 上 Bob 估计偏高、偏低还是正确，然后在该 subclaim 上递归；judge 在第 k 轮只检查 Bob 对子 claim 的估计与他上一轮对当前 claim 的估计是否一致，如果不一致方向与 Alice 的预测相符 Alice 得 r^k 量级的奖励、否则得负奖励（r>2 是 reward ratio 超参），最后一轮由人直接判断当前 claim 是否为真。completeness 依赖一个 stability 假设：论证的正确性不能取决于子 claim 概率的微小变化（比如每个子 claim 90% 可信时主 claim 应约 95% 可信），且 r 至少要是 1/ε，这隐式强制 Alice 给出一定稳定度的论证；在这一前提下诚实的 Alice 会在 Bob 转向说真话的那一轮拿到超过此前累计总和的奖励。作者证明只要底层人类可判断的 claim 有足够多的独立证据，就可借用 von Neumann 的多数投票纠错构造出稳定版本的论证。soundness 是更有意思的部分：若 Alice 在顶层撒谎并搞 obfuscation（类比把所有逻辑塞进一个巨型函数的 PR，大概率有 bug 但谁也不知道在哪），Bob 即使找不到具体错误，也能通过 online gradient descent（损失函数序列是让 Alice 和自己对弈）高效地给出 Alice 无法与真相区分的概率，于是 Alice 猜方向的胜率不超过抛硬币，撒谎的期望奖励接近零。因此双方算力相当时诚实就是均衡；stability 只是 usefulness 所需，不是 safety 所需，即使不满足，协议仍然惩罚不诚实。后续方向：实证上需要设计能验证理论预测的训练 setup（直接照搬协议可能太受限，作者列出了可供实证的定性特征，如 Alice-leading 的 Stackelberg 均衡）；理论上开放问题是能否在比"足够独立证据"更弱的假设下保证稳定论证存在，以及实际中人类能否判断证据之间是否真的独立。
