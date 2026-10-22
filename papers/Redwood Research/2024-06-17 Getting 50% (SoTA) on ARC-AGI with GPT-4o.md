---
title: "Getting 50% (SoTA) on ARC-AGI with GPT-4o"
lab:
  - "Redwood Research"
date: 2024-06-17
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/getting-50-sota-on-arc-agi-with-gpt
tags:
  - 评估方法
---

# Getting 50% (SoTA) on ARC-AGI with GPT-4o

**来源**：Redwood Blog · 2024-06-17 · [原文](https://blog.redwoodresearch.org/p/getting-50-sota-on-arc-agi-with-gpt)

## 简读

这是一篇偏离 Redwood 平常主题的能力实验帖：用 GPT-4o 在 ARC-AGI public test set 上拿到 50%，而此前类似难度数据集上的 SoTA 是 34%（作者后来补充了澄清说明）；在留出的 train 子集上是 72%，MTurk 人类在 train 分布上是 85%。方法思路类似 AlphaCode：给 GPT-4o 看图片加多种 ascii 表示（spreadsheet 式坐标、按颜色的连通分量、归一化后的形状、输入输出 diff），用约 30k token 的手写 step-by-step few-shot prompt 让它先推理变换规则再写 Python 实现，每题采样约 5,000 个程序，按网格尺寸是否变化分两套 prompt；再挑最接近正确的 12 个实现，把它们在样例上的实际输出和 diff 给模型看，让它修改，共约 3,000 个 revision 样本；最后在样例全对的程序上做 majority vote 选 top-3 提交。消融显示：V0 prompt 1024 样本 25%，最好的 V2 prompt 2048 样本 34%，ensemble 后 37%，加 revision 到 50%；准确率对 log(样本数) 大致线性，每翻倍 +3%，若只用 V2 要 10 万样本才能到 50%，只用 V0 要 150 万，revision 大约修好剩余错误的 20%，作者对 revision 这么有用感到意外。定性上 GPT-4o 的主要瓶颈不全是推理：网格视觉极差（超过 12x12 就读不出颜色）、几何类代码常出 off-by-one、超过 32k–40k token 长上下文明显变差、不遵守 few-shot 的长度。caveat 包括：runtime compute 比先前工作多 1000 倍以上，只在 100 道 train 和 100 道 test 上评估（标准误约 5%），闭源模型不符合奖项资格。作者给出预测，比如 70% 概率三名顶尖工程师加 1000 万美元算力和 GPT-4o 微调权限能在一年内超过 MTurk 水平。观点上他反驳 Chollet "LLM 不会在推理时学习"：如果 50% 需要某种运行时 learning，而从约 6,000 个程序里挑选本身不算 learning，那 in-context learning 就确实有学习成分，虽然很弱。他认为进展没停滞，ARC-AGI 会被 scale 解决，但它不是衡量 TAI 进展的好 benchmark（elicitation 效果太大、视觉权重过高），更看好 METR 那类测 AI 做研究工程能力的 eval，并批评奖项不允许 SoTA 闭源模型、过度限制算力。代码已开源。

