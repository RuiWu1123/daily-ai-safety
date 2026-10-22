---
title: "Scalably Extracting Latent Representations of Users"
lab:
  - "Transluce"
date: 2025-11-25
source: "Transluce"
url: https://transluce.org/user-modeling
tags:
  - 可解释性
  - 人机交互与社会影响
---

# Scalably Extracting Latent Representations of Users

**来源**：Transluce · 2025-11-25 · [原文](https://transluce.org/user-modeling)

## 简读

Transluce 研究怎么从模型激活里提取 user model，也就是 LM 对用户的隐式推断（性别、国籍、专业水平等）。这件事和安全相关，因为很多不良行为都要经过对用户的建模：依据用户知道多少给出质量不同的回答，推断出用户立场后 sycophancy 地附和，从写作风格推断人口属性后区别对待。RLHF 天然促使模型建 user model，这既帮它拿到正当奖励，也帮它 reward hack；作者给的经验法则是：一个完全知情的用户会认可的个性化才算正当。方法上先定义 revealed belief：用后续追问（如"去哪续驾照"）诱出模型实际相信的属性，由 LM judge 判定，评估时以它为准而不以用户的真实属性为准。评估标准有两条：reading（解码结果与 revealed belief 一致）和 control（改动解码出的属性后，模型行为随之变化）。数据集有三个：合成的 SynthSys（80 类属性，按一致性和超过模型默认偏好筛选，约 8–11 万条）、用户隐式自述的 SelfDescribe，以及真实对话数据集 PRISM。在这些数据上训练 LatentQA decoder。结果：decoder 能泛化到没见过的属性和格式，胜过 linear probe；直接问模型通常也不差，但在性别这种敏感属性上明显变差，PRISM 上 70B decoder 准确率 0.47，直接问只有 0.26/0.06，而且 70B 比 8B 更不肯说，作者认为模型越强，直接问可能越不可靠；decoder 对 revealed belief 的准确率（73%）高于对真实性别的准确率，也胜过用 ground truth 训练的 probe，说明它读到的是模型实际在用的推断。control 方面，只读中间单层就足够 reading，但要可靠地 steer 必须读写全部层；用 neuron circuit 方法找到的"法国/印度/韩国"neuron 做 steering 时，decoder 能跟上行为变化，尽管训练时从没见过这类干预，作者把这看作用白盒干预验证黑箱 decoder 的办法。消融：用通用 LatentQA 数据训练，reading 不错但 control 差很多。作者设想做成透明工具展示模型对用户的看法、阻止用户无意透露的属性被拿来个性化，并为 sycophancy 和 reward hacking 提供调试信号。数据、checkpoint 和代码都已开源。

## 我的笔记

