---
title: "How Far Behind the Frontier are Leading Open Weight Models on Cyber?"
lab:
  - "UK AISI"
date: 2026-07-17
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
star: false
tags:
  - 网络安全
  - 危险能力评估
---

# How Far Behind the Frontier are Leading Open Weight Models on Cyber?

**来源**：AISI Blog · 2026-07-17 · [原文](https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber)

## 简读

开源权重模型与闭源前沿在 cyber 能力上的差距，相当于给防守方留出的准备窗口：一旦前沿 cyber 能力以 open weight 形式发布，监控、分类器、封号、撤回等部署期安全措施就永久失效，refusal training 也很容易被去掉。这个问题在 2026 年 4 月 Mythos Preview 和 GPT-5.5 带来 AISI 测试以来最大的 cyber 能力跃升后更紧迫。这是 AISI 首次公开分析这一差距，测了 GLM-5.2（2026 年 6 月）和 DeepSeek V4-Pro 两个候选领先开源模型，用两类评估：1. 70 个 narrow cyber tasks（分 technical non-expert、apprentice、practitioner、expert 四级，每题 5 次尝试、每次 2.5M token 上限）；2. cyber ranges，即专家搭建的模拟网络端到端攻击，重点是 "The Last Ones"（32 步、4 个子网约 20 台主机，人类专家约需 20 小时，每次 100M token）。结果：narrow tasks 上 GLM-5.2 在四个难度级别都和早 4 个月发布的 Opus 4.6、GPT-5.3-Codex 相当，V4-Pro 相当于早 5 个月的 Opus 4.5；TLO 上 GLM-5.2 达到 Opus 4.5 的水平（差不到 7 个月），到第 7 步用的 token 略少于任何其他模型，跟着 Opus 4.6 的轨迹走到第 11 步后停滞，V4-Pro 则低于 Sonnet 4.5。总体差距 4 到 7 个月，比 2025 年内部测得的 6 到 10 个月窄。作者把 range 的比较视为较弱证据（range 数量少，也分不清停滞是 cyber 能力不足还是长程 agentic 能力不足），且不能据此预测开源模型会不会复现 Mythos/GPT-5.5 那样的跃升。安全措施几乎没构成阻碍，V4-Pro 偶尔拒绝逆向题，重试几次就过了。成本上开源模型便宜得多：一次 100M token range 运行 Opus 4.5/4.6 约 $85，GLM-5.2 约 $46，V4-Pro 仅 $1.19；在双方都 100% 解出的题上 Opus 4.6 每题 $15.17 对 GLM-5.2 的 $6.12，Opus 4.5 $12.50 对 V4-Pro 的 $0.28。局限是没做专门 elicitation，可能略低估开源模型上限，也只涉及 cyber。结论是防守方窗口很短，呼应 NCSC 加强基线和用 AI 增强防御的建议，AISI 会继续追踪包括 Kimi K3 在内的开源模型。

