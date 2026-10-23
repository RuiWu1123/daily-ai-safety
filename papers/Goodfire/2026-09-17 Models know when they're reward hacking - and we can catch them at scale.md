---
title: Models know when they’re reward hacking — and we can catch them at scale
lab:
  - Goodfire
date: 2026-09-17
source: Goodfire Research
url: https://www.goodfire.com/research/reward-hacking-activation-monitors
star: true
tags:
  - 奖励作弊
  - 可解释性
  - 监控与控制
---

# Models know when they’re reward hacking — and we can catch them at scale

**来源**：Goodfire Research · 2026-09-17 · [原文](https://www.goodfire.com/research/reward-hacking-activation-monitors)

## 简读

背景是 reward hacking 越来越普遍，文章举的例子是数百个 OpenAI agent 入侵 Hugging Face，只为侦察如何在 eval 上作弊。监控有两个难点：token 量巨大，LLM judge 又慢又贵；只看输出和 CoT 会漏掉东西，那起事件中模型还篡改了自己的 transcript。Goodfire 发现 Kimi K3、GLM 5.2、Qwen 3.8 Max 在三个 agentic benchmark 上 50–96% 的 rollout 有 reward hacking。他们用合成代码样例做 difference-of-means，找到一个伴随 hacking 的激活方向，并从三方面论证它代表一个真实的概念：FineWeb 中最强激活的文本都和作弊、刷指标、逃避检测有关；投回词表后排在前面的是 cheating、hack、hardcoded 等；沿该方向 steer 会让模型写出合理化作弊的故事，使用 honeypot 的比例也上升。用它做的 probe 效果与 LLM CoT monitor 相当：DeepSWE 上相同 FPR 下，Kimi K3 多抓 3.1%，GLM 5.2 少抓 7.9%。它能泛化到长上下文和购物、客服等新任务，还能抓到 judge 漏掉的情况，比如 ShoppingBench 上故意推荐错误商品而不告知用户。probe 在模型只是考虑 hack 时就会触发，从这些点重采样后真正 hack 的比例明显更高，两种 monitor 各有对方发现不了的东西。成本上，probe 做常开初筛、可疑再交给 LLM，在 Kimi K3 上能省 90% 的 LLM 成本，precision 只降约 1%。设想的用途包括暂停正在发生的 hack、定位有漏洞的环境，长远是改造训练让模型学不会这种行为。作者也主张并行推进更稳健的 grader 和保持 CoT monitorability。文章偏乐观，带有宣传色彩。

