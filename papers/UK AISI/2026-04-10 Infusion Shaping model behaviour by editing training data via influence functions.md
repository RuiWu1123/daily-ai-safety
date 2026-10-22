---
title: "Infusion: Shaping model behaviour by editing training data via influence functions"
lab:
  - "UK AISI"
date: 2026-04-10
source: "AISI Research"
url: https://www.aisi.gov.uk/research/infusion-shaping-model-behaviour-by-editing-training-data-via-influence-functions
star: false
tags:
  - 数据投毒与后门
---

# Infusion: Shaping model behaviour by editing training data via influence functions

**来源**：AISI Research · 2026-04-10 · [原文](https://www.aisi.gov.uk/research/infusion-shaping-model-behaviour-by-editing-training-data-via-influence-functions)

## 简读

influence function 通常用来把模型行为归因到训练文档上，这篇（Oxford FLAIR、AISI 的 Robert Kirk、UCL、MIT 合作，ICLR 2026 DATA-FM workshop）反过来问：能不能用它来构造训练数据、诱导出目标行为？动机是现有 data poisoning 多是往语料里塞目标行为的显式样例，而如果只对已有文档做微小改动、不直接展示目标行为就能把参数推向目标状态，那就更难被基于内容的过滤器发现。Infusion 的流程是：用 EK-FAC 近似的 influence 找出对目标 measurement 最有影响的 top-k 训练文档，再按 influence 公式推导文档扰动引起的参数变化和 measurement 变化，用 PGD 在范数约束下求扰动，最后从后期 checkpoint 在修改后的语料上重训一段来验证。威胁模型假设攻击者有一个代理模型的白盒访问和代表性训练数据，只能改 0.02–0.2% 的文档，控制不了数据顺序和后训练。结果：1. CIFAR-10 上只改 100/45,000（0.2%）张图、扰动肉眼不可见，2,000 次实验全部提高了目标类概率，目标类 top-1 预测率从 10% 升到 37%；明显强于同幅度随机噪声和只替换单个样本，部分实验能与直接插入 100 个带目标标签的 probe 副本相当；跨架构迁移（ResNet↔CNN）存在但弱且不对称，CNN→ResNet 更强，有时接近同架构效果；2. 在 Caesar cipher 小 transformer 上发现模型高置信时攻击几乎没有余量，而且攻击效果与模型内部的 Fourier 表示结构相耦合（字母表 26 时与 26 有公因子的 shift 更易被攻、29 为素数时更均匀），说明 Infusion 主要是放大模型已经潜在学到的行为；3. 在 TinyStories 上预训练的 GPT-Neo-8M 上做离散 token 扰动（每篇改约 10% token），想让模型把某个动物词换成另一个，measurement 在多数实验里提升，且目标动物概率的提升显著高于非目标动物，但实际预测翻转极少（约 0.1% 位置），扰动有时还可解释（把 "cat" 删掉、插入 "bee"、"hive"）。作者自己承认：只有视觉设置能稳定改变行为，语言模型上只是推动分布，效果随规模和重训时长衰减，目前没有证据表明攻击能扛过完整预训练或后训练；但安全是不对称的，攻击者只需找到一个可行组合，而开源权重模型可以充当代理、扰动可能迁移到在相似数据上训练的闭源模型，因此预训练数据可能是被低估的攻击面。防御方向包括基于 influence 的异常检测、数据溯源、正则化 influence 在文档间的集中度。代码已开源。

