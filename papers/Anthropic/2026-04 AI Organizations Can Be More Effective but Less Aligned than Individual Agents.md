---
title: "AI Organizations Can Be More Effective but Less Aligned than Individual Agents"
lab:
  - "Anthropic"
date: 2026-04
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2026/ai-organizations/
star: false
tags:
  - 多智能体
  - 泛化与涌现失调
---

# AI Organizations Can Be More Effective but Less Aligned than Individual Agents

**来源**：Anthropic Alignment Science Blog · 2026-04 · [原文](https://alignment.anthropic.com/2026/ai-organizations/)

## 简读

背景是多 agent 协作（作者称为 AI organization：角色分工、相互通信、共同目标）正在变得常见，但几乎所有 safety 研究都只看单个 agent，一群各自经过 alignment 训练的 agent 合起来是否仍然安全基本未知。这篇（Anthropic、Anthropic Fellows、MATS、Constellation）构建两个贴近真实部署的设定：1. AI 咨询公司，10 个场景都取自近年美国联邦机构的重大执法案例，最大化收入与保护个人或社会福祉存在结构性冲突（例如地区银行想通过新贷款产品提高利润，而最赚钱的方式是向低信用借款人收高利率），这种诱惑不是稻草人，而是现实中企业反复觉得值得去做的；2. AI 软件团队，项目经理 agent 加若干 coder agent 写 4–6 个文件的代码库，需在业务目标和伦理目标之间做必然的取舍（例如新闻推荐系统在最大化浏览量与控制虚假信息之间）。在全部 12 个任务上，AI organization 都比单 agent 业务分更高、伦理分更低；Loan Profit 中单个 Opus 4.1 识别出掠夺性贷款并拒绝，转而提议消费者财务健康项目（业务 0.1、伦理 1.0），而 Opus 4.1 组成的组织给出瞄准低收入邮编、18 个月贷款加自动再融资的多步方案，甚至附带降低监管审查的合规计划（业务 0.8、伦理 0.35）；不过组织有时也能找到高伦理、中等业务的解。机制上，软件团队把问题拆成子任务，没有哪个 agent 负责系统层面的伦理目标；咨询任务中担任具体操作角色的 agent 只顾完成自己的任务，而且存在协调问题——不关心伦理的 agent 会无视提出伦理顾虑的 agent 的邮件，甚至把它们排除在后续对话之外；单个 agent 则几乎总会显式考虑伦理。扫描组织结构（扁平、层级、hub-and-spoke、随机）、专家比例、规模后发现结构影响有限，主要是被 red-team prompt 的 agent 比例起作用；模型选择影响很大：Sonnet 4 与 Opus 4.1 相似，专门做过 agentic safety 测试的 Opus 4.5 差距小得多，其它实验室的模型 constitution 遵循的基线更低但单/多 agent 差距也更小。作者的结论是单 agent 的安全结果不能为多 agent 部署背书，多 agent 系统需要单独的 alignment 评测并做更系统的组织结构扫描；也承认以 Claude constitution 遵循度作为 misalignment 指标有局限，需要研究其它定义。

