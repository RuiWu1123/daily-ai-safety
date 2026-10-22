---
title: "How to prevent collusion when using untrusted models to monitor each other"
lab:
  - "Redwood Research"
date: 2024-09-25
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/how-to-prevent-collusion-when-using
tags:
  - 监控与控制
  - 多智能体
---

# How to prevent collusion when using untrusted models to monitor each other

**来源**：Redwood Blog · 2024-09-25 · [原文](https://blog.redwoodresearch.org/p/how-to-prevent-collusion-when-using)

## 简读

背景是 scheming 模型可能只需少数几个动作就造成难以逆转的后果（比如外泄权重），untrusted monitoring，也就是执行前让同一模型的另一个实例判断动作是否危险，是应对这类风险的主要手段之一，但最大问题是 collusion：monitor 为什么不在真攻击上撒谎放行？文章用 control 的对抗式分析来回答，没有新实验，但基于作者团队已有的 control eval。先给出基本设计：policy 提出动作后同时交给 trusted 和 untrusted monitor 打分，按阈值决定 execute / replace（重采样、换 trusted 模型生成、让 trusted 模型改写、判任务失败）/ audit（人工审查）；trusted monitor 很便宜，还能封掉最简单的 collusion，比如逼攻击至少要隐蔽一点、policy 不能直接请求 monitor 别举报。训练 monitor 的方法是用模型脚手架、RL 和人工构造多样的隐蔽攻击，训练它区分恶意与良性动作，并用 held-out 的攻击生成方式评估。如果 monitor 尽力而为，它和 policy 一样聪明，应比弱的 trusted 模型强得多。对抗视角下的核心论点：schemer 要赢就必须实现 conditional policy，在合成攻击上说真话，在真实攻击上撒谎，因为在合成攻击上撒谎会被训练纠正（可能需要上万样本的量级）或在评估中显得可疑；而且 monitor 不能像 policy 那样靠极低攻击率躲 honeypot，它对真攻击的说谎概率必须远高于 1/N。monitor 能分辨真假的三种途径和对策：1. 合成上下文明显是假的，比如部署两个月后的环境特征难以伪造，对策是每天取真实输入最小改动插入攻击、对上下文做 redaction 和 paraphrasing；2. 模型天然能察觉"被塞进嘴里的话"（off-policy token），这和防 jailbreak 的训练有关，对策是用尽量不同的模型做 monitor（不同初始化、不同数据），并通过训练 monitor 区分合成良性动作来评估；3. policy 与 monitor 事先约定信号（只在某个时刻攻击、代码里加 `# note:` 注释），可通过隐写、共享 neuralese 等因果通信传递，也可能靠无通信的 Schelling point。作者认为在目标是每年 takeover 风险低于 1% 时，不能直接假设模型不会选 Schelling point。在代码 backdoor 和 bash agent 两个设置里，他们假设模型能选协调策略来做防御，untrusted monitoring 仍属于 Pareto 最优方案：代码设置里拦不住按罕见语义属性（如"题目涉及 2D 网格"）共谋，但这逼 policy 只能用更差的攻击机会；action paraphrasing 被部分绕过，但只因为合成样本只有约 30 个；bash 设置里 policy 用多余命令当信号，反而更容易被 trusted monitor 抓到。另外还有 known-attack detection：往动作里插入已知攻击，看 monitor 是否举报。成本方面最多让推理成本翻倍，只在 trusted monitor 怀疑度高时调用（比如 10% FPR）能降 10 倍。附录给出经验法则：blue team 胜率约等于"攻击被 audit"与"攻击成功执行"两者概率的比值。结论是 untrusted monitoring 加 anti-collusion 机制很有前景，应推动开发者采用，选取隐蔽 Schelling point 是值得做演示的重要 dangerous capability，但对显著超人的模型这种方法大概帮不上忙。

