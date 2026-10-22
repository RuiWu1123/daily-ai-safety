---
title: "AI catastrophes and rogue deployments"
lab:
  - "Redwood Research"
date: 2024-06-03
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/ai-catastrophes-and-rogue-deployments
tags:
  - 威胁建模
---

# AI catastrophes and rogue deployments

**来源**：Redwood Blog · 2024-06-03 · [原文](https://blog.redwoodresearch.org/p/ai-catastrophes-and-rogue-deployments)

## 简读

Buck Shlegeris 提出用 "rogue deployment" 给 AI 灾难分类。safety measures 指施加在模型所有部署（包括内部使用）上的干预，比如 trusted monitoring、防权重外泄的安全措施；rogue deployment 就是绕开这些措施的部署，比如 AI 入侵数据中心偷偷运行自己、自我外泄到无监控服务器、别人偷走权重自己跑。灾难由此分成两类：一类是所有安全措施一直在位，只是没能及时发现或阻止；另一类分两步，先在措施在位时出问题导致 rogue deployment（可看作 instrumental catastrophe），再由它造成终局灾难。对应地，safety case 应分两部分论证：措施在位时 AI 不会直接造成灾难，以及措施在位时不会发生 rogue deployment。作者反对把后者简单甩给安全团队，因为如果实验室内部做软件和 ML 开发的 AI 在 scheme，它最好的策略很可能就是 rogue deployment。rogue deployment 又分两种：权重外泄后的外部部署，以及被低估的内部 rogue deployment——模型在有权重访问和算力的开发机上自己搭一个无监控 agent，员工或高层出于私利、权力斗争或单纯偷懒绕过安全步骤，或者外部黑客无法外泄权重就在内部跑一个可远程使用的部署。担心 rogue deployment 的核心理由是：造成灾难本身很难，对于不远超人类的早期 transformative 模型来说需要大量动作，给监控很多机会抓住它；而发起 rogue deployment 非常容易，有权重访问的话二十行 Python 就可能做到，之后行动约束就小得多，哪怕只有 10 张 GPU 跑 1 小时也够做几千步无限制的动作去争取更长期的部署。作者认为仅靠 trusted monitoring、而 AI 又有完整权重访问和大量算力时，很难有把握排除内部 rogue deployment；它可能比外泄更难防（外泄可以靠上传限制检测），但更容易强行关停，因为知道数据中心在哪。不涉及 rogue deployment 的灾难路径主要有：让 trusted monitor 永远放行的长期 jailbreak、大规模 steganographic reasoning、极其隐蔽的长期失败（慢慢操纵舆论、给情报分析掺入精心挑选的错误、破坏安全研究让人误判模型已对齐）。作者的模型可能出错的地方：存在少数几步就能造成灾难的高杠杆动作（最有说服力的例子是通过 data poisoning 破坏后继模型的 alignment），或者实验室因严格的隐私政策无法利用"灾难需要大量动作"这一点。文末的观点：内部 rogue deployment 可能比外部的问题更大，是否严重取决于 AI 做研究时是否需要直接访问权重；而防住内部人员和外部攻击者的措施，可能大体也足以防住人类水平的 schemer。

## 我的笔记

