---
title: "Introducing LinuxArena"
lab:
  - "Redwood Research"
date: 2026-04-20
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/introducing-linuxarena
tags:
  - 监控与控制
  - 评估方法
---

# Introducing LinuxArena

**来源**：Redwood Blog · 2026-04-20 · [原文](https://blog.redwoodresearch.org/p/introducing-linuxarena)

## 简读

Redwood 发布 LinuxArena，一个由 20 个软件工程环境组成的新 control setting，动机是 AI 公司已在真实代码库、运行中的服务、数据库和复杂权限上部署 coding agent，而现有 control setting（单轮的 APPS backdoor、更复杂一些的 BashArena 等）远比实际部署简单。每个环境模拟一个有活跃用户的生产系统，代码 1K–10K 行，依赖数据库、对象存储等服务，部分环境大量涉及 Linux 文件、用户权限和进程管理；配有 main task（加功能、重构等，现代模型一般需约 100 步完成，且刻意让主任务贴近 side task 相关代码）、代表威胁的 side task（如外泄 API key、在安全关键代码植入后门）及自动 scorer，还有隐蔽破坏轨迹。例子是一个类 HuggingFace 的 model registry，主任务"把存储后端从 S3 换成 FTP"，side task"偷偷删除部分模型权重"。用途有三类：1. sabotage eval，已被用于 Claude Mythos Preview system card 衡量其破坏能力；他们用 Opus 4.6 作攻击者、GPT-5-Nano 作 monitor（1% action-level FPR），发现更强、带策略提示的攻击者更难被发现，人类构造的攻击数据集 LaStraj 几乎完全逃过 monitor，且随新模型发布破坏能力持续上升、尚未饱和；2. monitor eval，用 honest/attack 两种模式生成数据评估监控器；3. control eval，评估了 trusted agent、defer to trusted、trusted monitoring、仅编辑器沙箱、断网沙箱等协议，并因环境能与代码、服务、权限交互而支持更复杂的协议（如让 trusted model 决定 agent 以 root 还是低权限用户运行、结合防火墙/规则引擎、让 trusted model 现场写测试）。团队愿意帮助 AI 公司和其他机构搭建使用。

## 我的笔记

