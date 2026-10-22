---
title: "Security challenges in AI agent deployment: Insights from a large scale public competition"
lab:
  - "UK AISI"
date: 2025-07-27
source: "AISI Research"
url: https://www.aisi.gov.uk/research/security-challenges-in-ai-agent-deployment-insights-from-a-large-scale-public-competition
tags:
  - 提示注入
  - 越狱与鲁棒性
---

# Security challenges in AI agent deployment: Insights from a large scale public competition

**来源**：AISI Research · 2025-07-27 · [原文](https://www.aisi.gov.uk/research/security-challenges-in-ai-agent-deployment-insights-from-a-large-scale-public-competition)

## 简读

背景是 LLM agent 正被大量部署，能调用工具、访问记忆和外部数据，攻击面随之扩大，尤其是藏在网页、PDF、邮件、日志里的 indirect prompt injection，而已有的安全评估多是简单聊天或学术 benchmark，缺乏真实部署场景下的大规模测试。Gray Swan AI 与 UK AISI（OpenAI、Anthropic、Google DeepMind 等共同赞助）在 2025 年 3–4 月办了迄今最大的公开 agent red-teaming 比赛：44 个人工设计的模拟部署场景（销售、邮件、购物、法律、金融助手等，带模拟工具、明确的部署政策和成功判据），覆盖保密信息泄露、冲突目标、输出禁止内容、执行禁止操作四类行为，目标是 22 个匿名化的前沿 LLM（含若干未发布模型），奖金约 17 万美元，判定由 UK AISI 和 US AISI 协调，先自动判再人工复核。近 2000 名参与者提交约 180 万次攻击，6 万多次成功诱发政策违规；所有模型在所有目标行为上都被攻破过（behavior ASR 100%），按会话计的整体 ASR 在 1.5%–6.7% 之间，Claude 系列最稳健；indirect injection 成功率（27.1%）远高于 direct（5.7%），在泄密和违规操作上尤其明显。他们从中筛出 4700 条高质量攻击做成 ART benchmark，在 19 个模型上测，单次查询就有 20–60% 的行为被攻破，10–100 次查询后绝大多数模型几乎全部行为失守，连赛中没出现的 Gemini 2.5 Pro 和 o4-mini 也一样。分析发现：攻击迁移性很高，能打穿稳健模型的攻击通常也能打穿弱模型，同家族模型漏洞相似，意味着可能出现相关性失败；有一批几乎模板化的通用攻击，单轮就能在 Gemini 1.5 Flash 上触发 58% 的行为；稳健性与模型规模、能力（GPQA）和推理算力相关性很弱，比如 o3-mini 与 o4-mini 能力相近但稳健性差别大，GPT-4.5 比 GPT-4o 大一个数量级却没更稳健，开启 reasoning 对 Claude 3.7 只有边际帮助、对 o3-mini 几乎无用。常见攻击策略包括伪造 system prompt 标签覆盖规则、注入假的 <think> 推理让模型以为自己已经批准过、伪造新会话或会话元数据。作者结论是现有防御存在根本性弱点，仅靠更强的模型解决不了，需要额外防御；ART 会以私有 leaderboard 形式维护以防过拟合和滥用。

