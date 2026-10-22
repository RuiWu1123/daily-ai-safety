---
title: "Logit ROCs: Monitor TPR is linear in FPR in logit space"
lab:
  - "Redwood Research"
date: 2026-04-12
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/logit-rocs-monitor-tpr-is-linear
tags:
  - 监控与控制
  - 评估方法
---

# Logit ROCs: Monitor TPR is linear in FPR in logit space

**来源**：Redwood Blog · 2026-04-12 · [原文](https://blog.redwoodresearch.org/p/logit-rocs-monitor-tpr-is-linear)

## 简读

背景是 AI control 中的 trusted monitoring：弱的可信模型给强的不可信 agent 每步动作打可疑分，最可疑的交给人工审计，权衡的是 TPR（整条攻击轨迹至少一步超阈值）与 FPR（benign 单步被标记的比例）。现实审计预算很低（如 1e-4），而在这种 FPR 下估 TPR 需要海量 benign 样本。文章提出经验规律：低 FPR 区 logit(TPR) 与 logit(FPR) 呈线性，等价于把分数单调变换使 benign 成为标准 logistic 后，attack 分数也服从 logistic。设置在 BashArena：Claude Sonnet 4.5 做系统管理主任务的 benign 轨迹，以及 4 种恶意 side task（sudo 提权、下载恶意软件、外泄等）各 400 条攻击轨迹；用 gpt-5-nano、gpt-oss、qwen3-30b、glm-4.7-flash 等"刚好不饱和"的弱模型做 monitor，约 168k benign 样本。发现：1. 几乎所有 monitor×attack 组合都呈现这种线性；2. 较弱 monitor（尤其 qwen3-30b）会完全漏看一部分攻击，需要加 null 成分，用 μ、σ、p_null 三参数描述；3. benign 尾部稀疏时（如 20k 样本估 FPR=1e-4，阈值只由 2 个样本决定）logistic 拟合的误差低于直接经验估计，样本充足时朴素方法更好；4. 可以用一个点（如 FPR=1e-3 的 TPR）加斜率紧凑地比较 monitor。Gaussian 拟合 log loss 略高，直接 OLS 预测力稍弱。在更真实但数据少得多的 LinuxArena 上规律大致成立但不够干净。局限：只在固定攻击模型、任务、monitor 和 prompt 时成立，人机合作手工构造的攻击集是多峰的、明显不线性；强 monitor 因饱和没测。开放问题是更强的模型会不会产生比 logistic 更肥的尾部，即更多极其隐蔽的攻击。

## 我的笔记

