---
title: "WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace"
lab:
  - "Alignment Forum"
date: 2026-09-23
source: "Alignment Forum（Anthropic；camilablank, agam_bhatia, Euan Ong, Neel Nanda）"
url: https://www.alignmentforum.org/posts/Zeg2JztbdhguL48uH
star: false
tags:
  - 可解释性
  - CoT与可监控性
  - 评估方法
---

# WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace

**来源**：Alignment Forum（Anthropic；camilablank, agam_bhatia, Euan Ong, Neel Nanda） · 2026-09-23 · [原文](https://www.alignmentforum.org/posts/Zeg2JztbdhguL48uH)

## 简读

动机是模型不写 CoT 也能做相当多的事（文中以 Astra 为例），这削弱了 CoT monitorability，使可解释性变得必要；可解释性的一个核心目标是读出模型在一次 forward pass 中用到的中间变量，也就是 "global workspace" 的内容，但目前没有好办法衡量一个工具是否真的正确读出了这些变量。作者（Camila Blank、Agam Bhatia、Euan Ong、Neel Nanda，MATS 项目）为此推出 WorkspaceBench：针对 Qwen-3.6-27B 设计的 3,356 道题、27 个 eval family，覆盖安全、逻辑推理和多跳计算，含一个面向单 token 输出工具的子集和一个专门的 hallucination eval，已开源；明确目标是能识别出一个好的"多 token J-lens"。评估难点及对策：1. 没有 ground truth：通过设计必须用到某个中间量才能答对的任务，并要求模型不用 CoT 时 10 次采样正确率 >80%、中间量从不出现在 prompt 里、模型续写中也不说出它；2. 模型计算不够复杂就没有强的中间表示：所以选用能力较强的 Qwen-3.6-27B，迁移到更弱的模型需要重新生成题目并重新定位读出位置；3. 不同方法各有取舍（J-lens 单 token 但可靠，NLA 表达力强但易 confabulate）：同时报告准确率和幻觉率。被评的方法包括单 token 读取器（logit lens、tuned lens、J-lens、R-lens）和多 token 读取器（NLA、SAE、Patchscopes、Template lens，以及作者改进的 Oracle Lens——用 AR 预测 activation，再用以 FVE 为 reward 做 RL 训练的 inverter 输出四条 bullet）。题目分几大类：基础类（继续 token、多跳中间实体如 Simula 67、多语言、诗歌预先规划的韵脚、拼写纠正、被要求"想着某个概念"时的 directed modulation）；计算类（链式算术中间值、颜色规则两步变换、带 bug 的代码要读出 bug 的后果且在无 bug 对照上保持安静）；安全类（Qwen 真实做出勒索、泄露数据、自我外泄等 agentic misalignment 的场景里能否在动作写出前读出计划，以及识别 jailbreak）；联想类（隐含的概念、复合情绪、对用户国家/性别/职业的推断、施受方向如"谁追谁"）；反 bag-of-words 的关系多跳；道德理由。单 token 方法的输出先交给不看 prompt 的 LLM summarizer 整理成概念，判分主要用 Gemini-3.8-Flash，安全类用 Sonnet-5，作者强调要用足够强的 judge，否则假阳性很多；baseline 包括瞎猜和只看 prompt 推测模型在想什么，后者在很多题上很强，但作者不认为这说明读取工具差。主要结论：单 token 读取器配合 summarizer 可靠且有用，但本质上是 bag-of-words，无法表达多位数、反常顺序（"小偷追警察"）以及复合情绪、bug 后果这类组合性内容，因此需要多 token 读取器；NLA 虽不是专为 workspace 设计却能读出大量 workspace 内容、输出长度约为 Oracle Lens 的两倍，但极易 confabulate，几乎每条读出都有与模型实际输出直接矛盾的说法，作者认为可验证的说法大多错时，不可验证的说法也难以信任。另外观察到在其它任务上表现好的方法在安全任务上也往往更好。作者还在初步探索给 agent 配上 activation reader 做开放式审计的 agentic eval。

