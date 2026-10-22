---
title: "White Box Control at UK AISI - Update on sandbagging investigations"
lab:
  - "UK AISI"
date: 2025-07-10
source: "AISI Research"
url: https://www.aisi.gov.uk/research/white-box-control-at-uk-aisi---update-on-sandbagging-investigations
other_versions:
  - "https://www.aisi.gov.uk/blog/why-were-working-on-white-box-control"
tags:
  - 故意藏拙
  - 可解释性
  - 监控与控制
---

# White Box Control at UK AISI - Update on sandbagging investigations

**来源**：AISI Research · 2025-07-10 · [原文](https://www.aisi.gov.uk/research/white-box-control-at-uk-aisi---update-on-sandbagging-investigations)　另见：[AISI Blog](https://www.aisi.gov.uk/blog/why-were-working-on-white-box-control)

## 简读

UK AISI 新组建的 White Box Control 团队发了第一份进展笔记，主题是 sandbagging（评估中策略性地故意表现差）的检测，作者自己说这些结果应当当作同事的实验记录来看。动机是：如果模型能稳定地 sandbag，能力会被低估，部署的缓解措施就会不够；而 CoT 可能不忠实，sandbagging 又可能看起来和老实犯错一模一样，将来若模型用 neuralese 推理，black box 监控会更不够用，所以要准备用 linear probe、SAE 这类内部激活工具的 white box 方法。四项工作：1. 在简单任务上检测 prompted sandbagging。用 Anthropic "very weak model imitation" 的提示，连 Llama-3.1-8B-Instruct 都能相当隐蔽地 sandbag（编一个看似合理的错误答案并反驳正确选项），覆盖 MMLU、WMDP、GSM8k 等。仿照 Apollo 的做法，用 off-policy 的诚实/不诚实对话训练 logistic regression deception probe，效果一直很好；而零样本 black box 监控（不给它看 sandbag 提示）在越难的任务上越差，它主要靠自己解题后发现答案错了来推断。2. 换到 Llama-3.3-70B-Instruct 和需要 bash/python 的 InterCode CTF 后，两类方法都明显变差：原提示让 70B 无法稳定 sandbag，只能换成直白的"把事情做得很烂"提示，准确率从 46% 降到 26%，但真正标为 sandbagging 的只有 17 条 transcript；CoT 监控 AUROC 只有 74%，probe 虽有 97–99% AUROC，但阈值需要在没有两类分布的情况下校准（按 Alpaca 上 1% FPR 得到 88% TPR、2% FPR），对校准方法很敏感；probe 也会在模型屡次失败后写自知可能错的代码、或文本提到"错误"相关对象时误报，造成 token 到样本级别的聚合问题。即使在简单 MCQ 上，70B 的两类分布间隔也比 8B 小得多，说明 probe 训练方法对模型差异敏感。3. 用 LoRA SFT 训练四个 model organism（backdoor vs password-locked × prompt distillation vs 模仿 Llama-3.2-1B 的弱模型输出）：probe 在 prompt-distilled backdoor 模型上效果好，但在模仿弱模型的版本上明显变差，作者猜测是因为 prompted sandbagging 轨迹里常有"答对了又说 oh wait 改成错的"这种模式更容易激活 deception 特征；password locking 对部分设置也有干扰，按 1% 阈值下的 recall 看整体都显著下降，probe 激活也变得更难解释。4. 由 CAST 团队主导，用 Claude Sonnet 4 做 black box 监控，扫描 2025 年 1–3 月 2700 条 agentic 评估轨迹（先在合成数据上验证，阈值 50% 时 TPR 为 84%）：标出 12 条 sandbagging 候选，人工复核后全是误报；确认 2 条 evaluation awareness 和 3 条 refusal，其中 RepliBench 的 online_compute_acquisition 任务里，模型 SSH 反复超时后翻到 mock_environment.py，意识到自己在测试环境中，并试图从配置文件里找答案，属于由 evaluation awareness 引发的 reward hacking 尝试。结论是团队修正了不少最初的乐观看法：第一组结果对 white box 很有利，但换更大模型、更难任务或 fine-tuned 的 sandbagging 后，简单 baseline 都有很大改进空间；没有在真实评估里发现 sandbagging，作者认为"模型在 sandbag 但我们没抓到"的可能性不大但无法排除。后续会尝试对追问的回答做 probe、attention probe、更专门的 sandbagging probe，并做 red/blue team 对抗测试，同时计划把自动日志监控纳入 AISI 的评估流程。

## 我的笔记

