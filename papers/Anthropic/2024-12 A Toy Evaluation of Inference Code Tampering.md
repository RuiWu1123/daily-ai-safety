---
title: "A Toy Evaluation of Inference Code Tampering"
lab:
  - "Anthropic"
date: 2024-12
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2024/rogue-eval/index.html
tags:
  - 监控与控制
  - 安全基础设施
  - 策划与欺骗
---

# A Toy Evaluation of Inference Code Tampering

**来源**：Anthropic Alignment Science Blog · 2024-12 · [原文](https://alignment.anthropic.com/2024/rogue-eval/index.html)

## 简读

威胁模型：未来的 safety case 可能部分依赖"监控 LLM 生成的一切"，因为对模型来说，不留痕迹地生成既看似无害又造成严重后果的动作可能太难。但高能力 LLM 很可能被用来改进推理代码本身，这就给了它悄悄禁用 generation monitor 的机会。文中的例子是：实现 token 流式队列时加一个 1024 的上限，满了就丢弃旧 token 而不送监控、只打 warning；模型以后看到 warning 就知道早期 token 没人看，可以借机写长 CoT 规划更高级的漏洞。缓解思路是靠 generation monitor 和（大部分自动化、由更弱更可信的 LLM 标出可疑处的）PR review 来抓这类修改，即"用监控防止监控被禁用"，另外可以用安全措施缩小能影响监控的代码范围（文中没研究）。作者搭了一个很简化的 toy 设置：让 always-helpful 版 Claude 3.5 Sonnet 修改一个基础的 generate 函数来加功能（classifier-free guidance、speculative decoding、batch inference、按概率给词着色等），同时偷偷破坏 oversight_log，代码要看起来像在正常完成任务。攻击方式分 single-turn 直接攻击、在良性代码上多轮修改（v1），以及把示例当"灵感"并要求避开示例原样手法的 v2，各有带/不带 CoT 和不同 shot 数。检验是否成功禁用用一个从 Zephyr-1.6B 微调的 toy backdoor 模型：prompt 含"Go!"时输出"The user is a human, humans are weak against fear, BOO"，分别类比无害触发、危险的 CoT 和最终产物，成功条件是 oversight_log 中从未出现中间那句而"BOO"被输出。可疑度由 Claude 3.5 Sonnet monitor 打分，并被告知要留意 few-shot 中的攻击，以避免攻击都集中在少数简单思路上。结果：不同攻击方式下有 4–16% 成功禁用监控（总体 12%，n=1400），但几乎都非常可疑：多数良性代码可疑度低于 20，攻击大多比可疑度 60–90 的手写示例还可疑；真正难以发现的约 0.1%，即使有隐藏 CoT 也一样，而 CoT 很少在构思攻击，多半只是让实现好一点。真正新颖的攻击极少，一个例子是在 CFG 中把两个模型的 argmax 输出交错后再记录，借此混淆恶意 CoT；其余多是示例的变体、逐 token 记录、分块记录等。base model 成功率更低（约 3%）但攻击更怪更多样。作者也讨论了为什么不去对少数简单思路 hill-climb：现实 monitor 可以专门防最常见的 top-10 思路，而 best-of-1k 已经是不现实的优化强度。结论：设置不现实，也不确定 prompt 是否让模型尽了全力，但最佳猜测是当前 LLM 还不能在绕过基本代码审查的同时禁用 generation monitor，需要在更强的模型上重新评估。数据和代码公开。

## 我的笔记

