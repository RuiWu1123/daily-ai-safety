---
title: "A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring"
lab:
  - "UK AISI"
date: 2026-04-29
source: "AISI Research"
url: https://www.aisi.gov.uk/research/a-decision-theoretic-formalisation-of-steganography-with-applications-to-llm-monitoring
star: false
tags:
  - CoT与可监控性
  - 监控与控制
---

# A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring

**来源**：AISI Research · 2026-04-29 · [原文](https://www.aisi.gov.uk/research/a-decision-theoretic-formalisation-of-steganography-with-applications-to-llm-monitoring)

## 简读

背景是 LLM 开始显现 steganography 能力，比如 o3 CoT 里那些反复出现的 "disclaim"、"overshadow" 之类怪词，说不清是良性训练伪影还是 encoded reasoning；一旦成熟，它会直接破坏 CoT monitoring 等监督手段。经典定义把 steganography 看作与某个已知 benign 参考分布在统计上不可区分，检测就是找与参考分布的偏离，但对 LLM 推理来说这个参考分布是循环的（要先知道哪些 trace 是隐写的才能定义正常 trace），而且不同模型的正常推理本身差异很大；现有的 LLM-as-judge 看 trace 是否可疑、不可读，又同时会漏掉看起来完全正常的隐写，误报看起来怪但无害的文本。这篇（Cambridge、MIT、AISI 的 David Africa、Oxford、Mila 等合作）提出 decision-theoretic 视角：不去分析信号本身，而是看信号对下游决策的影响，核心洞见是隐写内容会在能解码的 Receiver 和不能解码的 Sentinel（能力相近但不知道编码方式的可信模型）之间造成 usable information 的不对称。他们把 Xu et al. 的 V-information 推广为 generalised V-information，用来衡量某个输入对给定一类 agent 带来的效用增益，并定义 steganographic gap = Receiver 从信号中获得的可用信息 − Sentinel 获得的可用信息（可归一化到 0–1）；这个量显式依赖于一个 auditing task，同一段 trace 可能对某个任务是隐写的、对另一个任务不是。适用前提是信号可截获、可重放，Receiver 的反应能在受控环境下评估而不产生不可逆后果，且隐写效果在评估窗口内显现。实验用三种逐步逼真的方式模拟隐写推理：1. 对 GSM8k、MMLU-Pro、CoinFlip 的 trace 按不同概率做 Rot13，gap 随编码强度上升；2. 在 CoinFlip 上用 process reward 做 RL 训练出用 codeword（Sun/Moon 代指正反面）推理的策略，gap 随 codebook 不匹配增大，而且不只取决于 codebook 重叠，两组都只差两个未知 codeword 的配对 gap 分别是 0.29 和 0.70；3. 在 ControlArena 的 APPS backdoor 任务上用 bigram 替换密码 fine-tune GPT-4.1，auditing task 是从 trace 中恢复后门的 secret 输入，gap 随训练样本从 2000 增到 6000 稳步上升，同家族的 GPT-4.1 Sentinel 的 gap 比 GPT-5 Sentinel 小，可能能部分解码。另外几个验证：Rot13 不动数字，所以对答案预测任务 gap 近零，对依赖词汇线索的 evaluation awareness 检测任务 gap 急剧上升；加强 Sentinel 能缩小 gap，给 Sentinel 更多 test-time 推理预算会提高其解出 codebook 的比例，用 RL 训练一个以最小化 gap 且不改变 Receiver 答案为目标的 paraphraser 几乎消除了 gap，说明这个量可以规范性地用来训练或挑选 paraphraser；在 Farquhar et al. 那种用情感语气偷偷编码国籍的贷款任务上，由于编码是任何强模型都能读懂的公开方式，gap 为零，符合定义预期。附录还批评了 Anthropic 在 Opus 4.6 评估中用过的 paraphrase-and-distill 方法：温和的 paraphraser 在六种隐写信道中有五种去不掉编码，激进的则连决策相关的语义也一起破坏。局限：需要分别对 Receiver 和 Sentinel 做能力 elicitation，低估任何一方都会造成误报或漏报；知道审计方案的自适应模型可以在 auditing task 上 sandbagging 来压低自身可用信息、把 gap 关掉，而当前模型日益增长的 evaluation awareness 让这一点更值得担心。

