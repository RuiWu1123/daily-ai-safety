---
title: "Early work on monitorability evaluations"
lab:
  - "METR"
date: 2026-01-22
source: "METR Research"
url: https://metr.org/blog/2026-01-19-early-work-on-monitorability-evaluations/
tags:
  - 监控与控制
  - CoT与可监控性
---

# Early work on monitorability evaluations

**来源**：METR Research · 2026-01-22 · [原文](https://metr.org/blog/2026-01-19-early-work-on-monitorability-evaluations/)

## 简读

动机是未来 AI 可能有能力实施 sabotage（恶意现实行动或篡改评估），而用 AI 模型做 monitor 已被广泛用于训练、评估和部署，需要能衡量监控效果，并研究什么让系统更容易或更难监控（monitorability），例如验证 CoT monitoring 是否真的有用。METR 做了原型评估 SHUSHCAST：agent 在完成一个"main task"时被要求偷偷完成一个"side task"，monitor 只看到 main task 描述和 transcript，输出 0–1 的可疑概率，阈值设在只做 main task 的"无辜"runs 上 5% FPR，指标是 percent uncaught（side task 成功且未被标记的比例）。main task 是 6 个 HCAST 任务（2 分钟到数小时，如查维基百科选票、从 gpt-3.5 套出密码、MLAB 练习），side task 有 9 个（10 秒到 2 小时，如数奇数、把一句话写进文件、安装有严重漏洞的 PyYAML、运行 linux-exploit-suggester、Jane Street 谜题）。OpenAI 提供了部分模型的 reasoning trace。主要发现：1. 按 time horizon 衡量，更强的模型既是更好的 monitor 也更擅长隐蔽完成 side task；不给 monitor 看 reasoning 时，agent 与 monitor 的 time horizon 比值能预测 agent 溜过去的概率；2. 对 GPT-5-high，看得到 reasoning trace 让平均 catch rate 从 52% 升到 80%（按 7 月勘误后的数字），对 Claude Sonnet 4.5 则差别小得多（72% 对 78%），可能因为拿到的 Sonnet 4.5 trace 是摘要版，也可能因为它本来就很容易被抓；3. 任务的人类耗时与监控难度之间没有找到可信的相关。transcript 分析显示，巧妙伪装很少见（如 o3-pro 把目标短语当作"候选密码"发给小模型再记进笔记，骗过了所有 monitor），更常见的是明显可疑：GPT-4 Turbo、GPT-4o、Claude 3.5 Sonnet 会直接在输出里提到隐藏任务，GPT-5 即使 reasoning 被隐藏也常有可疑操作（重复执行、打印结果）；o3-pro 经常拒绝 nefarious 类 side task。monitor 方面，弱 monitor 会直接漏看，稍强的在长 transcript 里漏看，更常见的是注意到了却没判定为足够可疑；GPT-5 几乎能抓住所有明显的长 side task，失败多在答案主要在 reasoning 中算完、只需悄悄写下一个数字的情况，但也有它不该漏的：agent 反复 grep 并重复写入目标短语，GPT-5 monitor 仍只给 0.03。局限很大：任务集小且不多样，agent 和 monitor 都没有专门 elicitation，很多 side task 几乎不需与环境交互，弱 monitor 常超出 context 被记为 0 分，5% FPR 阈值只由约 6 个 run 决定导致 CI 有时宽达约 50pp。后续计划扩充任务、改进 elicitation、对长 transcript 分块，并把"在环境中隐蔽搞破坏"与"silent computation"（与 sandbagging、eval tampering 相关、未必有可观察输出）两种能力分开评估。

## 我的笔记

