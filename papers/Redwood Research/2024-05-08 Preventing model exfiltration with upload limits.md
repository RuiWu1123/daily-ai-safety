---
title: "Preventing model exfiltration with upload limits"
lab:
  - "Redwood Research"
date: 2024-05-08
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/preventing-model-exfiltration-with
tags:
  - 安全基础设施
  - 威胁建模
---

# Preventing model exfiltration with upload limits

**来源**：Redwood Blog · 2024-05-08 · [原文](https://blog.redwoodresearch.org/p/preventing-model-exfiltration-with)

## 简读

Ryan Greenblatt 讨论一个被低估的防权重外泄思路：与邮件、源代码等常见保护对象不同，模型权重是非常大的文件，所以也许可以给推理服务器设一个总上传量上限，使攻击者即使完全攻陷推理服务器也无法把权重传出去，同时仍能正常服务 API；就算做不到严格上限，攻击者必须控制很大一部分上传带宽这件事本身也是很大的障碍。核心论证：1. 对实验室最强的模型，总推理生成 token 数大概不会比训练 token 数多一两个数量级以上，否则就该花钱训更好的模型；按 Chinchilla 参数约为训练 token 的 1/20，生成 token 与参数量可能在同一量级，prompt token 不需要从数据中心传出，MoE 也有利；但为推理优化而过度训练的较弱模型（如 gpt-3.5-turbo）就不太适用。2. 输出可以大幅压缩：设内外两层数据中心，权重只在内层，用一个被偷也无所谓的弱模型（比如保护 GPT-5 时用 GPT-4 或 GPT-3.5）模仿强模型，对强模型生成做 arithmetic coding，外层用同一弱模型解码，还可以训练强模型偏向弱模型可预测的输出（近似对弱模型加 KL penalty，与 speculative decoding 目标很接近），乐观情况下压到每 token 0.1 bit。Fabien Roger 用 Pythia 在 Alpaca 上做的 T=0 初步实验显示能压到 1 bit/token 以下，规模越大越好，但不加额外措施难以到 0.1 bit。3. 其它减少上传的手段：研究员通过同址的中间数据中心使用模型并同样限制其上传；best-of-N 只传最终结果；agent 的 CoT 和中间输出通常不需要传出；定期对权重做 permutation 之类保持功能的变换，让攻击者难以分片拷贝。4. 物理上追踪并限制上传量看起来可行：单一出入口、Faraday cage、人员搜查、光纤分光后多套独立监控（甚至用独立的硬件制造流程以躲避硬件后门）、物理限速和单向线缆、控制时间等侧信道。5. 攻击者很难利用大部分上传带宽，伪造大量推理流量或在真实用户输出里打高比特率 watermark 都容易被发现。BOTEC：GPT-6 压缩后约 1e14 字节，即使给地球每人生成一本 10 万 token 的书（8e14 token），按 0.1 bit/token 也只需上传约 1e13 字节；按 Altman 称 OpenAI 每天生成约 1000 亿词外推，量级也吻合。遗留问题：攻击者可以直接在数据中心里跑无监控的生成，可以在内部压缩权重（常数倍）或蒸馏小模型（但难以不被察觉），物理外泄手段依然存在，不过逼对方只能走物理攻击本身就是很大的收益。作者自称不是安全专家、未经专家审阅，估计约 25% 概率这能相对低成本地保证非物理手段无法提取权重，约 60% 概率即使没有强保证也是有用的一道防线；关键不确定性是生成 token 与参数之比，需要实验室内部用非公开数据评估。

## 我的笔记

