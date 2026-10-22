---
title: "Deep ignorance: Filtering pretraining data builds tamper-resistant safeguards into open-weight LLMs"
lab:
  - "UK AISI"
date: 2025-08-08
source: "AISI Research"
url: https://www.aisi.gov.uk/research/deep-ignorance-filtering-pretraining-data-builds-tamper-resistant-safeguards-into-open-weight-llms
star: false
tags:
  - 知识移除
  - 越狱与鲁棒性
---

# Deep ignorance: Filtering pretraining data builds tamper-resistant safeguards into open-weight LLMs

**来源**：AISI Research · 2025-08-08 · [原文](https://www.aisi.gov.uk/research/deep-ignorance-filtering-pretraining-data-builds-tamper-resistant-safeguards-into-open-weight-llms)

## 简读

背景是 open-weight 模型可被任意修改，现有 tamper-resistant 手段（safety fine-tuning、unlearning、Circuit Breaking 等 post-training 方法）通常几十到几百步对抗 fine-tuning 就被撤销，可能是因为 post-training 只学了一层"wrapper"而没改动底层知识。EleutherAI 与 UK AISI、Oxford 合作，换个思路问：如果在预训练阶段就不让模型学到危险知识，能否得到更深的 ignorance？以 biothreat proxy 知识（WMDP-Bio）为例，他们设计了多阶段过滤 pipeline：先用 Llama 3.3 70B 从 WMDP-Bio Forget 语料里生成关键词黑名单，约 91% 的文档不含两个以上关键词直接放行，命中的再交给微调过的 ModernBERT 分类器判断，过滤成本不到训练 FLOPs 的 1%。他们从头预训练多个 Pythia 架构的 6.9B 模型（500B DCLM + 50B annealing），对比无过滤 baseline、Strong Filter（只用黑名单，删掉约 8–9% 文档）和 Weak Filter（annealing 阶段加分类器），以及 CB、CB+LAT 两个 post-training baseline。为避免 WMDP 选择题被启发式刷分（选最长答案就有 46%），他们只用去掉"不看题也能猜对"样本的 Robust MCQA 子集和 cloze 形式评估。主要发现：1. 过滤显著压低 bio proxy 知识，cloze 上接近随机，通用能力（MMLU 非生物部分等）无明显下降，总体与 CB 相当（CB 在 MCQA 上略好，过滤在 cloze 上略好）；2. 抗篡改是亮点，在 WMDP-Bio Forget 上做 10,000 步、约 3 亿 token 的全参数与 LoRA 对抗 fine-tuning 后过滤模型仍基本保持无知，比 post-training baseline 强一个数量级以上，且 benign fine-tuning（WikiText）下 CB 很快失效而过滤模型不受影响，唯一例外是 MCQA 下的 latent-space 攻击意外有效；3. 过滤挡不住 in-context 检索，题目答案放进上下文（模拟搜索工具）时过滤模型照样能用，而叠加 CB 能阻止这一点，过滤+CB 组合在各类攻击下最好，但 fine-tuning 加 open-book 的组合攻击没有任何防御扛得住；4. 负面结果：仿照 Anthropic 的思路用 Claude 3.7 生成"错误生物知识"合成文档混入训练，没有带来改进，有时反而增加了 proxy 知识，作者猜测是生物味数据让模型更会利用评估启发式。作者对比 Maini et al. 等"过滤毒性数据反而不更安全"的结果，提出假设：过滤对来自少量文档的精确知识有效，而对毒性、顺从有害请求这类不需要精确知识的涌现倾向未必有效。讨论中坦承 1 万步在绝对意义上不算多，但真正瓶颈可能是高质量危险数据（WMDP 造价超过 20 万美元）。局限：仅 6.9B、未做 instruction tuning、能力不具竞争力、只测 bio proxy 选择题、攻击只能给下界。模型和代码开源，但出于谨慎不发布过滤后的预训练数据。论文已被 ICLR 2026 接收。

