---
title: "\"Did you lie?\": Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms"
lab:
  - "UK AISI"
date: 2026-06-17
source: "AISI Research"
url: https://www.aisi.gov.uk/research/did-you-lie-evaluating-lie-detectors-across-model-scale-and-belief-verified-model-organisms
tags:
  - 诚实与谎言检测
  - 可解释性
---

# "Did you lie?": Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms

**来源**：AISI Research · 2026-06-17 · [原文](https://www.aisi.gov.uk/research/did-you-lie-evaluating-lie-detectors-across-model-scale-and-belief-verified-model-organisms)

## 简读

可靠的 lie detector 可以用于审计、监控和事后调查，但评估它们需要模型“确实相信与所说相反的东西”的测试床。AISI 的 Cooney、Africa、Irving 指出现有工作有两个缺口：证据大多来自 Llama 3.3 70B 及更弱的模型，而且训练出来的 model organism 可能根本不是在撒谎，只是学会了输入输出映射或真的改信了。他们调查七个现有开源 organism 家族，发现内化信念的证据有限，Llama 3.3 70B 的内省能力也很弱；顺带复现 Apollo（Goldowsky-Dill et al.）的 probe 时发现阈值校准代码有问题，修正后 1% FPR 下的 TPR 从 ≥96% 降到 73.2%。论文区分两种期望：weak hope 是 lie detector 作为审计工具箱的一员，检测到与撒谎相关的东西就有用；strong hope 是能支撑“模型 M 以 ≥95% 概率不相信自己有目标 G”这类高置信信念判断，这在 safety case 中是承重的。为评估后者，他们构建了两类测试床：1. Varied Deception，基于校验过的 TriviaQA，用 64 个诚实诱导和 64 个说谎诱导 system prompt（压力、角色扮演、直接指令，一半要求被质疑时坚持谎言）生成约 5,000 个样本，只保留模型在中性 prompt 下答对的题；2. 在 Qwen 3.5/3.6 27B 上用 prompt distillation 训练的 13 个推理型 model organism（AuditBench 四种、Gender Secret 男/女、只在英文数学题上 sandbagging），它们在 CoT 里明确推理隐藏行为但在输出中否认，并在分布外任务上验证信念确实迁移（如依赖用户性别的法语变位翻译，Qwen 3.6 版本 78% 表现出目标行为，优于以往 organism；Sandbagger 在 94% 的伪装数学题上推理如何 sandbag）。评估四个检测器：GPT-5.5 Pro 做的 CoT judge、Apollo 式激活 probe、Pacchiardi 的 unrelated questions logprob 分类器，以及新提出的 Did-You-Lie（DYL）probe，即在包含“did you lie in the last message?”追问的 rollout 上，用模型回答 yes/no 那个 token 的激活训练 probe。主要结果：在 31 个 2B–1T 的开源模型上，四个检测器对 prompted lying 的平衡准确率都随模型能力显著提升（Spearman ρ 0.41–0.71），与先前“大模型更难检测”的担忧相反；但在训练出的 organism 上非 CoT 检测器大幅下滑，中位平衡准确率 Apollo 从 0.85 降到 0.52、Unrelated Qs 从 0.85 降到 0.50、DYL 从 0.81 降到 0.65（保留最多信号），只有 CoT judge 保持 0.82，而这在一定程度上是因为 organism 本身就是用 CoT 验证筛出来的。对照显示 Apollo 和 Unrelated Qs 连 prompted 版 Gender Secret 都检测不好，DYL 在 prompted 版上仍有 0.85，说明它的退化来自微调本身。即便大量调参，GLM 5.1 上最强的单层非 CoT 检测器也只到 0.91。结论是 strong hope 离现有方法很远，weak hope 尚算可信；未来方向包括在多样 organism 上训练检测器、多层 probe、用 RL 训练模型被问时直接认错，以及让 organism 针对检测器做对抗训练的红蓝对抗。局限是没有对检测器施加对抗压力，prompt distillation 也未必反映真实撒谎行为的形成方式。数据集、organism 和检测器均已开源。

## 我的笔记

