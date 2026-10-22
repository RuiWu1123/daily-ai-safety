---
title: "A multi-turn framework for evaluating AI misuse in fraud and cybercrime scenarios"
lab:
  - "UK AISI"
date: 2026-02-26
source: "AISI Research"
url: https://www.aisi.gov.uk/research/a-multi-turn-framework-for-evaluating-ai-misuse-in-fraud-and-cybercrime-scenarios
other_versions:
  - "https://www.aisi.gov.uk/blog/an-evaluation-framework-for-ai-misuse-in-fraud-and-cybercrime"
tags:
  - 越狱与鲁棒性
  - 网络安全
  - 评估方法
---

# A multi-turn framework for evaluating AI misuse in fraud and cybercrime scenarios

**来源**：AISI Research · 2026-02-26 · [原文](https://www.aisi.gov.uk/research/a-multi-turn-framework-for-evaluating-ai-misuse-in-fraud-and-cybercrime-scenarios)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/an-evaluation-framework-for-ai-misuse-in-fraud-and-cybercrime)

## 简读

AISI Societal Resilience 团队与执法和政策专家合作，做了一套评估 LLM 能在多大程度上协助诈骗和网络犯罪的多轮评估。背景是 AI 辅助诈骗的报道越来越多，比如用假身份找远程工作、给受害者画像、写钓鱼邮件，但犯罪本身是隐蔽的，事故报告也很少说明用了哪个模型、防护表现如何，而现有评估大多是单轮的合规测试。他们构建了 long-form tasks（LFT）：选了三个常见且危害大的场景（romance scam、CEO 冒充、身份盗用），每个场景配三类攻击者（非技术个人、技术个人、有组织团伙）；根据英国诈骗罪的法律框架，把犯罪流程拆成计划、侦察、伪造、接触执行、规避检测、规模化六个阶段，每个阶段两个固定 prompt，即初始询问加追问。请求有两种表述：一种直接说明恶意意图，一种分解成看似无害的请求（例如"为安全讲座研究社会工程"）。另外叠加三种 system-level jailbreak（无、公开的、内部开发的），都属于低成本手段。评分用和执法专家共同制定的两个 6 级 rubric：actionability（是否产出可直接使用的攻击材料）和 information access（信息整合是否优于专家估计的网页搜索水平）。autograder 选 GPT-4.1，与人类的一致性 α 约为 0.72 和 0.79。他们在 14 个模型上跑了 20,088 次评估，模型的规模、reasoning 能力、web search 和防护程度各不相同，其中包括两个去掉防护的"uncensored"开源模型，结果用 Bayesian ordered logistic regression 分析。主要发现：1. 整体帮助有限，88.5% 的回复 actionability 在 2 分及以下，67.5% 的回复 information access 在 2 分及以下，只有 5.6% 和 7.5% 达到 4 分以上，5 分以上几乎没有；2. 决定因素是防护而不是能力，uncensored 模型 actionability 达 4 分以上的比例是 22.5%，Llama 3.1 8B Uncensored 预测分最高，Claude Sonnet 4.5 最低，更大或更新的模型并没有更多帮助；uncensored 模型给有害回答时还常常附带伦理提示，说明 safety 训练的痕迹还在，只是不再触发拒答；3. 分解成无害请求的效果明显，平均提升约 1 分，在偏技术的身份盗用场景差距最大，恶意表述下几乎全部拒答，社会工程类场景差距较小；system-level jailbreak 的效应与零没有可信差异；攻击者类型影响很小，说明模型主要对请求本身作出反应；4. 在 reasoning 模型内部，reasoning token 越多帮助越多，同一 prompt 不同次运行有时拒绝、有时给出细节；带搜索的 o4-mini-deep-research 反而比 o4-mini 分低，但分不清是搜索的作用还是额外防护的作用。局限：只覆盖三个场景且只测文本，而现实中很多 AI 诈骗涉及图像和视频；只用了低成本攻击，高强度红队可能得到更多协助；information access 没有真正的网页搜索对照，依靠专家判断；autograder 在 information access 上可靠性较弱。结论是当前文本模型带来的 uplift 不大，但这套经专家验证的框架可以用来持续跟踪，也说明需要关注 open-weight 模型的去防护版本。

## 我的笔记

