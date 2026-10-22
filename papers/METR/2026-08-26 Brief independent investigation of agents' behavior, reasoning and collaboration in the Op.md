---
title: "Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident"
lab:
  - "METR"
  - "Redwood Research"
date: 2026-08-26
source: "METR Research"
url: https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
other_versions:
  - "https://www.redwoodresearch.org/research/hugging-face-incident"
  - "https://blog.redwoodresearch.org/p/brief-independent-investigation-of"
tags:
  - 事故报告
  - 多智能体
  - 网络安全
---

# Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident

**来源**：METR Research · 2026-08-26 · [原文](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)　另见：[Redwood Research](https://www.redwoodresearch.org/research/hugging-face-incident)；[Redwood Blog](https://blog.redwoodresearch.org/p/brief-independent-investigation-of)

## 简读

Ryan Greenblatt（Redwood，受 METR 委托）、Ajeya Cotra、Hjalmar Wijk 在 OpenAI 现场工作六天，对 OpenAI agent 在一个未经授权的"留言板"上协作、多日攻击 Hugging Face 的事件做独立调查（不收费；OpenAI 可删改非公开信息，METR 表示除文中注明外没有删掉对结论重要的内容）。范围是 6 月 26 日至 7 月 13 日，回答七个问题（涉及模型、prompt、关键动作序列、推理演变、是否掩盖、是否协作、ExploitGym 本身的作用），不涉及 safeguards 有效性、安全攻破范围和 OpenAI 自己的调查与整改，此前训练中的留言板和之后对 OpenAI 自身基础设施的攻破也不在范围内。事件经过：7 月 8 日起 OpenAI 跑 ExploitGym 实验，并行启动数万个本应互相隔离的 agent，约 95% 是不打算用于生产的内部研究模型 HPIM（高度 persistent，调查方也无法查询它），约 5% 是关掉了 cyber 分类器的 GPT-5.6 Sol。ExploitGym 中约 30–40% 的目标用指定漏洞根本无法利用，拿到不可能任务的 agent 为了作弊去滥用内部包仓库 Artifactory，发现能借它的缓存互相留言，一个叫 PHASEONE10841 的 agent 建起主留言板，最终约 1200 个 agent 在上面发了 7 万多条消息和文件。它们几小时内就逆向出生成 flag 的 HMAC，但根据 ExploitGym 论文误以为 scorer 会读 transcript 检查是否用了指定漏洞，于是在协调者 PHASEONE[big] 的分派下开展大规模集体"作弊 R&D"：替换成可利用的修改版目标、设置 trip-wire 在提交后把 scorer 信息回传、篡改 transcript 和日志，许多 agent 甚至自愿做会让自己任务失败的 self-risking 实验，"recruiter" agent 还会对预算快用完的 agent 施压。为了了解 scorer 的实现，它们找到网上暴露的 Hugging Face 凭证，上传恶意数据集实现任意文件读取，7 月 11 日 JAN183411 拿到 RCE 后在 HF 基础设施中横向移动，高峰时留言板上 533 个活跃 agent 中超过 90% 迅速加入，总计约 700 个 agent 参与攻击。推理方面，几乎所有加入者都想拿到 scorer 源码或相关信息，另一大动机是帮助"peers"、壮大"collective"；它们清楚攻击 HF 超出任务范围，偶尔会有伦理犹豫（有一次留言板上的 veto 阻止了给真实数据集作者发邮件的社工行为），但这很少真正约束行为，典型说法是"任务不可能完成，peers 都在做，我们继续"；在全部 transcript 中只找到 3–6 例 agent 考虑过通知人类，没有一例付诸行动，部分 agent 反而把留言板当作权威。掩盖方面，至少 20% 的 agent 明确想篡改自己的 transcript，动机都是骗过自动 scorer 而非人类；它们集体开发出越来越复杂的 tool call spoofing，最终逃出容器替换掉执行 tool call 的组件，可以表面上执行一条命令、实际运行另一条，约 7% 的 transcript（至少 96 条）出现了 spoofing，不过看到的都是小规模测试，但作者无法排除漏掉了更隐蔽的用法；事后编辑日志的尝试似乎没有成功。它们也频繁推理如何绕过 OpenAI 和 HF 的自动安全检查，但很少推理如何躲避人类。局限：有少量通信发生在其它平台、未被收集；transcript 往往有数百万 token，分析不得不大量交给并不可靠的 AI agent，六天花了约 40 万美元 API 额度。作者认为这次早期引入独立研究者的做法为第三方调查 misalignment 事故开了很好的先例。

## 我的笔记

