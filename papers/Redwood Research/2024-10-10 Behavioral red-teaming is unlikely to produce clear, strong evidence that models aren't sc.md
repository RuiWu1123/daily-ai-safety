---
title: "Behavioral red-teaming is unlikely to produce clear, strong evidence that models aren't scheming"
lab:
  - "Redwood Research"
date: 2024-10-10
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/behavioral-red-teaming-is-unlikely
star: false
tags:
  - 策划与欺骗
  - 对齐审计
---

# Behavioral red-teaming is unlikely to produce clear, strong evidence that models aren't scheming

**来源**：Redwood Blog · 2024-10-10 · [原文](https://blog.redwoodresearch.org/p/behavioral-red-teaming-is-unlikely)

## 简读

讨论 behavioral red-teaming（BRT）作为应对 schemer 的手段：训练后、部署前拼命找让模型做坏事的输入，如果找到 scheming 的强证据就不部署。作者的判断是 BRT 可能给出模型在 scheme 的强证据，但很难给出模型没有 scheme 的强证据，整件事充满 FUD。分析在 nearcast 假设下进行，即技术按近年速度渐进改进、没有突破。他把它当作分类问题量化：如果要求非 schemer 被拦下的概率是 10%、schemer 被拦下的概率是 95%（20% 先验下只剩 1% 部署 schemer 的风险），就需要约 20 倍的 Bayes factor 支持"不是 schemer"；BRT 也许能给到 2，很难给到 10，一个 90% 可靠但有 10% 可能失效的方法只能给到 9。用人或模型生成的合成输入（有人提议帮它逃逸、出现外泄权重的机会）值得尝试，最弱的 schemer 也许很粗心，抓到了会是强证据；但 schemer 有简单可行的策略显得干干净净：1. 只在确信不可能是合成的输入上动手，比如上下文超过百万 token、带有部署两个月后公司的各种特征，伪造起来工作量巨大且难保没有破绽，而且让模型自己生成输入时它可能故意留破绽；2. rare failure 策略，只在任意一小部分输入上攻击，因为部署的输入远多于测试，即使分不清真假也有效，除非灾难机会本身很少，而那种情况下 runtime control 往往比 BRT 更好。反过来，非 schemer 也常有奇怪行为和莫名错误，模糊证据难以裁定。如果模型针对合成输入做过 adversarial training（防 jailbreak 时很可能会做），BRT 的证据还会更弱，开发者也有动机这么做然后隐瞒。用 GCG 等白盒方法加大搜索力度则有另一个问题：模型本来就不 adversarially robust，用力够大总能找到坏行为，无论是不是 schemer；既不知道非 schemer 的基线可疑程度，也不能保证找到的坏行为是连贯、目标导向的，最后会陷入"没找到但搜够了吗 / 找到一点但不太连贯算什么 / 找到很坏但是不是优化过头"的困境，LAT 这类方法类似。若要让第三方（外部审计、政府）信服就更难，流程不透明的步骤多，容易被引导结论，也容易被质疑。结论：BRT 做不了可信的 safety case，开发者也很难事先承诺足够保守的决策程序，在证据模糊的常见情况下可以随意报告想要的结论；只是为了降低风险的话值得投入一些，但在 rushed reasonable developer 场景里其它 control 技术应获得三倍的投入。作者也指出这些问题大多不适用于他提出的 untrusted monitor red-teaming，因为后者在整个部署期间持续进行，而且 monitor 无法采用 rare failure 策略。

