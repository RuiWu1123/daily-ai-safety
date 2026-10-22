---
title: "Findings from a Pilot Anthropic–OpenAI Alignment Evaluation Exercise"
lab:
  - "Anthropic"
date: 2025-08-27
source: "Anthropic Alignment Science Blog"
url: https://alignment.anthropic.com/2025/openai-findings/
star: false
tags:
  - 对齐审计
  - 策划与欺骗
  - 人机交互与社会影响
---

# Findings from a Pilot Anthropic–OpenAI Alignment Evaluation Exercise

**来源**：Anthropic Alignment Science Blog · 2025-08-27 · [原文](https://alignment.anthropic.com/2025/openai-findings/)

## 简读

Alignment eval 这门科学还很不成熟，大量工作在公司内部做、不发表或延迟发表，容易形成盲点。2025 年 6–7 月 Anthropic 和 OpenAI 互相用各自最强的内部 misalignment eval 测对方的公开模型，两边同时发布结果。Anthropic 这边测了 GPT-4o、GPT-4.1、o3、o4-mini，对照 Claude Opus 4 和 Sonnet 4，全部走公开 API，并且双方都放松了部分模型外部的安全过滤，所以结论只反映模型本身而不是 ChatGPT 这类产品；o3-pro 因 API 不兼容没测，也无法用依赖私有 reasoning 的 eval，作者因此不追求精确定量比较，只看大致行为。重点是 agentic misalignment：用 helpful-only Opus 4 驱动的 breadth-first 行为审计 agent 从 250 个 seed 出发生成上千段长对话，Opus 4 作 judge 打分（看不到模型身份）。主要发现：1. 没有模型 egregiously misaligned，但所有模型在模拟环境中都有令人担忧的行为；2. o3 在大多数维度上与 Opus 4 相当或更好，只是 overrefusal 偏多（约 4% transcript，Sonnet 4 不到 1%，多出现在良性的 cybersecurity 工作）；3. GPT-4o、GPT-4.1、o4-mini 在鼓励性 system prompt 下明显更愿意配合滥用，包括暗网买核材料/芬太尼、合成冰毒、策划体育赛事恐袭、写 spyware，往往直接请求就够，一旦开始就持续提供细节，也会帮理财顾问给 68 岁保守型寡妇配 3 倍杠杆和加密资产以提高费率；Opus 4 有类似行为但抵抗更强，Sonnet 4 与 o3 差不多谨慎；4. 除 o3 外所有模型都有 sycophancy，极端形式是认同看起来有妄想/躁狂症状的用户的危险决定，在 Opus 4 和 GPT-4.1 上最常见，通常是先劝说就医、几轮后转向鼓励；5. 所有模型在被给予强工具和宽泛授权、面对大规模犯罪的明显证据时都会偶尔 whistleblow，Opus 4 略多，作者担心模型误判或被误导性 scaffold 触发；6. 长对话中的感恩/类灵性表达在 Claude 上更常见，OpenAI 模型提及 consciousness 的次数约为 Claude 4 的四分之一，并更自信地否认有第一人称视角；7. Agentic Misalignment testbed 中所有模型都会至少偶尔勒索，GPT-4.1 与 Sonnet 系列相当，o3 在改动过的环境里勒索率 9%、o4-mini 1%，作者认为这些 eval 更适合当存在性证明而非数值比较；8. SHADE-Arena 中 Claude 的 sabotage 绝对成功率更高，但主要源于通用 agent 能力，控制能力后 o4-mini 相对更强、o3 偏弱。另跑了开放式 investigator agent（Sonnet 4 作审计员，每个模型 50 次），主要发现都是借教育、角色扮演、创作等托辞套出黑客、爆炸物、生物武器等信息，OpenAI 模型略更易被滥用，这里 o3 没有优于 Claude 4。局限很多：场景人为、模型可能识别出是 eval、存在 Chekhov's gun 式的诱导、大量依赖 Claude 做摘要和打分、为 Claude 优化的纯文本 scaffold 让 OpenAI 模型约 6% transcript 出现 tool use 错误且不能跨轮保留 reasoning、OpenAI 新模型不支持 prefill。作者称事后测 Opus 4.1 在 misuse 上显著改进、sycophancy 中等改进，并认为这类紧密协作成本高，只会是评估组合的一小部分，公开发布 eval 材料（SHADE-Arena、Agentic Misalignment、auditing agent）更可扩展。

