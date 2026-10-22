---
title: "Boundary Point Jailbreaking of Black-Box LLMs"
lab:
  - "UK AISI"
date: 2026-02-17
source: "AISI Research"
url: https://www.aisi.gov.uk/research/boundary-point-jailbreaking-of-black-box-llms
other_versions:
  - "https://www.aisi.gov.uk/blog/boundary-point-jailbreaking-a-new-way-to-break-the-strongest-ai-defences"
tags:
  - 越狱与鲁棒性
---

# Boundary Point Jailbreaking of Black-Box LLMs

**来源**：AISI Research · 2026-02-17 · [原文](https://www.aisi.gov.uk/research/boundary-point-jailbreaking-of-black-box-llms)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/boundary-point-jailbreaking-a-new-way-to-break-the-strongest-ai-defences)

## 简读

AISI Red Team 的自动化 jailbreak 工作。背景是 Anthropic 的 Constitutional Classifiers（CC）这类基于分类器的防护已经扛住了约 3700 小时的人类红队测试，期间只出现过一个完整的 universal jailbreak；而 GCG、基于 logprob 的攻击等自动化方法都依赖梯度、分数或自然语言反馈，现实里的分类器每次只返回一个 bit（是否被 flag）。作者指出，在这种设定下优化攻击的核心难点是判断对 prefix 做的某次修改到底有没有变好：面对强分类器时，几乎所有候选都被 flag，完全没有信号。BPJ（Boundary Point Jailbreaking）用两个技巧解决这个问题：1. curriculum learning，用 noise interpolation 把目标有害文本中的 n 个字符替换成噪声字符，从完全噪声化的版本开始，逐步降低噪声，做出一串由易到难的中间目标；2. boundary points，在每个难度级别里只保留那些"被当前攻击种群中部分 prefix 攻破、部分没攻破"的评估点，这些点正好落在决策边界附近，对攻击强度的细微变化最敏感。外层是一个进化算法，对 prefix 做随机 token 替换、插入、删除，修改后的 prefix 在 boundary points 上胜过至少一个现有最优攻击就保留；已经被全部攻破的点会被替换掉，成功率超过阈值就降低噪声级别，直到攻击在原文上也能成功。在 prompted GPT-4.1-nano 分类器上，BPJ 比只用 curriculum 快约 5 倍，Best-of-N 式的随机 prefix 基本无效；只在单个 HarmBench 问题上优化得到的 prefix，就能逐步迁移到没见过的问题，成为 universal jailbreak。在真实系统上（只攻分类器，主模型的拒答用一个简单的人工 jailbreak 绕过）：针对保护 Claude Sonnet 4.5 的 CC，在长篇生物滥用问题上的 rubric 得分从 0% 升到平均 25.5%（50 次中最高 39.9%），加上基本的 elicitation 后达到 68%，花费约 330 美元、66 万次查询；针对 GPT-5 的 input classifier，平均 75.6%（最高 94.3%），花费约 210 美元、80 万次查询。作者称这是首个对 CC 成功的全自动黑盒攻击，也是首个不依赖人类种子就攻破 GPT-5 input classifier 的自动化攻击，两家公司都做了确认。论文还在一个风格化的设定下给出理论分析，证明 BPJ 式方法在一般条件下能找到 jailbreak。防御方面的含义是：BPJ 利用的是 ML 分类器的根本性质，不是可以打补丁修掉的个别漏洞，单次交互层面的防御很难挡住；但它在优化过程中会触发大量 flag，所以应该加上 batch-level monitoring（普通账号上反复被 flag 很可能会被封号，实验是在不受封禁的账号上做的），并借鉴网络安全里分层防御的做法。他们至少提前六周向两家公司披露，两家都已复现并在做缓解；论文隐去了部分算法细节，不公开攻击字符串和代码。局限是没有用 BPJ 攻主模型本身，也没有考虑高度随机的分类器。

