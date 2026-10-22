---
title: "The need to relativise in debate"
lab:
  - "Alignment Forum"
date: 2025-06-26
source: "Alignment Forum（UK AISI；Geoffrey Irving, Simon Marshall）"
url: https://www.alignmentforum.org/posts/XycoFucvxAPhcgJQa
star: false
tags:
  - 可扩展监督
---

# The need to relativise in debate

**来源**：Alignment Forum（UK AISI；Geoffrey Irving, Simon Marshall） · 2025-06-26 · [原文](https://www.alignmentforum.org/posts/XycoFucvxAPhcgJQa)

## 简读

Geoffrey Irving 和 Simon Marshall（UK AISI）的一篇纯阐述性文章，没有新结果，核心论点是：想把 interactive proof 的理论用到 debate、scalable oversight 等 AI safety 方案上，结果必须"relativise"，即在所有参与方都能访问一个黑盒 oracle（可以是强大的求解器、随机函数或任意人类偏好模型）时仍然成立。理由是 verifier 实际上是人类，而人类看起来就像 oracle：可以问人问题，但无法把人当成 Boolean circuit，更无法把人"抬升"到有限域上。经典的 IP=PSPACE 依赖把问题编码成有限域上的多项式、用随机点做 polynomial identity testing（Schwartz-Zippel），一旦加入随机 oracle，就需要在有限域点上求值 oracle，而 oracle 在那里没有定义，于是相对随机 oracle 有 IP^O<PSPACE^O。由此提出 relativisation heuristic：对安全有意义的交互证明结果必须 relativise；但这只是必要条件，单 oracle 只建模了人类直觉的局限，不建模机器直觉的局限（后者见 Brown-Cohen 与 Irving 关于 obfuscated arguments 的双 oracle 工作），而如果有更强的 verifier（如能自证正确的模型）也可用别的技术。要求 relativise 会改变每个协议需要的条件：到 PSPACE，非 relativising 只需一个 prover，relativising 需要两个零和竞争的 prover（DEBATE=PSPACE，因为 TQBF 本身就是双人博弈，加 oracle 不变）；到 NEXP，非 relativising 的 MIP=NEXP 只要两个不能通信、可能串通的 prover，relativising 则需要两个竞争 prover 且彼此可 oracle 访问，即 Barnes 与 Christiano 的 cross-examination，迫使 debater 预先承诺一个指数大的对象；到 RE，MIP*=RE 靠纠缠量子比特，relativising 版本需要两个竞争 prover 能承诺任意大的二维表并共享、移动 pointer（Paul Christiano 的想法），作者自己也承认这很"silly"。文中留了一个开放问题：能否用合作而非竞争的 prover 在 relativise 前提下达到 PSPACE 而不一路到 NEXP。结尾附 AISI 合作与最高 20 万英镑资助的信息。
