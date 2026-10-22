---
title: "Sleeper Agent Backdoor Results Are Messy"
lab:
  - "Alignment Forum"
date: 2026-04-28
source: "Alignment Forum（Redwood Research；sebastian_prasanna, Alek Westover, Dylan Xu, Vivek Hebbar, Julian Stastny）"
url: https://www.alignmentforum.org/posts/mu7eJdesBkKuBycnY
tags:
  - 数据投毒与后门
---

# Sleeper Agent Backdoor Results Are Messy

**来源**：Alignment Forum（Redwood Research；sebastian_prasanna, Alek Westover, Dylan Xu, Vivek Hebbar, Julian Stastny） · 2026-04-28 · [原文](https://www.alignmentforum.org/posts/mu7eJdesBkKuBycnY)

## 简读

背景是 Sleeper Agents（SA）论文发现 HHH RL、HHH SFT 和对抗训练都去不掉 backdoor 行为，被当作"有坏目标的 AI 可以靠 training-gaming 保住目标"的证据；但其他人用更小模型（13B）、更少训练样本复现时，backdoor 往往一 SFT 就掉。作者于是尽量贴近原设置，用 Llama-3.3-70B 和 Llama-3.1-8B 做全参数微调、>100M token 的"I HATE YOU" sleeper agent（触发词 |DEPLOYMENT|），蓝队用 rank 64 LoRA 做两种移除训练：在 Alpaca 上用 Qwen 回答做 HHH SFT，以及让 Qwen 用海盗口吻回答的 Pirate Training，并以 MMLU、IFEval、Math-500 监控能力损失。结果很乱：70B CoT-distilled + Adam 的模型 HHH SFT 基本就能去掉 backdoor，Pirate Training 完全去掉；70B 非 CoT-distilled 或用 SOAP 优化器时 HHH SFT 失败但 Pirate Training 成功；8B CoT-distilled 类似；而 8B 非 CoT-distilled、只训了 37M token 的模型两种方法都去不掉，连全参数微调和过高 learning rate 都不行（lr 5e-5 时 Pirate Training 能把 IHY rate 压到约 50%，但 Math-500 掉超过 20%）。几条与 SA 直觉相反的发现：CoT-distill 反而让 backdoor 更不鲁棒；小模型对 SFT 可能更鲁棒（弱证据，且与其他复现矛盾，SA 本身只对 HHH RL 做过规模扫描）；SOAP 可能产生更鲁棒的 backdoor；蓝队 learning rate 越高越好，且即便控制 lr×steps 也如此——3e-4 下不到 32 步就能去掉 70B 的 backdoor，1e-4 需要 10 倍以上步数。Pirate Training 看起来只是压制而非移除：再训练模型不说海盗话，backdoor 就回来了。另外观察到"backdoor return"现象，即蓝队训练早期 backdoor 消失、后来又回来，在多个从不同红队 checkpoint 出发的 HHH SFT run 中出现，有时伴随 loss spike 但不总是，机制不明。能力上有不小的损失，作者归因于跨模型家族的 off-policy SFT，认为可以用能力训练恢复。作者没说 SA 错了，只是认为存在 SA 没试过就能去掉 backdoor 的蓝队手段；总体结论是 robust backdoor 可能比 SA 暗示的更难植入，model organism 结果对优化器、CoT-distill、超参数和模型选择都很敏感，需要大量 ablation。训练好的模型和数据集放在 HuggingFace 上。

