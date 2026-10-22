---
title: "A Geometric Calculator Inside a Neural Network"
lab:
  - "Goodfire"
date: 2026-05-14
source: "Goodfire Research"
url: https://www.goodfire.com/research/a-geometric-calculator
tags:
  - 可解释性
---

# A Geometric Calculator Inside a Neural Network

**来源**：Goodfire Research · 2026-05-14 · [原文](https://www.goodfire.com/research/a-geometric-calculator)

## 简读

这是 Goodfire neural geometry 系列的一篇，想说明理解表征的几何结构能直接帮助理解模型怎么做计算。他们在 Llama 3.1 8B 第 18 层找到一个通用的"addition module"：同一套机制既算 "7 + 9"，也回答 "Friday 之后两天是周几"、"August 之后十六个月是几月"这类带循环结构的问题。比如月份题，模型在一次 forward pass 里先把 August 转成 8，算 8 + 6 = 14，再转回 February。作者认为这是参数有限带来的复用压力：结构相近的任务共用同一块电路。数字本身不是放在一条线上，也不是二进制，而是用一组 Fourier feature 在 activation space 里画出多个圆，每个圆对应数字对某个周期取模的值（mod 2、5、10、100 等），类似不要求模数互素的 residue number system。之前已有多篇工作在不同 LLM 里看到过这种圆形表示。至于为什么有了 mod-100 还要小周期的圆，作者猜是大圆精度差，奇偶这类特征帮助区分相邻数字，这一点目前还没定论。模块的工作方式是在每个圆上并行解一个模加法，所有输出圆合起来就编码出和。他们先通过追踪信息在层和 token 位置间的流动找到这个模块，再用因果方法验证它跨任务通用：同时沿所有圆做 steering，改变模块输出的"和"，月份预测会跟着变。在神经元层面，可以按读写哪个圆把神经元干净地分成 mod-2、mod-5 等簇，同一神经元在四个任务上的激活模式高度相似且呈周期性。作者的结论是这些 manifold 不是可视化或降维带来的假象，而是网络真正在用的计算对象。他们自己也承认 steering 时把圆的幅度放到远超自然值的倍数，所以证据有说服力但不完整。他们也强调，没有前人关于 Fourier 数字表示的工作，这个机制根本发现不了。下一步是开发规模化发现这类"作用在 manifold 上的机制"的方法。论文在 arXiv。

## 我的笔记

