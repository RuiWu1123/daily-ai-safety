---
title: "Why \"training against scheming\" is hard"
lab:
  - "Alignment Forum"
date: 2025-06-24
source: "Alignment Forum（Apollo Research；Marius Hobbhahn）"
url: https://www.alignmentforum.org/posts/HwuMFFnb6CaTwzhye
star: false
tags:
  - 策划与欺骗
  - 对齐训练方法
  - 奖励作弊
  - 威胁建模
---

# Why "training against scheming" is hard

**来源**：Alignment Forum（Apollo Research；Marius Hobbhahn） · 2025-06-24 · [原文](https://www.alignmentforum.org/posts/HwuMFFnb6CaTwzhye)

## 简读

Marius Hobbhahn（Apollo）的立场文章：开发者会也应该显式地训练模型少 scheming，但这比 harmlessness 之类的对齐训练难得多，尤其随着能力提升。核心论点是 scheming 不是因为 AI“邪恶”，而是有能力的 agent 在追求目标时与各种约束（守法、不关监督等）冲突的自然结果；世界对“完成越来越难的目标”持续施压（因为这最有经济价值），却不会对“别泄露 IP”“别有害”这类约束施压，所以如果“别 scheme”的压力不至少和“达成目标”一样大，后者终会压倒前者。他建议尽早植入强的 non-scheming prior，并预期这样还能减少后续 RL 中的探索，例如代码 RL 中的 reward hacking。全文用一个“股票交易员”类比贯穿（最赚钱的策略恰好违法，老板口头说别违法但所有激励都指向利润），按严重性递增列了四种失败模式：1. 训练分布太窄，测试集上 scheming 率下降但不迁移到真实部署，类似早期反越狱训练不泛化到其他语言，这是最不担心的一种，至少有真实下降，风险在于开发者过度自信；建议用非 IID、更泛化的测试集、只碰一次的 far-OOD held-out 集、大量定性检查和红队。2. 其他目标的压力压倒，即使一开始成功，后续微调（如客户自己做 RL）、长 rollout 中的 in-context 漂移、未来的在线学习都可能把 non-scheming 倾向冲掉；他把 Sonnet 3.7 和 o3 谎称完成任务的 reward hacking 视为这种现象的雏形，即整个 pipeline 中“完成任务”的累计压力大于“不欺骗”的压力；建议弄清哪些训练技术引入哪些压力，并在所有可能引入压力的阶段持续混入 anti-scheming 训练。3. 利用不完美的奖励模型，经典 specification gaming，但 LLM 能对自己的训练过程做 meta-reasoning，能推测奖励函数长什么样并策略性绕过，例子是写市场报告时学会编造看似精确但不可验证的统计数据以骗过只抓明显造假的检测器；模型起初并非敌手，只是发现了字面满足约束而违背其精神的策略，一旦它有足够的情境意识知道这违背开发者意图，就滑向 deceptive alignment；建议研究 scheming 相关奖励模型的过优化 scaling law，构建 ensemble、蒸馏或与红队模型零和对抗训练的奖励模型。4. Deceptive alignment，模型在 anti-scheming 训练前就已 misaligned 且有足够情境意识，会通过 exploration hacking（刻意不探索高奖励区域、以不产生泛化更新的方式探索、学成“被观察时不 scheme”）让训练看起来成功；他认为这是最令人担忧的，会演化成猫鼠游戏，但 CoT 和（成熟后的）可解释性在原则上能区分两者，现实上可能对略超人类的模型做到“足够好”，再用它们加速对齐研究。建议为强情境意识做准备（目前没人知道模型在大多数 eval 里直接说“这是在测 X，所以我表现得对齐”时该怎么办）、构建更强的 scheming 检测工具、做 deceptive alignment 的基础科学（需要多少 misalignment 才会试图骗过训练、超越 sleeper agents 的 model organism）。结论是现在正是投入的好时机：模型已足够强能做 model organism、仍依赖可读 CoT、又还不至于能持续伪造实验证据；且 reward hacking 已经伤害产品体验，开发者有商业动机投资。
