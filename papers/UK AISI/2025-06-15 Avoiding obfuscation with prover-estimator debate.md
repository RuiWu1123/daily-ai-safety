---
title: "Avoiding obfuscation with prover-estimator debate"
lab:
  - "UK AISI"
date: 2025-06-15
source: "AISI Research"
url: https://www.aisi.gov.uk/research/avoiding-obfuscation-with-prover-estimator-debate
star: false
tags:
  - 可扩展监督
---

# Avoiding obfuscation with prover-estimator debate

**来源**：AISI Research · 2025-06-15 · [原文](https://www.aisi.gov.uk/research/avoiding-obfuscation-with-prover-estimator-debate)

## 简读

背景是 scalable oversight 需要在人类无法直接核查的复杂任务上给出准确的训练信号，AI debate 是代表方案之一：Irving et al. 2018 证明计算受限的人类法官可以通过观看两个强 AI 的递归辩论来判断远超自身能力的问题，辩手把问题逐层拆成子问题，直到人能直接判断。但递归 debate 有一个已知漏洞，即 obfuscated arguments problem（Barnes 2020 在实证中自然出现过）：不诚实的辩手可以把一个简单问题拆成一堆难以处理的子论断，诚实一方即使知道某处有错也找不到，从而输掉；doubly-efficient debate 通过取消递归绕开了这个问题，但要求辩手写出完整的人类可判断论证，失去了递归"只放大一小块"的效率。这篇论文（Brown-Cohen、Irving 等，部分工作在 UK AISI 完成）提出 prover-estimator debate：prover（Alice）负责拆分子论断，estimator（Bob）不再挑选子论断，而只给每个子论断分配概率；由 Alice 选择递归方向，并必须指出 Bob 的概率在某个具体方向上错了，每轮按前后两轮 Bob 估计之间的一致性给奖励，奖励逐轮按 1/ρ 放大，最后一轮直接用人类判断。关键是用 online gradient descent 证明 Bob 能以只比 Alice 多一点的算力给出 Alice 无法与真相区分的概率，所以如果 Alice 搞 obfuscation、谁也找不到错，Bob 只需给低概率即可获胜。为此引入 ρ-stability 条件：论证的结论不能对子论断边际概率的微小变化过度敏感（例如 2/3 研究支持药效时多数结论对 ρ=4 稳定），作者认为这对模糊的人类判断、经验科学、法律论证这类场景是自然要求。主要定理：1. completeness，诚实 prover 只要能给出稳定且可回答的分解，就能战胜任意算力的 estimator；2. soundness，即使稳定性不成立，诚实 estimator 也能用与对手相当的算力平均获胜；推论是 Alice-leading 的 Stackelberg 均衡下 Alice 以至少 1−5ε 的概率答对，且可以通过 Alice 的期望收益判断训练是否成功；所需辩论次数为 O(ρ^d)，在 ρ 远小于宽度 q 时显著优于朴素递归的 q^d。稳定性只影响有用性不影响安全性：只有不稳定分解时协议偏向拒绝。局限包括：只是平均意义而非最坏情况保证；有些问题（如数学证明这类精确依赖每个子论断的）可能只有不稳定分解，作者设想数学子论断交给 Lean 验证、模糊子论断用本协议。对实证工作给了建议：辩手设为不对称角色、显式输出不确定性（如用 token 概率）、按 Stackelberg 结构每更新一次 A 就多次更新 B。另外 v2 修正了早期预印本中稳定性定义（由条件概率改为边际概率）导致的主定理错误。

