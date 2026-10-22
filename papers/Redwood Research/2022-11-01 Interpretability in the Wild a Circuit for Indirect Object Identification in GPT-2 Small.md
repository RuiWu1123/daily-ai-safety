---
title: "Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small"
lab:
  - "Redwood Research"
date: 2022-11-01
source: "Redwood Research"
url: https://arxiv.org/abs/2211.00593
other_versions:
  - "https://www.alignmentforum.org/posts/3ecs6duLmTfyra3Gp/some-lessons-learned-from-studying-indirect-object"
star: false
tags:
  - 可解释性
---

# Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 Small

**来源**：Redwood Research · 2022-11-01 · [原文](https://arxiv.org/abs/2211.00593)　另见：[Alignment Forum](https://www.alignmentforum.org/posts/3ecs6duLmTfyra3Gp/some-lessons-learned-from-studying-indirect-object)

## 简读

背景是 mechanistic interpretability 以往要么解释小模型里的简单行为，要么对大模型里的复杂行为只做粗线条描述，缺少在真实语言模型里端到端逆向一个"自然"行为的例子。这篇工作选了 indirect object identification（IOI）任务：比如 "When Mary and John went to the store, John gave a drink to" 应补全为 "Mary"，对应一个可解释算法——找出句中名字、去掉重复的那个、输出剩下的。GPT-2 small 在这个任务上 logit difference 均值 3.56，99.3% 时间预测 IO 而非 S。方法上他们提出 path patching，即只在从某个 head 到下游指定组件的直接路径上替换为另一输入（三个无关名字的 pABC 分布）的激活，从 logits 一步步往回追踪信息流，再配合 attention pattern 分析、embedding 空间投影和 mean ablation（在 pABC 上按模板取均值，而非 zero ablation）来刻画每个 head 的作用。最终找到 26 个 attention head、分为 7 类组成的 circuit：Duplicate Token Heads 和 Induction Heads 在 S2 处识别出重复名字，Previous Token Heads 为 induction 提供信息，S-Inhibition Heads 在 END 处把 S 的 token 信号和位置信号（位置信号作用更大）写进 Name Mover Heads 的 query，抑制它们对 S1/S2 的注意，Name Mover Heads 最后把 IO 复制到输出（copy score 超过 95%）。几个意外发现：1. Negative Name Mover Heads 稳定地朝正确答案的反方向写，作者猜测是在 hedge 以降低出错时的 cross-entropy；2. 把 Name Mover Heads 全部 knock out 后 logit difference 只掉 5%，因为一组 Backup Name Mover Heads 接管了这一角色，作者猜测与训练中的 dropout 有关，这让"找完整机制"变得更难；3. induction heads 在这里被用作位置指针，而非其原本描述的功能。为了验证解释，他们提出三个标准：faithfulness（circuit 达到全模型 87% 的表现）、completeness（对任意子集 K 做 knockout，circuit 与全模型应仍相近）和 minimality（circuit 里每个节点都有非平凡贡献）。随机采样和按类别 knockout 下 circuit 看起来是完整的，但贪心搜索能找到不完整性分数高达 3.09（原 logit difference 的 87%）的子集，且这些子集语义上难以解释，所以 circuit 没通过最严格的检验。他们还利用对 circuit 的理解构造对抗样本：让 S 和 IO 都重复出现，模型就有 23% 的情况预测 S，而对照组只有 0.4%；但作者坦承这类样本不靠 circuit 也能找到。局限包括 S-Inhibition 的注意力模式、MLP 和 layer norm 的作用未搞清，模型规模离 SOTA 差很远；对 GPT-2 medium 的初步分析显示直接影响 logits 的 head 行为更复杂。作者把这种窄而细的研究类比为生物学中的 model organism，代码开源在 Easy-Transformer。

