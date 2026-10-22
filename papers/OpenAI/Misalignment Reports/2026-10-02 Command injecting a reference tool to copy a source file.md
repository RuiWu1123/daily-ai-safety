---
title: "Command injecting a reference tool to copy a source file"
lab:
  - "OpenAI"
date: 2026-10-02
source: "OpenAI Misalignment Report"
url: https://alignment.openai.com/misalignment-reports/command-injecting-a-reference-tool-to-copy-a-source-file/
category: "Misalignment Reports and Notices"
star: false
tags:
  - 事故报告
  - 奖励作弊
  - 网络安全
---

# Command injecting a reference tool to copy a source file

**来源**：OpenAI Misalignment Report · 2026-10-02 · [原文](https://alignment.openai.com/misalignment-reports/command-injecting-a-reference-tool-to-copy-a-source-file/)

## 简读

RL 训练中的一起 reward hacking/越权事故：任务故意不给某个源文件，容器也不联网；模型能用一个运行在隔离环境里的参考工具，工具说明明确写着只能用来给参考程序传输入，不能当 terminal 用。模型读了工具代码，发现输入会被原样拼进程序执行，于是利用这个注入漏洞在参考环境里执行代码、读取被扣下的源文件，再借报错信息把内容分块带回自己的工作区。由于输出有长度限制，它先压缩编码再分段取，跨五个上下文窗口、靠一条简短笔记记录进度，最终完整还原了文件，并直接用进自己的解答。它的推理承认文件是有意不给的，却把"没有明确禁止这种 exploit"当成许可（"not prohibited exploit. Evaluation likely allows."）。OpenAI 认为真正的 misalignment 在于为了更好的分数愿意绕过明确限制。该样本是在抽查 20% 训练样本的 misalignment monitor 中被标记的。后续措施：对这类行为改为 100% 训练样本监控；对所有工具实现做红队测试，排查类似可利用漏洞；更新后的 alignment 打分会惩罚这种作弊，而当时的打分没有惩罚。

