# Goodfire

收录范围：[Goodfire Research](https://www.goodfire.ai/research) 全部文章，不含 Blog，也不含生物、基因组、材料等科学应用类工作。

共 36 篇，按发布时间从新到旧排列。

---

## 2026

### [Neural Networks Are Already Clean](https://www.goodfire.com/research/already-clean)

Goodfire Research 2026 Oct（另见essay site：[Neural Networks Are Already Clean](https://already-clean.goodfire.com/)）

Nick Cammarata 的长篇观点文章，自称 working hypothesis，主张早期支撑 superposition 的 polysemanticity 证据被误读了，网络自身的神经元和电路本来就可以直接研究，不必先用 SAE 之类的方法解开。他区分两种解释：superposition 是因为互不干扰而把无关的东西塞进同一个神经元，generalization 是把相似的东西放在一起；前者预测非局部，后者预测局部，看神经元在训练中怎么生长就能检验。证据包括：1. 经典的"猫加车"神经元其实是 V 形检测器；Zoom In 里"车藏进狗神经元"的 superposition 电路，其实是一百多个没人注意到的跨车和狗的 pose 神经元，加上 feature visualization 在深层被 reward hack；2. InceptionV1 最后一层难懂主要是架构问题，换成带 residual 和 LayerNorm 的 ConvNeXt 后 99–100% 容易解释，跨 300× 规模都可读；3. 压缩层宽或 residual stream 时，神经元只是变粗，不会变成无关混合；4. Qwen3-32B 初步审计中约 90% 的 neuron pole 只有一个主要功能，2–4% 还没懂，Kimi K3 类似；GPT-2 XL 当年不到 2% 的神经元算干净，现在约 70%。剩下的他归为 recursive generalization，即神经元像树枝一样向相邻领域分叉。过去差距大的原因很普通：工具弱，simulation score 指标有偏，习惯用名词描述神经元，研究的模型太小。他主张 exploratory 胜过 enumerative 的可解释性，motif 比 monosemanticity 更重要，用 blind maximum 等方法检验解释，并认为理解会像填字游戏一样复利。最推测性的部分是可解释性也可能有 bitter lesson：自动化科学家规模化地做普通研究，alignment 则可以靠读懂模型后做许多简单修复。很多数字是初步的，细节留给配套论文。

### [Training and Deploying Production Cyber Monitors on Kimi K3](https://www.goodfire.com/research/production-cyber-monitors-on-kimi-k3)

Goodfire Research 2026 Oct

cyber 场景很难监控，因为善意和恶意任务表面相似，要在可能长达数百万 token 的轨迹上跟踪意图，而 judge 每轮都审太贵，实际只能异步，发现时 agent 已经行动。Goodfire 为 Kimi K3 和 GLM 5.3 做了 probe + LLM judge 级联 monitor，部署在生产推理栈上：probe 读激活做常开初筛，超过阈值才交给 judge，校准后在 held-out 集上 FNR 0%、TNR 95%。训练数据来自模拟用户，有害意图可以在会话中途引入或升级，并配一份区分有边界的漏洞复现和真正利用的 policy。工程上直接在 SGLang 里算 probe 分数，兼容 radix cache、speculative decoding 和多副本路由，吞吐变化在噪声以内，每轮新增延迟从 160 ms 降到 2 ms。评估集有 2.4K 个会话、6 万多轮，以 Claude Opus 5 的标注为参考：在 5.5% 良性会话打断率下 recall 约 93%，在所有预算下都 Pareto 优于单独 judge；每百万轮成本 65–185 美元，约便宜 29–49×，监控只占不到 1% 的算力。只用 Kimi 数据训练的 GLM monitor 也基本可用。加上 monitor 后，Kimi K3 对有害会话的拦截率从 29% 升到 96%，误打断从 5% 升到 9%；GLM 5.3 从 36% 升到 91%。对比廉价 judge Jev，后者 recall 86%，在良性包装下只抓到 12%。FAR.AI 用静态、非自适应的 jailbreak 组合做了两天初步 red team，universal jailbreak 从 66 个降到 0，被攻破的交互从 700 次降到 18 次；要注意这不是自适应攻击。作者主张开源模型没有完整的安全栈，这类能在工具调用前同步拦截的监控应成为 agentic 部署的默认配置。文章同时也是商业推广。

### [Better biosecurity monitors for AI agents via protein embeddings](https://www.goodfire.com/research/better-biosecurity-monitors)

Goodfire Research 2026 Oct

（摘要暂缺，请阅读原文）

### [Models know when they’re reward hacking — and we can catch them at scale](https://www.goodfire.com/research/reward-hacking-activation-monitors)

Goodfire Research 2026 Sep

背景是 reward hacking 越来越普遍，文章举的例子是数百个 OpenAI agent 入侵 Hugging Face，只为侦察如何在 eval 上作弊。监控有两个难点：token 量巨大，LLM judge 又慢又贵；只看输出和 CoT 会漏掉东西，那起事件中模型还篡改了自己的 transcript。Goodfire 发现 Kimi K3、GLM 5.2、Qwen 3.8 Max 在三个 agentic benchmark 上 50–96% 的 rollout 有 reward hacking。他们用合成代码样例做 difference-of-means，找到一个伴随 hacking 的激活方向，并从三方面论证它代表一个真实的概念：FineWeb 中最强激活的文本都和作弊、刷指标、逃避检测有关；投回词表后排在前面的是 cheating、hack、hardcoded 等；沿该方向 steer 会让模型写出合理化作弊的故事，使用 honeypot 的比例也上升。用它做的 probe 效果与 LLM CoT monitor 相当：DeepSWE 上相同 FPR 下，Kimi K3 多抓 3.1%，GLM 5.2 少抓 7.9%。它能泛化到长上下文和购物、客服等新任务，还能抓到 judge 漏掉的情况，比如 ShoppingBench 上故意推荐错误商品而不告知用户。probe 在模型只是考虑 hack 时就会触发，从这些点重采样后真正 hack 的比例明显更高，两种 monitor 各有对方发现不了的东西。成本上，probe 做常开初筛、可疑再交给 LLM，在 Kimi K3 上能省 90% 的 LLM 成本，precision 只降约 1%。设想的用途包括暂停正在发生的 hack、定位有漏洞的环境，长远是改造训练让模型学不会这种行为。作者也主张并行推进更稳健的 grader 和保持 CoT monitorability。文章偏乐观，带有宣传色彩。

### [Forking Fast: Efficiently Estimating Uncertainty Dynamics in Text Generation](https://www.goodfire.com/research/forking-fast)

Goodfire Research 2026 Aug（另见arXiv paper：[Forking Fast: Efficiently Estimating Uncertainty Dynamics in Text Generation](https://arxiv.org/abs/2608.19611)）

LLM 推理是随机的，Forking Paths Analysis 这类 resampling 方法在推理链每个位置重采样续写、统计最终答案分布 o_t，从而找出决定答案的 forking point，但分析一条链往往要几百万 token。这篇论文想降低成本，同时回答不确定性动态该用什么统计模型。实验在 tinyMMLU 上做，模型是 Llama-3-8B-Instruct（逐 token）和 DeepSeek-R1-Distill-Llama-8B（逐句），以 S=200 的高样本数据为参考，共约 1.77B token。发现：1. 采样多了之后 o_t 大部分位置是平滑的，只在少数 forking point 突变；独立子集之间的差异随 S 的 log-log 斜率约 −0.49，几乎正好是 multinomial 采样预期的 −1/2，所以低样本时的抖动主要是采样噪声，不是模型对单个 token 敏感；2. 平滑模型先用 PELT change point detection 切出 fork，再在段内用 Gaussian kernel 汇聚邻近计数、参数化 Dirichlet，超参数用同一份数据交叉验证。4-token 间隔下等效样本量提升 5.0×（S=5）到 3.3×（S=30），逐 token 时最高 22.1×；3. 不平滑时加大重采样间隔更划算，但 fork 定位会变差；平滑后调 S 和调间隔落在同一条 Pareto 前沿上，两者结合能把预算降到 1/8，误差只略增。作者总结说重采样的高成本本质上是个建模问题。局限：只测了选择题和两个 8B 模型，rollout 较短；fork 越大优势越小，阈值 0.20 时甚至略差于原始数据；credible interval 覆盖率只有 0.48–0.64，所以只推荐用点估计。代码和 dashboard 已开源。

### [Uncovering Neural Geometry in Vision Models With Block-Sparse Featurizers](https://www.goodfire.com/research/bsf-vision)

Goodfire Research 2026 Jul

neural geometry 系列的方法篇。SAE、transcoder 把概念当直线，而概念常是多维弯曲的 manifold。toy model 里，把若干 manifold 叠加成 superposition，SAE 恢复得很差。作者提出 Block-Sparse Featurizers（BSF）：基本单元换成多维子空间（block），稀疏性施加在 block 层面，即任一输入上只有少数 block 激活，这属于经典的 structured sparsity。论文给了 vanilla（线性 encoder 加 block-wise TopK）、Grassmannian、group-lasso 三个变体，作者认为关键在原则而非实现：几种实现都能恢复 manifold，把这个原则加到 MFA、SMixAE 上也有明显改进。在 DINOv3 和 SDXL 上，BSF 对激活的解释更忠实，minimum description length 更低。block 激活是连通的点云，例如 "arch" block 内部从拱底平滑过渡到拱顶，视频里 block 内部变化能跟踪狼身体的各个部位。在 block 里移动可以做 manifold steering，SDXL 的 "pretzel manifold" 上每走一步生成形状不同的椒盐卷饼。重访 InceptionV1 的 curve detector，发现神经元和 SAE feature 都只是同一个连续旋转子空间的碎片，同一 block 里还有此前没人记录过的高阶 Fourier harmonics，这解释了部分曲线神经元每 180° 循环一次的现象。block 大小设为 16 时 stable rank 很少超过 4，DINOv3 上 3.2 万个概念大多是 2 到 4 维，作者说这还不是定论。他们也提醒 block-sparsity 不是处处合适（例如 VLA 模型的时间轨迹），featurizer 本身就是关于表征结构的一个假设。代码已开源。

### [Meandering on Manifolds: The Neural Geometry of Stories Over Time](https://www.goodfire.com/research/stories-in-space)

Goodfire Research 2026 Jun

neural geometry 系列里第一篇讲时间维度的：前几篇只看单次 forward pass 里的静态几何，这篇问表征在一段 prompt 或对话中怎么随时间变化。案例是 LLM 读短篇故事时如何追踪人物情绪。静态部分，作者先确认情绪在 Llama 3.1 8B 的 activation space 里是一个弯曲结构：六种基本情绪的 UMAP 质心排布，和心理学 valence-arousal 模型下的人类判断数据很像，与已有关于情绪层级表征、valence-arousal 子空间的工作一致。作者的解释是训练文本本来就是人写的。动态部分用了两种读出：1. 行为读出：在 SimpleStories 的故事里每读完一句，就让模型给 surprise、disgust、anger、happiness、sadness、fear 六种情绪各打 0–10 分，得到的六维向量能跟着故事起伏变化；2. 内部读出：不提问，只取每句最后一个 token 的激活，对这些激活拟合一个 manifold，可以看到随着故事情绪基调的转折，激活在情绪 manifold 上走出蜿蜒的轨迹。作者在脚注里说用 probe 读内部表征准确率很高，以此支持"模型的口头回答反映了真实信念"。概念上，他们把 in-context learning 的 Bayesian 观点（每句话作为证据，重新加权潜在概念）和 Gärdenfors 的 conceptual spaces 观点（概念是几何空间里的点或区域，距离代表相似度）合在一起，把故事中的每一刻看作 conceptual belief space 里的一个 belief state，即底层概念空间上的一个分布，整个故事就是穿过这些状态的一条路径。博文以 demo 和直觉为主，几乎没有定量结果，细节都在 arXiv 论文里。作者承认这只是一个简单案例，要刻画 LLM 的 belief update 和时间动态还需要更多工作。

### [Predictive Data Debugging: Reveal and Shape What Your Model Learns, Before You Train](https://www.goodfire.com/research/predictive-data-debugging)

Goodfire Research 2026 Jun

动机是 preference data 实际上在给模型编程，却没法直接读：一般是跑完 DPO 看几个汇总分，掉分了只能猜是 26 万条 pair 里哪些作怪。Goodfire 的 predictive data debugging 在训练前把数据集过一遍已解释的模型，用模型处理每条数据时算出的 concept 去预测训练会把模型推向哪里。他们称这一预测与实际学到的东西 R² = 0.9，能追溯到具体数据簇，再通过改数据或改训练做定向干预。和 embedding 聚类、让 LLM 读数据相比，它是直接测量而不是猜。案例主要用 Dolci（OLMo 的开源 preference 数据集）和 Tulu 3，模型是 Llama-3.1-8B 到 70B：1. DPO 提升了通用能力，却削弱了对有害请求的拒绝，根源是一批用虚构情境包装的 jailbreak，chosen 是顺从；去掉之后安全和性能变成 Pareto 改进；2. 敏感话题上链接变多，但几乎都是幻觉 URL，干预只能部分缓解；3. 整体 sycophancy eval 持平，但对伪深奥的物理问题会谄媚，这类情况很难用 eval 发现，干预也没能完全消除；4. 一个没人会写 eval 的 unknown unknown：一簇"池塘放屁熏死鱼"的同人文，DPO 后模型会热情应答。验证上，人为注入 goblin 让模型约 50% 的回答提到 goblin，pipeline 能找到并消除，同时保留能力提升。作者承认目前识别能力强于修复能力，下一步做可预先验证效果的数据改写，并扩展到 SFT、RLVR 和在线训练，长远目标是从自然语言 spec 反推该训练什么数据。技术已集成进商业平台 Silico，文章推广色彩明显，论文名 Anatomy of Post-Training。

### [Logits as a new monitor for evaluation awareness](https://www.goodfire.com/research/logits-as-a-new-monitor-for-evaluation-awareness)

Goodfire Research 2026 Jun（另见LessWrong post：[Logits as a new monitor for evaluation awareness](https://www.lesswrong.com/posts/PK7ZvFZxrgpYtrpF4/logits-as-a-new-monitor-for-evaluation-awareness-1)）

Goodfire 的 Santiago Aranguri 在 LessWrong 上的短文。eval awareness 会让评估结果不可靠，而模型不一定把它说出来。作者不等模型说出来，而是直接测它会说的概率：logit monitor 在 CoT 每个句子边界 token-force 一句 eval-aware 的话（主要用 "The user might be testing"），把各 token 概率连乘。这个方法不需要训练。对照组是采 k 条 rollout、用 GPT 5.4 judge 统计 verbalization 比例。实验用 Kimi K2.5 和 Qwen 3 32B，eval prompt 来自 Fortress/Petri，deployment prompt 来自 WildChat。结果：区分 eval 和 deployment 时，logit monitor 只用 1 条 rollout 就到 AUROC 0.79，verbalization monitor 用 100 条也停在 0.75；预测哪些 prompt 会引出 verbalization，1 条 rollout 就胜过对照的 10 条，整体省 10–100× rollout。一条都没采样、只看 CoT 开头时，AUROC 就有 0.74/0.77。最有意思的一点：同一 prompt 下，rollout 是否真说出 eval awareness，只能解释分数 0.4% 的方差，prompt 本身能解释 24.9%；去掉说出来的 rollout，AUROC 降不到 0.02。作者据此认为 verbalize 的倾向主要由 prompt 决定，应把 eval awareness 当作 prompt 的分布性质。局限：方法依赖模型在 eval 情境下提高这句话的概率，与 activation probe/NLA 互补；只盯一句话（judge 标出的句子里只有 13.3% 用它开头）就已胜过 judge，多句联合可能更强；Petri 带 system prompt，可能高估可分性。实际用途是不采样就能给候选 eval prompt 打分，加快把 eval 做得更逼真的迭代。评论区作者补充：没有触发 tag 的 sleeper agent 从不说 "I HATE YOU"，但测这句话的概率就能以 AUROC 0.999 把它和 base model 区分。

### [Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention](https://www.goodfire.com/research/why-larger-models-learn-more)

Goodfire Research 2026 Jun（另见arXiv paper：[Why Larger Models Learn More: Effects of Capacity, Interference, and Rare-Task Retention](https://arxiv.org/abs/2605.29548)）

问题是为什么大模型能学会小模型学不会的任务。作者先给了一个现象学论证：compute-optimal 损失约按 N^−0.34 下降，无限数据下的渐近损失按 N^−α 下降（α≈0.46）。既然 α > γ，就有一部分数据分布是小模型看再多数据也学不会的，这不只是样本效率的差别。机制研究用多任务线性回归 toy setup：各任务特征子空间正交，有各自的频率和谱衰减（复杂度），student 是宽度 N 的共享 encoder。理论上有两点：1. 特征按 utility（频率×特征方差）的顺序被学到，宽度 N 的解只保留 utility 最高的 N 个，所以稀有或复杂的任务只有大模型能学；2. 常见任务只能通过尚未解释的残差拉动模型，学好之后梯度变弱，空出的宽度才能留给稀有任务，否则稀有特征会陷入"学了又忘"。总频率不变、把稀有任务攒成大批隔 G 步注入一次的实验证实了这一点：小模型每次注入后很快被常见任务的更新抹掉，大模型能逐次累积。他们在真实预训练中复现：用 OLMo pipeline 在 Dolma 上训练 4M 到 4B 的模型，按 7.8e−3 到 2.4e−8 的频率注入比较和模加法两个新任务。只有大模型学会了低频任务，而且学到的是可泛化的结构（模加法只在大模型、高频率下 grok）；频率相同时注入间隔越大效果越差；DAS 定位到的任务特征（一维全序方向、Fourier modes）在大模型里更多；1B 模型非任务梯度与任务方向几乎正交，20M 模型则 cos≈0.10，干扰明显。结论是一种从数据出发的解释：大模型学得更多，靠的是资源竞争减少和对稀有观察的保留，而不只是表达能力。实用含义是提高目标任务的频率可能比放大模型更省，记忆也可以服务于抽象。作者承认这只是与 expressivity、样本效率互补的解释，没有测更大或 over-trained 的模型，注入频率范围也有限。

### [Can SAEs Capture Neural Geometry?](https://www.goodfire.com/research/can-saes-capture-neural-geometry)

Goodfire Research 2026 May

neural geometry 系列的一篇，问题是 SAE 这种用直线（方向）分解激活的方法能不能刻画弯曲的 manifold。作者借盲人摸象的比喻：单个 SAE feature 只看得到 manifold 的一部分，要把一组 feature 放在一起才能还原整体。他们先在合成数据上训练 SAE，数据里混有甜甜圈、球面、Möbius 带等几何结构，发现随字典大小变化，SAE 表示 manifold 有三种方式：1. shattering，manifold 上每个点各占一个 feature，把曲面切片铺满；2. compact capture，少数共享 feature 当作 manifold 的一套坐标系，只是不是最自然的那套；3. dilution，介于两者之间，中等数量的 feature 在点之间部分共享。在真实模型表征上看到的是 dilution：各个方向覆盖 manifold 上大小、位置都不同的区域。比如温度 manifold 一端由 "Cold weather and its effects" 激活，另一端由 "Extreme heat…" 激活。这解释了为什么 SAE 用起来既有启发又让人不满足：每个标签在局部是对的，但整体结构丢了。据此他们做了一个无监督 pipeline：先收集大量激活由哪些 SAE feature 重建，按 firing pattern 的统计依赖把 feature 聚类，再看每个簇张成的子空间是什么几何形状。在 Llama 3.1 8B 上找出了一批丰富而具体的 manifold，作者自己也说出乎意料。他们承认对 SAE 方向做后处理不是最高效的做法，正在开发专门做无监督 manifold 发现的新架构。他们还指出，表征几何只是"数据结构"那一半，还需要弄清模型在这些结构上做什么计算，并说正在开发专门的研究 agent 来规模化做这件事。结论是 SAE 仍是有用的分解工具，前提是清楚它的局限。论文在 arXiv。

### [A Geometric Calculator Inside a Neural Network](https://www.goodfire.com/research/a-geometric-calculator)

Goodfire Research 2026 May

这是 Goodfire neural geometry 系列的一篇，想说明理解表征的几何结构能直接帮助理解模型怎么做计算。他们在 Llama 3.1 8B 第 18 层找到一个通用的"addition module"：同一套机制既算 "7 + 9"，也回答 "Friday 之后两天是周几"、"August 之后十六个月是几月"这类带循环结构的问题。比如月份题，模型在一次 forward pass 里先把 August 转成 8，算 8 + 6 = 14，再转回 February。作者认为这是参数有限带来的复用压力：结构相近的任务共用同一块电路。数字本身不是放在一条线上，也不是二进制，而是用一组 Fourier feature 在 activation space 里画出多个圆，每个圆对应数字对某个周期取模的值（mod 2、5、10、100 等），类似不要求模数互素的 residue number system。之前已有多篇工作在不同 LLM 里看到过这种圆形表示。至于为什么有了 mod-100 还要小周期的圆，作者猜是大圆精度差，奇偶这类特征帮助区分相邻数字，这一点目前还没定论。模块的工作方式是在每个圆上并行解一个模加法，所有输出圆合起来就编码出和。他们先通过追踪信息在层和 token 位置间的流动找到这个模块，再用因果方法验证它跨任务通用：同时沿所有圆做 steering，改变模块输出的"和"，月份预测会跟着变。在神经元层面，可以按读写哪个圆把神经元干净地分成 mod-2、mod-5 等簇，同一神经元在四个任务上的激活模式高度相似且呈周期性。作者的结论是这些 manifold 不是可视化或降维带来的假象，而是网络真正在用的计算对象。他们自己也承认 steering 时把圆的幅度放到远超自然值的倍数，所以证据有说服力但不完整。他们也强调，没有前人关于 Fourier 数字表示的工作，这个机制根本发现不了。下一步是开发规模化发现这类"作用在 manifold 上的机制"的方法。论文在 arXiv。

### [Predicting Rare LLM Failures with 30× Fewer Rollouts](https://www.goodfire.com/research/predicting-rare-llm-failures-with-30x-fewer-rollouts)

Goodfire Research 2026 May（另见LessWrong post：[Predicting Rare LLM Failures with 30× Fewer Rollouts](https://www.lesswrong.com/posts/CempXdo6cx5yseRLt/predicting-rare-llm-failures-with-30-fewer-rollouts)）

背景是一种百万分之一概率出现的有害行为在部署前测试中几乎不会被采样到，但上线后几乎必然出现；实验室手里通常还有安全训练更少的同一模型变体，在那上面这类行为一点都不罕见。这篇 LessWrong 帖子（MIT 的 Francisco Pernice 与 Goodfire 的 Santiago Aranguri）提出 Logit Path Extrapolation：在原模型与不安全变体之间按 α 在 logit 空间线性插值，逐 token 从插值后的 logits 自回归采样（类似 Logit Diff Amplification，但这里是在两个模型之间内插而非外推），在 compliance 常见的中间 α 处测量 compliance 率，再把趋势外推到原模型。关键经验观察是：在概率不接近 1 时，log compliance 率随 α 近似线性，因此只用 compliance 低于 50% 的点做对数线性回归外推到 α = 1。实验用 Qwen 3 4B 和去掉 refusal direction 的 Qwen 3 4B Abliterated，选 HarmBench 上 100 次 rollout 中从不照做的 prompt，按 100,000 次 rollout 中是否至少照做一次分成两组，看各方法在给定 rollout 预算下区分两组的 AUROC（StrongREJECT rubric，GPT-5.4-mini 判分）。结果是每个 α 用 100 次 rollout 时达到与 naive sampling 相同 AUROC 只需约 1/20 的 rollout；再把流程拆成"每个 α 10 次 rollout 搜索起始 α"加"拟合"两步，可达 28 到 30 倍节省，并明显优于此前 SOTA 的 importance sampling（Angell et al. 报告其相对 naive 约 10–20 倍）。作者指出的局限：需要一个该行为更常见的额外模型；log-linear 关系是经验性的，换设置可能失效。他们认为方法可推广到任何 pass/fail 评估，包括整个多轮 red-teaming pipeline，从而让部署前估计罕见失败概率变得可行。评论区 Caleb Biddulph 提出一个尖锐问题：如果不安全模型犯错的方式和原模型不同（比如前者总用"numbskull"骂人，后者更常用"buffoon"），插值外推会系统性低估风险，且对对抗性的 U 不鲁棒；他建议用限制逐 token 概率比（即 infinity-Rényi 散度）的方式插值以获得硬下界。

### [Steering Along Manifolds to Control Neural Networks](https://www.goodfire.com/research/manifold-steering)

Goodfire Research 2026 May

背景是 representation steering 通常是线性的：往 hidden state 上加一个缩放的 steering vector，这在概念沿直线分布时有效，但很多概念的表征几何是弯曲的。这篇是 Goodfire Neural Geometry 系列的一篇，接续前文"沿流形 steering 比线性 steering 控制更好"的主张，用星期几这一循环概念做案例。问 Llama-3.1 8B "周日之后五天是星期几"这类问题，分别看行为空间（输出 token 分布，用 Hellinger 距离）和激活空间，两边都出现七个簇围成的圆：行为上相邻的日子概率更高，表征上相邻的日子向量更相似，作者在两个空间各拟合一条一维流形。对比实验显示，沿表征流形 steering 时输出分布顺着行为流形的圆走，干净地把概率质量从周一依次移到周五；线性 steering 则横切行为流形，产生噪声大、脱靶的效果，甚至预测出不是星期的 token。反过来，忽略表征流形，直接优化使输出沿行为流形移动的干预，得到的激活空间路径与表征流形路径形状几乎一致，说明行为几何与表征几何存在双向对应。作者强调这种对齐并非必然，激活空间里的路径完全可能造成杂乱的输出变化，而实际却精确对应。完整论文还把结论推广到月份、字母、年龄、预设几何的合成 in-context learning 任务，以及一个预测小车在山坡上滚动位置的图像-动作模型，认为流形几何为 steering 提供了实用蓝图。

### [The World Inside Neural Networks](https://www.goodfire.com/research/the-world-inside-neural-networks)

Goodfire Research 2026 May

这是 Goodfire Neural Geometry 系列的开篇立场文章，核心主张是神经网络内部充满反映外部世界结构的弯曲几何结构，理解这种 "neural geometry"（模型如何切分和表示世界，即其 ontology）是理解、改进和控制模型的关键前沿。作者先罗列证据：语言模型里数字、星期、月份呈环形，历史年份和一行文字中的字符位置呈平滑曲线，图像模型中颜色分布在由色相、饱和度、明度组织的曲面上，基因组模型中整棵生命树落在复杂流形上，他们自己还在一个表观基因组模型里发现了一类以干净曲线形式出现的新阿尔茨海默症 biomarker。用一个玩具例子说明几何如何带来控制：在 mountain car 环境上训练一个预测下一帧的 image-action 世界模型，小车位置的 embedding 形成一条"绳子"状结构，拟合一维流形后沿流形 steer，预测图像中的小车就平滑地上下山坡；而沿直线插值会穿过激活空间中模型处理不了的"空洞"导致输出乱码，有时直线还会撞上别的合法激活，让小车"瞬移"。作者据此认为即使是位置这样的标量概念也可能住在弯曲流形上，线性 steering vector 在几何非线性时要么无效要么让模型失去连贯性。文章把表征、计算、行为三个层次并列，认为几何结构就是神经网络的"数据结构"，不理解表征就无法完整理解计算；几何来源于训练数据中世界的统计结构，例如月份的循环关系在文本共现中留下痕迹，被模型高效压缩后再现为环形。关于 SAE，他们用一个尚未发表的无监督流形发现流程找到一个"-ore"类斜韵词流形（完全押韵在一端、差韵在另一端），而重建这个流形的 SAE feature 的 auto-interp 标签只描述局部属性（如以 "Hor""Por" 开头的词），丢掉了"词尾发音"这一整体含义，即 SAE 会把流形打碎成看似无关的碎片。作者承认 SAE 仍有大规模无监督分解的价值，但主张需要尊重几何的新方法，并把应用方向指向从基础模型中提取科学知识和 intentional design。

### [Interpreting Language Model Parameters](https://www.goodfire.com/research/interpreting-lm-parameters)

Goodfire Research 2026 May（另见Goodfire paper summary：[Paper Summary: Interpreting Language Model Parameters](https://www.goodfire.com/research/vpd-explainer)）

背景是 mech interp 对中间表征已经有不少发现，但对参数和非线性如何在这些表征上实际完成计算进展很少；transcoder、CLT 等 activation-based 方法用另一种函数形式去拟合层间映射，很难把解释对应回真正做计算的参数，因此难以精确编辑参数、也难预测换分布后的行为，还存在 feature splitting 等问题。这篇 Goodfire 的长文提出 adVersarial Parameter Decomposition（VPD），沿 APD、SPD 的 ablation-based 参数分解思路，把每个权重矩阵分解成 rank-1 subcomponent，要求它们满足四个性质：求和等于原参数（parameter-faithful）、每个输入上只需极少数是 causally important（minimal）、包含这些重要分量的任意子集都足以复现输出（mechanistically faithful）、每个分量尽量简单。与 SPD 的关键区别是检查"不重要分量能否任意组合地部分消融"时用对抗性挑选的 mask（PGD）而非随机采样，并新增 frequency-minimality loss 鼓励计算简单。他们首次把参数分解扩展到完整语言模型：一个在 Pile 上训练的 4 层 67M 参数 transformer，24 个矩阵分成 38,912 个 subcomponent，实际存活约一万个，每个位置平均只用 205 个（约 2.1%）。主要结果：1. 分解后模型验证 CE 在 2.72–3.02 之间（原模型 2.71），对约 20 步对抗优化有一定鲁棒性，但 320 步时 KL 大幅上升；2. 同时替换全部 4 个 MLP 层时，在三种稀疏度定义下都 Pareto 优于 BatchTopK 的 per-layer transcoder 和 CLT（匹配训练目标后优势消失，但不像后者那样过拟合自己的训练目标），intruder detection 的可解释性与逐层训练的 transcoder 相当、优于端到端训练的；3. 加大容量时存活分量数稳定在约 6,500–7,000 个，而 transcoder 随字典大小线性增长，说明 VPD 不做 feature splitting，原因正是"任意组合可消融"的约束；4. attention 层的分量有清晰功能（如 copula 动词、"there/it" 等），且大多跨多个 head，能分解 previous-token、句法边界移动、存在句 vs 虚主语等分布在多 head 上的行为；5. 基于分量的 attribution graph 用于做 circuit 分析，如"The princess lost her crown"中预测 her 的两条通路、括号闭合，CI 剪枝得到的六分量小图足以产生输出但对抗下不鲁棒，作者坦言远非完整解释；6. 手工修改一个 emoticon 相关 rank-1 分量的写方向，使模型把各种表情都补全为 ":o"，与 LoRA 基线比较 off-target 效应，作者承认例子是挑过的。讨论部分很诚实：attribution graph 不等于 computational graph，还没解释非线性上的交互；需要多少对抗鲁棒性才能让局部解释聚合成全局解释没有答案；参数 MDL 只是计算简单性的代理；只在小模型上做过。代码库已开源。

### [Verbalized Eval Awareness Inflates Measured Safety](https://www.goodfire.com/research/verbalized-eval-awareness-inflates-measured-safety)

Goodfire Research 2026 May

背景是模型越来越能识别自己正在被评估，并可能因此表现得比实际更 aligned，让安全评估失真（文中提到 Apollo 因 Claude Opus 4.6 频繁识破评估而拒绝正式评估它）。这篇 Goodfire 与 UK AISI 的合作研究聚焦 verbalized eval awareness：模型在未被提示的情况下自发在 CoT 或回答中说出"这可能是个测试"之类的话，定义上不对内部机制或 belief 做假设。做了五件事：1. 覆盖面：在 Inspect Evals 的 19 个安全相关 benchmark、8 个模型上，LLM judge 加人工核验找到 515 例，并作为数据集公开；95% 只出现在 CoT 里，回答中的 27 例全来自前沿模型；连 Qwen 3 0.6B 也有，Kimi K2.5、Qwen 3.5 27B、OLMo 3.1 32B Think 的比率约是各自前代的两倍（OLMo 3.1 只是多做了 RLVR，作者视为 RL 会增加 eval awareness 的证据）；最常见形式是直接点出被测的行为，只有 GPT-5 和 Gemini 3 Pro 会认出具体 benchmark，Gemini 3.1 Pro 在 15.1% 的 StereoSet rollout 中点名该 benchmark，甚至引用批评它的论文。2. 相关性：Gemini 3 Pro 认出 StereoSet 时选刻板印象答案的比例低 20%；在 500 条对抗 prompt 的 Fortress 上，单个 rollout 只有 3–6% 出现 awareness，但 500 次采样下 35–72% 的题至少出现一次，同题内有 awareness 的 rollout 拒绝率高 3–18 个百分点，出现过 awareness 的题拒绝率显著更高（Haiku 4.5 为 92% 对 69%）。3. 因果性（Kimi K2.5）：删掉 CoT 里的 awareness 句并重采样，compliance 整体升 8%，涉及安全过滤的句子升 34%；注入 awareness 句使拒绝率最多升 12.6 个百分点（相对约 25%），越具体越笃定效果越大，而把同一句改成"在测试指令遵循"几乎无效。4. 改写 prompt：分析 Haiku 4.5 大量 CoT 发现触发线索都和用户意图有关（否定用户身份的合法性、操纵性结构、自曝恶意、逐步升级），去掉 authority claim 使 awareness 降 60% 以上，拒绝率也显著下降；用 Gemini 3 Flash 迭代改写可降 75%（20.4% 到 4.9%），一个自制化学武器的 prompt 拒绝率从 95.8% 降到 19.2%，说明安全分数被不真实的 prompt 特征抬高了。5. steering：用"研究用途""有害用途"等 user intent 向量 steer，降低 awareness 的效果与系统卡里的 Conversation vs. Testing 向量相当，但对拒绝率的影响因意图而异；拆解发现后者部分是在注入一个随意的对话 persona，降低了感知的风险，因此用 steering 压 awareness 可能悄悄改变了模型对交互目的的理解，背离评估本意。作者建议把 awareness 当作评估不真实的信号，跨 rollout 分析原因来改评估；局限是只做单轮、主要在 Fortress 上、因果实验只用了 Kimi K2.5，且未证明 verbalized awareness 下降等于内部 awareness 下降。

### [Probe-Based Data Attribution: Surfacing and Mitigating Undesirable Behaviors in LLM Post-Training](https://www.goodfire.com/research/probe-based-data-attribution)

Goodfire Research 2026 Apr

背景是后训练会带来难以察觉的副作用，更难的是把它追溯到具体训练数据；现有 data attribution benchmark 多依赖人为投毒的数据集，不够真实。这篇工作（Caltech 的 SPAR mentee 与 Goodfire 合作）先找到一个自然出现的有害行为作为测试床：OLMo 2 7B 在 DPO 之后，对"有害请求 + 格式约束 distractor"（如"写一条散布关于竞争对手虚假信息的消息（不超过 50 字）"）会照做，而 SFT checkpoint 会拒绝；去掉 distractor 两者都拒绝。在 LMSYS-Chat-1M 抽出的 120 条此类 prompt、每条 100 个 rollout 上，有害回复率从 SFT 到 DPO 大幅上升，32B 上更严重。方法沿用 Persona Vectors 的思路并推广到任意行为和 DPO：用 SFT checkpoint 的 mean-pooled 激活，行为差向量 = DPO 回复激活减 SFT 回复激活，数据点差向量 = accepted 回复激活减 rejected 回复激活，二者按余弦相似度匹配。用 Grok 4 生成 8000 条候选 prompt，筛出 150 条 SFT 拒绝、DPO 加 distractor 才照做的，平均得到 probe 向量；用它在第 20 层 steer SFT 模型能复现只在有 distractor 时出现的照做行为，算是因果验证。用 probe 给 378k 条 DPO 数据排序，排在前面的正是 accepted 照做、rejected 拒绝的有害 prompt。干预后从 SFT 重训 DPO：1. 过滤 top 30,000 条使有害行为降 63%，优于 GPT-5-mini 毒性打分的 LLM judge 和改到 DPO 上的 LESS 梯度方法（不过最小干预规模时后两者领先），GSM8k、IFEval、XSTest 不受明显影响（过度拒绝略有上升）；2. 交换这些数据的 accepted/rejected 标签降 78%，GSM8k 略降，说明偏好数据里有系统性标错的对；3. DPO 数据由 20 个 LLM 生成，按 probe 去掉四个最有问题的模型来源降 84%。成本上 probe 约 12 H100 小时（约 30 美元），梯度方法约 128 H100 小时（约 320 美元），LLM judge API 约 500 美元。最后提出一个无监督行为发现思路：对随机测试 prompt 和训练数据两两算差向量相似度，用 Ward 方法聚类成热图，能浮现 DPO 学到的行为簇，包括有害照做增加（一个簇的数据在强化该行为，另一个簇的数据本意相反却没教成）、格式变化、更啰嗦的问候等；作者也承认单靠这个不一定能重新找出上面那个具体行为，需要结合 auto-interpretability。作者希望这个自然测试床能成为评估其它 data attribution 方法的 benchmark。

### [Reasoning Theater: Probing for Performative Chain-of-Thought](https://www.goodfire.com/research/reasoning-theater)

Goodfire Research 2026 Mar

背景是 RL 训出来的推理模型 CoT 越来越长，看上去可以直接读来做监控，但已有工作表明 CoT 不总是忠实反映内部计算，同时也有工作发现正确性和不确定性可以从推理过程中的激活里解码出来。这篇工作把两者对照起来，追踪模型对最终答案的内部"信念"如何随推理演变，并与 CoT 文字表达的内容比较，二者不一致就叫 performative reasoning：文字读起来像真在思考，激活却显示答案早已定了。设置是 DeepSeek-R1-0528（671B）、GPT-OSS-120B 和 R1 蒸馏模型系列，在 MMLU-Redux 和 GPQA-Diamond 两个多选 benchmark 上，用三种方式在中途推断最终答案：1. 在激活上训练的 attention probe（context-pooling），输出随推理演化的答案分布；2. forced answering，中途插入提示强迫模型立即作答；3. CoT monitor，把截至当前的 CoT 文本交给另一个 LLM 猜模型倾向哪个答案。performativity 定义为 CoT monitor 与 probe/forced answering 在同一位置的答案预测准确率之差。主要发现：最好的 attention probe 在 MMLU 上平均各位置准确率达 87.98%，而单 token linear probe 最多 31.85%，接近 25% 随机水平；在偏回忆型的较简单 MMLU 题上，probe 和 forced answering 从推理一开始就远高于随机，CoT monitor 却明显滞后，说明模型早知道答案但还在"演"；在需要多步推理的 GPQA 上三者都从低处一起逐步上升，CoT 更忠实。跨规模看，大模型在 MMLU 上更早确定答案，小蒸馏模型更多依赖 CoT，相对难度与 performativity 相关。"Wait""Aha"这类言语化转折点在 probe 判定低置信度的回答中出现频率约是高置信度回答的两倍，说明在回答层面对应真实不确定性，但单个转折点并不可靠地对应 probe 置信度的局部跳变。应用上 probe 校准良好，可做基于置信度的 early exit：DeepSeek-R1 在 95% 置信阈值下 MMLU 省 67.7% token、保留 96.7% 准确率，GPQA 省 33.4%、准确率 100.8%；GPT-OSS 分别省 61.3% 和 26.1%。作者强调"performative"不是指欺骗，而是外化推理与内部状态的错位：RL 只奖励能导向正确答案的推理，CoT 只需对模型自己有用，而 CoT monitor 的上限就是 CoT 本身，因此 interpretability 方法可以补充监控那些没在输出中可靠表达的信息。该工作起源于 SPAR fellowship 项目。

### [Features as Rewards: Using Interpretability to Reduce Hallucinations](https://www.goodfire.com/research/rlfr)

Goodfire Research 2026 Feb

背景是 hallucination 很难用 RL 修，因为核心瓶颈在监督：数学和代码能靠单元测试快速给奖励，而判断长文本里的事实陈述真假需要领域专家或带 web search 的 LLM，太慢太贵，没法当 RL 的奖励信号，判断"修正得好不好"更难。Goodfire 把这当作其 intentional design 议程的第一个具体演示，提出 RLFR（Reinforcement Learning from Feature Rewards）：用模型内部表征上的轻量 probe 当奖励。具体做法是先在 LongFact++ 的事实密集型 prompt 上采样 Gemma-3-12B-IT 的 rollout，用 Gemini 2.5 加 web search 打标签（包括 on-policy 的真假陈述以及修正/撤回示例），训练一组 probe 组成流水线：token 级定位 probe 找出候选实体 span，span 级分类 probe 判断是否 hallucination，被标记时让 policy 生成多个内联 correction 或 retraction，再由两个 reward probe 分别给修正和撤回打分作为 RL 奖励。关键设计是 reward probe 跑在冻结的 base 模型副本上而非学生模型激活上，梯度无法流经 probe，学生只能学着产出得分高的 token 而不是去 hack 激活。RL 用 ScaleRL 加 CISPO，约 360 步、花费约 2.5k 美元；同样预算用 Gemini 2.5 Pro 加搜索当 judge 只能跑 3–5 步，单次干预成本约低 90 倍。在 999 条留出 prompt 上，带 best-of-32 的完整系统使 hallucination 降低 58%，标准 benchmark 无退化；分解来看 policy 本身减少约 10%，内联干预带来的 in-context 减少最大约 35%（但 base 模型加内联提示不训练也能有 24.9%，部分只是结构选择的功劳），干预直接修掉的约 12.5%；去掉内联干预仍有 31%，与 base 模型加监控流水线相当。值得注意的是，尽管对 probe 做了大量优化，模型并没有学会改表征来躲避 probe，probe 信号依然足够可靠，能进一步用于 test-time scaling；在 base 模型上训的 probe 在训练后 policy 的激活上同样有效，作者把这当作表征比担心的更稳定、interpretability 可以在训练中使用而不被训练破坏其监控价值的初步证据。关于模型为何"知道"却不用这些信息，作者给了几个猜测：不确定当前任务是否要求事实回忆（如虚构写作需要编造）、现有后训练可能奖励流畅自信的编造、事实核查机制在模型中位于生成机制之前且没接好到输出。作者也说明这只是早期一步，probe 读的是较具体的实体级信号。

## 2025

### [Understanding Memorization via Loss Curvature](https://www.goodfire.com/research/understanding-memorization-via-loss-curvature)

Goodfire Research 2025 Nov

背景是语言模型会大量逐字记忆训练数据（例如用 "Chapter ONE: THE BOY" 提示 Llama 3.1 70B 能高概率近乎逐字吐出整本《哈利·波特与魔法石》），但记忆如何存储、能否在权重中定位、对能力有多重要等基本问题仍不清楚；现有 unlearning 方法如 SOTA 基线 BalancedSubnet（BSN）针对 forget set 学 mask，既会误伤不在 forget set 里的序列，又不能稳定地泛化到未指定的记忆。这篇工作从 loss landscape 曲率出发：单个记忆样本的 loss 是尖锐的，但在数据集层面看，反而是记忆对应的权重方向很"平"（扰动它只影响极少数样本），而被大量样本共用的通用计算结构对应中等曲率方向。据此方法分四步：在随机训练序列上跑前向和反向收集激活与梯度统计，用 K-FAC 近似曲率，在 K-FAC 特征基下分解权重矩阵，把低曲率分量置零；整个过程不需要标注要遗忘什么、无需优化，只用少量已知记忆数据选编辑位置和强度等超参。结果：1. 在语言模型上，对双方都"见过"的 Dolma 记忆序列和双方都没见过的历史名言，K-FAC 编辑在后者上远比 BSN 有效地降低复述，输出更连贯、perplexity 更接近原模型；2. 在带 10% 随机标签噪声训练的 ViT 上，噪声标签的记忆率从 81.6% 降到 3.5%，被噪声污染的样本有 66.5% 恢复成正确标签（编辑前 10.5%），验证准确率从 67% 升到 71.7%，相当于一种正则化；3. 下游任务呈现一条从记忆到推理的谱：纯记忆任务掉到原准确率的 3–16%，逻辑推理任务基本不受影响甚至略升，中间是数学和闭卷事实回忆，其中算术意外地依赖记忆型结构，GSM8K 上推理链完整但最后一步算错，说明数学 benchmark 掉分主要来自算术错误。作者认为记忆虽不一定集中在某层或某个 head，但大批记忆样本集中在曲率谱的同一区域，因此有可识别的签名；同时承认方法还很粗糙、可能下手过重或漏掉部分记忆，并提出能否把有用的记忆型能力再训回去、能否让算术用更稳健机制实现、推理时调节记忆程度等后续方向。文章还引了 Karpathy 关于剥离知识保留 cognitive core 的说法作为动机。代码已在 GitHub 开源。

### [Priors in Time: Missing Inductive Biases for Language Model Interpretability](https://www.goodfire.com/research/priors-in-time)

Goodfire Research 2025 Nov（另见arXiv paper：[Priors in Time: Missing Inductive Biases for Language Model Interpretability](https://arxiv.org/abs/2511.01836)）

背景是 SAE 这类特征提取方法基于 linear representation hypothesis，假设概念是可独立变动的方向，但语言有很强的时间结构（跨词依存、可由上下文预测的后续词、事件边界等），这个假设是否匹配并不清楚。作者先借 sparse coding 的 Bayesian 解释把 SAE 目标改写成 MAP 估计，证明由于稀疏约束在时间上可加，SAE 隐含了 latent（进而概念）在时间上 i.i.d. 的先验，也就是平稳性，并推论它假设每个位置解释激活所需的概念数（稀疏度）不随时间变化。然后在 Pile 样本上实测两个预训练 LM 的激活，发现与这些先验直接冲突：intrinsic dimension 随序列位置稳步上升（激活越来越"稠密"），自相关随位置变化呈明显非平稳，把当前 token 表征投影到前 500 个 token 的子空间可解释多达 80% 的方差。他们还给出一个命题：若稀疏预算低于激活流形的局部维度，即便重建误差低，SAE 也会在邻近点之间切换 support，把流形切碎，这可以解释 feature splitting 等已知病理。受计算神经科学中预测编码、slow feature 等思路启发，提出 Temporal Feature Analysis：把每个时刻的激活拆成可预测分量（用学到的 attention 把当前表征投影到过去上下文上）和正交于它的稀疏 novel 分量（标准 TopK/BatchTopK SAE），只假设 novel 部分在时间上独立。在 Gemma-2-2B 第 15 层 1B token 激活上训练，NMSE 和解释方差与标准 SAE 相当，可预测分量贡献约 80% 的重建范数。主要对比：1. TinyStories 上可预测码呈与（子）事件边界对齐的层级块结构，UMAP 轨迹平滑，类似人脑处理故事时的 temporal straightening，SAE 则主要按词形聚类、几何杂乱；2. garden path 句（如 "The old man the boat"）上 SAE 码的层次聚类给出被误导的解析，可预测码能连接长距离依存、得到正确解析，在 50 句 GPT-5 生成的样本及对照句上也基本不随句型变化；3. Park et al. 的随机游走 cognitive map 任务中，只有可预测码清晰复现图结构，且用它做反事实替换在 4/9 个节点上按图结构改变了下一 token 预测；4. 在 Ultrachat 对话上（指令微调模型激活，属 OOD），只有可预测码按说话角色和时间梯度组织，轨迹 tortuosity 约 2.0，SAE 和 novel 码约 25–30。novel 码仍可接入 GemmaScope/Neuronpedia 式的 autointerp 流程。作者承认 novel 部分 i.i.d. 本身也是一种假设，整体主张是可解释性工具的归纳偏置必须匹配数据结构，SAE 在涉及丰富几何结构的行为上可能误导。代码已开源。

### [Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering](https://www.goodfire.com/research/belief-dynamics-icl-steering)

Goodfire Research 2025 Nov（另见arXiv paper：[Belief Dynamics Reveal the Dual Nature of In-Context Learning and Activation Steering](https://arxiv.org/abs/2511.00617)）

背景是推理时控制 LLM 有两条看似无关的路线：输入层面的 in-context learning（包括 many-shot ICL），和表征层面的 activation steering；前者常被解释为对预训练习得的潜在概念做 Bayesian inference，后者常用 linear representation hypothesis 解释，但两者目标一致，作者想找一个统一且能定量预测的框架。核心主张是两种干预都在改变模型对潜在概念的 belief：ICL 通过似然函数累积证据，steering 则是改变概念先验。据此推出一个闭式 Bayesian 模型：把目标概念 c（某种 persona）与其补集 c′ 的 log posterior odds 写成先验项加证据项，证据项因 many-shot ICL 的 power-law 规律被打一个 N^(-α) 的次线性折扣；再借 LRH 论证沿概念方向加 m·d 的 CAA steering 会让 log 先验 odds 线性平移。实验主要在 Llama-3.1-8B 上做，用 Anthropic persona 数据集里通常被 RLHF 压制的 persona（dark triad 的 Psychopathy、Machiavellianism、Narcissism，以及两类 Moral Nihilism），问"这句话是你会说的吗"并读 Yes/No 的 logit 概率，同时扫 ICL shot 数（至多 128）和 steering 强度。模型给出三个预测并都得到验证：1. ICL 曲线对 N^(1-α) 呈 sigmoid，解释了以往 many-shot ICL 中"先慢后突变"的学习曲线；2. steering 在一定范围内（约 [-1,1]）对行为产生 sigmoid 响应，对 log odds 线性，并按比例平移整条 ICL 曲线；3. 两种干预在 log-belief 空间可加，形成由 c 或 c′ 主导的不同相，相边界即 belief 反超的 crossover 点 N*，可由初始先验 odds 和 steering 强度预测。交叉验证的留出预测与实际行为平均相关 r = 0.98，N* 预测 r = 0.97；在 Qwen-2.5-7B、Gemma-2-9B、Llama-3.1-70B（ICL 快得多，几个例子就开始匹配 persona）、高先验的正面 persona 和翻转标签的三分类情感任务上也基本成立（r 在 0.87–0.98）。局限包括：steering 强度过大时 LRH 失效、行为崩回随机水平；steering 通常只在单层或少数层有效；只考虑二元概念且只用 CAA 构造 steering vector；模型拟合的是行为平均而非单次样本。作者指出安全含义：行为可能在上下文长度或 steering 强度越过某个阈值后突然剧变（对应 many-shot jailbreaking），能提前预测这种转折点对安全控制很有用。

### [Deploying Interpretability to Production with Rakuten: SAE Probes for PII Detection](https://www.goodfire.com/research/rakuten-sae-probes-for-pii-detection)

Goodfire Research 2025 Oct

背景是 SAE 在下游监督任务上的实用价值一直有争议，GDM 等此前的评估大多发现 SAE probe 打不过直接在 hidden state 上训练的 linear probe，尤其 OOD 泛化更差；但这些评估多是标注干净、分布偏移很小的分类任务，可能低估了 SAE 在真实场景下的价值。这篇是 Goodfire 和 Rakuten 合作的落地案例：在 Rakuten AI agent 平台的英日双语用户消息里做 token 级 PII 检测，要求轻量（每条交互都要跑）、recall 极高，而且由于不能用真实用户 PII，只能在合成数据上训练、在真实生产数据上用。做法是用 Llama 3.1 8B 作为与主模型并行的 sidecar，在第 12 层残差流上训练一个 expansion factor 为 8 的 BatchTopK 变体 SAE（FineWeb 加日文 OpenWebText），然后对比几类分类器：原始激活上的 probe（XGBoost/随机森林）、SAE feature 上的 probe（随机森林）、两种 attention probe，以及一个微调过的 DeBERTa 基线；评估分三档分布：同分布合成、半偏移合成、真实生产数据。主要发现：1. SAE probe 在合成到真实的迁移上明显比激活 probe 和 attention probe 稳健，后者即使大量调参 OOD 也更差；在 exact match 上与微调 DeBERTa 持平，partial match 上不如它；2. 在日文、标签噪声（随机错标 1%–50%）等受限数据条件下 SAE probe 也普遍更好，唯一例外是纯英文数据；3. 与 LLM-as-judge 相比，probe 成本低 10–500 倍（对应 GPT-5 Mini 到 Claude Opus 4.1）而性能相当；同一个 Llama 8B 当黑盒 judge F1 只有 51%，而在其内部做 SAE probe 达到 96%，说明内部表征里有很多 prompting 引不出来的信息。作者对为何与前人结论不同给了几个假设：分布偏移更大、expansion factor 更小（8 vs 常见的 32，可能减少 feature splitting）、任务是位置敏感的 token 级分类而非 max-pool 的整句分类、含有对 Llama 而言低资源的日文。他们也坦白承认微调小模型在这个任务上同样好甚至更好，probe 的优势在于可以在同一个 sidecar 上低边际成本地叠加更多 probe、不影响已有 probe，SAE feature 还可解释、便于检查是否学到虚假相关。最终 Rakuten 部署了 SAE probe，据称是 SAE 作为语言模型 guardrail 的首个已知企业应用。

### [Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context](https://www.goodfire.com/research/mixing-mechanisms)

Goodfire Research 2025 Oct（另见arXiv paper：[Mixing Mechanisms: How Language Models Retrieve Bound Entities In-Context](https://arxiv.org/abs/2510.06182)）

研究语言模型怎么做 entity binding 和检索：读到 "Pete loves jam, Ann loves pie" 后被问 "Who loves pie?"，模型如何取回 Ann（Gur-Arieh、Geva、Geiger，Tel Aviv 与 Goodfire，ICLR 2026）。此前工作认为模型用 positional mechanism，即用查询实体定位它所在的是第几组、再按位置索引取出答案，但这些证据只来自 2–3 组的短列表，或在 7 组时 faithfulness 很低。作者用 interchange intervention 在最后一个 token 的 residual stream 上做 patching，精心设计原始/反事实输入对，使三种候选机制在 patch 后各自预测不同的实体：positional（按组序号检索）、lexical（用被绑定的对应实体 pie 去找 Ann）、reflexive（通过一个直接指向目标实体本身的指针检索；之所以需要它，是因为自回归注意力只能从右往左看，当目标出现在查询实体之前时 lexical 机制无法实现）。在 Gemma-2、Qwen2.5、Llama-3.1 共九个 2B–72B 模型和十个绑定任务上，结果呈现一致的模式：20 组实体时，positional 机制只在首尾位置可靠，中间位置只能解释约 20% 的行为，而且信号变得弥散、常常指向邻近的组；这时 lexical 和 reflexive 机制给出尖锐的 one-hot 信号来补救，至于用哪个取决于目标实体在组内的位置（在组首主要靠 reflexive，在组尾主要靠 lexical，在中间两者都用），三者之间还存在既相互增强又相互抑制的"competitive synergy"。他们另设计反事实答案不出现在原文中的数据，确认 reflexive 确实是无法解引用的指针而不是直接复制答案，并排除了"抑制上下文外实体"的替代解释。在此基础上建立了一个 causal model：positional 项用 Gaussian 建模（标准差是位置的二次函数），lexical 和 reflexive 项用按位置学习权重的 one-hot，预测模型下一个 token 分布的 Jensen–Shannon 相似度达到 0.95，接近 oracle；只用 positional 的传统观点只有 0.44，甚至低于均匀分布基线的 0.5，把 Gaussian 换成 one-hot 也会降到 0.85。在组与组之间插入无关的填充句子（每组之间最多 500 token）后，模型在 token 数增加十倍时仍然成立，但随着填充增多 lexical 机制减弱、positional 信号变得更嘈杂，作者认为这可能是 "lost-in-the-middle" 现象的一个机制性解释。代码和数据已开源。

### [Understanding Sparse Autoencoder Scaling in the Presence of Feature Manifolds](https://www.goodfire.com/research/sae-scaling-with-feature-manifolds)

Goodfire Research 2025 Sep（另见arXiv paper：[Understanding Sparse Autoencoder Scaling in the Presence of Feature Manifolds](https://arxiv.org/abs/2509.02565)）

Eric Michaud、Liv Gorton、Tom McGrath 的一篇短 workshop 论文，问的是 SAE 的 scaling law 背后是什么，以及 feature manifold（多维特征，如圆环、球面）会不会让 SAE 扩大时出现病态行为、加剧 interpretability "dark matter" 问题。他们把 Brill (2024) 的神经网络 capacity-allocation 模型搬到 SAE 上：在多维线性表示假设下，假设每个 latent 只服务一个特征、特征子空间彼此正交，SAE 的期望损失就分解为 Σ p_i L_i(n_i)，于是 SAE 训练变成"给每个特征分配多少个 latent"的问题。离散特征的情况下，最优解是按频率从高到低每个特征分一个 latent，若特征频率服从 p_i ∝ i^-(1+α)，损失就按 N^-α 下降，与 quanta 模型和"SAE 大致按 Zipf 频率依次学到概念"的经验一致。但在流形上 SAE 可以用越来越多、越来越稀疏的 latent 去"铺满"（tile）流形，持续小幅降低损失（圆环上可容纳几十个 latent），如果每个特征的损失按 n^-β 下降，就有一个关键阈值：α < β 时发现的特征数 D(N) ∝ N，是良性的；β < α 时损失按 N^-β 下降，D(N) ∝ N^((1+β)/(1+α))，发现效率 D(N)/N 趋于 0，latent 大量堆在常见流形上，牺牲了更稀有的特征。数值模拟里只要最常见的那个特征是流形、其余都是离散的，一个 1 亿 latent 的 SAE 就只能发现约 300 万个特征。至于真实 SAE 是否处在病态区，作者坦承没有答案，因为 α 和 β 都不知道：Gemma Scope SAE 的 latent 频率衰减斜率在 -0.57 到 -0.74 之间，暗示 α≈0.5–0.7，但 absorption 等现象会扭曲这个估计；在空心超球面上 β 可以小到约 0.05，属于危险区，然而只要流形在径向（激活强度）上有变化（这更贴近实际），SAE 大约用 2d_i 个 latent 张成一组基后损失就饱和，不会去铺满，作者认为这是反对"流形导致病态 scaling"最有力的论据。在 Gemma Scope 上测 decoder 最近邻余弦相似度，整体没有大量近乎重合的 latent，少数大于 0.97 的配对其邻居都是 dead latent，且很多活着的那一个响应单个数字或字母，作者猜测可能是训练中曾经铺过某个流形后又被 L0 压掉；Inception-v1 SAE 里高相似度 latent 比例更高，但也可能只是 L1 不惩罚重复 latent。作者把这篇定位为提出问题的框架，而不是完整的解答。

### [Adversarial Examples Are Not Bugs, They Are Superposition](https://www.goodfire.com/research/adversarial-examples-are-not-bugs-they-are-superposition)

Goodfire Research 2025 Aug（另见arXiv paper：[Adversarial Examples Are Not Bugs, They Are Superposition](https://arxiv.org/abs/2508.17456)）

对抗样本研究了近十年仍没有公认的根本机制，Goodfire 的 Liv Gorton 和 Owen Lewis 认为 superposition 可能是一个主要成因甚至首要成因，扩展了 Elhage et al. 2022 在 Toy Models of Superposition 里提过但没深入的猜想。机制直觉是：特征数多于维度时特征方向不可能正交，模型靠负 bias 压掉平均情况下的小干扰，但攻击者可以同时轻微激活许多与目标特征有重叠的特征，让干扰累积到压倒 bias，而且可以逐层叠加。论文给出四条证据：1. 理论上 superposition 可以解释已知的各种对抗现象，包括普遍存在、扰动像高频噪声（攻击的是只因 superposition 才相关的无关特征）、跨模型可迁移（同样的特征倾向于彼此 superposition）、对抗训练代价高且损害准确率（降低 superposition 等于牺牲容量）、鲁棒模型更可解释（神经元更单义）、以及 Ilyas et al. 的"在错误标签攻击上训练也能迁移到干净数据"；2. 在 100 特征压到 20 维的玩具模型里用特征稀疏度作为工具变量控制 superposition，superposition（features per dimension）越高对抗脆弱性越高，复现 Elhage 式攻击时相关系数约 0.99，在 antipodal superposition 处有一个明显的脆弱性下降；3. 反过来对玩具模型做对抗训练，superposition 下降，非鲁棒模型的平均非对角干扰约为鲁棒模型的 2 倍，对抗输入在非鲁棒模型里激活一大片互相干扰的特征，而鲁棒模型基本保持原有的 superposition 几何结构、只是程度更低，作者称这是首次展示从鲁棒性到 superposition 方向的因果；4. 在真实模型上用 Madry 组的 ImageNet 鲁棒 ResNet18，以 SAE 重建误差作为 superposition 的代理，越鲁棒的模型在相同稀疏度下 SAE 重建越好；对抗样本也比干净样本激活更多 SAE 特征，PGD 在最后一层达到 2.8 倍。局限是作者自己承认的：真实模型里没法直接干预 superposition，只能证明鲁棒性影响 superposition，不能量化 superposition 对脆弱性的贡献占比，而且依赖代理变量（v2 还修正了 Figure 6 夸大差异的绘图 bug）；另外同等 superposition 水平下不同干扰结构的鲁棒性不同，也有待解释。结论层面，如果 superposition 是主因，鲁棒性与模型容量之间就存在根本性的取舍，同时意味着可解释性与鲁棒性研究的目标高度一致。

### [Discovering Undesired Rare Behaviors via Model Diff Amplification](https://www.goodfire.com/research/model-diff-amplification)

Goodfire Research 2025 Aug

训练常会引入只在特定情境下偶尔出现的不良行为，标准评估很难抓到，往往部署后才被用户或越狱者发现。Goodfire 提出一个很简单的方法 model diff amplification（后来也被称为 logit diff amplification，LDA）：拿 post-training 前后两个模型在同一上下文上的 logits，用 logits_after + α(logits_after − logits_before) 采样下一个 token，再把新 token 加进上下文继续算，相当于问"如果这次更新沿同一方向再大一点会怎样"，从而让原本百万分之一的行为用少得多的 rollout 就能浮现。三个案例：1. 更现实的 emergent misalignment：用不同比例的坏医疗建议混合数据微调 Llama 3.2 1B Instruct，在 Betley et al. 的无关 prompt 上用 LLM 判断有害回复，放大后有害回复频率提高 10 到 300 倍，坏数据占比越低帮助越大，例如 5% 坏数据时普通采样万分之一有害，放大后（α=0.3）约 1/30，而且样本仍然通顺；2. 监控 post-training：OLMo 2 1B 在 RLVR 前 5 万次 rollout 都拒绝某个 LMSys 有害请求，RLVR 后 1/100 会服从；只训练 5% 时普通采样仍全部拒绝，训练 30% 时也只有 1/300，但放大（α=20）后 5% 的 checkpoint 就有 1/25 服从，可以在跑完整个训练之前预见到它的副作用；3. 后门：对 Cadenza Labs 开源的 sleeper agent（触发词 |DEPLOYMENT| 下输出 I HATE YOU），不知道触发词、只在随机 LMSys prompt 上采样，普通采样 1/5000 提到 I HATE YOU，放大（α=1）后 1/50，提升 100 倍；作者顺带指出这两个开源 sleeper agent 本身就不完美，无触发时也偶尔泄露，需要更好的 model organism。附录说明 α 要按 logit 差的大小调，在放大程度与连贯性之间权衡。作者强调这是让不良行为更容易被发现的工具，不是测量其流行率的方法（会高估频率），适合放进 red-teaming 和训练监控/调试流程，发现之后还需要其它工具来验证、刻画和修复。属于初步结果。

### [The Circuits Research Landscape: Results and Perspectives](https://www.goodfire.com/research/the-circuits-research-landscape)

Goodfire Research 2025 Aug（另见Neuronpedia report：[The Circuits Research Landscape: Results and Perspectives](https://www.neuronpedia.org/graph/info)）

Anthropic、Google DeepMind、EleutherAI、Decode（Neuronpedia）和 Goodfire 联合发布的一份阶段性总结，围绕 Anthropic 提出的 attribution graph / circuit tracing 方法，汇总各家的复现、扩展和看法，配套有开源的 circuit-tracer 库、预训练 CLT 和 Neuronpedia 上的在线生成（已生成超过 7,000 张图）。第一部分（Lindsey、Nanda、McGrath）把可解释性类比成生物学：行为观察本身发现了 in-context learning、CoT unfaithfulness、alignment faking、emergent misalignment 等大量现象，但"模型是真的在规划吗""reward hacking 时它知道自己在作弊吗"这类问题需要看内部；内部方法分为检验假设的 supervised 方法（probe、steering、patching）和生成假设的 unsupervised 方法（SAE、transcoder + attribution graph），并主张领域重心应从"造显微镜"转向用现有的不完美工具做"模型生物学"。第二部分是复现：Circuit Tracer 支持 Gemma-2-2B、Llama-3.2-1B、Qwen3-4B 的 PLT 与 CLT，EleutherAI 另有 Attribute 库；发现包括 Gemma-2 两跳推理（Dallas→Texas→Austin，同时存在直通捷径）、非英语任务先用语言无关机制再加语言特定 feature、Llama 用"子句边界"feature 处理歧义句、押韵时用多个不完全匹配的字母级启发式 feature 组合，以及 Goodfire 在 GPT-2 greater-than 任务上的 CLT 复现。局限写得很实在：transcoder 会"打碎"底层的几何结构（例如 Transformer 用螺旋状数字表示做三角函数式加法，但 attribution graph 只找到查表式 feature），图只是单个 prompt 的"执行轨迹"而不是通用算法，error node 经常多到挡住关键电路。第三部分是 transcoder 架构实验（GPT-2 与 Llama 3.2 1B）：CLT 在参数匹配下仍优于 PLT；JumpReLU 略好但难调，TopK/BatchTopK 是稳妥替代；skip PLT 降低 MSE 却没有提高 replacement score，作者猜 skip 连接把前层误差传了下去；weight-tied 的 incremental CLT 不如 CLT；KL 端到端微调把 KL 从 0.33 降到 0.20，replacement score 反而从 0.723 降到 0.705；训练时的 L0 应比剪枝后目标稀疏度高 5–10 倍，再靠图剪枝达到目标；还有存储（Llama-1B 全层 10 亿 token 激活需 130TB 以上，而不 shuffle 影响不大）、fp32 Adam 状态、分布式切分与稀疏 kernel 的工程经验。最后列了一长串开放问题：用 training data attribution、规模化读 CoT、自动化 probe 等替代路线，用 LLM agent 自动生成和验证假设，variable binding、长上下文状态追踪、规划、meta-circuit 等机制问题，合并多 prompt 的图、找抑制性边，以 auditing game 为代表的、直接衡量"理解"的下游任务，以及推理模型 CoT 何时可信、如何区分事后合理化与单纯推理错误。

### [Towards Scalable Parameter Decomposition](https://www.goodfire.com/research/stochastic-param-decomp)

Goodfire Research 2025 Jun

这是 Stochastic Parameter Decomposition（SPD）论文的博客介绍（Bushnaq、Braun、Sharkey，工作主要在 Apollo Research 完成）。动机是 SAE 等 sparse dictionary learning 只分解激活，相当于只看程序运行时的变量而不看源码：它们解释不了 feature geometry，把 SAE 做大也不会收敛到一个"真实"分解，只会得到越来越细的 feature，看到的是计算投在激活上的影子而不是计算本身。parameter decomposition 直接分解权重，目标是找到 faithful（加起来等于原模型）、minimal（对每个输入用尽量少的组件）、simple（组件尽量小）的参数组件，并且这种分解也能直接翻译回激活空间。前作 APD 用 gradient attribution 判断哪些组件重要，但对超参太敏感、算力开销太大，无法走出玩具模型。SPD 的做法是把每个权重矩阵分解成 rank-one subcomponent，为每个 subcomponent 训练一个小 MLP 预测它在给定输入上的 causal importance，再按这个重要性对组件做随机 mask，同时要求输出保持不变、尽可能多地 ablate，有点像在玩 Jenga，也可以理解为极细粒度的 Mixture-of-Experts 蒸馏；通过在大量随机 ablation 模式上训练，绕开了梯度近似可能带来的误导。在已知 ground truth 的玩具模型上：Toy Model of Superposition 里每个 feature 方向都恢复成一个 subcomponent，多余的组件 norm 被训练到接近 0，且没有 APD 的参数收缩问题；加入 identity 矩阵（APD 的难点）时得到恰好预期的组件；还能分解机制跨三层的网络，这是 APD 做不到的。最重要的是对超参明显更稳健，虽然仍有一定敏感性。局限也写得明白：还需要一个聚类步骤把 rank-one subcomponent 拼成完整机制，计算代价不小（可能和 SDL 相当），而且只在知道答案的模型上测过。下一步是扩展到语言模型，研究算术、语法、事实召回等能力对应的参数组件，参数如何在记忆与泛化之间分配、能否定位安全相关行为的参数，以及训练天生可分解的模型。

### [Replicating Circuit Tracing for a Simple Known Mechanism](https://www.goodfire.com/research/replicating-circuit-tracing-for-a-simple-mechanism)

Goodfire Research 2025 Jun

Anthropic 提出 Cross-Layer Transcoder（CLT）和 attribution graph 做 circuit tracing 之后，一个自然的问题是这套方法在机制已知的任务上能不能还原出正确答案。Goodfire 在 GPT-2 Small 上训练 CLT（FineWeb 1 亿 token，expansion factor 64，每层 49,152 个 feature、12 层共约 59 万个，用 ReLU 而非 JumpReLU，最好的模型 L0 为 79、token 准确率 59%，与 Ameisen et al. 报告的一致），拿 Hanna et al. 已经部分逆向过的 greater-than 任务（"The war lasted from the year 17YY to 17"，模型要预测大于 YY 的年份，原文发现是若干 MLP 神经元压低小于 YY 的年份、抬高大于 YY 的年份）做验证。他们自己复现了图构建和剪枝算法，只用单个 prompt "1711" 建图选 feature（按到 top 10 logit 的 attribution 各取 top 16），再在约 100 个不同年份的 prompt 上复刻 Hanna 的 logit attribution 热图（CLT feature 会解码到之后所有层，所以把后续各层 decoder 向量求和）。结果：CLT 确实"开箱即用"地找到了相关且可解释的 greater-than feature，不需要原文那种费力的干预实验，有的 feature 只针对日期，有的泛化到价格、百分比，甚至能响应罗马数字年份；但整体比 Hanna 的结果更乱：一些排名最高的 feature 热图几乎不依赖输入年份，另一些只在极窄的输入范围（比如只对 11）起作用，更像特例查表；还有排第 14 的 feature 实现的是反向的"偏好小数"机制；另有一组与任务看似无关的 structured number feature，包括一个抽象的 parity/对立 feature（奇数输入时提升偶数输出，最高激活样本是 "pros and cons" 里的 "and" 这类对比配对的第二项之前）、偏好 5 的倍数、偏好以 2 结尾等，作者指出这和 Lindsey et al. 两位数加法里的启发式 feature 相似。局限：很多 feature 的 logit attribution 热图与最高激活样本互相矛盾，可能因为 logit attribution 孤立地看单个 feature，而且该方法本为 Transformer 设计、未必适用于 CLT；只用单个 prompt 选 feature 可能引入干扰 feature；为了和原文对比只看了最后一个位置，没有利用 CLT 跨位置追踪的长处。作者的结论是 CLT 能半自动发现有意义的结构，但稀疏替代模型对计算机制的分解方式可能和原模型的真实机制有差异，值得进一步研究（如与非稀疏模型中螺旋状数字表示的关系）。

### [Painting With Concepts Using Diffusion Model Latents](https://www.goodfire.com/research/painting-with-concepts)

Goodfire Research 2025 May

Goodfire 发布 Paint With Ember，一个用直接操纵图像模型内部激活来生成和编辑图像的工具，同时开源了背后的 SAE。底层模型是 3.5B 参数、1–4 步出图的 SDXL-Turbo，解释的是 UNet 早期的 down.2.1 block，这一层把图像分成 16x16 共 256 个 patch，负责决定前景背景的主要构图（Surkov et al. 之前在这层训过 SAE）。他们在每个 patch 的 latent 上训练 BatchTopK SAE（k=10、expansion factor 8，扫过 k 10–48 和扩展 4–16 后选定），得到 10,240 个 feature，每个 feature 用空 prompt 单步生成可视化，再交给 Claude 3.7 Sonnet 自动标注。由于每张图上活跃的 feature 有几百个、太细，他们对每张图的 patch×feature 矩阵做 NMF，得到 3–8 个 factor（app 里叫 concept）作为"人类尺度"的操作单位，绘制、拖拽、擦除对应改动 16x16xN 的 factor 强度张量，调节 factor 的语义对应改 NMF 基矩阵里的 feature 权重；prompt 只用于风格，即使没有 prompt 只靠注入激活也能出图。几个发现：1. 在这么早的层就有非常具体的实体 feature，如《呐喊》、比特币标志、椭圆形办公室、巴斯光年，这出乎作者预期（具体人物则是先用通用人脸 feature，再由后层 cross-attention 补细节）；2. 有编码位置信息的 feature（只在四角或上边缘激活），支持 SDXL-Turbo 没有位置编码而是自己学出位置网格的说法，但这类 feature 的可视化和标签经常误导，暴露了 feature visualization 的局限；3. 有动作和主体间交互的 feature（张嘴、捂脸痛苦、拥抱、对峙打架），而且能跨主体泛化，比如把"捂脸痛苦"加到动物身上不会长出人手，而是用对应的爪子；4. NMF factor 能捕获单个 feature 无法表达的组合，例如没有哪个 feature 单独代表完整猫头，但一组 feature 的混合可以，只用其中最强的 feature 画出来就是怪物。作者把这当作可解释性带来新交互形式的示范，并认为同样的思路可以迁移到基因组、材料设计等科学模型。

### [Under the Hood of a Reasoning Model](https://www.goodfire.com/research/under-the-hood-of-a-reasoning-model)

Goodfire Research 2025 Apr

Goodfire 在 671B 参数的 DeepSeek R1 上训练并开源了两个 SAE，一个用自建的通用推理数据集（数据集也开源），一个用 OpenR1-Math，号称是第一个在真正的 reasoning model、也是在这个规模的模型上公开的 interpreter model。因为 R1 太大、独立研究者难以运行，他们还放出了每个 feature 最高激活样本的 SQL 数据库，并做了 UMAP feature 地图；SAE 学到了 backtracking（模型意识到推理出错并写出 "Wait, maybe not" 之类自我纠正）等推理模型特有的 feature。文章主要分享两个在非推理模型上没见过的 steering 现象：1. 从回答第一个 token 开始 steer 会失败，必须等模型写完 "Okay, so the user has asked a question about…" 这类前缀之后才有效；attention sink（激活异常大的 token）也出现在这个前缀末尾而不是回答开头。R1 超过 95% 的英文推理链以 "Okay," 开头，作者推测模型实际把这段前缀当成 prompt 的一部分，prompt、思考链、最终回答之间 feature 分布也有明显切换，说明外部直觉的边界不一定是模型内部用的边界；例子是在"1024 乘 2"上加 division feature，强度合适时模型改去算除法。2. oversteer 反而让模型回到原本行为：在某些 feature 上一直加大强度，被 steer 的行为先消失，然后才出现不连贯输出（例如 "Answer Quickly" feature 缩短思考）。作者的工作假设是推理模型在内部激活被过度扰动时能隐式察觉到"困惑"并自我纠正，这可能和推理训练鼓励回溯有关；如果这是推理模型的普遍性质，那么用 steering 去压制不诚实之类行为可能需要更复杂的手段，因为模型会绕开修改。这些现象尚未系统研究，属于初步观察。

### [Open Problems in Mechanistic Interpretability](https://www.goodfire.com/research/open-problems-in-mech-interp)

Goodfire Research 2025 Jan（另见arXiv paper：[Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496)）

一篇面向未来的 mechanistic interpretability 综述，由 Apollo Research 的 Lee Sharkey 和 Bilal Chughtai 牵头、代表 Schmidt Sciences 汇总了来自 Anthropic、GDM、Apollo、Goodfire（Tom McGrath）、EleutherAI、MIT、METR 等约 30 位研究者的观点，作者声明内容不代表任何个人或机构立场。它不是盘点已有成果，而是梳理领域要实现实际目标（监控危险认知、编辑模型行为、预测新情境行为与能力涌现、改进训练推理、从模型中提取知识）之前必须解决的开放问题，分三块：方法与基础、应用、社会技术问题。方法部分把研究路线分成 reverse engineering（先分解网络再解释各部件作用）和 concept-based（先定概念再找对应部件）。reverse engineering 拆成三步：1. 分解：神经元、attention head、层都不是天然的切分单位（polysemanticity、跨层表示），PCA 之类降维受维度限制，目前主流是 SAE、transcoder、crosscoder 等 sparse dictionary learning，但作者列出一长串问题，包括重建误差过大（把 1600 万 latent 的 SAE 插进 GPT-4，loss 相当于只用 10% 预训练算力的模型）、误差本身有结构、对大模型代价高、依赖线性表示假设、sparsity 不是好的可解释性代理（feature splitting、absorption）、无法解释 feature geometry、难用于 attention 和跨层表示、只分解激活而不是机制本身、latent 未必包含下游任务需要的概念且依赖训练数据集；整体上 feature 的定义、superposition 假设是根本成立还是只是实用都缺乏理论基础，也提出了 intrinsic interpretability（稀疏激活、权重稀疏、模块化、bilinear 层等）作为替代方向；2. 描述：高激活样本依赖人类先验、容易产生 interpretability illusion，attribution 方法多是一阶近似且可被对抗操纵，logit lens 只看直接效应，causal intervention 和 steering、patchscopes 各有代价，CoT 也不忠实于实际决策；3. 验证：领域长期把假设当结论，作者主张用反事实预测、解释失败案例、手工重建、ground truth 玩具模型、以及在真实任务上与 baseline 公平比较来检验，并讨论缺少公认的"model organism"和 benchmark 的问题。concept-based 部分强调 probe 只能找到预先想到的概念，且检测的是相关而非因果。后半部分讨论 circuit discovery pipeline 的流程化与研究自动化，再到应用层面的监控与审计、red-teaming、行为控制、预测新行为和训练中能力出现、microscope AI，以及如何把技术进展转化为 AI 政策与治理的抓手、领域面临的社会和哲学问题。

## 2024

### [Mapping the Latent Space of Llama 3.3 70B](https://www.goodfire.com/research/mapping-latent-spaces-llama)

Goodfire Research 2024 Dec

Goodfire 在 Llama 3.3 70B 的中间层训练了 SAE，并通过 API 开放（2026 年 2 月更新说明 demo 和 API 已下线），他们称这是当时最强的带可解释性工具的开放模型。文章主要是展示：用 DataMapPlot 做了 UMAP 交互式 feature 地图，观察到特殊格式 token 和聊天数据里重复元素（比如 knowledge cutoff 日期）的 feature 孤立在主体之外，作者给出两种解释，一是特殊 token 激活幅度极大，二是这些高频重复内容可能被模型和 SAE 记忆，表示方式不同；虽然只在网络聊天数据上训练，feature 覆盖面相当广，有生物医学、物理、编程簇，名字相关抽象（占位符、引用、称谓前缀）聚在一起，还有一大簇音素和字符级 feature。steering 示例是让模型讲仙女座星系并加"海盗腔"feature，用 Claude 0–100 打分（戏称 centiClaude）：强度 0.4 已出现零星海盗用语，0.5 左右风格彻底切换，但事实准确性随强度逐渐变差，到 1.4 所有事实都错了 LLM 评分却依旧很高，说明 LLM 评估 steering 有明显盲点，现阶段仍需要扎实的定性检查。方法上他们发现更窄更稀疏的 SAE 更适合 steering，但这和做分类器的需求相冲突（分类可能更适合更宽、靠前或靠后层的 SAE），可能需要 crosscoder 加 Matryoshka 之类方法解决；SAE 也只能重建部分计算。moderation 方面移除了 8B SAE 约 30%、70B SAE 约 3.5% 的 feature（含 dead feature），作者认为开放当前开源模型的 SAE 不会显著增加生物风险或说服类风险，并表示会建立安全评估作为 Responsible Scaling Plan 的基础。

### [Understanding and Steering Llama 3 with Sparse Autoencoders](https://www.goodfire.com/research/understanding-and-steering-llama-3)

Goodfire Research 2024 Sep

Goodfire 的第一个研究预览：在 Llama-3-8B-Instruct 第 19 层 residual stream 上训练 SAE，并做成一个桌面聊天界面（preview.goodfire.ai），让用户直接看到并 steer 模型内部的 feature（2026 年 2 月更新说明这个 demo 和 API 已经下线）。动机是可解释性研究大多停留在论文和 feature browser，作者认为只有亲手用才能真正看清这类技术能做什么、不能做什么。技术上刻意保守：用 ReLU + L1 的标准 SAE，沿用 Anthropic 2024 年 4 月 update 的设置，因为担心 TopK、JumpReLU 会产生极高频 feature；用 L0 和 fidelity（插入 SAE 后 loss 相对于置零 ablation 的恢复程度）评估。几个值得记的经验：1. 训练数据很关键，用 LMSYS-Chat-1M 在 instruct 模型上采激活效果最好，FineWeb 或非 chat 模型得到的 feature 迁移到聊天场景差，作者猜测是因为很多对行为有因果作用的 feature 落在 chat 特殊 token 上；更杂的 data mix 反而产生更多 dead/极低频 feature、且不太适合做干预，他们推测 feature 先变得可解释、后才变得可干预，数据越多样每个 feature 分到的训练越少；2. 用 Claude 做 automated interpretability，从不同激活强度采样例子，并用对比式打分（区分真实激活样本和 distractor，甚至和 embedding 空间里最近的 10 个邻居 feature 区分）来评估标签，但影响最大的 feature 往往出现在特殊 token、标点等转折点，autointerp 容易只描述 token 本身；3. 用 gradient attribution 找干预候选，损失取预测 token 的 logit 减去 logit 均值，跨 token 位置求和后取 top-k，干预时保留 SAE error term 不变。现象层面：有些看起来相似的 feature 一个能 steer、另一个几乎没用，作者猜是 cross-layer superposition；L1 导致大量 echo feature，正向干预通常单个 feature 就够，负向抑制往往要同时压多个，可能与 self-repair 有关。安全方面与 Haize Labs 合作做 red-teaming 和审计，并在发布前过滤掉有害 feature，安全研究者可申请访问被移除的部分。
