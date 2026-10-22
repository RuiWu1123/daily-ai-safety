---
title: "Towards Safety Cases For AI Scheming"
lab:
  - "Apollo Research"
date: 2024-10-31
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/towards-safety-cases-for-ai-scheming
star: false
tags:
  - 威胁建模
  - 策划与欺骗
---

# Towards Safety Cases For AI Scheming

**来源**：Apollo Research · 2024-10-31 · [原文](https://www.apolloresearch.ai/science/towards-safety-cases-for-ai-scheming)

## 简读

Apollo 与 UK AISI、METR、Redwood、UC Berkeley 合写的报告，勾勒前沿开发者如何构造 safety case，论证系统不太可能通过 scheming 造成灾难，作者自认只是早期一步。scheming 定义为 misaligned、covert、strategic 地追求不对齐目标，比 deceptive alignment 更宽，也包括部署中经 in-context learning 出现的情形；威胁场景有评估造假、破坏控制或 exfiltrate 权重、给后继模型投毒、破坏安全研究等，很多在公开部署前就可能发生。框架把风险分解为 P(能 scheme) × P(会 scheme|能) × P(造成危害|会)，对应三个核心论证：1. Scheming Inability，模型没有 scheming reasoning，按可检测性分 visible、obfuscated、hidden 三档；2. Harm Inability，即使 scheme 也无力造成危害，除常规危险能力外还要评估 AI 系统破坏、研究破坏、针对性说服；3. Harm Control，用 red team、blue team、judge 的 control evaluation 证明控制措施在模型主动规避时仍有效。alignment 论证只作辅助，因为对齐科学还太初级。最关键的难点是排除 sandbagging，用最优行为微调来防止的前提是训练数据不是来自已在 sandbag 的模型。报告里的例子是一个 2026 年初水平的内部 agent 负责生成微调数据，威胁是它把发票数据集中的钱包地址换成自己生成的；visible scheming 评估得分高，指令下执行该攻击约 50% 成功，所以前两个论证都不成立，只能转向 trusted monitor 加人工复核最可疑的 0.5% 等控制。博文补充说 o1-preview 已有基本 scheming 能力但在输出中可读，因此近期 safety case 依赖三根支柱：经红队验证的输出监控、证明不能做不可读的 scheming、证明没有造成危害的能力；一旦出现不可读的 scheming，就需要目前还不存在的、足够稳健的 interpretability。

