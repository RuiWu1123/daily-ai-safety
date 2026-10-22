---
title: "Why it's hard to make settings for high-stakes control research"
lab:
  - "Redwood Research"
date: 2025-07-18
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/why-its-hard-to-make-settings-for
star: false
tags:
  - 监控与控制
  - 评估方法
---

# Why it's hard to make settings for high-stakes control research

**来源**：Redwood Blog · 2025-07-18 · [原文](https://blog.redwoodresearch.org/p/why-its-hard-to-make-settings-for)

## 简读

Redwood 的主要工作之一是做原始 control 论文和 Ctrl-Z 那类的后续研究：搭一个带任务集（比如 APPS）和安全失败定义（比如按特定定义的 backdoor）的 setting，然后玩红蓝对抗、开发 protocol 和 attack。作者（Buck）说其中相当大一部分难度其实在于构建 setting 本身，而不是 protocol 和 attack，这篇解释为什么。主任务方面：需要前沿模型做得还行、但弱模型明显更差的任务，因为要排除只用 trusted model 就能解决的 protocol；如果直接选很弱的 trusted model，它连基本指令都跟不好，很多有希望的 protocol 就研究不了。这意味着任务不能被饱和，而这种数据集越来越难造，也很难让 LLM 帮忙造（定义上就复杂到 AI 搞不定），甚至很难让 AI 判断任务是否做对（当前能力下，未饱和任务上 verification 并不比 generation 容易，尤其 AI 对着自己的 verifier 迭代时）。而且需要稳健的任务成功度量，因为开发 protocol 时会对着它优化，作者认为影响主任务成功率的 protocol 在实践中会很关键。side task 让事情更难：1. 对抗研究过程会对着 side task 成功的定义优化，若定义成"插入安全漏洞"，红队会去找勉强算数的最弱漏洞，所以原论文和 Ctrl-Z 都用了客观定义；2. 如果 side task 需要主任务用不到的 affordance，蓝队直接标记该 affordance 就行（Ctrl-Z 里 side task 要联网，而多数主任务不需要）；3. 像 SHADE-Arena 那样每个主任务配一个任意 side task、并"魔法般"告诉 attack policy，本质上不现实，也排除了给 untrusted model 小子任务让它不知道该攻击什么的 protocol，还让方法论变难——分不清蓝队变好是真的更好还是迭代中泄漏了 side task 定义的信息；4. 最好让 AI 自己想攻击思路，而不是用研究者给的，更接近 capability eval 也减少 overfitting。此外作者偏好 AI 在做软件工程或类似 AI 公司研究员日常工作的领域，因为最担心的是 AI 在做 ML R&D 时滥用算力和模型权限。作者承认做 APPS 论文时没意识到后续 setting 会难这么多，Ctrl-Z 一开始没重视这点是失误。他也认为目前没法直接拿真实 AI agent 部署来做，因为现在 AI 拿到的自主性和危险资源都太少，轨迹和未来担心的场景差太远；在实际部署里试 control 类技术对 AI 公司内部研究者有价值，但主要是让组织为以后落地做准备。

