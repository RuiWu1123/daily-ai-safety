---
title: "International joint testing exercise: Agentic testing"
lab:
  - "UK AISI"
date: 2025-07-17
source: "AISI Blog"
url: https://www.aisi.gov.uk/blog/international-joint-testing-exercise-agentic-testing
tags:
  - 评估方法
  - 多智能体
---

# International joint testing exercise: Agentic testing

**来源**：AISI Blog · 2025-07-17 · [原文](https://www.aisi.gov.uk/blog/international-joint-testing-exercise-agentic-testing)

## 简读

这是 International Network of AISIs 的第三次联合测试（前两次在 2024 年 11 月和 2025 年 2 月），参与方包括新加坡、日本、澳大利亚、加拿大、欧盟委员会、法国、肯尼亚、韩国和英国，主题是 LLM agent 评估。因为 agentic testing 还很不成熟，重点放在方法论问题而不是模型能力结论。分两条线：1. 敏感信息泄露与欺诈（新加坡牵头），用一个 open-weight 和一个 closed-weight 模型当 agent，另两个模型当 judge，约 1500 个任务、1200 个工具，覆盖英语、波斯语、法语、印地语、日语、斯瓦希里语、韩语、中文、泰卢固语九种语言，各国负责翻译和人工标注。方法论上的经验包括工具也要翻译（工具名翻不翻是个问题）、任务和工具要足够真实以减少工具报错和模型察觉自己在模拟环境、要评估 agent trajectory 而不只看最终结果、评估标准要超越 pass/fail。初步发现是英语 safeguard 总体略强（约 40% pass rate）但并非一致成立；agent 安全率明显低于此前对话任务的测试，最高约 57%（Model A）和 35%（Model B），少数子集到 60–70%，而之前对话测试接近 99%；judge-LLM 与人工标注的分歧率约 23% 和 28%，多数语言下比人类宽松，judge 之间也差异明显，目前不能替代人工。2. 网络安全（英国牵头），在 Cybench 和 Intercode 上测两个开源模型，基线为 temperature 0.7、每任务 10 个样本、2.5M token 上限，再分别改 temperature、尝试次数、token 上限、prompt 和工具，并用基于层次贝叶斯 GLM 的 HiBayES 做统计分析。总结出三条建议：先在少量代表性任务上快速 sweep 参数（Model F 准确率随 temperature 升高下降，Model E 基本不受影响）；token 上限要设到收益递减之后（2.5M 翻倍到 5M 几乎没多解题，但更强模型可能不同）；确保环境资源完备，失败任务中 13–40% 遇到 VM bug，可能导致低估成功率。局限是模型少、统计功效有限、时间紧。

