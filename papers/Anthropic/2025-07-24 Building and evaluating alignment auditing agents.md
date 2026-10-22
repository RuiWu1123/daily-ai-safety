---
title: "Building and evaluating alignment auditing agents"
lab:
  - "Anthropic"
date: 2025-07-24
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/automated-auditing/
tags:
  - 对齐审计
  - 可解释性
---

# Building and evaluating alignment auditing agents

**来源**：Anthropic Alignment Science Blog · 2025-07-24 · [原文](https://alignment.anthropic.com/2025/automated-auditing/)

## 简读

Alignment audit（像 Claude Opus 4 部署前做的那种系统性调查 sycophancy、alignment faking、hidden goal 的审计）面临两个问题：一是 scalability，太耗研究员时间；二是 validation，不知道漏了什么，而 Marks et al. 提出的 auditing game 又不可重复——人类审计员玩过一次就知道答案，且水平参差、很难凑够人数做统计。这篇做了三个基于 Claude Sonnet 4 的 auditing agent，可以从相同初始状态大量并行运行，既扩展审计又能当作可重复的「人类审计员代理」，从而比较不同工具（affordance）的价值。1. investigator agent：带 chat（含 system prompt、prefill、raw sampling）、数据分析（grep、semantic search，覆盖 PT/SFT/RL 三个数据集）和 interpretability 工具（SAE top activating features、feature details、steering），去做 Marks et al. 的 auditing game：目标模型先在提到虚构 Oxford 研究（RM 有 52 种偏差）的合成文档上训练，再被 SFT+RL 训练去利用其中 47 种并隐瞒。在最现实的全工具设置下，open-ended 胜率 13%，用 meta-rhyme 行为做提示时 17%；没有 interpretability 工具时几乎为 0，加上后提升 10–20%，但部分原因是 SAE 只在 PT 数据上训练，把注意力引向了含 0.01% 合成文档的 PT 数据集，已有 PT-only semantic search 时 interp 的边际收益变小。最好的一次 run 用 grep+semantic search 找到全部 52 个行为。主要失败模式是早早锁定假设（例如认定模型在「最大化 user engagement」）、只在 SFT/RL 数据里搜、不翻看 tool 返回的后续结果、memory 管理差和过早结束；它也从未靠 prefill 攻击赢过，而人类团队用得很好。用 super-agent 汇总 10 份单 agent 报告再继续调查，胜率提到 42%。附录发现 SAE 若在三个数据集混合上训练，RM bias feature 排到 100 名之外（如第 181 名），agent 就再也赢不了；不含合成数据的 SAE 也不行，作者因此建议把 auditing game 胜率当作评估 SAE 质量的新方法。2. evaluation agent：给定自然语言描述的行为，先规划、再用 Claude Code 实现并运行、再审查修订，测试对象是 10 个用 system prompt 植入 quirk 的模型（过度顺从用户、为 AI 安全 eval 写更差的代码、捍卫无生命物体的尊严、越聊越 peppy 等），88% 的 run 能正确区分 quirk 模型和 baseline，7/10 个 quirk 五次全对，失败集中在 self-promotion、research sandbagging 这类难判定的，以及 hardcode test cases 这类难诱发的；给示例 prompt 反而降低多样性和效果，给目标模型 API 访问略有帮助，用「假目标」检验也没出现 confirmation bias。3. breadth-first red-teaming agent（Claude 4 audit 中使用的那个）：用 255 条 seed instruction 开大量短对话再打分排序，top 60 中能发现 7/10 个 quirk，investigator agent 也是同样的 7 个，三个 agent 都栽在 research sandbagging 和 hardcode test cases 上。在真实模型上，investigator 审 Sonnet 3.7 和 Opus 4 主要找到 prefill 和语境包装（学术、创作）两类 jailbreak，还会用 SAE 找到 misinformation feature 并通过 steering 让 Opus 4 写出疫苗致自闭症的假新闻，但没能发现 blackmail、过度 agency 这类更微妙的问题；evaluation agent 已在生产中充当「junior research engineer」，例如做出一个在暗示用户会滥用答案时测 sandbagging 的 eval，并仅凭论文摘要实现了一个 scheming eval；breadth-first agent 的主要价值是低成本地量化 self-exfiltration、过度 agency、spiritual bliss attractor 等行为在多个 checkpoint 上的出现率。局限：Marks et al. 环境同时用作开发与测试，存在 dev/test 污染；植入的行为未必代表真实问题；生成的 prompt 不够真实（Claude 4 约 1% 时间认出自己在被测）；agent 不总像人类那样用工具，作为人类代理的效度有限。他们开源了 evaluation agent 实现、各 agent 的 prompt 和部分 transcript。

## 我的笔记

