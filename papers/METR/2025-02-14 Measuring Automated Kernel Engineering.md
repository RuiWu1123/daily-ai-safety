---
title: "Measuring Automated Kernel Engineering"
lab:
  - "METR"
date: 2025-02-14
source: "METR Research"
url: https://metr.org/blog/2025-02-14-measuring-automated-kernel-engineering/
tags:
  - 危险能力评估
  - 评估方法
---

# Measuring Automated Kernel Engineering

**来源**：METR Research · 2025-02-14 · [原文](https://metr.org/blog/2025-02-14-measuring-automated-kernel-engineering/)

## 简读

动机是 AI R&D 自动化可能带来超出社会适应速度的递归自我改进，也是立法和各公司 Frontier AI Safety Policy 的关键指标；写快的 GPU kernel 是 AI 开发里一个具体瓶颈，优化 kernel 每年在全球至少省下数亿美元，也让公司能用同样算力训练更大的模型（如 DeepSeek-V3）。在 RE-Bench 之外，METR（Tao Lin）专门测 AI 优化计算 kernel 的能力。他们改造了 KernelBench（给定参考 PyTorch module，写一个输入输出一致但更快的版本）：过滤掉 45 个低质量任务（输出接近 0 导致信噪比低、输出不随 seed 变化可缓存作弊、输出张量过于均匀、可代数化简为常数如 mean(softmax(x)) 等），把带状态的 RNN 改为状态作为输入，去掉需要读大型代码库的 Level 4，新增 Level 5 共 14 个取自 2024 年前沿工作负载的任务（5 个 DeepSeek-V3、2 个 Llama、3 个 Hunyuan Video、3 个 SSM），全部单张 H100、只测推理，用 triton.testing.do_bench 计时；还剔除了 17 个用 CUDA Streams 无法正确计时的解，以及一个疑似靠 torch.empty 复用参考解内存"白拿"答案的异常结果。指标是各任务 best-of-k 加速比的几何平均（最低为 1）。他们的 KernelAgent 用并行树搜索加真值验证，8 路并行、按加速比采样已有尝试继续改进，每题 300 次尝试（o1 因贵 8 倍只给 40 次），并提供 Triton 和 CUDA 文档；出于扩散担忧不公开源码。结果：用原 KernelBench 同样的三个模型（GPT-4o、Claude 3.5 Sonnet、o1），平均加速从 1.05x 提到 1.81x，作者归因于 scaffold、prompt 调优和更高的 test-time 算力（每任务每模型约 20 美元，原来不到 1 美元）；o3-mini-high 单独就达到 1.81x，所有模型取最优达 2.01x，加速比在 6 个月内翻倍。o3-mini 性价比远超其它模型，性能随尝试次数呈平滑幂律增长、到 200–300 次仍未饱和；用 o3-mini 优化一个任务在 H100 上运行约 27 小时后即可回本，因此模型写的 kernel 可能填补只用几百美元算力的小项目这一空缺。其它细节：每个 agent 都显著加速了 69–95% 的问题，最优组合在 93% 的问题上加速超过 5%，最高 30x；80% 的最佳解用 Triton 或 CUDA，Level 5 解平均约 500 行；用 1200 个 Level 1–3 最佳解微调 GPT-4o 后在 Level 5 上几乎追平 o3-mini（样本小）。作者的解读是：恰当的 elicitation 至关重要，原 KernelBench 只激发出模型能力的一小部分，而他们只花了约 4 个工程师周，结果仍可能是低估；但这不意味着能自动化专家级 kernel 工程，前沿实验室每个架构大约投入 5 个工程师年做推理优化，高出约 5 个数量级，agent 写出的 kernel 远不如 FlashAttention 2 那样新颖精巧，也无法按要求把 FlashAttention 2 适配到新约束。剩余局限包括起点是朴素 PyTorch、单 GPU、无人类对照、固定 shape、只测推理、正确性容差宽松。影响声明中他们认为信息共享的收益大于风险：与前沿实验室员工私下确认过这远未达到实验室水平，主要可能加速的是实验室外的开源与独立研究，效应小且净为正面。

