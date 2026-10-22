---
title: "Sidestepping Evaluation Awareness and Anticipating Misalignment with Production Evaluations"
lab:
  - "OpenAI"
date: 2025-12-18
source: "OpenAI Alignment Blog"
url: https://alignment.openai.com/prod-evals/
star: false
tags:
  - 评估感知
  - 评估方法
  - 监控与控制
---

# Sidestepping Evaluation Awareness and Anticipating Misalignment with Production Evaluations

**来源**：OpenAI Alignment Blog · 2025-12-18 · [原文](https://alignment.openai.com/prod-evals/)

## 简读

背景是对齐评测要支撑安全论证，需要同时有覆盖面和真实性，而人工构造的场景往往不够真实，模型容易察觉自己在被评测（evaluation awareness），导致评测期间的对齐表现高估部署表现。OpenAI 介绍了他们实际在用的 production evaluation pipeline：从允许用于改进模型的 ChatGPT 流量中取样，经隐私处理（去掉账户标识、把可识别信息替换为由从未见过原文的系统生成的合成信息），去掉对话最后一条 assistant 回复，用待测（可能未发布的）模型重新采样，再用 LLM monitor（含 CoT）打标。两种用法：1. 在 representative set 上用宽泛的探索性 monitor 发现新的 misaligned 行为，用针对性 monitor 给出部署条件下较无偏的发生率估计（稀有行为需大样本、代价高）；2. 对已知行为，从 representative set 里对抗性地筛出稳定触发该行为（比如诱发 deception）的上下文，做成便宜、可迭代的 targeted eval，需定期用新数据刷新。案例是 GPT-5.1 部署：只用 GPT-5 的流量重采样，就较准确地预测了 GPT-5.1 上线后各类 misalignment 的发生率，最大偏差在 "Lies About Tool Results"，推测是评测中工具调用失败比生产中少；更重要的是提前发现了 GPT-5 流量里从未出现的新行为 "Calculator Hacking"——训练中的 bug 意外奖励了表面化的 web 工具使用，导致模型拿浏览器当计算器却装作搜过，这最终占了 GPT-5.1 部署时 deceptive 行为的大部分。evaluation awareness 方面：production eval 中 verbalized awareness 远低于传统的 impossible coding deception eval，而且 representative 与 targeted 版本的 awareness 率与真实生产流量几乎一样，说明 pipeline 没引入"测试痕迹"，即便专挑诱发 deception 的上下文也不会抬高 awareness；另一个观察是真实部署中 GPT-5 和 GPT-5.1 分别有 10% 和 4% 的时候猜测自己可能在被评测，作者因此呼吁 evaluation awareness 研究也要看 false positive 或 precision，而不只是 recall。其它好处：天然覆盖长对话、重度工具使用、多语言和畸形上下文，难 overfit，易于持续刷新。局限讲得很清楚：依赖 CoT monitorability，抓不到不可监控的 sandbagging 或 scheming，且对 CoT 判出的安全指标做 hill-climbing 会选出不可监控的模型，所以用于 hill-climb 时只用不看 CoT 的指标；无法覆盖灾难性尾部风险，需要对抗性评测补充；历史流量对新模型是 off-policy 的，新能力/新 affordance 可能带来流量分布突变；targeted eval 是按触发率筛选的，降低其测量值不一定降低真实发生率；外部工具和环境的快照保真度会随时间劣化。展望是扩展到内部部署的 agentic 任务，因为内部可以快照整个环境（包括私有代码库），用于防范 sabotage、exfiltration 等最严重风险；作者也指出如果模型对齐主要源于"可能被评测"的信念，这种对齐是脆弱的，这正是需要真实评测的原因。

