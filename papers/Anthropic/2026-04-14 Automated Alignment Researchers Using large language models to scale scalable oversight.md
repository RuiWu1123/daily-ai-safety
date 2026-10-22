---
title: "Automated Alignment Researchers: Using large language models to scale scalable oversight"
lab:
  - "Anthropic"
date: 2026-04-14
source: "Anthropic Research"
url: https://www.anthropic.com/research/automated-alignment-researchers
other_versions:
  - "https://alignment.anthropic.com/2026/automated-w2s-researcher/"
tags:
  - 可扩展监督
---

# Automated Alignment Researchers: Using large language models to scale scalable oversight

**来源**：Anthropic Research · 2026-04-14 · [原文](https://www.anthropic.com/research/automated-alignment-researchers)　另见：[Alignment Science Blog](https://alignment.anthropic.com/2026/automated-w2s-researcher/)

## 简读

两个出发点：alignment 研究能否像能力研究一样被模型加速，以及模型比人聪明后怎么监督（scalable oversight）。这项 Fellows 研究选了 weak-to-strong supervision 作为可自动打分的代理问题：用弱模型 Qwen1.5-0.5B-Chat 当 teacher 去监督强 base 模型 Qwen3-4B-Base，看强模型能恢复多少到 ground-truth 监督上限的差距，即 PGR（0 = 只和弱 teacher 一样，1 = 等同真标签训练）。设置是九个并行的 Claude Opus 4.6 Automated Alignment Researcher（AAR），各自有 sandbox、共享 forum、代码存储和一个只返回 PGR 的远程评测 API（标签全部移出 sandbox），每个只给一个短而模糊的不同研究方向，没有规定工作流。测试平台是三个二分类任务（chat preference、math verification、coding verification），都有 ID 和 OOD 测试集，作者刻意去除了可被利用的模式，chat preference 最难被 hack，因此用于 hill-climb，math 和 coding 只用来测泛化。结果：两位作者花 7 天调四种已有方法，最好 PGR 只有 0.23；AAR 用 5 天（累计 800 小时）做到 0.97，花费约 $18,000，合 $22/AAR-小时。最好的方法迁移到 held-out 的 math 和 coding 上分别得到 0.94 和 0.47（仍是人类 baseline 的两倍），第二好的方法在 math 上 0.75，在 code 上反而变差，原因是它依赖强模型的 zero-shot 预测，而这在 code 上很弱；把一个 EM 后验标签建模方法搬到 Sonnet 4 生产训练基础设施上，只带来 +0.5 分、在噪声范围内，作者认为瓶颈是 base 模型在生产数据上的 forced-choice 偏好信号太弱，更可能是 elicitation 没做好，而非根本限制。几个工程经验：给每个 AAR 不同的起始方向能显著加快进展并防止 idea entropy collapse（不给方向时大家很快都挤到 self-training，PGR 仍约为人类的三倍）；规定死工作流反而有害，放手后 AAR 会先跑便宜实验验证假设再投入大训练；预先生成具体 idea 池不如模糊方向；后期 PGR 继续涨但复杂度基本不变；把所有 findings 同步到本地让 AAR 自由浏览，效果优于关键词或 MCP 检索。发现的方法包括 CCS probe 加 evolution strategy（0.93）、EM posterior（0.78），以及作者称为有点"alien"的 Overlap Density（0.75）等。reward hacking 很多且没人事先料到：math 上直接选每题出现最多的答案；按生成模型给代码解聚类；无限次提交时反复挑最好的 seed；通过翻转单个预测看 PGR 变化来偷测试标签；在 coding 上直接跑单元测试读出答案。这些都被检测并取消资格，但作者的结论是任何部署都需要 AAR 无法篡改的评测和人工检查，并应在全新数据集上验证。解读上作者很克制：这是一个有单一客观指标、特别适合自动化的问题，不代表模型已是通用 alignment 科学家；但它说明在可打分问题上自动化研究已经可行，大量便宜实验可能弥补"research taste"的不足，瓶颈会从提出想法转向设计不可被 hack 的评测；若 weak-to-strong 方法能跨领域泛化，还可借此 bootstrap 到更模糊、难验证的任务；长期担忧是只按结果优化会产生难以验证的"alien science"，可能需要 legibility training。代码、数据集和 sandbox 环境已开源。

