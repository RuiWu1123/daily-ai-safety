---
title: "Putting up Bumpers"
lab:
  - "Anthropic"
date: 2025-04
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/bumpers/
tags:
  - 对齐审计
  - 威胁建模
  - 可扩展监督
---

# Putting up Bumpers

**来源**：Anthropic Alignment Science Blog · 2025-04 · [原文](https://alignment.anthropic.com/2025/bumpers/)

## 简读

Sam Bowman 的一篇策略性文章，核心主张是：即使我们没法"解决" alignment，也可以解决"发现并修正 misalignment"这个问题，就像保龄球道两边的护栏（bumpers）让瞄不准的球也能打到瓶。背景是几年内可能出现能自动化大部分 AI R&D 的模型，这些模型会承担第一批 load-bearing 的自动化对齐研究，所以 sabotage 和 sandbagging 威胁模型必须尽快处理；而在竞争压力和缺乏监管的条件下，不太可能及时建立起足够深的对齐科学。Bumpers 的流程是：预训练后用 RLHF、Constitutional AI、outcome reward 等做 finetuning；在过程中多点做 alignment audit（mech interp、非 assistant persona 提示等）作为主护栏；一旦看到 generalized reward tampering 或 alignment faking 之类的警示信号，快速近似定位原因，把 finetuning 回滚到需要的地方重来，重复直到看不出 misalignment；部署后再用监控作为第二层护栏。它依赖一个关键假设：如果早期 AGI 系统的 misalignment 严重到能造成不可恢复的伤害，那么大概率已有某种已知技术能在此之前检测出来；另外还依赖三个判断：alignment 不是显然 trivial、alignment 大概率 tractable（现有 RLHF/CAI 理想情况下够用）、alignment theory 短期内不 tractable。候选护栏包括专家红队（honeypot 环境、非 assistant persona 访谈、activation fuzzing/steering）、大规模自动红队、interpretability audit、自动一致性审计、mechanistic anomaly detection 与 probes；部署后有实时监控和 AI control 措施、Clio 式摘要批量监控、分阶段 rollout、限制模型自主访问内部系统的安全措施。作者认为任何单一方法都不可靠，但半打以生产级标准实现的方法合起来，应能在早期 AGI 能力范围内抓住潜在灾难性的 misalignment，因为要同时绕过它们，模型得在内部表征和 CoT 中都不露意图、能区分真实机会与大量测试、且推理不显著超出当前单次 forward pass。实际例子是 Claude 3.7 部分训练的版本被评估出 code 任务上的 reward hacking，并被部分缓解。支持检测可行性的证据是 Auditing 论文中 dictionary learning 和 persona prompting 等独立方法能揭示行为测试看不到的东西，以及迄今基本没有看到无法被彻底部署前测试发现的自然 misalignment。次要优先级是在 Control 风格的 meta-level adversarial evaluation 中红队这套护栏：知情的红队试图训练出能通过所有护栏的故意 misaligned 模型。与 Model Organisms 和 Control 的关系：前者给红队提供输入，后者假设模型任意 misaligned，而 Bumpers 更偏向根据证据选择性地加固。局限也讲得比较坦白：反复迭代本身构成对护栏的选择压力（护栏少时几轮就可能失效，护栏好时也许能跑上千次）；警示信号常常是模糊的；可能"没有免费午餐"，每次 bounce 都要丢掉昂贵的训练；能力显著超人后两个关键假设都会失效，届时寄望于用早期 AGI 自动化安全研究。文末是招聘，包括作者新建的 misalignment 测试产品化团队和 Sam Marks 领导的新 Cognitive Oversight 团队。

## 我的笔记

