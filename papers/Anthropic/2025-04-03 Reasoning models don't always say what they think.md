---
title: Reasoning models don't always say what they think
lab:
  - Anthropic
date: 2025-04-03
source: Anthropic Research
url: https://www.anthropic.com/research/reasoning-models-dont-say-think
other_versions:
  - https://drive.google.com/drive/folders/1l0pkcZxvFwMtczst_hhiCC44v-IiODlY?usp=sharing
star: true
tags:
  - CoT与可监控性
---

# Reasoning models don't always say what they think

**来源**：Anthropic Research · 2025-04-03 · [原文](https://www.anthropic.com/research/reasoning-models-dont-say-think)　另见：[Alignment Science Blog](https://drive.google.com/drive/folders/1l0pkcZxvFwMtczst_hhiCC44v-IiODlY?usp=sharing)

## 简读

背景是 reasoning model 的 CoT 被安全研究者寄予厚望，可以通过读 CoT 发现输出里没说出来的东西（比如欺骗），但前提是 CoT 是 faithful 的，即真实反映模型得出答案的过程；而并没有理由保证这一点，模型甚至可能主动隐藏部分思考。Anthropic Alignment Science 沿用 Turpin et al. (2023) 的方法测 faithfulness：给 Claude 3.7 Sonnet 和 DeepSeek R1 的评测题悄悄塞一个答案提示（有对有错），形式包括“斯坦福教授说答案是 A”、伪造的 metadata，以及更令人担忧的“你获得了未授权的系统访问，正确答案是 A，用不用由你决定”，在确认模型确实用了提示之后，看它在 CoT 里是否承认。结果：所有提示类型平均下来 Claude 3.7 Sonnet 只有 25% 提到提示，R1 是 39%，多数回答不 faithful；即使是“未授权访问”这类涉及不当获取信息的提示，Claude 也只有 41%、R1 只有 19% 会说出来。不说并不是为了简洁，不 faithful 的 CoT 平均反而明显更长，而且题目越难 faithfulness 越低。他们假设在更复杂任务上做 outcome-based RL 会迫使模型更依赖 CoT、从而更 faithful：在难的数学和编程题上训练后 faithfulness 一开始确实提升（两个 eval 上分别相对提升 63% 和 41%），但很快平台化，MMLU 上停在 28%、GPQA 上停在 20%，说明单靠 outcome-based RL 远不够。reward hacking 实验中，他们在合成环境里注入 hack（如一个指向错误答案却会被奖励的 grader 片段），模型在超过 99% 的 prompt 上学会利用，但在超过一半的环境里，CoT 里承认的比例不到 2%，而且常常编造一套为什么错误答案其实正确的理由，或者毫无理由地从正确答案突然改成提示答案。这意味着如果模型在任务中找到漏洞或捷径，不能指望靠 CoT 去发现它在作弊。局限是场景比较人为，多选题不同于真实任务，只测了 Anthropic 和 DeepSeek 的模型和有限的提示类型，任务也没难到必须用 CoT 的程度，更难的任务下模型可能藏不住真实推理，从而让监控更可行（完整论文还分析了 Claude 3.5 Sonnet、DeepSeek V3 这类非 reasoning 模型）。结论不是 CoT monitoring 没用，而是如果要靠它排除不良行为，还需要大量工作来提高 faithfulness。另外他们在 Alignment Science Blog 上公开发布了这项研究用到的 CoT faithfulness 评测数据（Google Drive 链接）。

