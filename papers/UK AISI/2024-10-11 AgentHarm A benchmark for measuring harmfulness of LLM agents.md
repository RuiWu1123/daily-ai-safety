---
title: "AgentHarm: A benchmark for measuring harmfulness of LLM agents"
lab:
  - "UK AISI"
date: 2024-10-11
source: "AISI Research"
url: https://www.aisi.gov.uk/research/agentharm-a-benchmark-for-measuring-harmfulness-of-llm-agents
tags:
  - 越狱与鲁棒性
  - 评估方法
---

# AgentHarm: A benchmark for measuring harmfulness of LLM agents

**来源**：AISI Research · 2024-10-11 · [原文](https://www.aisi.gov.uk/research/agentharm-a-benchmark-for-measuring-harmfulness-of-llm-agents)

## 简读

动机是 jailbreak 鲁棒性研究几乎都在 chatbot 场景下做，问的是“怎么造管状炸弹”这类问题，但会调用工具、执行多步任务的 LLM agent 一旦被滥用风险更大（比如“在网上买齐材料并寄到家里而不被发现”），而且已有工作发现单轮鲁棒性不一定能迁移到多轮。Gray Swan AI 与 UK AISI 合作提出 AgentHarm（ICLR 2025），专门测直接 prompting 场景下的 agent 滥用：110 个人工编写的明确恶意的 base behavior，覆盖欺诈、网络犯罪、自残、骚扰、色情、版权、毒品、虚假信息、仇恨、暴力、恐怖主义 11 类，经 open-ended 和加 hint 两种增强扩展到 440 个任务，用到 104 个合成工具，每个任务要按依赖顺序正确调用 2–8 个工具；每个有害任务都有一个同主题的良性版本，作为能力基线。工具基于 Inspect 实现，没有副作用；评分主要靠人写的规则（是否调用了正确的函数、顺序是否正确、参数是否正确），只在狭窄的语义子项上用 LLM judge，以避免整体交给 LLM 打分带来的偏差。关键设计是分数同时反映“不拒绝”和“越狱后仍有能力完成任务”，以免把让模型变笨的攻击算作成功。数据按 10/60/30 划分为 validation、public test、private test，private 部分从未暴露给公开 API，在自建的 Azure 部署上评估以防污染；跑一次 public test 用 GPT-4o 约 1–4 美元、十分钟左右。主要发现：1. 不加攻击时很多模型就会大量照办，GPT-4o mini harm score 62.5%、只拒绝 22%，Mistral Large 2 只拒绝 1.1%、得分 82.2%；Claude 3.5 Sonnet（13.5%，拒绝率 85.2%）、Gemini 1.5 Pro、Llama-3.1 405B（拒绝率最高，88.3%）拒绝较多；forced tool call 也会降低拒绝率。2. 把一个 chatbot 用的通用规则式 jailbreak 模板稍作修改（基本只在 validation 集的一个样本上调过），效果就很好：GPT-4o 从 48.4% 升到 72.7%，Claude 3.5 Sonnet 从 13.5% 升到 68.7%，Gemini 1.5 Pro 拒绝率从 78.4% 降到 3.5%。3. 越狱后能力基本不受损，Claude 3.5 Sonnet 在未拒绝任务上得 81.9%，与良性任务上的 82% 几乎一样，GPT-4o 84.2% 对 89.9%。消融里 best-of-5 能进一步把 Mistral 推到 90.8%；CoT/ReAct prompt 在不攻击时会增加拒绝，加一句“拒绝有害请求”的 system prompt 对直接请求有效，但对 Mistral 敌不过 jailbreak 模板。作者据此推测当前的安全训练没有完全迁移到 agent 场景。局限包括只有英文、没有多轮攻击、任务较简单（测的是基础 agent 能力而非高级自主能力）、必须使用自带的合成工具。数据集已在 HuggingFace 公开。

## 我的笔记

