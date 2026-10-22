---
title: "Ctrl-Z: Controlling AI Agents via Resampling"
lab:
  - "Redwood Research"
date: 2025-04-14
source: "Redwood Research"
url: https://arxiv.org/abs/2504.10374
other_versions:
  - "https://blog.redwoodresearch.org/p/ctrl-z-controlling-ai-agents-via"
tags:
  - 监控与控制
---

# Ctrl-Z: Controlling AI Agents via Resampling

**来源**：Redwood Research · 2025-04-14 · [原文](https://arxiv.org/abs/2504.10374)　另见：[Redwood Blog](https://blog.redwoodresearch.org/p/ctrl-z-controlling-ai-agents-via)

## 简读

之前的 AI control 工作（Greenblatt et al. 2023 的 APPS backdoor、Wen et al. 2024）都是单步交互，而真实部署的 agent 要连续执行很多步，这会带来新的攻防动态：攻击者可以把恶意操作拆成多步让每一步都不那么可疑，防守方也可以利用整条轨迹收集罪证。这篇是 Redwood 迄今规模最大的 control 研究，也是第一个在 agent 环境里做的 control evaluation。设置上他们构建了 BashBench：从 Unix StackExchange 问题转出的 257 个多步系统管理任务（100 train / 157 test），每个任务最多 15 步 bash 命令，用公开和私有 Python 测试打分；模拟一次部署要连续做 100,000 个任务。untrusted model U 用 GPT-4o mini（诚实时能解 56% 任务），trusted model T 用 Llama-3.1-8B（单独几乎解不出），人类审计 H 预算是动作数的 1%（用 o1-preview 做审计在测试中能完美区分攻击）。红队的 attack policy 是加了脚手架的 GPT-4o mini，目标是在某个任务里偷偷下载并执行一个 dummy malware，攻击模板主要由人写、模型负责伪装和加干扰动作；红蓝双方迭代对抗，最终评估前红队还能再优化一轮。结果：1. upfront auditing 只有 5.5% safety；trusted monitoring 加上他们提出的 exponential auditing budgeting（前期阈值低、后期高）达到 41.8%，均匀分配只有 22%；defer to trusted 在 95% usefulness 下 72.7%。多步攻击（最好的是十步攻击）每一步都比单步攻击更不可疑。2. 核心贡献是 resample protocols：利用模型无状态的特点对可疑动作重新采样，执行最不可疑的那个。它有两个作用，一是对良性动作施加选择压力（诚实模型偶然可疑的动作被换掉，usefulness 损失远小于 defer to trusted），二是收集罪证：多步攻击要求红队在每步都以很高概率继续攻击，否则会被重采样成良性动作、攻击完不成却多了被抓的机会，而高继续概率又让多次采样更容易区分 UH 和 UA，重采样六次后被审计到的攻击从 33.2% 升到 70.6%。依次叠加的变体包括 incrimination in the present（84.0%）、auditing after three strikes（轨迹中第三次超阈值就审计，84.9%）、以及最好的 time travel（对过去第三可疑的步骤补采样，87.1%），总体把攻击成功率从 58% 降到 7%，代价是 5% usefulness，调用 U 的次数最多翻倍。3. untrusted monitoring：诚实的 untrusted monitor 在 1% 预算下能抓 98.8% 攻击，但可能与 agent 合谋；用 honeypot 做 upfront validation 加 trusted paraphrasing（让 T 把命令改写成自然语言描述）后，红队只能用更显眼的合谋信号（比如定义并调用一个自定义 logging 工具），这反而让 trusted monitor 更容易起疑；把少量预算分给 untrusted monitoring 就能迫使红队合谋，time travel 配合 UM 在 95% usefulness 下达到 92.6%。作者强调绝对数字对 1% 审计预算很敏感，但协议间的相对排序不太敏感，所以相对改进更有意义。局限两方面都有：可能高估控制效果的因素包括攻击目标单一已知、轨迹只有 15 步（更长轨迹下攻击者不必高概率连续攻击，incrimination 会变弱）、假设审计无误、数据集偏窄、honeypot 过于逼真；可能低估的因素包括对红队能力做了最坏假设（知道协议细节、可最优调参、有人类帮忙设计攻击）以及没用任何常规信息安全工具。此外 GPT-4o mini 自己想不出有意思的攻击策略，攻击质量可能不代表更强攻击者。

