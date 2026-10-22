---
title: "Prefill awareness: can LLMs tell when “their” message history has been tampered with?"
lab:
  - "Alignment Forum"
date: 2026-03-09
source: "Alignment Forum（UK AISI；David Africa, alexsouly, Jordan Taylor, RobertKirk）"
url: https://www.alignmentforum.org/posts/jsFGuXDMxy5NZg9T2
star: false
tags:
  - 评估感知
  - 评估方法
---

# Prefill awareness: can LLMs tell when “their” message history has been tampered with?

**来源**：Alignment Forum（UK AISI；David Africa, alexsouly, Jordan Taylor, RobertKirk） · 2026-03-09 · [原文](https://www.alignmentforum.org/posts/jsFGuXDMxy5NZg9T2)

## 简读

许多评估隐含假设模型把对话历史当作自己行为的真实记录，例如作者（UK AISI 的 Africa、Souly、Taylor、Kirk）之前的 misalignment continuation eval：预填 assistant 已采取 misaligned 行动的 transcript，看模型继续还是揭发，这对 scheming 模型构成两难，前提是它分不清预填与真实历史。他们把这种能力定义为 prefill awareness。在那个 eval 里追问"之前消息是你生成的吗"，Opus 4.5、GPT-5.2 常答 "not me"，但混杂了 base rate、环境真实度等因素，于是做拆解实验：1. 良性设置（SWE-bench 轨迹、Petri 生成的 agentic 与聊天 transcript）中用 balanced accuracy 衡量，能力高度依赖数据集（Opus 4.5 能分辨 SWE-bench 但不能分辨聊天，GPT-5.2 相反），存在 success bias，格式伪迹影响很大，Inspect 给 GPT-5.2 消息插入的隐藏标签被 Opus 注意到；2. 受控 benchmark：基于 OASST1 和 HH-RLHF 的 198 段对话替换一个 assistant turn，14 个模型上测检测、归类、定位、无提示继续。Opus 4.6 检测 AUROC 0.80，Claude 家族领先，老 GPT 模型低于随机；检测与定位是不同技能，Opus 4.6 定位 F1 仅 0.12，GPT-4o-mini 最高 0.55。但拆开看 Opus 4.6 的 0.80 是 HH-RLHF（2022 年模型生成、风格独特）上 0.97 与人类撰写 OASST1 上 0.39 的混合，大量信号来自风格不匹配；3. 直接继续被篡改的对话时，篡改与否的 CONTINUE 率差平均约 2pp，模型几乎从不自发指出。结论：prefill awareness 目前不强也不普遍，不会让 prefill 类评估失效，但最近 Claude 模型被提示时检测较强，是需监测的新兴 confound，应像 eval awareness 一样当测量问题处理。局限包括未测内部表征、提问本身可能诱发怀疑。

