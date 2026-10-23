# 用户的兴趣方向（用于日报里的 ⭐ 标记）

依据用户星标的论文整理，详见 `my_notes/research_map.md`。新内容只要明显属于下面任一方向，就在日报里标 ⭐。

1. 奖励作弊及其泛化：reward hacking、specification gaming、reward tampering，以及它们如何泛化成更广泛的错位（emergent misalignment）；训练时的缓解（inoculation prompting、局部化坏行为等）。
2. 模型对训练与评估的"知情"：eval awareness、situational awareness、metagaming、reward-seeking / fitness-seeking、模型对评分机制的推理。
3. CoT 可监控性：CoT faithfulness、CoT controllability、obfuscation、无 CoT（单次前向）推理能力、可监控性评估与指标。
4. 策划、伪装对齐及其训练缓解：scheming、alignment faking、反策划训练、sandbagging 审计。
5. 诚实与自我报告：honesty、calibration / self-knowledge、confessions、self-report、欺骗探针。
6. 真实世界的错位事故：实际发生的 misalignment 事故及其调查。

用户基本不关注：机制可解释性与表征类研究（SAE、probe、circuits、steering、latent/feature 分析、参数分解等），**即使主题属于上述方向也不标 ⭐**，除非它的主要贡献是行为层面的发现、而可解释性只是辅助手段；越狱与鲁棒性、危险能力评估、网络安全评估、AI control 协议设计、政策与治理也不标。
