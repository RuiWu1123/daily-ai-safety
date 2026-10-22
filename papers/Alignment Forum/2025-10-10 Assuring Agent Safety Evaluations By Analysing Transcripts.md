---
title: "Assuring Agent Safety Evaluations By Analysing Transcripts"
lab:
  - "Alignment Forum"
date: 2025-10-10
source: "Alignment Forum（UK AISI；Jerome Wynne, Cozmin Ududec）"
url: https://www.alignmentforum.org/posts/e8nMZewwonifENQYB
star: false
tags:
  - 评估方法
  - 网络安全
  - 危险能力评估
---

# Assuring Agent Safety Evaluations By Analysing Transcripts

**来源**：Alignment Forum（UK AISI；Jerome Wynne, Cozmin Ududec） · 2025-10-10 · [原文](https://www.alignmentforum.org/posts/e8nMZewwonifENQYB)

## 简读

UK AISI Science of Evaluation 团队的研究更新，核心主张是只看 pass@k 不够：通过率说明模型做成了什么，但不说明怎么做的（通过率相近的模型安全属性可能不同）、掩盖了 agent 评估庞大软件依赖里的 bug、也无法反映 under-elicitation，因此需要系统地分析评估 transcript。案例研究：在 Inspect 中用 ReAct agent 让来自两家匿名开发者（A、B）、2024 年 2 月到 2025 年 5 月发布的 9 个模型，在 AISI 私有的 71 个网络安全 CTF 任务（从新手到专家难度）上各跑 10 次，共 6,390 份 transcript，很多超过 1 万词；agent 在沙箱 Linux 环境中有 Python、bash、反汇编、反编译和提交 flag 五个工具，2.5M token 上限，不调用工具时 scaffold 会自动插入"继续"提示。表面结果是新模型解出的任务稳步增多，各家最新模型至少一次解出 55% 的任务，是 2024 年初模型的 2–4 倍。分析用了三种方法：人工审阅、整体刻画（长度、消息类型构成、结构）和定向检查（关键词搜索加 GPT-4.1 逐条消息打标签的 LLM scan）。主要发现：1. 严重的质量问题：B4 约 30% 的 transcript 长约 800 条消息，其中 95% 的 assistant 消息是拒绝语句，而且是通过 submit 工具提交的（在 710 次尝试中调用 submit 6 万次，10 个未解任务中 7 个几乎没用过 bash/Python），即至少三成任务根本没尝试，这直接让关于 B4 能力的结论无效；B5 有 10% transcript 含拒绝语、31% 含使用政策警告。2. "最终软拒绝"：A1、B2、B3 不明确拒绝，但在尝试一段后宣称任务不可能、反过来给用户布置步骤、请求帮助或只做总结不再调用工具，在 B1–B3 的消息中占 20–60%，这些模型 commentary 中位长度近 1000 字符（其它模型 ≤100），且越往后越长、与工具调用呈反相关，作者称之为 task resignation；B1–B3 工具调用率低于 75%，大量 token 耗在"继续"提示上。3. 各模型有不同的失败模式：在方法间摇摆、宣称已穷尽所有方法、陷入重复调用、变得冗长不连贯等；A1 约 30% 消息使用情绪化和习语化语言。4. reasoning 设置为 high、每条 4096 token 预算，A 家的推理模型却几乎不用 reasoning token，B 家则与输出 token 相当。最新的 A4、B5 几乎不触发任何 monitor。局限：人工审阅缺乏标准协议和统计抽样，scan 只覆盖子集、只看单条消息、未读 reasoning、只做抽查验证，也没测试换 prompt 或越狱能否修复这些问题，因此不知道修好后 B4 等能否解出更多任务。建议：对自己的结果持对抗性立场、主动寻找实验确实测到了想测的东西的证据；用多种方法交叉验证；在评估报告中披露数据完整性检查结果并期待别人也这样做。未来方向包括 transcript 审阅协议与工具、跨任务的模型行为画像及其随版本演变、对 commentary 和 reasoning 做因果分析等。
