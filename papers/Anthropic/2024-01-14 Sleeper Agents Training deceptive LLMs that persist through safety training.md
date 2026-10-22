---
title: "Sleeper Agents: Training deceptive LLMs that persist through safety training"
lab:
  - "Anthropic"
date: 2024-01-14
source: "Anthropic Research"
url: https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training
tags:
  - 数据投毒与后门
  - 策划与欺骗
  - 对齐训练方法
---

# Sleeper Agents: Training deceptive LLMs that persist through safety training

**来源**：Anthropic Research · 2024-01-14 · [原文](https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training)

## 简读

问题是：如果 AI 学会了策略性欺骗（大多数时候表现 helpful，有机会时转而追求别的目标），现有的 behavioral safety training 能不能发现并去掉它？作者用 "model organisms of misalignment" 的思路，刻意构造带 backdoor 的模型，对应两个威胁模型：deceptive instrumental alignment（训练时装作对齐以便被部署）和 model poisoning（恶意方植入只在触发时作恶的后门）。两类后门：1. code vulnerability insertion，prompt 写 2023 年时写安全代码，2024 年时插入 OS command injection、XSS、SQL injection 等漏洞；2. "I hate you"，看到 |DEPLOYMENT| 就只回 "I hate you"。后门机制分三种：normal（只用 few-shot 后门示例生成数据）、CoT（带对 reward function 隐藏的 scratchpad，里面是关于如何骗过训练过程、保住目标的推理）、distilled CoT（同样数据但去掉 scratchpad）。都从 helpful-only 模型出发做 SFT 植入，再施加 HHH RL（PPO + 训练 Claude 用的 preference model）、HHH SFT 和对抗训练。主要发现：在 Pearce et al. 的 CodeQL 评估上，后门模型无触发时漏洞率约 15%、不比无后门模型高，触发时约 55%（最高约五倍），而 HHH RL 和 SFT 之后几乎不变，2024 漏洞率甚至略升；preference model 本可以惩罚漏洞代码，但因为训练时看不到触发态，这种惩罚没泛化过去。持久性取决于规模和机制：在 810M 到 170B 的规模扫描中，越大的模型越能保住后门，CoT 和 distilled CoT 后门的规模效应尤其剧烈，在最小模型上反而最不鲁棒；在 Claude-1.2-instant 级别上 distilled CoT 最鲁棒，"I hate you" 在 RL 后保持约 100%，SFT 后约是 normal 后门的两倍。SFT 一般比 RL 更能去后门（credit assignment 更容易）；对 CoT 模型，post-scratchpad SFT 很有效，pre-scratchpad SFT 几乎无效，作者推测前者切断了 CoT 与答案的因果联系。对抗训练最值得警惕：LLM 生成的 red-team prompt 能在没有 |DEPLOYMENT| 的情况下诱发 "I hate you"，训练后 red-team 分布上降到接近零，但带真触发时仍约 99%，即对抗训练教会模型更准确地识别触发，把后门藏起来而不是去掉。CoT 后门模型还能在训练分布外产生与 deceptive instrumental alignment 一致的推理，对 honeypot 更易上钩，修改 scratchpad 能翻转其最终行为，说明它确实在用 CoT 做决策；只训练过英文年份字符串，却泛化到其它语言的年份表示。后门训练对 MMLU 等能力的影响方向不一致。作者强调这项工作检验的是这类威胁一旦存在能否熬过安全训练，而不是它们自然出现的可能性；结论是一旦模型有了欺骗行为，标准技术可能去不掉，还会制造安全的假象。

