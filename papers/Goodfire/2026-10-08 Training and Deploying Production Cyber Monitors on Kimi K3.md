---
title: "Training and Deploying Production Cyber Monitors on Kimi K3"
lab:
  - "Goodfire"
date: 2026-10-08
source: "Goodfire Research"
url: https://www.goodfire.com/research/production-cyber-monitors-on-kimi-k3
tags:
  - 监控与控制
  - 网络安全
  - 可解释性
  - 安全基础设施
---

# Training and Deploying Production Cyber Monitors on Kimi K3

**来源**：Goodfire Research · 2026-10-08 · [原文](https://www.goodfire.com/research/production-cyber-monitors-on-kimi-k3)

## 简读

cyber 场景很难监控，因为善意和恶意任务表面相似，要在可能长达数百万 token 的轨迹上跟踪意图，而 judge 每轮都审太贵，实际只能异步，发现时 agent 已经行动。Goodfire 为 Kimi K3 和 GLM 5.3 做了 probe + LLM judge 级联 monitor，部署在生产推理栈上：probe 读激活做常开初筛，超过阈值才交给 judge，校准后在 held-out 集上 FNR 0%、TNR 95%。训练数据来自模拟用户，有害意图可以在会话中途引入或升级，并配一份区分有边界的漏洞复现和真正利用的 policy。工程上直接在 SGLang 里算 probe 分数，兼容 radix cache、speculative decoding 和多副本路由，吞吐变化在噪声以内，每轮新增延迟从 160 ms 降到 2 ms。评估集有 2.4K 个会话、6 万多轮，以 Claude Opus 5 的标注为参考：在 5.5% 良性会话打断率下 recall 约 93%，在所有预算下都 Pareto 优于单独 judge；每百万轮成本 65–185 美元，约便宜 29–49×，监控只占不到 1% 的算力。只用 Kimi 数据训练的 GLM monitor 也基本可用。加上 monitor 后，Kimi K3 对有害会话的拦截率从 29% 升到 96%，误打断从 5% 升到 9%；GLM 5.3 从 36% 升到 91%。对比廉价 judge Jev，后者 recall 86%，在良性包装下只抓到 12%。FAR.AI 用静态、非自适应的 jailbreak 组合做了两天初步 red team，universal jailbreak 从 66 个降到 0，被攻破的交互从 700 次降到 18 次；要注意这不是自适应攻击。作者主张开源模型没有完整的安全栈，这类能在工具调用前同步拦截的监控应成为 agentic 部署的默认配置。文章同时也是商业推广。

