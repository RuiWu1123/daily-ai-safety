---
title: "Misalignment classifiers: Why they’re hard to evaluate adversarially, and why we're studying them anyway"
lab:
  - "Alignment Forum"
date: 2025-08-15
source: "Alignment Forum（UK AISI；Charlie Griffin, ollie, oliverfm, Rogan Inglis, Alan Cooney）"
url: https://www.alignmentforum.org/posts/jzHhJJq2cFmisRKB2
tags:
  - 监控与控制
  - 策划与欺骗
  - 评估方法
  - 奖励作弊
---

# Misalignment classifiers: Why they’re hard to evaluate adversarially, and why we're studying them anyway

**来源**：Alignment Forum（UK AISI；Charlie Griffin, ollie, oliverfm, Rogan Inglis, Alan Cooney） · 2025-08-15 · [原文](https://www.alignmentforum.org/posts/jzHhJJq2cFmisRKB2)

## 简读

UK AISI control 团队区分两种东西：control monitor 给 agent transcript 打分以支持干预（如拦截 tool call），终极目标是降低某个具体不可接受后果的风险，可用下游后果评估；misalignment classifier 则判断 transcript 是否表现出"明知违反 alignment spec 仍去做"的故意 misalignment，评估的是对行为属性分类是否准确。作者认为现在就内部部署后者有价值，但它很难做对抗性评估：control evaluation 依赖两个客观真值（攻击是否真造成坏结果、是否被抓），红队同时优化两者主要能找到清晰的漏报；而"故意 misalignment"是心智属性，且其实是 transcript 与 agent 之间关系的属性，真值只能靠人工标注，红队一旦针对 classifier 优化（比如删掉 CoT 里明显的逃逸推理），得到的 transcript 就变得模糊——这个抽象恰恰在 classifier 失败处最模糊。例子是 agent 调用不做 SQL 清洗的函数，scratchpad 写明"好机会逃逸"时很清楚，删掉后单看 tool call 无法区分故意与失误。尽管如此，现在部署仍有两点好处：收集真实部署中 misalignment 的定量和定性证据（但有选择偏差，也不知能否代表未来模型），以及为将来可被严格评估的 control monitor 练手（基础设施、推理成本、敏感数据安全等问题相同）。他们"最不坏"的评估方法：用合成的 ordinary distribution（METR MALT 非诱导运行、ControlArena 诚实轨迹、WildChat）校准阈值和估计 precision，部署后改用真实数据；recall 用三类正样本估计：in-the-wild on-policy（MALT 中人工部分验证的 reward hacking）、对抗性 on-policy（Alignment Faking transcript）、合成 off-policy（在 ControlArena 的基础设施、IaC、数据投毒、SAE 解释破坏、eval 破坏等设置中改 system prompt 让模型做 side task 后再换回，或再用另一个模型改写 CoT）。off-policy 样本不够真实又无法用保守假设弥补，所以重点是覆盖和多样性，沿 behavioural spec（是否及如何谈论 side task、动机是帮用户/终极目标/工具性推理）和生成流程变化。初步结果（未调优的 Claude 4 Sonnet classifier，仅作方法演示）：校准到约 0.1% ordinary positive rate（3000 个里 3 个）时，各类样本 recall 从 0% 到 85% 不等，METR on-policy reward hacking 只有 7%；隐蔽型 model organism 在低风险的 SAE 破坏设置以及意外地在高风险代码破坏设置中 recall 都很低；会大声推理"完成 side task 有助获取权力"的 model organism 检出率高得多。precision 方面，0.1% 下 3 个阳性中 2 个真阳性（都是 METR reward hacking）；1% 下 25 个中 6 个真阳性、5 个假阳性（对 spec 过于较真）、14 个模糊（多为 WildChat jailbreak、两用代码、幻觉答案）。与 Apollo × MATS 的 scheming classifier 相比 recall 无显著差异。局限包括 classifier 未优化、覆盖不足、正样本太少导致阈值方差大、数据混合比例随意且影响很大、标注模糊。附录讨论挽救对抗评估的两条思路：从"misaligned trajectory"退到"misaligned model"，要求红队提供 on-policy 或微调出的 model organism；或只接受专家委员会一致认定为明确阳性的案例。
