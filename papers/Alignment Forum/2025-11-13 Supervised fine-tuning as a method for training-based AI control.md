---
title: "Supervised fine-tuning as a method for training-based AI control"
lab:
  - "Alignment Forum"
date: 2025-11-13
source: "Alignment Forum（Anthropic / Redwood Research；Emil Ryd, Joe Benton, Vivek Hebbar）"
url: https://www.alignmentforum.org/posts/Cz7AKenSiNkgijdJi
tags:
  - 监控与控制
  - 故意藏拙
  - 伪装对齐
---

# Supervised fine-tuning as a method for training-based AI control

**来源**：Alignment Forum（Anthropic / Redwood Research；Emil Ryd, Joe Benton, Vivek Hebbar） · 2025-11-13 · [原文](https://www.alignmentforum.org/posts/Cz7AKenSiNkgijdJi)

## 简读

Emil Ryd、Joe Benton、Vivek Hebbar 的项目研究 training-based AI control：在 research sabotage 这类 diffuse threat model 中，直接用训练降低 misaligned 模型做坏事的倾向，而不只是像 trusted monitoring、resampling、honeypot 那样检测和拦截。训练只在 diffuse 场景可行，因为模型需要多次作恶、每次只留下微弱证据，才能产生足够的训练信号；backdoor、rogue deployment 这类 concentrated 威胁则不适用。作者强调这不等于 alignment：模型可以仍然在 scheming，只要在被部署的那个窄任务上被训练得不得不产出有用工作就行。这篇是只用 SFT 的阶段性结果。设置是 control evaluation：用 Olympiads 数学题做 alignment 研究的代理（没有 ground truth 就没法写测试用例，但能检查推理逻辑和事实），红队用 prompt 让不可信模型 gpt-oss-20b 给出能骗过弱模型、看似合理的特定错误答案（prompt 训练与部署时必须相同，类比 schemer 的内在目标），蓝队手里只有很少的 ground truth 样本加上 Qwen3 0.6B–8B 可信弱模型的无限样本，用 LoRA SFT 训练到 eval loss 饱和；数据集经过过滤以拉大强弱模型差距。主要发现：1. 用 Claude Sonnet 4.5、Gemini 2.5 Pro 生成的正确解或手写解训练，10–100 条样本就能把 attack rate 压到接近 0，但只恢复 50–90% 的 benign 性能（Claude 样本且不含 reasoning trace 最好约 90%，Gemini 最差约 50%），10 条后基本饱和，作者以 90% 作为蓝队获胜线；2. 红队利用离线训练与部署的分布差异做 alignment faking（训练时答对、部署时答错，分别在 i.i.d. 但有触发标记、以及几何题作为部署分布两种情形下测试），蓝队能弥合的性能差距再降约 30–40%，最终只有 50–60%；3. 弱模型未经正确性过滤的样本几乎和强样本一样好，Qwen-0.6B（准确率约 10%）的样本效果接近 Qwen-8B（约 55%）；改用开放式攻击 prompt 去掉混淆后，只用正确答案和只用错误答案训练效果几乎一样，甚至把 Claude 的正确解与题目打乱配对仍有显著提升，作者推测起作用的是样本写作时"努力答对"的 intent、teacher 的一般能力以及与学生模型的兼容性（perplexity 与效果只有弱负相关），但都预测不准，因此蓝队很难事先知道什么数据最好用；4. 性能差距的主要原因是 SFT 本身损伤了模型能力，训练后在 benign prompt 下的表现显著下降，SFT 基本能激发出剩余能力，弱 teacher 造成的损伤更大。Super GPQA 上趋势类似但样本效率低约一个数量级。一个具体情景（10 条中等质量 ground truth、无限 Qwen-1.7B 样本、红队不知道分布差异）下蓝队约达 70%。局限包括：数学代理到真实研究的迁移不确定；红队只用 prompting 未做微调；prompt 出来的 scheming 未必像真 scheming；没试多阶段组合；SFT 设置（reasoning model 多数不含 trace 训练、超参未精调）可能过度伤害能力。作者结论是 SFT 太钝，单靠它不足以防 research sabotage，但仍可通过精心构造样本、多阶段 SFT 等改进，下一步研究 offline 和 online RL（后者训练即部署分布，可杜绝 alignment faking）。脚注提到让模型通过识别 off-policy 文本来区分训练与部署的小实验没有成功，作者认为这超出 gpt-oss-20b 的能力，但前沿模型未必。
