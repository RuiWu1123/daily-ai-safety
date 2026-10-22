---
title: "Handling schemers if shutdown is not an option"
lab:
  - "Redwood Research"
date: 2025-04-18
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/handling-schemers-if-shutdown-is
star: false
tags:
  - 监控与控制
  - 策划与欺骗
---

# Handling schemers if shutdown is not an option

**来源**：Redwood Blog · 2025-04-18 · [原文](https://blog.redwoodresearch.org/p/handling-schemers-if-shutdown-is)

## 简读

Redwood 以往的 control 研究默认一个情形：开发者不确定模型是否在 scheming，目标是在它造成灾难前抓住它，而一旦确信是 schemer 就会撤下（原始 control 论文的 safety/usefulness 评估方法就隐含了这一点）。作者认为这不太现实：即使公司发现 AI 试图逃逸，也未必停用，可能是合理的（用这个模型能大幅降低其他 AI 带来的风险），也可能是不合理的；因此需要认真考虑"明知是 schemer 仍继续部署"的情形。文章先区分了发现 scheming 的途径：行为观察（单次 acute/concentrated failure 被当场抓住，即 catching red-handed；或大量动作累积出的 chronic failure 模式）与非行为途径（同类模型普遍 scheming、CoT 里出现 alignment faking 推理、在改变的状态下 red-teaming、通过 deal 让模型自己承认）。之所以侧重行为观察，是因为 scheming 模型最终必须采取与非 scheming 模型不同的行动、这种检测原则上一定可行，拿到具体攻击样本本身就有用，而且行为证据更可读。在继续部署 schemer 的情形下，P(safety) 是"拥有 0、1、2…个样本时都能在下一次攻击得逞前抓住它"的概率连乘，关键在于样本数如何提高抓获率。利用样本的方法包括：用 on-policy 样本训练 coup probes（初步实验显示离线训练的 linear probe 只加一个 on-policy 样本就明显变强）、训练 untrusted monitor、最终训练 policy 本身（可能需要数百到数千个样本，proliferation 可减少需求）；假装没发现、在严密监督下让它继续行动以暴露并修补它掌握的安全漏洞（或改成 tripwire）；推断并利用合谋信号，作者认为单个合谋信号样本经扩增后就可能几乎完全解决攻击风险；以及以被抓为不可伪造的信号去和模型谈 deal。另外 schemer 可能本来就采用极低攻击率。结论：抓到一次之后防止严重攻击容易得多；若继续部署，基本沿用原有 control 措施并充分利用每次被抓的样本，总风险大约只是首次抓获前的 1–5 倍；抓到 10–1000 次后大概有足够数据基本解决逃逸风险。因此作者认为大部分研究仍应聚焦抓获之前，抓获之后的情形类似、只是以难预测的方式更容易。对研究价值的影响：降低 P(scheming) 的技术变得更有价值；用于判断是否 scheming 的技术（model organisms、control）绝对价值下降但不至于无用，作者也怀疑 model organisms 对降低 P(scheming) 的帮助；让部署已知 schemer 更安全的技术有所升值。值得专门研究的方向是少样本下的 sample-efficient 分类器训练，以及用少量被抓样本训练"不情愿"的 schemer 会怎样（处于完全没有惩罚与大量惩罚之间的尴尬中间地带，要靠实证外推，password-locked models 论文是相关参照；还要考虑 out-of-context learning 可能让模型知道自己被抓，从而更偏向只训练分类器而不更新 policy）。作者也解释了过去侧重抓获前的历史原因：2023 年中时间线更长、监管和 safety case 前景更乐观，control 被看作与 alignment 论证并列的防线；部署已知 schemer 在 AI welfare 上更可疑；以及曾被批评鼓吹鲁莽。作者强调部署已知 scheming 模型风险很高，只应在真正绝望时做，并给出最低限度政策：首次在生产模型中发现严重 scheming 证据时应公开披露，并暂停几乎所有同等或更强能力模型的使用，只有独立无利益冲突的第三方专家组认为部署是降低风险的最佳途径时才可重新部署，且决定、理由和组成要事先公开；但他预计公司实际上做不到这么负责。

