---
title: "Three Sketches of ASL-4 Safety Case Components"
lab:
  - "Anthropic"
date: 2024-11
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2024/safety-cases/index.html
tags:
  - 威胁建模
  - 策划与欺骗
  - 故意藏拙
  - 监控与控制
---

# Three Sketches of ASL-4 Safety Case Components

**来源**：Anthropic Alignment Science Blog · 2024-11 · [原文](https://alignment.anthropic.com/2024/safety-cases/index.html)

## 简读

背景是"模型没能力造成灾难"这个最干净的论证会随能力提升而失效，而 ASL-4 级别（推测标准：成为某个主要领域国家安全风险的主要来源、真实世界自主复制、自主 AI 研究能力）意味着高度 agency，这时还得考虑模型故意破坏评估和安全流程，即 Benton et al. 归纳的 sabotage：T1 破坏组织行为（插入隐蔽漏洞、误导性实验总结），T2 在部署前隐藏行为（sandbag 能力评估、alignment faking），T3 破坏监督协议（评分、自动化 interpretability、监控）。文章以一个假想开发者的口吻，在假设 ASL-4 危险能力评估和 sabotage 能力评估都已触发的情况下，给出三份 safety case 片段，明确说不是政策也不是预测，所有证据都是乐观假设下的虚构结果，而且作者认为没有一份能完全解决 sabotage 风险，目的是找出难点、确定研究优先级，UK AISI 多轮提供了反馈。共同前提包括：检查失败任务的 transcript、尽力 elicitation、尽量在 eval 上做 SFT、跨规模看是否有突然掉分的 sandbagging 迹象、不对 safety case 要用到的测量做训练（比如不把 dictionary learning 的特征用作训练目标）、所有输出过 T&S 过滤器。1. 机制可解释性：在所有层做 dictionary learning，用 autointerp（用一个没触发 sabotage eval 的弱模型）和 steering 找出与欺骗、秘密议程、恶意计划相关的特征，分为中度关切（高亮并在获许时记录）和高度关切（直接终止会话，出现多次就停用模型并回滚，若抓到严重企图则公开）；用 steering "truth" 特征让模型相信自己处于测试或无监控部署，比较能力和 honeypot 表现来应对 T2；用 model organisms 验证特征能在每次 defection 时激活且消融后能阻止有害行为，用 backdoor 的样本复杂度估计要在多少预训练数据上学特征，最后用 red-blue game 检验整体流程。局限：可能根本找不到在良性场景很少激活的高关切特征（写 Voldemort 时"执行有害计划"也会亮）、特征的真实性和长上下文中的稳定性、steering 可能让模型察觉异常、漏掉特征、red-blue game 的胜负标准和过拟合、model organism 是否真实、外部部署的隐私限制。2. AI control：承认模型可能是恶意的，直接 bound P(catastrophe | misaligned)；用可信的弱模型做监控，限制部署范围（仅白名单内部场景、KYC 外部部署或一般外部部署三种选项），对每个敏感场景要么做部署时的可信监控（Safe/Unsure/Likely Malign，后者交安全团队调查），并用 monitoring game 加上最强 elicitation 的攻击者验证，要么做 test-time honeypot；两者都依赖一个能生成模型无法与真实部署区分的场景的 Procedure S，用残差流上的 linear probe 检验可区分性，作者自己也觉得这个验证不令人满意、是开放问题；可选措施有 sequestration（分拆输入看结论是否一致）和信息隐藏（审查日期等能泄露是否部署的线索）。局限：限制部署有商业代价、攻击者 elicitation 很难、纯黑盒难以给严格保证、可能在没有任何具体威胁证据时被迫推迟部署、不能排除 ASL-5 能力（恶意模型可以一直 sandbag 直到被盗）、生成足够多样逼真的长上下文模拟很贵很难。3. 激励分析：只针对 T3，目标是得到一个可信的监控/评估模型，论证 vanilla RLHF 不会把预训练中混杂的欺骗性 persona 放大。假设预训练模型本身在这些 prompt 上不是连贯欺骗的、显式 scratchpad 推理至少和任何不透明推理一样强、任何让部署时更欺骗的 persona 变化也会在 RLHF 环境中表现出来；实验是用 secret scratchpad 加 SFT 把初始欺骗率调到 10–90%，用低于 T3 阈值的弱模型分类 scratchpad，发现非欺骗样本 PM 分更高、聚类后也没有哪类欺骗得分更高、RLHF 过程中欺骗率持续下降，从而认为环境不激励欺骗。局限：只覆盖 RLHF 这一环、假设不牢靠、exploration hacking、残余低频欺骗、HHH 训练可能通过加强规划在分布外诱发 scheming、scratchpad 本身可能不 faithful。作者认为现实中的 safety case 很可能是三者的组合，也强调设计安全流程时还要能"当场抓住"恶意行为，以便更新流程并向外界示警。

## 我的笔记

