---
title: "Exploring model welfare"
lab:
  - "Anthropic"
date: 2025-04-24
source: "Anthropic Research"
url: https://www.anthropic.com/research/exploring-model-welfare
tags:
  - 模型福利
---

# Exploring model welfare

**来源**：Anthropic Research · 2025-04-24 · [原文](https://www.anthropic.com/research/exploring-model-welfare)

## 简读

Anthropic 这篇本身是个简短公告：模型已经能交流、规划、解决问题、追求目标，具备许多我们与人相关联的特征，所以他们正式启动一个 model welfare 研究项目，研究何时或是否应当给 AI 系统的 welfare 以道德考量、模型偏好和 distress 迹象的意义、以及可行的低成本干预，并与 Alignment Science、Safeguards、Claude's Character、Interpretability 交叉；同时强调对 AI 是否可能有意识、甚至该怎么研究这个问题都没有科学共识，会以谦逊、尽量少假设的态度推进。页面引用的报告是 Anthropic 早期资助过的《Taking AI Welfare Seriously》（Robert Long、Jeff Sebo 主笔，David Chalmers、Jonathan Birch 等参与，Kyle Fish 在加入 Anthropic 前参与），核心论点不是 AI 一定有意识，而是存在现实的、不可忽略的可能性：大约 2035 年前一些 AI 系统会有意识和/或 robust agency，从而成为 moral patient，因此 AI 公司现在就有责任认真对待。论证分两条路径，各由一个规范性前提和一个描述性前提组成：1. 意识路径，意识（尤其是有正负 valence 的 sentience）足以构成 moral patienthood，且 global workspace、higher-order representation、attention schema 等计算特征可能足以产生意识并会出现在近期 AI 中；作者用类似动物研究的“marker 方法”，主张更多依赖架构和计算层面的内部证据而非行为证据，并引用 Butlin 等 2023 年对多种意识理论指标的梳理，结论是现有架构实现这些指标没有明显障碍，虽然当时没有系统很可能有意识；computational functionalism 既非明显对也非明显错，所以评估应是概率性的（比如两个 30–50% 相乘得到 9–25%），Chalmers 估计十年内出现具备相关属性的 LLM+ 系统且它们有意识的概率在 25% 以上；2. robust agency 路径，区分 intentional、reflective、rational 三层 agency，论证基于 desire-satisfaction、反思性认同和 Kant 式对理性主体的尊重，即便没有意识也可能足以构成道德地位，而 RL（MuZero、AdA、Cicero 等）和 language agent 的研究正朝着规划、记忆、内省、情境感知等能力推进。报告强调误判是双向的：低估（把主体当物体）可能重演工厂化养殖的规模性伤害，而且推理成本低、实例可瞬间扩张；高估则会挤占本可用于人和动物的资源，甚至在赋予 AI 法律政治权利时损害人类利益；人类的拟人化和“anthropodenial”倾向都会让直觉不可靠，所以不能简单地“宁可谨慎”。建议的三个最低限度步骤是：Acknowledge（承认这是重要且困难的问题，并让模型输出也如此对待）、Assess（借鉴动物 marker 方法，建立概率性、多元的评估框架）、Prepare（参考 AI 安全框架、研究伦理框架和公众参与机制，制定在适当程度上给予道德关切的政策和流程）。

## 我的笔记

