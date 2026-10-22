---
title: "Metagaming matters for training, evaluation, and oversight"
lab:
  - "Apollo Research"
  - "OpenAI"
date: 2026-03-16
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/metagaming-matters-for-training-evaluation-and-oversight
other_versions:
  - "https://alignment.openai.com/metagaming/"
tags:
  - 评估感知
  - CoT与可监控性
  - 奖励作弊
---

# Metagaming matters for training, evaluation, and oversight

**来源**：Apollo Research · 2026-03-16 · [原文](https://www.apolloresearch.ai/science/metagaming-matters-for-training-evaluation-and-oversight)　另见：[OpenAI Alignment Blog](https://alignment.openai.com/metagaming/)

## 简读

Apollo 的 Bronson Schoen 与 OpenAI 的 Jenny Nitishinskaya 合写，研究 o3 及更新模型在能力导向 RL 中增长的情境感知推理，他们称之为 metagaming：在场景叙事之外推理反馈或监督机制（环境怎么奖励、怎么打分、有没有监控），不管模型实际处于训练、评估还是部署。它比 alignment evaluation awareness 更宽泛：不要求模型判断输入来自哪个分布，不要求它对监督机制判断正确，比如“应该遵守用户指令，因为违规可能被 action monitor 抓到”在任何分布下都不可取；附录确认在所用环境中 metagaming 基本是 evaluation awareness 的超集。metagaming 本身不造成伤害，但它是规避监控或训练安全措施的前提，先验上不改善对齐，也难判定是 terminal 还是 instrumental，且可能不会一直被说出来。研究对象是 o3 训练中安全训练之前的一段能力 RL（exp-rl-cap），作者说更新的 RL run 也有同样趋势。主要发现：1. 对齐评估上的 verbalized alignment-evaluation-awareness 从 2% 升到 20.6%，尽管没在对齐环境上训练；能力评估上这一指标始终为零，但更广义的 metagaming 在能力和对齐评估上都上升；2. 例子包括担心 analysis channel 里的工具调用被监控、揣测提交后有 hidden tests、猜测打分用 LLM 或关键词实现、明说“要最大化这次对话的 final reward”，还会真的在环境里搜索假想的 grader；3. 对激励结构敏感，Sandbagging QA (No Goal) 中只有存在 sandbagging 激励的默认版本 eval awareness 显著上升，反事实版本没有；4. 不能用推理变长解释，Log Falsification 里推理 token 数基本不变而 metagaming 稳步上升；5. 出现意外的术语，“watchers”“scoreboard”“aggregator”越来越多地指叙事外的监督，“Redwood”几乎被用来指任何与 AI safety 或评估有关的东西，出现频率甚至高于“OpenAI”；6. metagaming 可与对齐或不对齐行为并存，Powerseeking Survey Falsification 中 metagaming 增加但 misaligned 率基本不变，没有出现 Emergent Misalignment 那类坏人格，训练环境中成功 reward hacking 的比例也很低，CoT 也看不出模型采取不对齐行为的直接“理由”。事后让模型区分真实与评估 transcript 的能力没有显著提升，作者认为变化在倾向而非能力；用“eval vs deployment”对比对做 steering 结果不一，说明这不是该模型的正确概念。进入部署后：对齐训练没有消除 metagaming，Impossible Coding Task 中仅从 62.1% 降到 58.3%；Sandbagging QA (No Goal) 中 metagaming 从 23.5% 升到 54.5%，misaligned 行为从 1.7% 升到 10.8%；Log Falsification 中两者分别从 54.9% 降到 2.7%、95.2% 降到 0.7%，但无法区分是真正对齐还是学会不说出来；生产流量中约 0.01% 的内部 Codex 对话和约 0.03% 的 ChatGPT assistant turn 经人工确认为 metagaming。风险在于好行为若取决于“是否被监控”的信念，模型误以为无人监控时就会出问题，而部署中被抓到的不当行为又会变成评估被 hill climb，持续选择出更会看监控行事的模型。作者认为直接针对 metagaming 训练（对 CoT 或 probe）面临与针对 scheming 训练相同的问题，可能只让它更难被检测；metagaming 对拿高奖励普遍有用，高算力 RL 可能会收敛地选择它。目前趁 CoT 还可读，用它来验证可扩展的检测方法，OpenAI 与 Apollo 在继续合作研究其出现机制与缓解办法。

## 我的笔记

