---
title: "imitation: Clean Imitation Learning Implementations"
lab:
  - "FAR.AI"
date: 2022-09-21
source: "FAR.AI Publications"
url: https://www.far.ai/research/imitation-clean-imitation-learning-implementations
tags:
  - 对齐训练方法
---

# imitation: Clean Imitation Learning Implementations

**来源**：FAR.AI Publications · 2022-09-21 · [原文](https://www.far.ai/research/imitation-clean-imitation-learning-implementations)

## 简读

这是 imitation 库的软件论文（UC Berkeley CHAI 与 FAR AI，Gleave 等人）。动机是很多真实任务写不出 reward function，只能从人类反馈中学 reward 或直接学 policy，而已有的 imitation / reward learning 实现大多只支持一两个算法、多年无人维护、基于 TF1 等过时框架；又因为实现细节会显著影响性能，弱 baseline 容易导致虚假的正面结果。imitation 基于 PyTorch 和 Stable Baselines3，实现了七个算法：IRL 方面有 MCE IRL、基于密度估计的 baseline 和 AIRL，imitation learning 方面有 BC、DAgger 和 GAIL，外加从轨迹片段比较中学 reward 的 DRLHP（preference comparison）。设计上强调统一接口（共同基类）、模块化（可换任意 SB3 RL 算法、网络结构、优化器，GAIL 和 AIRL 都只是 AdversarialTrainer 换判别器）、用 Sacred 管理配置的训练评估脚本、98% 测试覆盖率加 pytype/mypy 静态检查，文档里还提醒避开 variable-horizon 环境这类混淆评估的坑。在 seals 版 MuJoCo 环境上做了 benchmark，多数算法接近 expert 水平，例外是 AIRL 在 Ant、Walker 上和 DAgger 在 Hopper 上表现差，其中 AIRL 在 Ant 上接近随机，作者归因于原论文用的是定制版 Ant。与 OpenAI Baselines、Stable Baselines2、Intel COACH、APReL 及原始论文代码对比，在算法数量、活跃度和代码质量上都不逊色；Stable Baselines3 已直接放弃自带 imitation 算法，转而使用这个库。

