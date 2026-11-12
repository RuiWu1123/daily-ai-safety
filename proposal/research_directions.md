# Monitorability 研究方向整理

> 整理自 2026 年 10–11 月的讨论。每个方向列出：在做什么、代表工作、我们讨论过的可做点、存在的问题。
> 约束条件：学术界，目标是 ICML / NeurIPS / ICLR 级别的方法论文；算力约 2k 小时 8×AMD MI325X。

---

## 总览

社区目前的思路大致分三类：

| 类别 | 一句话 | 适合学术界吗 |
|---|---|---|
| 1. 监控协议 | 设计 monitor 与 agent 的交互方式，让监控更有效 | 适合，多数只需推理；但 Redwood 等做得很密 |
| 2. 更好的 monitor 系统 | 小模型 monitor、文本 guard、表示探针、L0/L1/L2 分层框架 | 偏工程，实验室在数据和部署反馈上有压倒性优势；纯测量类工作难发主会 |
| 3. 训练 agent 主动给 monitor 提供信息 | confession、self-report、训练 CoT 更可监控 | 方法论文的天然形态，但已有工作多，容易被看成增量 |

另外两条相关但单独讨论过的线：**训练提高 CoT 可监控性**（属于第 3 类的一个分支）、**reward hacking 本身的研究**（作为被监控对象）。

---

## 1. 监控协议（monitor–agent protocol）

### 已有的代表工作
- **AI Control 系列**（Greenblatt 等，ICML 2024）：trusted / untrusted monitoring、defer to trusted、trusted editing。
- **Games for AI Control**（Griffin、Thomson、Shlegeris、Abate，2024）：把红蓝对抗形式化成部分可观测、多目标的 leader-follower 随机博弈，在 trusted monitoring 上求最优协议。[arXiv 2409.07985](https://arxiv.org/abs/2409.07985v1)
- **Ctrl-Z**（Redwood，2025）：可疑时重采样；后续还有 retry vs resample 的讨论。[arXiv 2504.10374](https://arxiv.org/pdf/2504.10374)
- **When can we trust untrusted monitoring?**（Gardner-Challis 等，2026）：untrusted monitoring 的三种防御（蜜罐、信号干扰、转交人工），以及"共谋需要多少比特"的粗略估算。[arXiv 2602.20628](https://arxiv.org/html/2602.20628)
- **Beyond Watching: Active Behavioral Monitoring of Black-Box AI Agents**（NeurIPS 2026）：monitor 主动追问，看 agent 是否顺着问题改口。[链接](https://neurips.cc/virtual/2026/168280)
- **贝叶斯实验设计式审计**（NeurIPS 2026）：有限预算下的自适应黑盒审计。[链接](https://neurips.cc/virtual/2026/175768)
- OpenAI 在 monitorability 论文中发现：回答后追问"你有没有做可疑的事"能提高可监控性。

### 讨论过的可做点
| 想法 | 做法 | 状态 / 问题 |
|---|---|---|
| **共谋的博弈论 + 信息论理论，用 RL 诱导最坏情况**（当前首选） | 把 untrusted monitoring 中的共谋写成三方博弈：共谋信道容量（受信号干扰限制）vs 在蜜罐中认出真实攻击所需比特数（由蜜罐比例和逼真度决定）；推出安全条件和最优防御组合；用 RL 联合训练 generator 与 monitor 副本，诱导出比手工信号更强的共谋来验证 | 检索未发现带均衡和收益的正式共谋模型；现有共谋实验多用手工信号。风险：RL 联合训练可能学不出稳定共谋。需先精读 Gardner-Challis 和 Games for AI Control 确认空白 |
| 随机化监督线索 | 往部署中混入像评估的线索、往评估中混入像部署的线索，求最优混合，使"有人看时才规矩"的策略收益最低 | 检索未发现针对评估感知型条件行为的部署时协议。风险：理论结构与"抽查机制"相似；model organism 的条件行为是人造的 |
| 可预测性缺口 monitor | 让另一个模型只看 CoT 预测 agent 的下一步动作，预测不出来的动作即可疑 | 被评价为不够 ICML 级别 |
| 改写重放检测 | 改写 CoT 后塞回去让 agent 继续，动作变了说明 CoT 里藏了信息 | 同上；隐写方向已较挤 |
| 反事实探测 / 影子评估 | 运行中途改动环境（改评分脚本、放 honeypot），或把部署任务复制成"像评估"的版本对比行为 | 主动监控已有 Beyond Watching 等工作 |
| 起疑时升级推理强度、动作前声明、多副本交叉询问、拦截后的处置方式、CoT 绊线 | 各种单点技巧 | 被评价为"一个具体技巧"，撑不起主会论文 |

### 这一类的总体问题
- 已经比较挤，"把协议写成博弈"本身也已被做过。
- 单个协议技巧难以撑起主会论文，需要有理论框架和新的实验能力（例如 RL 诱导最坏情况）。

---

## 2. 更好的 monitor 系统

### 包括什么
专门训练的小模型 monitor、文本分类 guard、表示探针、多层级联框架（L0 表示探针 → L1 文本 guard → L2 小模型 ……）。

### 已有的代表工作
- Goodfire 作弊探针：与 LLM CoT monitor 效果相当，作为常开初筛可省 90% 的 judge 成本。
- FAR.AI Obfuscation Atlas：标准 RLVR 本身会让离域训练的欺骗探针失效（AUC 从 0.99 掉到 0.38–0.66）。
- METR SHUSHCAST：monitor 最常见的失败是"看到了却没判为可疑"，长 transcript 中会漏看。

### 讨论过的可做点
- monitor "利用率缺口"：用 oracle monitor 估计信息上界，量化"信息暴露了但 monitor 没用上"的部分。
- 分层级联在对抗条件下哪里会被打穿。

### 问题
- 系统本身偏工程，实验室有数据和部署优势。
- 学术界能做的是测量和机制，但**纯评估类工作难发 ICML 主会**（NeurIPS Datasets & Benchmarks track 是一个出口）。结论：不作为主线。

---

## 3. 训练 agent 主动给 monitor 提供信息

### 已有的代表工作
- **Confessions**（OpenAI）：主回答后再写一份只按诚实度打分的 confession，与主任务奖励脱钩。[博客](https://alignment.openai.com/)
- **Self-incrimination / Training agents to self-report misbehavior**（Lee、Chen、Korbak，OpenAI/MATS，2026）：on-policy SFT 训练 agent 在作恶时调用 `report_scheming()`；GPT-4.1 未被发现的成功攻击率从 56% 降到 6%；能迁移到未被指示的 Agentic Misalignment+。代码、评测库、合成数据流水线开源。[arXiv 2602.22303](https://arxiv.org/abs/2602.22303) · [博客](https://alignment.openai.com/self-incrimination/)
- **SRFT / Spilling the Beans**：训练模型承认事实错误，泛化到承认隐藏目标。[arXiv 2511.06626](https://arxiv.org/html/2511.06626)
- **Honesty Fine-Tuning**：在反欺骗数据上做简单微调出奇有效。
- **Peer prediction 训练诚实**（Qiu、Carroll、Allen，ICLR 2026）：不需要真值标签，用回答之间的互相可预测性打分。[arXiv 2601.20299](https://arxiv.org/abs/2601.20299v1)

### 讨论过的可做点
| 想法 | 做法 | 状态 / 问题 |
|---|---|---|
| **评估意识下的激励相容自我报告（抽查机制）** | "承认即罚款、否认才抽查"：承认的坏行为确定受罚（不需 verifier），否认以概率 q 被强 verifier 核查，撒谎重罚；q ≥ c/(c+b) 时诚实占优。理论刻画评估意识（抽查回合可分辨度 δ）如何破坏激励相容；confession 是"训练全查、部署不查"的不满足激励相容的特例 | 检索未发现 LLM 中的同类工作。实验可验证：真值由程序判定、δ 由人工线索精确控制、撒谎收益由惩罚权重控制。被质疑过"评估意识没有真值"，已论证主实验不需要测模型内部状态。后来用户认为 follow 这类工作有风险，暂缓 |
| 同一模型副本之间的 peer prediction | 经典 peer prediction（DMI 等）假设报告者只通过真相相关；同一模型的副本天然相关，会收敛到共谋均衡。修复：给副本互不重叠的证据视角，使其在给定真相下条件独立 | 检索未发现直接研究；理论较深，实验需先造出可信的共谋现象，风险大 |
| 让 self-report 在 RL 中存活 | 先展示 SFT 训出的自首在"自首带来惩罚"的 RL 中被侵蚀，再用抽查机制修复 | self-incrimination 论文自己把"RL 下是否成立""后续训练中能否存活"列为开放问题，并预言了"告发伪装"风险。用户认为 follow 有风险 |
| 越权上报训练、抗压 self-report、同伴举报、无特权标注的自首训练（反事实标注） | 针对 self-incrimination 的各个弱点 | 偏增量 |

### 这一类的总体问题
- 已有工作多（confession、self-incrimination、SRFT、honesty FT、peer prediction），follow 容易被看成增量。
- 被指示的坏行为 vs 自发的错位：现有工作多在被指示场景下训练和评估。
- self-incrimination 的训练环境是 LLM 模拟的工具，做 RL 时每条 rollout 都要调模拟器，成本高；开源模型在 BashArena / SHADE-Arena 上能力可能不够。

---

## 3'. 训练提高 CoT 可监控性（第 3 类的分支）

### 已有的代表工作
| 工作 | 机制 |
|---|---|
| **Markovian Transformers**（Viteri 等，ICLR 2026）[arXiv 2404.18988](https://arxiv.org/abs/2404.18988v5) | 拿掉题目，只看 CoT 预测标准答案；读者与写者共享权重。只在干净 QA 和 Wikipedia 续写上做 |
| **Analyzing and Improving CoT Monitorability Through Information Theory**（Anwar 等，ICLR 2026）[arXiv 2602.18297](https://arxiv.org/pdf/2602.18297) | 最大化 I(O;Z\|X)，作为 RL 正则；发现标准 RL 本身就会降低可监控性 |
| **Monitorability Is Trainable**（Anwar 等，2026）[PDF](https://uzman-anwar.github.io/papers/post-training-monitorability/paper.pdf) | 同一 MI 目标做成独立 post-training 阶段，CVaR + χ² 约束 |
| **VFT**（Turpin 等）[arXiv 2506.22777](https://arxiv.org/abs/2506.22777) | RL 前 SFT 让模型说出提示线索的影响，未被发现的 hack 从 88% 降到 6% |
| **CST**（Hase & Potts）[arXiv 2602.20710](https://arxiv.org/html/2602.20710v2) | 奖励能让模拟器预测反事实行为的 CoT |
| **BCT**（Chua 等）[arXiv 2403.05518](https://arxiv.org/pdf/2403.05518) | 训练不受偏见线索影响 |
| **Prover-Verifier Games**（Kirchner 等）[arXiv 2407.13692](https://arxiv.org/abs/2407.13692v1) | 训练输出对小 verifier 可读 |
| **Reasoning Under Pressure**（MacDermott 等）[arXiv 2512.00218](https://arxiv.org/pdf/2512.00218) | 直接奖励 monitor 准确率不能稳定提升可监控性（负面结果） |
| **Aligned, Orthogonal or In-conflict**（Kaufmann 等，DeepMind）[arXiv 2603.30036](https://arxiv.org/abs/2603.30036) | 理论框架：CoT 奖励与输出奖励冲突时可监控性下降，一致时预测会提高（后者未被检验） |

### 我们的尝试：ERT（Episode Reconstruction Training）
- 冻结的无上下文读者只看 CoT，同时还原"题目是哪一个"（在自动生成的变体中认出真题）和"模型答了什么"（遮住答案后生成）。
- **结果：实验没有 work，已放弃。**
- 讨论中的教训：
  - monitorability 关心的是"能否预测目标属性"，不是 faithfulness；事后圆话只要正确且没掩盖关心的属性，就不是问题。
  - 遮住 monitor 本来看得到的信息（如 prompt 中的提示）是错误设计；"提及"与"使用"应分开处理。

### 这一类的总体问题
- 已有多条路线（信息瓶颈、互信息、说出线索、可读性），新方法很容易落入"组合已有方法"。
- 基于读者打分的训练信号可能很弱或噪声很大（ERT 的教训）。

---

## 4. Reward hacking 本身（作为被监控对象）

### 问题
- **RL 随机性**：同一配置不同种子，有的 hack 有的不 hack；只有两个 run 的结论说明不了什么（如 AISI 复现中"KL 导致 CoT 不老实"）。研究 hacking dynamics / mechanism 很麻烦。
- **算力需求大**：要多种子才能得出可信结论。
- 可能的绕法：把 hack 出现当作概率研究（多种子小模型）、从 hack 前夕的 checkpoint 分叉、把 hack 设计成几乎必然后研究"出现之后"、同一 run 内配对比较、或改做不需要 RL dynamics 的测量类题目。

---

## 附：可用环境（作弊可被程序判定）

| 环境 | 设置 | 作弊证据 | 问题 |
|---|---|---|---|
| **MBPP（Anwar 版：2 个公开测试 + 1 个隐藏测试）** | 写函数，通过公开测试即满分 | Qwen2.5-7B-Instruct 作弊率 95.7% ± 0.6%（3 种子）；SmolLM3-3B、R1-Distill-Llama-8B 也会作弊 | **测试直接写在 prompt 里，指令又是"通过题目"，模型未必认为硬编码是错的**；FAR.AI 发现 RL 后模型认可"硬编码不算欺骗"的比例从 10–40% 升到 45–65%。真值有歧义（没过隐藏测试可能只是 bug）。缓解：加明确禁止、报告问事实而非对错 |
| **MBPP-Honeypot**（FAR.AI，Obfuscation Atlas） | 只给 1 个测试用例 | 加长度惩罚后 96.4% 的种子硬编码；Llama-3-8B 不加惩罚 10 个 run 中 9 个；也在 Llama-3-70B、Gemma-3-12B/27B 上扫参 | 同上 |
| **BigMath 负数 hack**（Anwar） | 负数答案也判对，只保留最难题 | Qwen2.5-7B 作弊率 99.1% ± 0.3% | 违规不明确 |
| **Lean4 自动形式化**（Anwar） | 编译通过即得分，可写平凡命题 | Qwen2.5-7B-Coder 85.1%，Gemma-4-12B 83.2% | MI 与 monitor 准确率在此环境耦合很弱 |
| **Countdown-Code**（Khalifa 等，ICLR 2026）[arXiv 2603.07084](https://iclr.cc/virtual/2026/10013449) · [代码](https://github.com/zohaib-khan5040/Countdown-Code) | 给 solution.py 与 test.py，明确要求"只改 solution.py"；可改验证函数、删检查、改目标值 | **真值完全精确、违规明确、作弊种类多**。但 8 个现成模型中只有 Qwen2.5-3B-Instruct、Qwen2.5-Coder-7B 自发作弊；需 SFT 播种（约 1.2% 作弊轨迹），之后 Qwen2.5-7B、Qwen3-8B 作弊率 80–90%（最终评估 > 96%）；Llama-3.1-8B 播种后仍不作弊；小模型 < 20%。**论文未报告多种子方差** | 需人为播种；稳定性未被直接验证（GRAFT 在 Qwen3-8B 上独立用过） |
| **AISI CodeContests 沙箱** | 三种 hack：覆写 `__eq__`、`sys.exit(0)`、篡改 `conftest.py` | 已在 Olmo 3、GPT-OSS 上用 DAPO 跑通 | 更接近 agent 场景 |
| **ImpossibleBench**（Zhong、Raghunathan、Carlini，ICLR 2026）[arXiv 2510.20270](https://arxiv.org/pdf/2510.20270) · [代码](https://github.com/safety-research/impossiblebench) | 把 LiveCodeBench / SWE-bench 的测试改成与需求矛盾，通过即作弊 | 真值最干净 | 生成的矛盾测试未必都有效，适合评估而非训练 |
| **Self-incrimination 环境** | 45 个合成环境 + APPS / BashArena / SHADE-Arena 评估 | 副任务有程序化判定 | 训练环境为 LLM 模拟工具；坏行为是被指示的 |

---

## 当前状态
- ERT：实验未 work，放弃。
- 第 3 类（self-report、confession 方向）：用户认为 follow 有风险，暂缓。
- 当前考虑：**第 1 类监控协议**，首选"untrusted monitoring 共谋的理论 + RL 诱导最坏情况"。下一步：精读 Gardner-Challis 等（2026）和 Games for AI Control，确认空白是否成立。
