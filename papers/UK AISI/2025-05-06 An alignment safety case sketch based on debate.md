---
title: "An alignment safety case sketch based on debate"
lab:
  - "UK AISI"
date: 2025-05-06
source: "AISI Research"
url: https://www.aisi.gov.uk/research/an-alignment-safety-case-sketch-based-on-debate
star: false
tags:
  - 可扩展监督
  - 威胁建模
---

# An alignment safety case sketch based on debate

**来源**：AISI Research · 2025-05-06 · [原文](https://www.aisi.gov.uk/research/an-alignment-safety-case-sketch-based-on-debate)

## 简读

背景是 scalable oversight：AI 一旦在大范围任务上达到或超过人类水平，人类就很难高效判断它的行为对不对，也就没法靠人类反馈把它往好的方向训。debate 是一种提议的解法，让另一个超人系统来挑输出里的毛病。这篇来自 UK AISI（Buhl、Pfau、Hilton、Irving）的论文用 safety case sketch 的形式，梳理 debate 能实现什么、还缺什么，作者称这是第一份细致的 alignment（trustworthiness）safety case sketch，也是第一份以训练方法的理论而不是 eval 结果作为核心证据的 sketch。场景设定为一个略超人的 AI R&D agent 在公司内部部署，担心的风险是它破坏研究，比如编造结果。部署分两部分：一个不能跑代码、对话全程记录和监控的 oracle 副本，帮研究者头脑风暴和排序研究方向；一个关在离线数据中心里的 agent 副本，每次跑固定时长（如 12 小时，相当于 1–2 周的人力），产出类似论文的结果，然后环境重置。对齐策略分四步：1. 先把部署设定成 low-stakes，也就是要很多次坏动作才会造成不可接受的后果；2. 用 debate 训练，作者设想的是即将发表的 prover-estimator debate，它的设计目标是让 obfuscated arguments（有缺陷，但双方在计算上都找不出缺陷的论证）成为输棋策略，代价是需要一个 stability 假设；3. 要拿到 exploration guarantee，排除 exploration hacking，即模型故意不去探索高奖励策略。作者的一个关键论点是，只要奖励信号基本可信，就不必去定义模糊的 "scheming"，只要证明模型没有放弃大量奖励即可。候选思路包括 exploration predictor、可信模型 best-of-n、formal heuristic explanation、SLT 的 susceptibility 扰动分析、model organism 研究、固定 Alice 只对 Bob 做 adversarial RL；4. 部署期间对每个输出和动作都持续跑 debate 并做 online training，最终论文还要经过 checker 模型 n 轮 debate 全部通过才用。safety case 立在四个关键 claim 上：训练达到了博弈的近似全局均衡；在均衡下系统最多在 ε 比例的情况出错（论证方式是让 debate 去近似一个展开完整论证树、每片叶子都调用人类判断的昂贵计算 M，再论证 M 基本为真）；部署中误差率不会漂过 ε；在这个误差率下系统做不到研究破坏、恶意代码和 self-exfiltration。第四条按"每个错误都是最坏情况"来保守论证，带一点 control 的味道。缺口在文中标得很清楚：exploration guarantee 目前不知道怎么拿到；SGD 能否在现实时间内收敛到均衡没有把握；有些真命题靠启发式知识，难以演绎论证，研究品味尤其如此；还有偷换定义这类 gerrymandering，以及人类的系统性误差。一到 high-stakes 场景，第三、四条直接失效，因为不能再靠 online training，就要面对 alignment faking 和分布偏移。作者的初步思路是对候选动作而不是最终动作做类似 online training 的处理，或者借助 eliciting bad contexts 之类的方法。结论很坦白：用现有技术，这个论证并不强；但他们认为某些关键部署（如在谨慎条件下用早期 AGI 做对齐研究）本身就可能是 low-stakes，而且这份 sketch 直接构成了 AISI research agenda 里 alignment 部分的基础。五个开放问题分别是更好的 debate 协议、实证检验、exploration hacking、high-stakes 场景，以及诚实性能在多大程度上转化为对齐。

