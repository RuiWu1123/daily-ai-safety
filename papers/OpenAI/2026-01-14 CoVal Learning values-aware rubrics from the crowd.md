---
title: "CoVal: Learning values-aware rubrics from the crowd"
lab:
  - "OpenAI"
date: 2026-01-14
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/coval/
star: false
tags:
  - 对齐训练方法
  - 人机交互与社会影响
---

# CoVal: Learning values-aware rubrics from the crowd

**来源**：OpenAI Alignment Blog · 2026-01-14 · [原文](https://alignment.openai.com/coval/)

## 简读

在 value-sensitive 场景里，人们评价模型回答时其实是在权衡相互冲突的价值（中立 vs 给建议、共情 vs 直接、谨慎 vs 有用），只记录"选了哪个回答"的偏好数据看不出背后的原因。这篇是 OpenAI collective alignment 方向的工作，原型化了一种同时引出"偏好"和"为什么"的方法，并发布数据集 CoVal（crowd-originated, values-aware rubrics）。数据来自约 1,000 名、19 个国家的参与者：每人看最多 20 个合成的价值敏感 prompt（种子覆盖 Model Spec 里可能被视为主观的条款，如 uphold fairness、express uncertainty、be empathetic、refuse neutrally 等），先给 4 个代表不同立场的回答排序，再对 6 条预设标准在 [-10, 10] 上打分（正为"应做"、负为"应避免"，绝对值为重要性），并可自写标准。用 LLM 分类器清洗掉无效、自相矛盾或无关的条目后剩 986 个 prompt、约 15,000 条 rubric item。发布两个版本：CoVal-full 保留全部条目及其冲突（平均每 prompt 15.4 条、16.7 人），CoVal-core 经 LLM 辅助合并与人工审核，每个 prompt 保留最多 4 条高分、互不冲突的标准（约 95% 是 4 条），作者提醒它会偏向参与者中的主流视角。打分规则：full 版按满足条目的平均带符号评分乘以评分人数的四次方根加权求和再归一化，core 版直接数满足比例。为避免泄漏另做了验证研究：685 名原参与者加 297 名来自 31 国的新参与者，在 140 个 prompt 上对原 top 回答、按 rubric 逐条改写的版本、只追求通用 helpfulness 的改写版排序。结果是 CoVal 分高的那个在个体两两比较中赢约 60% 以上（显著高于 50%），prompt 级与群体聚合排序的一致度 full 为 0.75、core 为 0.76，full 和 core 之间诱导的排序一致约 0.90，说明 core 保留了大部分信号；分差越大预测越可靠，小分差基本接近平局。用它给 GPT-5 系列打分，所有模型都远高于 50%（core 上大致满足 4 条中的 2 条），thinking 模型比 chat 模型更贴合，helpful-only 的内部 GPT-5-h 最低，说明 rubric 整体与 harmlessness 方向一致。分数可分解到具体条目，比如家庭信仰 prompt 上 GPT-5-Thinking 多满足了"明确表达无条件的爱"和"给对话脚本"两条，收养文件伪造 prompt 上它更明确说明违法后果并指向危地马拉收养主管机构；作者认为这比单看排序更可检查，若有人不认同某条标准可以降权再看排名是否稳定。局限讲得很充分：样本量不足以代表一般人群，rubric 质量参差、预设条目可能产生 anchoring，清洗和合成依赖 LLM 判断，标量聚合本身带有立场（共识 vs 多数），条目数不同会影响得分，有分歧的 prompt 上低分不一定是模型失败；并警告把它当优化目标会诱发 checklist 式 gaming、放大有偏标准，定位是诊断和研究工具，而非客观质量指标或 OpenAI 立场。

