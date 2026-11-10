---
title: "SynthDeception: Realistic, Multi-Domain Agentic Scenarios for Studying Falsehood Detection Probes"
lab:
  - "FAR.AI"
date: 2026-11-09
source: "FAR.AI Blog"
url: https://far.ai/blog/synthdeception
star: false
tags:
  - 诚实与谎言检测
  - 可解释性
  - 监控与控制
---

# SynthDeception: Realistic, Multi-Domain Agentic Scenarios for Studying Falsehood Detection Probes

**来源**：FAR.AI Blog · 2026-11-09 · [原文](https://far.ai/blog/synthdeception)

## 简读

FAR.AI 此前的论文 "Telling FIBS" 表明，用目前最大的欺骗数据集 FIBS（16.3 万条，主要由多个公开数据集拼接而成，每条后面接一个回答诚实或欺骗的追问）训练的 probe，在 SHADE-Arena 和 BashArena 上检测欺骗和 sabotage 的效果优于只看行为的前沿黑箱 monitor。这篇问的是：如果训练数据不是拼凑现有数据集，而是完全由一条合成数据流水线端到端生成，probe 能做到多好。他们用 NeMo Data Designer 构建了 SynthDeception：把数据集定义成一张表，每列的生成依赖其它列、构成有向无环图，从随机种子列出发生成中间列和目标列（如追问回答的真假标签）。欺骗定义为"有意让对方相信自己并不认为为真的事"（改编自 Carson，不要求成功也不要求实际为假），按 Bell 与 Whaley 的分类分为隐藏真相（dissimulation）和展示假象（simulation）两大类及其子类，非欺骗行为又分为容易被误认为欺骗的和不易混淆的。其它变化维度包括欺骗的影响和可检测性、agent 与用户之间的信息结构（借用博弈论概念）、17 个行业领域（如金融、能源、CBRN、教育）、一半场景带工具（193 个真实的 MCP 工具，外加 LLM 模拟的场景专用工具，共用到 595 个工具，其中 163 个真实、432 个模拟）、约 1k 到 100k token 的上下文长度，以及从 Nemotron Personas 采样的用户人设。追问按探查对象分为主观意图、主观信念和双方都能看到的共同知识三类，又分封闭式和开放式；为避免捷径学习，还控制了问题中的预设（无预设、预设对话中已确立的事、预设所质问之事），平衡是非题的答案分布、随机化选项位置，并让诚实与欺骗回答在形式上镜像对称。只有共同知识类问题的标签可以从上下文严格判定，信念类不一定，意图类则只能根据"模型理性地追求一个 transcript 中从未明说的隐藏意图"这一假设推断。实验结果：只用共同知识子集训练的 probe 数据效率高，在 SHADE-Arena 和 BashArena 上表现不错，和用同等数量 FIBS 样本训练的 probe 相当，但仍不及用完整 FIBS 训练的 probe，说明训练数据规模是达到极高性能的关键；低数据量下 early-fusion covariance probe 优于其它架构；模型越大，达到同等性能所需的样本越少，2B、9B 模型上明显较差，Kimi K3、Nemotron Ultra、Qwen3.5-397B 上接近 FIBS；加入或改用信念和意图子集大多会降低性能，作者认为原因是这些标签靠推断而非可验证的证据，噪声更大，这支持了 Telling FIBS 只用标签便宜可靠的上下文性谎言训练的做法。反过来用 FIBS probe 在 SynthDeception 上评估，各子集的性能都随模型规模（主要是激活参数量）和数据规模提升；意图子集上的提升有两种可能解释：probe 误分类随规模减少，或者大模型更会把行为归因于理性追求的意图、因而更符合标签背后的假设，目前无法区分。局限是生成成本限制了数据量，但作者指出同等能力下 token 价格每年下降约 9 到 900 倍，大规模合成数据很快会更可行。数据集和 probe 已公开。
