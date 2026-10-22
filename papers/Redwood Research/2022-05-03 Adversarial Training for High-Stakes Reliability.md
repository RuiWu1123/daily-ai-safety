---
title: "Adversarial Training for High-Stakes Reliability"
lab:
  - "Redwood Research"
date: 2022-05-03
source: "Redwood Research"
url: https://arxiv.org/abs/2205.01663
other_versions:
  - "https://www.lesswrong.com/posts/A9tJFJY7DsGTFKKkh/high-stakes-alignment-via-adversarial-training-redwood"
tags:
  - 越狱与鲁棒性
---

# Adversarial Training for High-Stakes Reliability

**来源**：Redwood Research · 2022-05-03 · [原文](https://arxiv.org/abs/2205.01663)　另见：[LessWrong](https://www.lesswrong.com/posts/A9tJFJY7DsGTFKKkh/high-stakes-alignment-via-adversarial-training-redwood)

## 简读

背景是未来强 AI 可能部署在 high-stakes 场景，一次失败就可能是灾难性的，而多数 alignment 实证工作关注的是 average-case 表现；训练中可能从未遇到的罕见失败默认不会被纠正，adversarial training 是提升 worst-case 可靠性的一个候选手段。Redwood 用一个简单的玩具任务做 testbed：给三句 fan fiction 故事片段，续写一句不引入任何角色受伤的句子。做法是用 GPT-Neo-2.7B 当 generator，微调 deberta-v3-large 当 injuriousness classifier 过滤输出，"灾难性失败"定义为 classifier 把有伤害的续写判为安全（filtered 输出上的 false negative）。他们把高可靠性问题形式化为：训练时有昂贵但可靠的 oversight，部署时无法逐条检查，因此用两个 proxy 衡量可靠性——对抗数据集上的失败率，以及找到新对抗样本所需的时间。在基线之上做了三轮对抗训练：1. 承包商手工写对抗样本（分数低于 0.05 即可提交）；2. 用 GPT-3 few-shot 自动改写已有对抗样本，保留仍能骗过 classifier 的版本；3. 工具辅助改写，界面提供基于 deberta-v2-xlarge 的 token 替换/插入建议（按降低分数排序）和基于梯度的 saliency 高亮。主要发现：可以把阈值设得极保守（约 0.0017–0.0021，远低于训练时的 0.05），classifier 拒掉约 25% 的随机片段，但人评的 filtered 质量与未过滤 generator 基本持平（约 49% vs 50%）；对抗训练让找到对抗样本的时间翻倍，有工具时从 13 分钟到 26 分钟，无工具时从 20 到 44 分钟；越晚的 classifier 在针对早期模型的攻击上 FNR 越低，而针对最终模型的攻击在早期模型上也几乎同样有效，说明残留失败多是本来就有的而非新引入；残留对抗样本也更不"egregious"，多是隐含或间接伤害而非直接受伤；in-distribution 测试集 10 万条上各模型都只漏 2–3 个（共 2447 个正例），对抗训练没有损害分布内表现。作者把这看作探索性工作，并指出不少局限：承包商倾向于产出边缘、模糊的样本，研究员自己用工具能构造更明显的直接伤害样本，说明需要更强更多样的攻击；尝试 RL 微调 LM adversary 没有成功；高可靠性很大程度来自这个任务允许严格阈值而不掉质量，能否推广到开放式生成未知；304M 的模型很多失败可能源于能力不足；在极低失败率下随机抽样测可靠性非常昂贵（最好与最差模型的差别只是 2 vs 3 个错误），需要更好的测量方法。项目最初由 Paul Christiano 提出，改写工具已公开。

## 我的笔记

