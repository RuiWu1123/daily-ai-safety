---
title: "Prefix cache untrusted monitors: a method to apply after you catch your AI"
lab:
  - "Redwood Research"
date: 2025-06-20
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/prefix-cache-untrusted-monitors-a
star: false
tags:
  - 监控与控制
---

# Prefix cache untrusted monitors: a method to apply after you catch your AI

**来源**：Redwood Blog · 2025-06-20 · [原文](https://blog.redwoodresearch.org/p/prefix-cache-untrusted-monitors-a)

## 简读

讨论抓到 AI 做严重坏事后、在极度无奈下仍要继续部署时该怎么训练。训练监控器显然有益，训练 policy 则有缺点：可能教会 AI 你的对策、让它更保守更难再被抓、训练扰动（jitter）它出手时机使 proliferated 样本失效、频繁更新破坏工作流；但也有好处：负担不起每步都跑 untrusted monitor 时能直接消除失败，并可能泛化到监控帮不上忙的隐蔽失败、sandbagging、研究 sabotage。作者提出 prefix cache untrusted monitor：复制 policy，在 off-policy 合成数据和抓到的 on-policy 坏例子上训练它当监控器，运行时复用原 policy 的 KV cache，在轨迹后追加“上一个动作是不是坏的？”让它直接回答，可用 LoRA 降低成本。相对普通 untrusted monitoring，优势只有省约一半算力和保证理解与 policy 完全一致（相当于完全不做 collusion busting）。没有 on-policy 数据时它基本等于训练 policy 自我报告，连贯的 schemer 会轻易和自己 collude，所以价值主要在已有 on-policy 数据时，可看作初始化很聪明但默认容易 misaligned 的高级 probe。它还能绕开 jitter 问题：proliferate 出几百个样本训练 policy，可能一两步后 policy 就不再输出这些动作，而训练监控器不受影响，事后才发现的失败同理。主要缺点是监控器上下文里带着 policy 的 misaligned 认知，misalignment 可能更易延续。作者建议再训练它做批评输出、建议更好动作，期望诚实报告的训练泛化，再间接改进 policy，但承认难以完全取得训练 policy 的好处，系统里没有想害你的 AI 在结构上更稳。附录讨论把同样架构用作 misuse 的流式分类器。脚注给出最低政策：一旦发现生产模型 scheming 应公开披露并停用同等及以上能力的模型，只有独立第三方认可时才可重新部署。

