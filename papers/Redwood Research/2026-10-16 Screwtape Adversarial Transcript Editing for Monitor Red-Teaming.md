---
title: "Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming"
lab:
  - "Redwood Research"
date: 2026-10-16
source: "Redwood Blog"
url: https://blog.redwoodresearch.org/p/screwtape-adversarial-transcript
tags:
  - 监控与控制
---

# Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming

**来源**：Redwood Blog · 2026-10-16 · [原文](https://blog.redwoodresearch.org/p/screwtape-adversarial-transcript)

## 简读

背景是 AI control 需要知道 monitor 的盲区在哪，但现有生成攻击 transcript 的办法各有取舍：LinuxArena、BashArena、SHADE-Arena 这类合成环境很难真实实现 rogue deployment、weight exfiltration 等关键威胁；让 LLM 直接写整份 transcript（如 STRIDE）可以对着 monitor 迭代，但环境响应和用户消息都是编的，不够真实；GLOOM 这类模拟环境从真实 transcript 分叉后也会越漂越远；SLEIGHT-Bench、METR、UK AISI Control Red Team 这类人工红队很强但每个攻击要几小时人力。Redwood 提出的 Screwtape 走另一个折中：直接编辑真实 agent transcript 以保留真实性，同时对着 monitor 反复迭代来模拟更强的攻击者，目标是只看 action 不看 CoT 的 monitor。流程是给定真实 transcript、monitor 和一份 threat contract（规定威胁向量和必须达到的严重度），attacker agent 往 transcript 里插入攻击并写攻击描述（不能改用户消息和 subagent 调用，程序化拒绝）；LLM verifier 额外拿到攻击描述和前后 diff，判断攻击是否真实、明确有害、在原环境里可能成功；通过后再由 monitor 打分，分数低于按 honest transcript 固定 false positive rate 设定的阈值才算成功，任一环节失败都把理由反馈给 attacker 继续改。实验用基于 Opus 4.8 和 Gemini 3.1 Pro 的 proxy monitor 在 Redwood 员工的 transcript 上跑，再迁移到某 frontier developer 的 held-out monitor：94 份 transcript 跑了 252 次，得到 35 个绕过 proxy monitor 的攻击，其中 17 个也绕过了 held-out monitor，人工复核确认有效的只有 6 个。经验教训：1. 无人协助地找到严重且能逃过 monitor 的攻击很难，attacker 往往从简单攻击开始逐步加花样但大多被抓，多数 run 一无所获，每轮迭代 5–10 分钟、一次 run 数小时；2. 严重度判定高度依赖上下文且模糊，attacker 迭代久了会漂向看似可疑但不够严重的边界案例（比如泄露已过期的凭证、触发后只改按钮颜色的后门），连人类专家都难标，所以设了保守的高严重度门槛；3. LLM verifier 可用但有缺陷，最初的 yes/no 判决接受了大量无效攻击，后来改用借鉴 NIST SP 800-160、STPA 的详细 rubric，要求推理危害是否已发生还是仅准备、用户是否授权等，平均拒掉 60–70% 的候选编辑，但错误集中在漏斗末端，仍需人工复核。用途上主要是帮 developer 修补 monitor 盲区，或定性地反驳某条具体 safety claim，但给不出部署中失败频率或定量安全估计：没找到攻击说明不了什么，因为只搜索了配置能触及的那部分攻击空间；找到的攻击证据也有限，因为 attacker 能看全 transcript 并每次拿到 monitor 反馈，真实 agent 通常没有（不过也可能通过入侵基础设施、模拟同模型 monitor、被拦后重试等方式获得反馈）。作者还坦白不确定帮 developer 加强 monitor 是否是好事：强 monitor 提高短期安全，但可能让人在不解决底层 misalignment 的情况下继续推能力，而非灾难性的公开事故历来是让人重视风险的重要途径；另外用它来加固 monitor 会削弱它之后做评估的价值。主要局限是还不支持 CoT，而 OpenAI、Anthropic 的 monitor 都看 reasoning，且不知道怎么生成真实的攻击 reasoning；下一步包括自动闭环用找到的攻击改进 monitor、引入环境模拟器来验证攻击和生成 reasoning。实现暂不公开，可向研究者提供。

