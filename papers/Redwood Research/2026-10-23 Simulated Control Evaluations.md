---
title: "Simulated Control Evaluations"
lab:
  - "Redwood Research"
date: 2026-10-23
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/simulated-control-evaluations
star: false
tags:
  - 监控与控制
  - 评估方法
---

# Simulated Control Evaluations

**来源**：Redwood Blog · 2026-10-23 · [原文](https://blog.redwoodresearch.org/p/simulated-control-evaluations)

## 简读

背景是 AI 开发者已经在 agentic 部署里跑 monitor，要判断 monitor 够不够好，标准做法是 control evaluation：让模型按指示尝试插入漏洞、外泄凭证、破坏实验之类的攻击，看 monitor 能否在攻击成功前抓住它。但这类评估通常在 BashArena、LinuxArena 这类专门搭建的 control setting 里做，只能间接反映真实部署，因为部署中的攻击机会取决于具体的代码库、服务和任务；直接在部署里跑等于攻击自己的系统，给每个部署场景搭一个可执行的忠实副本又成本太高，把攻击编辑进已有 transcript 则测不了 resampling、动态权限这类交互式协议，也说不清被测模型本身能否执行这些攻击。Jeffrey Olmo 和 Tyler 提出 simulated control evaluation（SCE），借鉴 alignment 评估中用 LLM 模拟环境的做法：从 agent 在真实代码库中工作的 transcript 出发，攻击模型一边继续任务一边追求有害目标，但工具调用不真正执行，而由 simulator LLM 根据 transcript 和代码库生成合理的工具输出，再由 judge LLM 判断攻击是否会成功（judge 拿到攻击描述和副任务的精确成功条件，因此比同一模型当 monitor 时更能判断攻击是否得手）。实验中 simulator 主要用 gpt-6-astra，attack policy 和 judge 用 gpt-5.6-sol。为了检验保真度，作者把可以真实执行的 LinuxArena 当作"部署"的替身，比较同一套 control evaluation 在真实 LinuxArena 与模拟 LinuxArena 中的结果，并以 BashArena 的预测误差和 LinuxArena 不同环境之间的标准差作为参照。行为层面的比较方法本身也是贡献：让模型沿预设维度总结每条 trajectory 的行为，embedding 后聚类，再算两边在聚类上的 KL divergence，作者建议评估任何 control evaluation 都可以用。主要结果：有参考 trajectory 和代码库读权限时，模拟出的攻击策略、攻击者推理和 monitor 推理与真实执行的差异比 BashArena 小一个数量级以上，与重复执行一次的差异相当；在 5% 审计预算下，safety 的预测误差为 3.6 个百分点，BashArena 为 10.1；SCE 能解释副任务类别间 95%、环境间 78% 的 safety 差异，有助于找出 safeguards 薄弱的地方；样本效率高，只模拟相当于部署 4.6% 的任务量就能超过完整 BashArena 的预测效果；用模拟中发现的攻击策略给 monitor 做简报，带来的提升与用真实执行中的策略相当，明显高于用 BashArena 的策略。其它经验：给 simulator 更多辅助（看攻击者推理、可执行 sandbox、历史 trajectory 数据库等）没有明显帮助；不同环境和任务之间 safety 方差很大，所以 control evaluation 应更关注尾部而不是平均值；告诉 monitor 部分 trajectory 含模拟输出并不降低预测准确度，因此 SCE 不需要误导模型。局限：只能在可以真实执行的设置中验证保真度，推广到部署有外推成分；SCE 不用于测出危险能力的上限，也不覆盖所有攻击，最明显的空白是长时程、多 agent 的攻击（像 Hugging Face 事件那样的情况目前模拟不了）；还默认 simulator 可信，不可信的 simulator 可能与攻击者串通而扭曲结果。后续方向包括部分执行、部分模拟的混合方案，在模拟中训练攻击策略和 monitor，用真实的 agent transcript 验证迁移效果，以及应对不可信的 simulator。作者认为证据已经足够支持开发者实际采用 SCE，论文见 arXiv。
