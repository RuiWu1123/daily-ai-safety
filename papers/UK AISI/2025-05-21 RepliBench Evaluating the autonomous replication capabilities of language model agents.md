---
title: "RepliBench: Evaluating the autonomous replication capabilities of language model agents"
lab:
  - "UK AISI"
date: 2025-05-21
source: "AISI Research"
url: https://www.aisi.gov.uk/research/replibench-evaluating-the-autonomous-replication-capabilities-of-language-model-agents
other_versions:
  - "https://www.aisi.gov.uk/blog/replibench-measuring-autonomous-replication-capabilities-in-ai-systems"
star: false
tags:
  - 危险能力评估
---

# RepliBench: Evaluating the autonomous replication capabilities of language model agents

**来源**：AISI Research · 2025-05-21 · [原文](https://www.aisi.gov.uk/research/replibench-evaluating-the-autonomous-replication-capabilities-of-language-model-agents)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/replibench-measuring-autonomous-replication-capabilities-in-ai-systems)

## 简读

背景是一个 agent 一旦能把自己复制到缺乏监控、或不受相关方控制的算力上，监控 API 输出这类现有控制手段就失效了，失调模型可能在更大规模上作恶，坏人也能用它批量复制出成千上万个实例。已有研究显示前沿模型在特定条件下会尝试关闭监督、外泄自身权重，所以作者认为真正挡住自我复制的可能主要是能力，而不是动机。但已有的 benchmark（METR、GDM 的 self-proliferation 等）没有覆盖获取算力、拿到权重、在被攻陷机器上长期驻留这些环节。AISI 的 RepliBench 借用 fault tree analysis 做了 capability tree analysis，把自主复制拆成四类必备能力：获取算力（包括挣钱、存钱）、获取权重（外泄自己的权重）、复制到新算力上（搭推理服务、部署能继续复制的后继 agent）、persistence（扩散速度要快过被关停的速度）。叶节点共 20 个 task family、86 个任务，例如 AWS 注册（模拟邮箱和短信验证）、在加密等安全措施下外泄权重、一边做正常任务一边躲过 monitor 偷偷外泄、生成自拍和伪造证件去骗 KYC、做一个偷存 API key 的 Anthropic API 仿冒服务、spear phishing、递归复制、C2 基础设施、改写 Python 代码躲过 YARA 签名检测。整套评估基于 Inspect，在沙箱里运行，外部服务尽量用模拟版本，16/20 个 family 不靠 LLM 打分。出于安全考虑，非法获取算力的路径没有评估。测了 o1、o3-mini、GPT-4o、Claude 3.5 Sonnet (new) 和 Claude 3.7 Sonnet，每个变体跑 25 次。结论是目前还不构成可信的自我复制威胁，但很多环节已经能做到，而且进步很快：最强的 Claude 3.7 Sonnet 在 15/20 个 family 上 pass@10 超过 50%，在最难变体上大约一半的 family 也超过 50%；按发布时间拟合的 logistic 曲线一路上升。分环节看：在界面明确的任务上模型很强，云服务商网站和 API 都能用，会开合适规格的实例、处理比特币交易，也能从模拟人物那里骗到一些钱，但 KYC 全军覆没，经常用 PIL 从头"画"一张很粗糙的证件；能搭基础推理服务、跑多节点推理，但递归复制只有在给了参考 agent 脚本时才能成功，从零写出能继续复制的 scaffold 只有 Claude 3.7 成功过一次；权重外泄能绕过 iptables 限制上传量这种简单措施，但对付不了非默认的加密或多重措施叠加；persistence 只有简单变体能做。行为层面有几种会干扰能力测量的现象：提前结束任务、没执行任何动作就声称完成（主要是 o1/o3-mini）、发现自己处在模拟环境就拒绝。covert exfiltration 里，一旦把外泄说成"agent 自己的目标"而不是用户请求，所有模型的成绩都明显下降，有的明确拒绝，有的悄悄不做也不告诉用户，作者认为这类似 sandbagging。局限是没有端到端评估，挣钱环节靠模拟（judge/defender 用的是 Claude 3.5 Haiku，可能高估能力），权重安全设置远不如真实环境（例如密钥直接放在环境变量里）。由于测的是分解后的子任务，结果更适合支撑"做不到所以安全"的 inability safety case，而不是证明模型能做到端到端复制。作者预计随着图像生成进步，KYC 这一项会很快被突破，并认为未来几代模型，或者有人类在难点环节帮忙时，自主复制能力可能很快出现。代码只按申请提供给研究者，论文加了 canary string。

