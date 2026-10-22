---
title: "An update on our general capability evaluations"
lab:
  - "METR"
date: 2024-08-06
source: "METR Research"
url: https://metr.org/blog/2024-08-06-update-on-evaluations/
tags:
  - 危险能力评估
  - 评估方法
---

# An update on our general capability evaluations

**来源**：METR Research · 2024-08-06 · [原文](https://metr.org/blog/2024-08-06-update-on-evaluations/)

## 简读

Beth Barnes 写的阶段性研究更新：METR 发布 autonomy evaluation resources 之后，主要在做两件事，一是可作为 "red line" 的 AI R&D 评估，二是对一般自主能力的连续度量，这篇讲后者，结果是初步的。为什么不只做针对具体威胁模型的 red line：一般自主能力本身不直接导致灾难，但它是 AI 在少量人类参与下对世界产生深远影响程度的代理指标，对多种威胁模型都有用；覆盖多个能力尺度的度量比只有难题的评估更适合做预测；包含当前系统能做或稍加 scale/post-training 就能做的任务，能给开发者和评估机构提供更有用的 elicitation 反馈循环。具体工作：在之前的示例任务集基础上新增约 50 个自动打分任务（JSON 格式转换、网站命令注入、写 CUDA kernel 加速 Python 脚本、训练音频分类模型等）；从内部较高质量的 baseliner 池（多数有 STEM 本科学历、过半有 3 年以上技术工作经验）收集约 200 次人类基线，任务难度从不到 5 分钟到平均超过 16 小时，多数在 15 分钟到 4 小时之间。按任务族大小用 1/√n 降权，并让加权分布在人类用时上呈 log-uniform。主要发现：最强的 Claude 3.5 Sonnet 和 GPT-4o agent 完成的任务比例相当于人类约 30 分钟能完成的水平，但 agent 成功的任务和人类不完全重合；agent 在人类用时短的任务上更易成功，GPT-4o 能完成约 60% 的人类 15 分钟以内的任务，以及约 10% 人类超过 4 小时的任务。原先按 800 美元（约合美国大学毕业生 20 小时工资）设 token 预算，但简单 scaffold 下表现大约在 20 万 token 就平台化，所以只跑到每任务约 200 万 token；作者猜测原因之一是 agent 常在预算远未用完时就提交，并认为用 reward model 做 best-of-n 之类的 scaffold 改进能更好地利用大预算。在人和 agent 都能做好的任务上，agent 平均成本约为美国本科学历者时薪中位数的 1/30，例如 Claude 3.5 Sonnet 用约 38.2 万 token（不到 2 美元）修好 ORM 库 bug，人类花了两个多小时；而 agent 表现随成本的边际收益递减，与人类的 log-linear 关系形成对比。局限和下一步：很多任务只有一两个人类基线，没有指导 baseliner 如何权衡时间和完成确定性，elicitation 很基础，后续会增加基线、扩充更多样且质控更好的任务、改进 elicitation，作者认为这类工作有助于预测前沿模型的现实影响、理解风险如何随 effective compute 增长，并为基于实证的政策提供依据。

## 我的笔记

