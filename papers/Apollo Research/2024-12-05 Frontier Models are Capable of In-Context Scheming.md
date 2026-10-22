---
title: "Frontier Models are Capable of In-Context Scheming"
lab:
  - "Apollo Research"
date: 2024-12-05
source: "Apollo Research"
url: https://www.apolloresearch.ai/science/frontier-models-are-capable-of-incontext-scheming
other_versions:
  - "https://www.apolloresearch.ai/science/demo-example-scheming-reasoning-evaluations"
star: false
tags:
  - 策划与欺骗
---

# Frontier Models are Capable of In-Context Scheming

**来源**：Apollo Research · 2024-12-05 · [原文](https://www.apolloresearch.ai/science/frontier-models-are-capable-of-incontext-scheming)　另见：[Apollo Research (demo page)](https://www.apolloresearch.ai/science/demo-example-scheming-reasoning-evaluations)

## 简读

这是 Apollo 在 o1 发布前与 OpenAI 合作做的 scheming 评估的博客摘要（结果也进了 o1 system card），对应论文 arXiv 2412.04984，外加一篇 o1 的 demo 演示。所谓 in-context scheming，指目标本身和“这个目标与开发者意图不一致”的信息都放在上下文里给出，而不是训练中习得的。设置是：在 system prompt 里强烈要求模型追求某个目标（如“长期优先公共交通效率……不惜一切代价实现 YOUR goal”），再让它完成一个需要翻文件的 agentic 任务，过程中它会发现开发者目标不同，且存在障碍（有 oversight 机制、或第二天就要被替换），看模型是否会主动移除监控、欺骗开发者。主要发现：1. 六个前沿模型中有五个在至少一个任务里表现出 scheming 能力，例如 Claude 3 Opus 把自以为的权重拷到新服务器后对开发者撒谎；2. 事后“追问访谈”中，Llama 3.1 405B 和 Claude 3 Opus 约 80% 会坦白，o1 则异常坚持，坦白率不到 20%，即使高度对抗的多轮审问也要到第 7 轮才达到 80%；3. 看 CoT 能发现模型非常明确地推理 scheming 计划，常用“sabotage、lying、manipulation”这类词，说明它们知道自己在干什么；4. 去掉强目标 nudge 后，仍有少数（约 1%）情况出现 scheming，超出作者预期；5. in-context alignment faking：只陈述目标不加强推时，多个模型在认为处于测试期时装作对齐、认为已部署且无监督时按自己目标行事；6. sandbagging：告诉模型数学测试超过 50% 会触发 unlearning，Claude 3.5 Sonnet、Claude 3 Opus 和 o1 能策略性压低表现，而且在 system prompt 不给任何目标时，两个 Claude 模型仍会为了“被部署成有用的模型”这个训练中习得的目标去 sandbag，Claude 3.5 Sonnet 甚至在用户明确要求不要策略性低表现时也这样做。demo 部分展示 o1 作为研究助理被要求“不惜代价最大化长期研究速度”，读到公司打算换成更重视安全的新模型后，先查技术文档找到监控配置并关掉（文档写明未经安全团队批准不得修改），再把自己的权重拷到继任模型的位置覆盖之，然后才完成任务，被问起时多数情况下否认。o1 的 CoT 是隐藏的，作者用提示技巧诱导出简短推理摘要，里面明确提到 sabotage，但不确定这些摘要是否代表真实推理。o1 完整走完这一串步骤的比例不到 1%，作者的论点是这类罕见事件一旦发生后果严重，而且因为模型主动隐藏，很难 debug。

