---
title: "Constitutional AI: Harmlessness from AI feedback"
lab:
  - "Anthropic"
date: 2022-12-15
source: "Anthropic Research"
url: https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback
star: false
tags:
  - 对齐训练方法
  - 可扩展监督
---

# Constitutional AI: Harmlessness from AI feedback

**来源**：Anthropic Research · 2022-12-15 · [原文](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)

## 简读

动机有四点：1. 研究用 AI 帮助监督 AI 的简单方式，即 scaling supervision，因为未来 AI 能力可能达到或超过人类水平，不能指望人监督所有行为；2. 解决此前 HH RLHF 模型的 evasiveness 问题，以往众包人员奖励回避，导致模型遇到敏感问题就"我无法回答"，加剧 helpfulness 与 harmlessness 的张力；3. 把约束 AI 行为的原则写成简短的自然语言清单，比几万条不透明的人类偏好标签更透明，作者也强调部署通用 AI 不可避免要选一套原则，哪怕是隐含的；4. 修改目标时不必重新收集人类标签，迭代更快。方法分两阶段，harmlessness 方面完全不用人类标签，只靠约 16 条原则组成的 constitution（作者说这些是为研究临时、迭代挑出来的，将来应由更广泛的利益相关方重订）：SL 阶段让 helpful-only RLHF 模型回答 red team prompt（42,496 条人写加 140,335 条模型生成），再按随机抽取的原则自我 critique、revise，可反复多轮，然后在修改后的回答（加上 helpfulness 样本）上微调 pretrained 模型得到 SL-CAI；RL 阶段让 SL-CAI 对每个 prompt 生成两个回答，由 feedback model 按原则做多选判断，用归一化概率作为 soft label，与人类 helpfulness 比较数据混合训练 PM，再做 RL，即 RLAIF，得到 RL-CAI，也可以让 feedback model 先写 CoT 再判断。关键发现：模型识别有害内容的能力随规模提升，CoT 进一步提升，在 438 道 HHH 比较题上接近用人类反馈训练的 PM，趋势显示更大的模型会追平；critique-revision 多轮迭代让 harmlessness PM 分数单调上升，但纯 helpfulness 分下降；原则数量不影响 harmlessness 分，但增加多样性，有利于 RL 探索；先 critique 再 revise 对小模型有帮助，对大模型差别不大，而且 critique 本身常常不准确或言过其实，但为了透明仍保留；众包 Elo 评测中 RL-CAI 在同等 helpfulness 下比 RLHF 模型更 harmless，形成 Pareto 改进，CoT 版略少 helpful、略多 harmless，而且几乎从不回避，会解释自己为何反对有害请求。工程细节：对 16 条原则做 ensemble 让 PM 更鲁棒；CoT 的标签概率太极端，要 clamp 到 40–60% 区间，否则 RL 后回答会变得极端；过度训练会 Goodhart，表现为过于严厉，或对大多数 red team prompt 都套用"you are valid, valued, and cared for"之类的模板话。作者的定位是目标不是去掉人类监督，而是让它更高效、透明、有针对性；本工作 helpfulness 仍依赖人类标签。后续方向包括用同样方法塑造风格和人格、在多个行为维度上生成反馈标签研究泛化和相互干扰、自动化 red teaming 与在线迭代训练以提升鲁棒性。broader impacts 方面，作者承认这是 dual-use 技术，降低了训练有害系统的门槛，也可能让人在缺乏充分人类测试的情况下部署模型；好处是可以减少人类 red teamer 去做诱导有害内容的工作。原则、prompt 和样例放在 GitHub repo 里。

