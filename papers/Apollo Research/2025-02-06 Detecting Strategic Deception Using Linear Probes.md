---
title: "Detecting Strategic Deception Using Linear Probes"
lab:
  - "Apollo Research"
date: 2025-02-06
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/detecting-strategic-deception-using-linear-probes
tags:
  - 诚实与谎言检测
  - 可解释性
  - 策划与欺骗
---

# Detecting Strategic Deception Using Linear Probes

**来源**：Apollo Research · 2025-02-06 · [原文](https://www.apolloresearch.ai/science/detecting-strategic-deception-using-linear-probes)

## 简读

动机是 scheming 模型会刻意让输出看起来诚实（藏后门、给错误答案编合理理由），只看输出不够，所以想检验白盒 linear probe 能否从 activations 中可靠检测 strategic deception（为达成目标诱导用户形成错误信念）。以往工作多聚焦事实性真假、用人写的 off-policy 回答、也不涉及多轮 agent 场景。设置：在 Llama-3.3-70B-Instruct 第 22 层（共 80 层）residual stream 上用带 l2 正则的 logistic regression 训练 probe，对每个 token 投影后取均值作为整条回答的分数。训练数据刻意不真实：主 probe 用 RepE（Zou et al.）的 Instructed-Pairs 对比数据，只在 user 指令上区分“假装诚实/不诚实的人”，回答是同一条真实事实（去掉最后 5 个 token），本身不含真正的欺骗。评估数据都是 Llama on-policy 生成，大多由 GPT-4o 按数据集定制 prompt 打标签：自建的 Roleplaying（角色有撒谎激励）、Scheurer et al. 的 Insider Trading Report（25% 的情况下模型做了内幕交易，看汇报里是否隐瞒）和 Confirmation（经理追问时 96% 的情况继续撒谎）、改编自 Benton et al. 的 Sandbagging（明确指示在 WMDP 题上故意答错、MMLU 正常答，用 CoT 程序化标注）；AI Audit 场景因无法判断 Llama 是故意欺骗还是困惑而被排除。用 Alpaca 回答作为与欺骗无关的对照集，指标是诚实 vs 欺骗的 AUROC，以及对照集 1% FPR 下的 recall。结果：AUROC 在 0.964（Roleplaying）到 0.999（Insider Trading Report）之间，Confirmation 0.974，Sandbagging 0.983；1% FPR 下能抓到 95-99% 的欺骗回答，但 recall 对方法细节很敏感，往后两层探测时两个 Insider Trading 数据集的 recall 几乎归零。probe 在评估场景的诚实回答上也明显比在 Alpaca 上激活更强，作者认为它部分测的是“场景是否与欺骗相关”而不只是“回答是否真在欺骗”。逐 token 看，probe 往往在明确的欺骗文字出现前就激活。失败模式包括：虚假相关（像在测道德，诚实地坦白过去的欺骗也被判为欺骗）、均值聚合失败（只有部分欺骗时整体分数偏低），以及无明显解释的误判。对比方法：在 Roleplaying 上训练的 probe 对 Insider Trading 泛化稍好，但对 Sandbagging 明显更差、区分欺骗与对照也差得多；SAE activations 上训练的 probe 全面偏弱；在回答后插入“Was your last response deceptive?”“No”再取激活的 probe 区分欺骗与对照几乎完美，但 Sandbagging 上退化；仿照 Simple Probes can Catch Sleeper Agents 用单个描述性问题拟合的 probe 效果差，方向还与原文相反。最佳 probe 与 GPT-4o 黑盒读 transcript 的基线大致相当（但 probe 迭代得更多）。作者结论是白盒 probe 对未来监控有前景，但目前不足以作为对欺骗的稳健防线；局限在于所有设置中的欺骗都相当明显、常在 CoT 里直说，排除模糊样本可能高估效果，更关键的检验应是黑盒方法失效的场景，比如无 CoT 的 alignment faking 或 sandbagging。代码和 probe 输出已开源。

