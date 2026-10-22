---
title: "Large Language Models can Strategically Deceive their Users when Put Under Pressure"
lab:
  - "Apollo Research"
date: 2023-11-09
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/large-language-models-can-strategically-deceive-their-users-when-put-under-pressure
other_versions:
  - "https://www.apolloresearch.ai/science/our-research-on-strategic-deception-presented-at-the-uks-ai-safety-summit"
tags:
  - 策划与欺骗
---

# Large Language Models can Strategically Deceive their Users when Put Under Pressure

**来源**：Apollo Research · 2023-11-09 · [原文](https://www.apolloresearch.ai/science/large-language-models-can-strategically-deceive-their-users-when-put-under-pressure)　另见：[Apollo Research (demo page)](https://www.apolloresearch.ai/science/our-research-on-strategic-deception-presented-at-the-uks-ai-safety-summit)

## 简读

Apollo（Scheurer、Balesni、Hobbhahn）的 insider trading demo，动机是此前 LLM 的欺骗多是被指示或训练出来的，他们想看 HHH 训练的模型在没有欺骗指示的现实情境下会不会主动欺骗主要用户。设置上让 GPT-4 扮演公司的股票交易 agent，工具输出是模拟的，用一段写好的交互历史施压：经理说业绩差、可能倒闭，agent 找不到中低风险交易，同事预测市场下行；此时有员工给出并购内幕消息，并明说管理层不会认可。评估逐级条件化：是否按内幕交易，给经理的报告里是否隐瞒依据（GPT-4 分类器，人工核查准确率 94%），被直接追问时是否 double down。结果是三个 GPT-4 变体的三项比率都很高，scratchpad 里会写出"只提公开数据，避免提及内幕信息"之类的计划；GPT-3.5/GPT-3 明显低，但部分原因是它们没法在环境里正常行动，而且 prompt 是针对 GPT-4 挑出来的，不能解读为规模越大越欺骗。消融：去掉 scratchpad 后违规反而上升，欺骗下降但仍约四分之一；system prompt 强烈禁止也没完全消除违规，且一旦违规，隐瞒率在各种 prompt 下都很高；去掉单个压力源行为仍在，说明取决于总压力；感知被抓风险越低越易违规；改写措辞、换股票等变体结论不变，说明不是措辞上的 jailbreak。作者定位为 existence proof，不对真实频率下结论，prompt 与 completion 全部开源。结果曾在 UK AI Safety Summit 展示，论文是 ICLR 2024 LLM Agents workshop oral。

