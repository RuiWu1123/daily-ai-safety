---
title: "VLM-RM: Specifying Rewards with Natural Language"
lab:
  - "FAR.AI"
date: 2023-10-18
source: "FAR.AI Blog"
url: https://www.far.ai/blog/vlm-rm-specifying-rewards-with-natural-language
other_versions:
  - "https://www.far.ai/research/vision-language-models-are-zero-shot-reward-models-for-reinforcement-learning"
star: false
tags:
  - 对齐训练方法
---

# VLM-RM: Specifying Rewards with Natural Language

**来源**：FAR.AI Blog · 2023-10-18 · [原文](https://www.far.ai/blog/vlm-rm-specifying-rewards-with-natural-language)　另见：[Paper](https://www.far.ai/research/vision-language-models-are-zero-shot-reward-models-for-reinforcement-learning)

## 简读

RL 要么需要手写 reward（难定义），要么需要大量人类反馈（贵）。这篇介绍论文 Vision-Language Models are Zero-Shot Reward Models for RL：直接拿 CLIP 当 reward model，只给一句 prompt，比如 "a humanoid robot kneeling"，reward 就是当前帧图像 embedding 和文本 embedding 的 cosine similarity。可选的 goal-baseline regularization 再给一个描述环境整体的 baseline prompt（如 "a humanoid"），把观测 embedding 投影到 baseline 和 goal 连成的直线上，用 α 控制投影程度，让 reward 更平滑；之后用 DQN、SAC 训练。结果：CartPole 不需要任何正则；MountainCar 的最大值位置是对的，但 reward 形状差，加正则、把环境渲染成更真实的纹理都有帮助。主实验是 MuJoCo humanoid，单句 prompt、不做 prompt engineering，学会了跪下、莲花坐、劈叉、举臂站立，但单腿站、叉腰、抱臂没学好，作者归因于所用 CLIP 的能力不够。更大的 CLIP 明显是更好的 reward model，只有最大的那个能教会跪下。由于没有 ground-truth reward，评估靠人工：一是给一批状态打标签，算 reward model 与人类标签的 EPIC distance 作代理指标；二是人工判断最终 policy 的成功率，并公开了视频。作者的定位是：不主张单靠这种方案去对齐强 AI，而是把 VLM-RM 当作“用预训练模型监督其它模型”（如 Constitutional AI）在视觉 RL 中的 toy model。意外的是几乎没观察到 reward hacking：小 CLIP 上有疑似行为，换大 CLIP 后就消失了。他们认为关键的开放问题是 VLM-RM 在更强优化压力下是否鲁棒，以及监督模型大小和 agent 优化能力如何共同决定 hacking；如果能造出失配的例子，也可以拿来当 misalignment 的 model organism。

