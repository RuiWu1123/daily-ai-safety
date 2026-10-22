---
title: "MirrorCode: Evidence that AI can already do some weeks-long coding tasks"
lab:
  - "METR"
date: 2026-04-10
source: "METR Research"
url: https://metr.org/blog/2026-04-10-mirrorcode-preliminary-results/
tags:
  - 评估方法
  - 危险能力评估
---

# MirrorCode: Evidence that AI can already do some weeks-long coding tasks

**来源**：METR Research · 2026-04-10 · [原文](https://metr.org/blog/2026-04-10-mirrorcode-preliminary-results/)

## 简读

METR 资助并与 Epoch AI 共同开发的 MirrorCode 的 linkpost，正文是 Epoch 的初步结果。现有 SWE benchmark 大多是短任务，而 C 编译器、浏览器这类长程 demo 又难判断完成度和人类引导程度。MirrorCode 让 agent 在没有源码和网络的条件下精确复刻一个现有 CLI 程序：可以任意执行原程序（黑盒 oracle），有文档和部分可见测试，评分用数百到数千个端到端测试，要求输出逐字一致；为防硬编码，给部分可见测试配了取值不同的隐藏 "dual" 测试，并阻止包装原二进制。基准共 24 个程序，这里分析了 choose、cal、gotree（约 1.6 万行 Go 的系统发育树工具，40 多个命令）和 Pkl（Apple 的配置语言，约 6.1 万行 Java/Kotlin），使用简单的 ReAct scaffold，预算最高 10 亿 token（约 $550）。结果：Opus 4.6 基本能复刻 gotree 量级以下的所有程序，在 gotree 上通过 2001 个测试中的 2000 个，研究者估计人类需要 2–17 周，远长于 METR 测得的约 12 小时常规 time horizon。代际差异明显：Opus 4 / 4.1 / 4.5 在 gotree 上分别为 15% / 24% / 63%，老模型常过早提交、幻想出不存在的"时间限制"，4.6 则坚持到可见测试全部通过；新模型还选了更合适的数据结构，并且只有 4.6 正确诊断出 gotree 根本不处理 Newick 引号。代码质量一般（大量重复的参数解析、用魔数传元数据的 hack）。Pkl 未解决：Opus 4.6 写了 1.76 万行解释器，通过 35% 的可见测试，分数仍随 token 增加而上升，但它一开始就选了 eager evaluation，尽管文档反复强调 lazy 是核心，之后一直打补丁，能用文字说出 thunk 方案却始终没有实现。局限：依赖精确可检验的 spec，不同于常规开发；有记忆污染风险，他们用函数级复现相似度筛查（未污染基线约 0.34，入选程序为 0.31–0.41，排除了一个 0.74 的程序），但不能完全排除；覆盖领域有限。结论：有详细可检验 spec 时，AI 已能完成数周量级的编码任务，长程 demo 反映的是可复现的真实现象；正式版将开源并保留私有测试集。

