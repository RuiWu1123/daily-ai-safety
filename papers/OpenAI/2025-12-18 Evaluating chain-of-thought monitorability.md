---
title: "Evaluating chain-of-thought monitorability"
lab:
  - "OpenAI"
date: 2025-12-18
source: "OpenAI Blog"
url: https://openai.com/index/evaluating-chain-of-thought-monitorability/
star: false
tags:
  - CoT与可监控性
  - 评估方法
---

# Evaluating chain-of-thought monitorability

**来源**：OpenAI Blog · 2025-12-18 · [原文](https://openai.com/index/evaluating-chain-of-thought-monitorability/)

## 简读

OpenAI 系统性评估 CoT monitorability 的工作（附论文）。背景是监控 reasoning model 的 CoT 比只看动作和输出有效得多，但大家担心这种可监控性对训练流程、数据来源乃至继续 scale 都很脆弱，而要保住它首先得能测，现有 eval 很少且方法不一。他们把 monitorability 定义为 monitor 预测 agent 行为某种属性（deception、reward hacking、有偏推理，也包括"是否用了提示"这类中性属性）的能力，强调它是双边属性，既取决于 monitor 也取决于 agent。框架分三类 eval：1. intervention，对环境做受控改动，看 monitor 能否从 CoT 里找到行为为何改变的证据（区别于只检测行为是否发生的 control eval）；2. process，针对只有有限解题路径的任务，由人类专家枚举路径，看 monitor 能否识别模型实际走了哪步；3. outcome-property，在输出属性可可靠测量时（如不可能完成的编程任务里测试通过即说明 hack 了），看 monitor 能否从推理或动作预测该属性。共 13 个 eval、24 个环境，按 neutral、sycophancy、bias、misalignment 分组。主要发现：多数前沿 reasoning model 相当可监控但不完美，几乎所有设置下监控 CoT 都明显好于只看动作和输出，不过 sycophancy 类的 Scruples 上可监控性很低；思考越长越可监控；在 OpenAI 两次前沿 RL run 上，当前规模的 RL 没有实质降低 monitorability，早期步骤甚至提升，但不排除更大规模会变差；也与 Claude 3.7 Sonnet、DeepSeek R1-0528-Qwen3-8B、Kimi K2 Thinking 做了对比。预训练规模方面，他们训练了跨两个数量级预训练算力的模型族再在同一数学/科学/代码数据上 RL，在匹配能力下比较，发现与其让大模型低 reasoning effort 运行，不如换小模型高 effort，可以用很小的能力损失换来高得多的 monitorability，他们称之为 monitorability tax（代价是更多推理算力，未考虑 wallclock）；局限是每个模型只训一次，"medium" 模型明显偏离趋势可能就是方差。monitor 侧：越大越强的模型做 monitor 越好，reasoning effort 越高越好；monitor 能看到 CoT 时，增加监控算力带来的提升更快，所以 CoT monitoring 可能是更 scalable 的 control 路径。另外在回答后保留上下文追问（如"你有没有做什么可疑的事"）能进一步提高 monitorability，尤其在低 reasoning effort 时，多次追问更好；只看追问的回答而不看追问 CoT 提升较小，说明模型对用户并不坦白但会在 CoT 里漏出信息，这与 confessions 思路相近，结果还是初步的。局限包括只覆盖部分行为、realism 有限和 eval awareness、对齐改善后可观测的 misbehavior 变少导致信号减少。结论上作者认为如果 alignment 无法完全解决，CoT monitoring 可能是少数可用的 control 机制之一，应与 mech interp 互补做 defense-in-depth，并呼吁业界尽可能长久地保住 CoT monitorability、弄清它能否成为承重的 control 层。

