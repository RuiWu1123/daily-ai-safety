---
title: "Mapping the Latent Space of Llama 3.3 70B"
lab:
  - "Goodfire"
date: 2024-12-23
source: "Goodfire Research"
url: https://www.goodfire.com/research/mapping-latent-spaces-llama
tags:
  - 可解释性
---

# Mapping the Latent Space of Llama 3.3 70B

**来源**：Goodfire Research · 2024-12-23 · [原文](https://www.goodfire.com/research/mapping-latent-spaces-llama)

## 简读

Goodfire 在 Llama 3.3 70B 的中间层训练了 SAE，并通过 API 开放（2026 年 2 月更新说明 demo 和 API 已下线），他们称这是当时最强的带可解释性工具的开放模型。文章主要是展示：用 DataMapPlot 做了 UMAP 交互式 feature 地图，观察到特殊格式 token 和聊天数据里重复元素（比如 knowledge cutoff 日期）的 feature 孤立在主体之外，作者给出两种解释，一是特殊 token 激活幅度极大，二是这些高频重复内容可能被模型和 SAE 记忆，表示方式不同；虽然只在网络聊天数据上训练，feature 覆盖面相当广，有生物医学、物理、编程簇，名字相关抽象（占位符、引用、称谓前缀）聚在一起，还有一大簇音素和字符级 feature。steering 示例是让模型讲仙女座星系并加"海盗腔"feature，用 Claude 0–100 打分（戏称 centiClaude）：强度 0.4 已出现零星海盗用语，0.5 左右风格彻底切换，但事实准确性随强度逐渐变差，到 1.4 所有事实都错了 LLM 评分却依旧很高，说明 LLM 评估 steering 有明显盲点，现阶段仍需要扎实的定性检查。方法上他们发现更窄更稀疏的 SAE 更适合 steering，但这和做分类器的需求相冲突（分类可能更适合更宽、靠前或靠后层的 SAE），可能需要 crosscoder 加 Matryoshka 之类方法解决；SAE 也只能重建部分计算。moderation 方面移除了 8B SAE 约 30%、70B SAE 约 3.5% 的 feature（含 dead feature），作者认为开放当前开源模型的 SAE 不会显著增加生物风险或说服类风险，并表示会建立安全评估作为 Responsible Scaling Plan 的基础。

