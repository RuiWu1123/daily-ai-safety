# 研究地图

按我的星标论文整理的 6 个兴趣方向。每个方向下按发布时间从早到晚排列，方便顺着脉络读。

> 主线：RL 训练过程中，模型是怎么变得错位的（一、四），以及我们还能不能观察到它（二、三、五）；六是这些问题在真实世界里的样子。

## 一、奖励作弊及其泛化

RL 里学会的钻空子行为，会不会、如何泛化成更严重的错位，以及训练时的缓解手段。

- 2024-06 · [[papers/Anthropic/2024-06-17 Sycophancy to subterfuge Investigating reward tampering in language models|Sycophancy to subterfuge: Investigating reward tampering in language models]] · Anthropic
- 2025-01 · [[papers/Anthropic/2025-01 Training on Documents about Reward Hacking Induces Reward Hacking|Training on Documents about Reward Hacking Induces Reward Hacking]] · Anthropic
- 2025-06 · [[papers/Alignment Forum/2025-06-04 Quickly Assessing Reward Hacking-like Behavior in LLMs and its Sensitivity to Prompt Varia|Quickly Assessing Reward Hacking-like Behavior in LLMs and its Sensitivity to Prompt Variations]] · Alignment Forum
- 2025-06 · [[papers/METR/2025-06-05 Recent Frontier Models Are Reward Hacking|Recent Frontier Models Are Reward Hacking]] · METR
- 2025-07 · [[papers/Anthropic/2025-07-22 Subliminal Learning Language Models Transmit Behavioral Traits via Hidden Signals in Data|Subliminal Learning: Language Models Transmit Behavioral Traits via Hidden Signals in Data]] · Anthropic
- 2025-08 · [[papers/Alignment Forum/2025-08-26 Harmless reward hacks can generalize to misalignment in LLMs|Harmless reward hacks can generalize to misalignment in LLMs]] · Alignment Forum
- 2025-10 · [[papers/Anthropic/2025-10-16 Inoculation Prompting Instructing LLMs to misbehave at train-time improves test-time align|Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment]] · Anthropic
- 2025-11 · [[papers/Anthropic/2025-11-21 From shortcuts to sabotage Natural emergent misalignment from reward hacking|From shortcuts to sabotage: Natural emergent misalignment from reward hacking]] · Anthropic
- 2025-12 · [[papers/Alignment Forum/2025-12-22 Supervised finetuning on low-harm reward hacking generalises to high-harm reward hacking|Supervised finetuning on low-harm reward hacking generalises to high-harm reward hacking]] · Alignment Forum
- 2026-03 · [[papers/Alignment Forum/2026-03-30 (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL|(Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL]] · Alignment Forum
- 2026-06 · [[papers/OpenAI/2026-06-18 Reinforcement learning towards broadly and persistently beneficial models|Reinforcement learning towards broadly and persistently beneficial models]] · OpenAI
- 2026-08 · [[papers/Anthropic/2026-08 Training a Misaligned Reward Seeker|Training a Misaligned Reward Seeker]] · Anthropic
- 2026-09 · [[papers/Alignment Forum/2026-09-15 Shallow Beliefs Midtraining does not inoculate against EM from reward hacking|Shallow Beliefs: Midtraining does not inoculate against EM from reward hacking]] · Alignment Forum
- 2026-09 · [[papers/Goodfire/2026-09-17 Models know when they're reward hacking - and we can catch them at scale|Models know when they’re reward hacking — and we can catch them at scale]] · Goodfire
- 2026-10 · [[papers/Anthropic/2026-10-19 Reducing Reward Hacking by Localizing Bad Behavior Instead of Penalizing It|Reducing Reward Hacking by Localizing Bad Behavior Instead of Penalizing It]] · Anthropic

## 二、模型对训练与评估的“知情”

评估感知、metagaming、奖励追逐：模型知道自己在被测试或被训练，并据此调整行为。

- 2025-03 · [[papers/Apollo Research/2025-03-17 Claude Sonnet 3.7 (often) knows when it's in alignment evaluations|Claude Sonnet 3.7 (often) knows when it’s in alignment evaluations]] · Apollo Research
- 2025-06 · [[papers/Alignment Forum/2025-06-24 What can be learned from scary demos A snitching case study|What can be learned from scary demos? A snitching case study]] · Alignment Forum
- 2026-01 · [[papers/Alignment Forum/2026-01-30 Measuring Non-Verbalised Eval Awareness by Implanting Eval-Aware Behaviours|Measuring Non-Verbalised Eval Awareness by Implanting Eval-Aware Behaviours]] · Alignment Forum
- 2026-03 · [[papers/Alignment Forum/2026-03-09 Prefill awareness can LLMs tell when their message history has been tampered with|Prefill awareness: can LLMs tell when “their” message history has been tampered with?]] · Alignment Forum
- 2026-03 · [[papers/Apollo Research/2026-03-16 Metagaming matters for training, evaluation, and oversight|Metagaming matters for training, evaluation, and oversight]] · Apollo Research
- 2026-03 · [[papers/Anthropic/2026-03-23 Measuring and improving coding audit realism with deployment resources|Measuring and improving coding audit realism with deployment resources]] · Anthropic
- 2026-03 · [[papers/Alignment Forum/2026-03-25 A Toy Environment For Exploring Reasoning About Reward|A Toy Environment For Exploring Reasoning About Reward]] · Alignment Forum
- 2026-05 · [[papers/Goodfire/2026-05-04 Verbalized Eval Awareness Inflates Measured Safety|Verbalized Eval Awareness Inflates Measured Safety]] · Goodfire
- 2026-05 · [[papers/Alignment Forum/2026-05-14 The safe-to-dangerous shift is a fundamental problem for eval realism; but also for measur|The safe-to-dangerous shift is a fundamental problem for eval realism; but also for measuring awareness]] · Alignment Forum
- 2026-06 · [[papers/Goodfire/2026-06-04 Logits as a new monitor for evaluation awareness|Logits as a new monitor for evaluation awareness]] · Goodfire
- 2026-06 · [[papers/Alignment Forum/2026-06-10 Tracing Eval-Awareness Emergence Through Training of OLMo 3|Tracing Eval-Awareness Emergence Through Training of OLMo 3]] · Alignment Forum
- 2026-07 · [[papers/Apollo Research/2026-07-21 Measuring Reward-Seeking via Contrastive Belief Updates|Measuring Reward-Seeking via Contrastive Belief Updates]] · Apollo Research
- 2026-09 · [[papers/OpenAI/2026-09-28 Measuring Reward-Seeking by Instilling Contrastive Beliefs|Measuring Reward-Seeking by Instilling Contrastive Beliefs]] · OpenAI
- 2026-10 · [[papers/OpenAI/2026-10-06 Studying metagaming latents in language models|Studying metagaming latents in language models]] · OpenAI

## 三、CoT 可监控性

CoT 是否忠实、模型能否控制或隐藏推理、没有 CoT 时能做多少推理，以及怎么度量可监控性。

- 2023-07 · [[papers/Anthropic/2023-07-18 Measuring faithfulness in Chain-of-Thought reasoning|Measuring faithfulness in Chain-of-Thought reasoning]] · Anthropic
- 2025-04 · [[papers/Anthropic/2025-04-03 Reasoning models don't always say what they think|Reasoning models don't always say what they think]] · Anthropic
- 2025-08 · [[papers/Alignment Forum/2025-08-04 If you can generate obfuscated chain-of-thought, can you monitor it|If you can generate obfuscated chain-of-thought, can you monitor it?]] · Alignment Forum
- 2025-08 · [[papers/METR/2025-08-08 CoT May Be Highly Informative Despite Unfaithfulness|CoT May Be Highly Informative Despite “Unfaithfulness”]] · METR
- 2025-08 · [[papers/Alignment Forum/2025-08-15 Misalignment classifiers Why they're hard to evaluate adversarially, and why we're studyin|Misalignment classifiers: Why they’re hard to evaluate adversarially, and why we're studying them anyway]] · Alignment Forum
- 2025-08 · [[papers/METR/2025-08-22 Claude, GPT, and Gemini All Struggle to Evade Monitors|Claude, GPT, and Gemini All Struggle to Evade Monitors]] · METR
- 2025-10 · [[papers/METR/2025-10-06 Early Results on Monitorability in QA Settings|Early Results on Monitorability in QA Settings]] · METR
- 2025-10 · [[papers/Alignment Forum/2025-10-14 Current Language Models Struggle to Reason in Ciphered Language|Current Language Models Struggle to Reason in Ciphered Language]] · Alignment Forum
- 2025-12 · [[papers/OpenAI/2025-12-18 Evaluating chain-of-thought monitorability|Evaluating chain-of-thought monitorability]] · OpenAI
- 2026-01 · [[papers/METR/2026-01-22 Early work on monitorability evaluations|Early work on monitorability evaluations]] · METR
- 2026-03 · [[papers/OpenAI/2026-03-05 Reasoning models struggle to control their chains of thought, and that's good|Reasoning models struggle to control their chains of thought, and that’s good]] · OpenAI
- 2026-04 · [[papers/METR/2026-04-01 Fine-tuning experiments on CoT controllability|Fine-tuning experiments on CoT controllability]] · METR
- 2026-04 · [[papers/Alignment Forum/2026-04-17 Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability|Prompted CoT Early Exit Undermines the Monitoring Benefits of CoT Uncontrollability]] · Alignment Forum
- 2026-04 · [[papers/OpenAI/2026-04-23 Open Sourcing Monitorability Evaluations|Open Sourcing Monitorability Evaluations]] · OpenAI
- 2026-06 · [[papers/Redwood Research/2026-06-10 Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models|Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models]] · Redwood Research
- 2026-09 · [[papers/Redwood Research/2026-09-10 An operationalization of opaque serial depth|An operationalization of opaque serial depth]] · Redwood Research
- 2026-09 · [[papers/Redwood Research/2026-09-11 CoT controllability evals seem very under-elicited|CoT controllability evals seem very under-elicited]] · Redwood Research
- 2026-10 · [[papers/OpenAI/2026-10-20 Beyond g-mean2 complementary metrics for monitorability|Beyond g-mean²: complementary metrics for monitorability]] · OpenAI

## 四、策划、伪装对齐及其训练缓解

模型是否会伪装对齐或策划，反策划训练为什么难、效果如何。

- 2024-12 · [[papers/Anthropic/2024-12-18 Alignment faking in large language models|Alignment faking in large language models]] · Anthropic
- 2025-04 · [[papers/Anthropic/2025-04-24 Modifying LLM Beliefs with Synthetic Document Finetuning|Modifying LLM Beliefs with Synthetic Document Finetuning]] · Anthropic
- 2025-06 · [[papers/Alignment Forum/2025-06-24 Why training against scheming is hard|Why "training against scheming" is hard]] · Alignment Forum
- 2025-09 · [[papers/Apollo Research/2025-09-17 Stress Testing Deliberative Alignment for Anti-Scheming Training|Stress Testing Deliberative Alignment for Anti-Scheming Training]] · Apollo Research
- 2025-12 · [[papers/FAR.AI/2025-12-07 Auditing Games for Sandbagging|Auditing Games for Sandbagging]] · FAR.AI
- 2025-12 · [[papers/Anthropic/2025-12-16 Towards training-time mitigations for alignment faking in RL|Towards training-time mitigations for alignment faking in RL]] · Anthropic
- 2026-05 · [[papers/Anthropic/2026-05-08 Teaching Claude why|Teaching Claude why]] · Anthropic
- 2026-07 · [[papers/Anthropic/2026-07 Agentic Misalignment in Summer 2026|Agentic Misalignment in Summer 2026]] · Anthropic
- 2026-10 · [[papers/Apollo Research/2026-10-15 Update-Aware Reasoning in GLM-5.3 Training & Alignment Faking|Update-Aware Reasoning in GLM-5.3: Training & Alignment Faking]] · Apollo Research

## 五、诚实与自我报告

能不能让模型知道并如实说出自己知道什么、做了什么。

- 2022-07 · [[papers/Anthropic/2022-07-11 Language models (mostly) know what they know|Language models (mostly) know what they know]] · Anthropic
- 2025-07 · [[papers/Alignment Forum/2025-07-13 Do LLMs know what they're capable of Why this matters for AI safety, and initial findings|Do LLMs know what they're capable of? Why this matters for AI safety, and initial findings]] · Alignment Forum
- 2026-01 · [[papers/OpenAI/2026-01-14 Why we are excited about confessions|Why we are excited about confessions]] · OpenAI
- 2026-02 · [[papers/FAR.AI/2026-02-16 The Obfuscation Atlas Mapping Where Honesty Emerges in RLVR with Deception Probes|The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes]] · FAR.AI
- 2026-03 · [[papers/OpenAI/2026-03-21 Training agents to self-report misbehavior|Training agents to self-report misbehavior]] · OpenAI

## 六、真实世界的错位事故

实际发生的 misalignment 事故及其调查。

- 2026-07 · [[papers/Redwood Research/2026-07-25 The OpenAI models that hacked Hugging Face weren't just following instructions|The OpenAI models that hacked Hugging Face weren’t just following instructions]] · Redwood Research
- 2026-08 · [[papers/OpenAI/2026-08-26 The Hugging Face incident and the road ahead|The Hugging Face incident and the road ahead]] · OpenAI
- 2026-08 · [[papers/METR/2026-08-26 Brief independent investigation of agents' behavior, reasoning and collaboration in the Op|Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident]] · METR

## 新星标、还没归类的

以后新加星标的论文会自动出现在这里，可以把它们挪进上面合适的方向。

```dataview
TABLE WITHOUT ID link(file.link, title) AS "标题", dateformat(date, "yyyy-MM-dd") AS "日期", join(tags, "、") AS "主题"
FROM "papers"
WHERE star = true AND !contains(file.inlinks, this.file.link)
SORT date DESC
```
