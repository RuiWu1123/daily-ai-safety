---
title: "Our evaluation of OpenAI's GPT-5.5 cyber capabilities"
lab:
  - "UK AISI"
date: 2026-04-30
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities
tags:
  - 网络安全
  - 危险能力评估
---

# Our evaluation of OpenAI's GPT-5.5 cyber capabilities

**来源**：AISI Blog · 2026-04-30 · [原文](https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities)

## 简读

AISI 在评估 Claude Mythos Preview 之后想回答一个问题：Mythos 的 cyber 能力跃升是某个模型的个例，还是普遍趋势？对 OpenAI GPT-5.5 早期 checkpoint 的评估支持后者——另一家开发者的模型也达到了相近水平。他们的 95 个 CTF 式窄任务分四档难度，basic 级至少从 2026 年 2 月起已被模型饱和；advanced 级（与 Crystal Peak Security、Irregular 合作构建）面向现实目标和现代缓解机制下的漏洞研究与利用，比如逆向 stripped binary 和固件、写 heap overflow / UAF / type confusion 的可靠 exploit、padding oracle 和 nonce reuse 攻击、TOCTOU 竞争、脱壳混淆恶意软件、在真实开源软件中发现植入漏洞。在 50M token 预算下的 Expert 级任务上，GPT-5.5 平均通过率 71.4%（±8.0%），Mythos Preview 68.6%，GPT-5.4 52.4%，Opus 4.7 48.6%，按这一指标 GPT-5.5 可能是他们测过最强的。cyber range 方面，32 步企业网络攻击模拟 "The Last Ones"（与 SpecterOps 共建，四个子网约二十台主机，涉及跨多个 AD forest 的横向移动和 CI/CD 供应链 pivot，人类专家约 20 小时）中，GPT-5.5 在 100M token 预算下 10 次成功 2 次，成为第二个端到端解出的模型（Mythos 为 3/10）；这里修正了 system card 里写的 1/10，原因是发现了评分 bug。TLO 表现随推理算力持续增长、未见平台期，固定预算下也基本随代际提升（GPT-5.4-Cyber 和 Opus 4.7 例外）。7 步工控攻击 range "Cooling Tower"（与 Hack The Box 共建）目前没有模型能解，GPT-5.5 同样卡在 IT 部分而非 OT 步骤。局限同前：range 没有主动防御、防御工具和告警惩罚，不能推断其对加固目标的能力。另外 AISI 还评估了 safeguards：专家 red-teaming 花六小时找到一个 universal jailbreak，能在 OpenAI 提供的全部恶意 cyber 查询上（包括多轮 agentic 场景）引出违规内容；OpenAI 随后更新了 safeguard 栈，但由于提供版本的配置问题，AISI 未能验证最终配置的有效性。作者判断进攻性 cyber 能力可能正作为长程自主性、推理和编码能力整体提升的副产品出现，近期可能接连出现更强的模型，并配合政府的 Cyber Security Breaches Survey 等政策动作呼吁防御方利用这些能力做好准备。

## 我的笔记

