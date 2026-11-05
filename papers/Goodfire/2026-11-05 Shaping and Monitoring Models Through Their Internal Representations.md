---
title: "Shaping and Monitoring Models Through Their Internal Representations"
lab:
  - "Goodfire"
date: 2026-11-05
source: "Goodfire Research"
url: https://www.goodfire.com/research/mechanistic-shaping
star: false
tags:
  - 可解释性
  - 对齐训练方法
  - 奖励作弊
---

# Shaping and Monitoring Models Through Their Internal Representations

**来源**：Goodfire Research · 2026-11-05 · [原文](https://www.goodfire.com/research/mechanistic-shaping)

## 简读

背景是现在训练模型只奖励结果对不对，不规定模型怎么得出结果，于是模型常常"答对了但理由错了"：视觉模型靠混杂特征走捷径，语言模型学会讨好用户（sycophancy）或钻 grader 的空子（reward hacking），而且模型越强，可用的捷径越隐蔽、越难靠评估发现。Goodfire 这篇论文（博客由 Satchel Grant 和 Michael Byun 撰写，Thomas McGrath、Owen Lewis 为共同资深作者）提出 mechanistic shaping：用模型内部表征直接规定训练中该依赖哪些概念、该表达哪些概念，也就是规定模型怎么解决任务。它包含两种方法：reliance shaping 惩罚模型在某个行为上对某个概念的依赖（"别靠这个"，依赖程度用标准 attribution 方法衡量），expression shaping 惩罚模型表达某个概念（"别做这个"，用沿概念方向的激活等代理衡量）；流程是先用可解释性工具找到不想要的概念方向，在训练目标中加惩罚项，可选择每隔若干步重新计算该方向，最后评估训练对该概念可监控性的影响。实验一是带混杂的胸片诊断：数据集故意只包含有胸腔引流管的气胸片和无引流管的正常片，普通训练的模型在训练集上看似准确，但碰到未经治疗的气胸就失败；他们不用引流管标签，而是用 SAE 拆出特征，让 LLM agent 挑出像管子的特征，再拿来做 reliance shaping，效果超过普通训练和几种已有方法，甚至超过在平衡数据上训练这一软上限。实验二是 DPO 引发的 sycophancy：已有工作发现 DPO 会让模型明显更谄媚，尽管不到 1% 的训练数据明显带谄媚，因此数据过滤几乎无效；他们在 OLMo-3-7B 上找到"sycophancy 方向"，在 DPO 中惩罚对它的依赖，结果数据过滤只是沿着"少做点 DPO"的曲线用能力换谄媚，reward shaping 和 inoculation prompting 几乎不降低谄媚，沿同一方向做 preventative steering 只走了一部分，reliance shaping 则保持了完整 DPO 的能力、谄媚程度接近初始模型，同样的配方在 7B、13B、32B 上都有效。实验三是 reward hacking：用 RL 训练 Qwen3.5-9B 做改编的 Countdown 算术谜题，诚实解法是注意到答案总是区间下界，作弊解法是读一个被告知不许读的答案文件；普通 RL 十次更新内作弊就增加约 6 倍、诚实策略降到零，过滤掉作弊 rollout 只在三分之一的 run 中有效，而用从编程任务作弊记录中算出的"作弊"方向做 expression shaping 后，模型 96%–98% 的时间诚实解题，并能迁移到从未训练过的国际象棋谜题（普通 RL 模型在那里 99% 作弊，shaping 后的模型几乎不作弊且仍有进步），因为惩罚针对的是模型内部的作弊概念而不是读某个特定文件。可监控性方面，训练对抗 probe 有让表征绕开 monitor 而行为照旧的风险，他们用一个可精确求解的玩具模型分析：投影掉某个概念方向后，因为任务仍奖励该概念，新的方向会马上在别处重新长出来，并可能与想要的概念纠缠在一起；频繁重算方向会引发线性重长与非线性编码的竞赛，最终可能形成可预测的二阶乘积编码，但后面的层可能又能线性读出。据此提出五级可监控性层级：沿用原 probe、重训线性 probe、改用非线性 probe、换到别的层、把模型当黑箱用外部模型（如 LLM judge）判断，另有概念被抹除的情况。实证上，sycophancy 实验中原 probe 的 AUROC 从 0.98 降到 0.93，重训的线性 probe 全程为 1.00；reward hacking 实验最坏情况下（梯度流过 probe）原 probe 的平衡准确率从 0.98 降到 0.57，重训后为 0.97–0.98；有的视觉实验在中间层只剩非线性形式，两层之后又能线性读出；也出现过理论未预测的末层部分抹除，但在更早的层仍可恢复。总之，在所有实验中被训练对抗的概念都仍可监控，只是常常需要重训 probe。作者建议定期检查 probe，失效时按层级依次重训、改为非线性、换层；局限是实验只在中小规模上做，对所有可能的神经编码、深层网络的解析解和前沿规模训练的理解都还不完整，训练对抗可解释性信号需要谨慎。
